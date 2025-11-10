/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        // Colores inspirados en Claude
        primary: {
          50: '#fef5ee',
          100: '#fde9d7',
          200: '#fbcfae',
          300: '#f7ad7a',
          400: '#f38144',
          500: '#f05f1f',
          600: '#e14515',
          700: '#bb3313',
          800: '#952a17',
          900: '#792516',
        },
        dark: {
          50: '#f6f6f7',
          100: '#e1e2e6',
          200: '#c3c5cd',
          300: '#9ea1ae',
          400: '#7a7d8c',
          500: '#5f6270',
          600: '#4b4d5a',
          700: '#3e3f4a',
          800: '#2d2e35',
          900: '#1a1b1f',
          950: '#0f0f11',
        },
        light: {
          50: '#ffffff',
          100: '#fafafa',
          200: '#f5f5f5',
          300: '#e5e5e5',
          400: '#d4d4d4',
          500: '#a3a3a3',
          600: '#737373',
          700: '#525252',
          800: '#404040',
          900: '#262626',
        }
      },
      fontFamily: {
        sans: [
          'Inter var',
          'ui-sans-serif',
          'system-ui',
          '-apple-system',
          'BlinkMacSystemFont',
          'Segoe UI',
          'Roboto',
          'Helvetica Neue',
          'Arial',
          'sans-serif',
        ],
        mono: [
          'JetBrains Mono',
          'Fira Code',
          'ui-monospace',
          'SFMono-Regular',
          'Menlo',
          'Monaco',
          'Consolas',
          'monospace',
        ],
      },
      borderRadius: {
        'xl': '0.75rem',
        '2xl': '1rem',
      },
      boxShadow: {
        'soft': '0 2px 8px 0 rgba(0, 0, 0, 0.05)',
        'medium': '0 4px 16px 0 rgba(0, 0, 0, 0.08)',
        'strong': '0 8px 24px 0 rgba(0, 0, 0, 0.12)',
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
  ],
};
