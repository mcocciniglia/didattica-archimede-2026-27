(() => {
  function updateThemeControls(theme) {
    document.querySelectorAll("[data-theme-toggle]").forEach((button) => {
      const dark = theme === "dark";
      button.setAttribute("aria-pressed", String(dark));
      button.textContent = dark ? "Tema: scuro" : "Tema: chiaro";
      button.setAttribute(
        "aria-label",
        dark ? "Passa al tema chiaro" : "Passa al tema scuro"
      );
    });
  }

  window.addEventListener("DOMContentLoaded", () => {
    if (!window.ArchimedeTheme) {
      return;
    }

    updateThemeControls(window.ArchimedeTheme.current());

    document.querySelectorAll("[data-theme-toggle]").forEach((button) => {
      button.addEventListener("click", window.ArchimedeTheme.toggle);
    });
  });

  document.addEventListener("archimede:themechange", (event) => {
    updateThemeControls(event.detail.theme);
  });
})();
