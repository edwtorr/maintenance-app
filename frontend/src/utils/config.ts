// Configuración general de la aplicación

export const APP_NAME = 'Gestión de Averías';
export const APP_VERSION = '1.0.0';

// URLs de API
export const API_BASE_URL = import.meta.env.PUBLIC_API_URL || 'http://localhost:8000';
export const API_ENDPOINTS = {
  AUTH: {
    LOGIN: '/api/auth/login',
    REGISTER: '/api/auth/register',
    LOGOUT: '/api/auth/logout',
    REFRESH: '/api/auth/refresh',
    ME: '/api/auth/me',
  },
  FAILURES: {
    LIST: '/api/failures',
    CREATE: '/api/failures',
    UPDATE: (id: string) => `/api/failures/${id}`,
    DELETE: (id: string) => `/api/failures/${id}`,
  },
  MACHINES: {
    LIST: '/api/machines',
    BY_LINE: (lineId: string) => `/api/machines/line/${lineId}`,
  },
  PRODUCTION_LINES: {
    LIST: '/api/production-lines',
  },
  SOLUTIONS: {
    LIST: '/api/solutions',
    BY_FAILURE: (failureId: string) => `/api/solutions/failure/${failureId}`,
  },
  MANUALS: {
    LIST: '/api/manuals',
    BY_MACHINE: (machineId: string) => `/api/manuals/machine/${machineId}`,
  },
  KPI: {
    DASHBOARD: '/api/kpi/dashboard',
    BY_LINE: (lineId: string) => `/api/kpi/line/${lineId}`,
  },
  AI: {
    SUGGEST_SOLUTION: '/api/ai/suggest-solution',
    ANALYZE_FAILURE: '/api/ai/analyze-failure',
  },
} as const;

// Configuración de tema
export const THEME_CONFIG = {
  colors: {
    primary: {
      light: '#f05f1f',
      dark: '#f38144',
    },
    background: {
      light: {
        primary: '#ffffff',
        secondary: '#fafafa',
        tertiary: '#f5f5f5',
      },
      dark: {
        primary: '#0f0f11',
        secondary: '#1a1b1f',
        tertiary: '#2d2e35',
      },
    },
    text: {
      light: {
        primary: '#1a1b1f',
        secondary: '#5e6070',
        tertiary: '#9ea1ae',
      },
      dark: {
        primary: '#f6f6f7',
        secondary: '#bec0ca',
        tertiary: '#9ea1ae',
      },
    },
  },
  borderRadius: {
    sm: '0.375rem',
    md: '0.5rem',
    lg: '0.75rem',
    xl: '1rem',
  },
} as const;

// Líneas de producción disponibles
export const PRODUCTION_LINES = [
  'L16',
  'L20',
  'L33',
] as const;

export type ProductionLine = typeof PRODUCTION_LINES[number];

// Roles de usuario
export const USER_ROLES = {
  ADMIN: 'admin',
  TECHNICIAN: 'technician',
  OPERATOR: 'operator',
  VIEWER: 'viewer',
} as const;

export type UserRole = typeof USER_ROLES[keyof typeof USER_ROLES];

// Niveles de suscripción
export const SUBSCRIPTION_TIERS = {
  FREE: 'free',
  BASIC: 'basic',
  PREMIUM: 'premium',
  ENTERPRISE: 'enterprise',
} as const;

export type SubscriptionTier = typeof SUBSCRIPTION_TIERS[keyof typeof SUBSCRIPTION_TIERS];
