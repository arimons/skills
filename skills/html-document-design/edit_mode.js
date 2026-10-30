(function () {
  // 직접 수정 모드: 우하단 '✎ 편집' 버튼으로 켜고, '수정본 저장'으로 고친 문서를 새 파일로 받는다.
  // 글자 고치기 전용이다. 줄·항목·표를 늘리고 줄이는 일은 Claude에게 맡긴다.
  var ROOT = '.wrap';
  var editing = false;

  var bar = document.createElement('div');
  bar.id = 'editbar';
  bar.innerHTML =
    '<button type="button" data-a="start">✎ 편집</button>' +
    '<span class="on-only">수정 중</span>' +
    '<button type="button" class="on-only" data-a="save">수정본 저장</button>' +
    '<button type="button" class="on-only" data-a="done">편집 끝</button>';
  document.body.appendChild(bar);

  function mark() {
    document.querySelectorAll(ROOT + ' *').forEach(function (el) {
      if (/^(SCRIPT|STYLE|IMG|BR)$/i.test(el.tagName) || el.closest('svg,button,[data-ed]')) return;
      var own = Array.prototype.some.call(el.childNodes, function (n) {
        return n.nodeType === 3 && n.textContent.trim();
      });
      if (own) {
        el.setAttribute('contenteditable', 'true');
        el.setAttribute('data-ed', '');
        el.setAttribute('spellcheck', 'false');
      }
    });
  }
  function unmark(root) {
    root.querySelectorAll('[data-ed]').forEach(function (n) {
      n.removeAttribute('contenteditable'); n.removeAttribute('data-ed'); n.removeAttribute('spellcheck');
    });
  }
  function snapshot() {
    var c = document.documentElement.cloneNode(true);
    var b = c.querySelector('#editbar'); if (b) b.remove();
    unmark(c);
    var body = c.querySelector('body');
    body.classList.remove('editing');
    if (!body.getAttribute('class')) body.removeAttribute('class');
    c.removeAttribute('data-theme');   // 테마 선택은 문서에 굳히지 않는다
    return '<!DOCTYPE html>\n' + c.outerHTML;
  }
  function save() {
    var name = decodeURIComponent(location.pathname.split('/').pop() || 'document')
      .replace(/\.html?$/i, '').replace(/_edited$/, '');
    var a = document.createElement('a');
    a.href = URL.createObjectURL(new Blob([snapshot()], { type: 'text/html' }));
    a.download = name + '_edited.html';
    document.body.appendChild(a); a.click(); a.remove();
    setTimeout(function () { URL.revokeObjectURL(a.href); }, 1000);
  }
  function setEdit(on) {
    editing = on;
    document.body.classList.toggle('editing', on);
    if (on) mark(); else unmark(document);
  }

  bar.addEventListener('click', function (e) {
    var a = e.target.dataset && e.target.dataset.a;
    if (a === 'start') setEdit(true);
    else if (a === 'save') save();
    else if (a === 'done') setEdit(false);
  });
  document.addEventListener('paste', function (e) {
    if (!editing || !e.target.isContentEditable) return;
    e.preventDefault();
    document.execCommand('insertText', false, (e.clipboardData || window.clipboardData).getData('text/plain'));
  });
  document.addEventListener('keydown', function (e) {
    if (!editing) return;
    if (e.key === 'Escape') setEdit(false);
    else if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 's') { e.preventDefault(); save(); }
    else if (e.key === 'Enter' && !e.shiftKey && e.target.isContentEditable) {
      e.preventDefault(); document.execCommand('insertLineBreak');
    }
  });
})();
