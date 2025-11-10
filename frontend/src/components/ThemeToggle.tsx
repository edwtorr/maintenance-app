import { useState, useEffect } from 'react';
import { getTheme, setTheme, type Theme } from '@/utils/theme';

export default function ThemeToggle() {
  const [currentTheme, setCurrentTheme] = useState<Theme>('system');

  useEffect(() => {
    setCurrentTheme(getTheme());
  }, []);

  const handleThemeChange = (newTheme: Theme) => {
    setTheme(newTheme);
    setCurrentTheme(newTheme);
  };

  return (
    <div className="flex items-center gap-2 p-2 rounded-lg bg-light-200 dark:bg-dark-800">
      <button
        onClick={() => handleThemeChange('light')}
        className={`px-3 py-1 rounded transition-colors ${
          currentTheme === 'light'
            ? 'bg-white dark:bg-dark-700 text-dark-900 dark:text-dark-50'
            : 'text-dark-600 dark:text-dark-400 hover:text-dark-900 dark:hover:text-dark-50'
        }`}
        title="Modo claro"
      >
        ☀️
      </button>
      <button
        onClick={() => handleThemeChange('system')}
        className={`px-3 py-1 rounded transition-colors ${
          currentTheme === 'system'
            ? 'bg-white dark:bg-dark-700 text-dark-900 dark:text-dark-50'
            : 'text-dark-600 dark:text-dark-400 hover:text-dark-900 dark:hover:text-dark-50'
        }`}
        title="Sistema"
      >
        💻
      </button>
      <button
        onClick={() => handleThemeChange('dark')}
        className={`px-3 py-1 rounded transition-colors ${
          currentTheme === 'dark'
            ? 'bg-white dark:bg-dark-700 text-dark-900 dark:text-dark-50'
            : 'text-dark-600 dark:text-dark-400 hover:text-dark-900 dark:hover:text-dark-50'
        }`}
        title="Modo oscuro"
      >
        🌙
      </button>
    </div>
  );
}
