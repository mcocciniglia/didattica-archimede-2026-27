(() => {
  const root = document.documentElement;
  const storageKey = "archimede-theme";
  const media = window.matchMedia("(prefers-color-scheme: dark)");

  function savedTheme() {
    try {
      const value = localStorage.getItem(storageKey);
      return value === "light" || value === "dark" ? value : null;
    } catch {
      return null;
    }
  }

  function setTheme(theme, persist = false) {
    root.dataset.theme = theme;

    if (persist) {
      try {
        localStorage.setItem(storageKey, theme);
      } catch {
        // La pagina rimane utilizzabile anche se lo storage è disabilitato.
      }
    }

    document.dispatchEvent(
      new CustomEvent("archimede:themechange", { detail: { theme } })
    );
  }

  setTheme(savedTheme() || (media.matches ? "dark" : "light"));

  window.ArchimedeTheme = {
    current: () => root.dataset.theme,
    toggle: () => setTheme(root.dataset.theme === "dark" ? "light" : "dark", true),
  };

  media.addEventListener?.("change", (event) => {
    if (!savedTheme()) {
      setTheme(event.matches ? "dark" : "light");
    }
  });
})();
