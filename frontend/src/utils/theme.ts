export type Theme = 'light' | 'dark' | 'system';

export const THEME_KEY = 'maintenance-app-theme';

export const getTheme = (): Theme => {
  if (typeof window === 'undefined') return 'system';

  const stored = localStorage.getItem(THEME_KEY) as Theme;
  if (stored && ['light', 'dark', 'system'].includes(stored)) {
    return stored;
  }

  return 'system';
};

export const setTheme = (theme: Theme): void => {
  if (typeof window === 'undefined') return;

  localStorage.setItem(THEME_KEY, theme);
  applyTheme(theme);
};

export const applyTheme = (theme: Theme): void => {
  if (typeof window === 'undefined') return;

  const root = document.documentElement;

  if (theme === 'system') {
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    root.classList.toggle('dark', prefersDark);
  } else {
    root.classList.toggle('dark', theme === 'dark');
  }
};

export const initTheme = (): void => {
  const theme = getTheme();
  applyTheme(theme);

  // Escuchar cambios en preferencias del sistema
  if (theme === 'system') {
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
      if (getTheme() === 'system') {
        document.documentElement.classList.toggle('dark', e.matches);
      }
    });
  }
};
