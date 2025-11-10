/**
 * Formatea una fecha a formato local español
 */
export function formatDate(date: string | Date, includeTime: boolean = false): string {
  const d = typeof date === 'string' ? new Date(date) : date;

  if (includeTime) {
    return d.toLocaleString('es-ES', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
    });
  }

  return d.toLocaleDateString('es-ES', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
  });
}

/**
 * Formatea una duración en minutos a formato legible
 */
export function formatDuration(minutes: number): string {
  if (minutes < 60) {
    return `${minutes} min`;
  }

  const hours = Math.floor(minutes / 60);
  const mins = minutes % 60;

  if (mins === 0) {
    return `${hours}h`;
  }

  return `${hours}h ${mins}min`;
}

/**
 * Obtiene el tiempo transcurrido desde una fecha
 */
export function timeAgo(date: string | Date): string {
  const d = typeof date === 'string' ? new Date(date) : date;
  const now = new Date();
  const seconds = Math.floor((now.getTime() - d.getTime()) / 1000);

  const intervals = {
    año: 31536000,
    mes: 2592000,
    semana: 604800,
    día: 86400,
    hora: 3600,
    minuto: 60,
  };

  for (const [name, secondsInInterval] of Object.entries(intervals)) {
    const interval = Math.floor(seconds / secondsInInterval);

    if (interval >= 1) {
      return interval === 1
        ? `hace 1 ${name}`
        : `hace ${interval} ${name}${name !== 'mes' ? 's' : 'es'}`;
    }
  }

  return 'hace un momento';
}

/**
 * Trunca un texto a un número máximo de caracteres
 */
export function truncate(text: string, maxLength: number): string {
  if (text.length <= maxLength) return text;
  return text.slice(0, maxLength) + '...';
}

/**
 * Capitaliza la primera letra de un string
 */
export function capitalize(text: string): string {
  return text.charAt(0).toUpperCase() + text.slice(1);
}

/**
 * Obtiene las iniciales de un nombre
 */
export function getInitials(name: string): string {
  return name
    .split(' ')
    .map(word => word[0])
    .join('')
    .toUpperCase()
    .slice(0, 2);
}

/**
 * Obtiene el color para un estado de avería
 */
export function getFailureStatusColor(status: string): string {
  const colors: Record<string, string> = {
    open: 'bg-red-100 text-red-700 dark:bg-red-900/30 dark:text-red-400',
    in_progress: 'bg-yellow-100 text-yellow-700 dark:bg-yellow-900/30 dark:text-yellow-400',
    resolved: 'bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400',
    closed: 'bg-gray-100 text-gray-700 dark:bg-gray-900/30 dark:text-gray-400',
  };
  return colors[status] || colors.open;
}

/**
 * Obtiene el color para la severidad de una avería
 */
export function getFailureSeverityColor(severity: string): string {
  const colors: Record<string, string> = {
    low: 'bg-blue-100 text-blue-700 dark:bg-blue-900/30 dark:text-blue-400',
    medium: 'bg-yellow-100 text-yellow-700 dark:bg-yellow-900/30 dark:text-yellow-400',
    high: 'bg-orange-100 text-orange-700 dark:bg-orange-900/30 dark:text-orange-400',
    critical: 'bg-red-100 text-red-700 dark:bg-red-900/30 dark:text-red-400',
  };
  return colors[severity] || colors.medium;
}

/**
 * Traduce el rol de usuario al español
 */
export function translateRole(role: string): string {
  const translations: Record<string, string> = {
    admin: 'Administrador',
    technician: 'Técnico',
    operator: 'Operador',
    viewer: 'Visualizador',
  };
  return translations[role] || role;
}

/**
 * Traduce el tier de suscripción al español
 */
export function translateSubscriptionTier(tier: string): string {
  const translations: Record<string, string> = {
    free: 'Gratuito',
    basic: 'Básico',
    premium: 'Premium',
    enterprise: 'Empresarial',
  };
  return translations[tier] || tier;
}
