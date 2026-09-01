(function () {
  var copyIcon =
    '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1" fill="none" stroke="currentColor" stroke-width="2"/></svg>';

  var live = document.createElement("div");
  live.className = "visually-hidden";
  live.setAttribute("aria-live", "polite");
  document.body.appendChild(live);

  function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text);
    }
    return new Promise(function (resolve, reject) {
      var area = document.createElement("textarea");
      area.value = text;
      area.setAttribute("readonly", "");
      area.style.position = "fixed";
      area.style.left = "-9999px";
      document.body.appendChild(area);
      area.select();
      try {
        document.execCommand("copy");
        resolve();
      } catch (err) {
        reject(err);
      } finally {
        document.body.removeChild(area);
      }
    });
  }

  function selectFallback(pre) {
    var range = document.createRange();
    range.selectNodeContents(pre);
    var selection = window.getSelection();
    selection.removeAllRanges();
    selection.addRange(range);
  }

  function enhance(pre) {
    if (pre.closest(".code-block")) {
      return;
    }
    var wrap = document.createElement("div");
    wrap.className = "code-block";
    pre.parentNode.insertBefore(wrap, pre);
    wrap.appendChild(pre);

    var button = document.createElement("button");
    button.type = "button";
    button.className = "copy-btn";
    button.setAttribute("aria-label", "Copy command");
    button.innerHTML = copyIcon;
    wrap.appendChild(button);

    button.addEventListener("click", function () {
      var text = (pre.innerText || "").replace(/\n$/, "");
      copyText(text)
        .then(function () {
          button.classList.add("is-copied");
          button.textContent = "Copied";
          live.textContent = "Command copied to clipboard";
          setTimeout(function () {
            button.classList.remove("is-copied");
            button.innerHTML = copyIcon;
            live.textContent = "";
          }, 1600);
        })
        .catch(function () {
          selectFallback(pre);
        });
    });
  }

  document.querySelectorAll("pre").forEach(function (pre) {
    if (pre.classList.contains("copy-skip") || pre.closest(".copy-skip")) {
      return;
    }
    enhance(pre);
  });
})();
