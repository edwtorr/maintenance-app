import { type ReactNode } from 'react';
import { clsx } from 'clsx';

export type BadgeVariant = 'success' | 'warning' | 'danger' | 'info' | 'neutral' | 'primary';
export type BadgeSize = 'sm' | 'md' | 'lg';

interface BadgeProps {
  children: ReactNode;
  variant?: BadgeVariant;
  size?: BadgeSize;
  dot?: boolean;
  className?: string;
}

export default function Badge({
  children,
  variant = 'neutral',
  size = 'md',
  dot = false,
  className,
}: BadgeProps) {
  const baseClasses = 'inline-flex items-center font-medium rounded-full';

  const variantClasses = {
    success: 'bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400',
    warning: 'bg-yellow-100 text-yellow-700 dark:bg-yellow-900/30 dark:text-yellow-400',
    danger: 'bg-red-100 text-red-700 dark:bg-red-900/30 dark:text-red-400',
    info: 'bg-blue-100 text-blue-700 dark:bg-blue-900/30 dark:text-blue-400',
    neutral: 'bg-gray-100 text-gray-700 dark:bg-gray-900/30 dark:text-gray-400',
    primary: 'bg-primary-100 text-primary-700 dark:bg-primary-900/30 dark:text-primary-400',
  };

  const sizeClasses = {
    sm: 'px-2 py-0.5 text-xs gap-1',
    md: 'px-2.5 py-1 text-sm gap-1.5',
    lg: 'px-3 py-1.5 text-base gap-2',
  };

  const dotSizeClasses = {
    sm: 'w-1.5 h-1.5',
    md: 'w-2 h-2',
    lg: 'w-2.5 h-2.5',
  };

  return (
    <span className={clsx(baseClasses, variantClasses[variant], sizeClasses[size], className)}>
      {dot && (
        <span className={clsx('rounded-full bg-current', dotSizeClasses[size])} />
      )}
      {children}
    </span>
  );
}

// Componentes específicos para estados de averías
export function FailureStatusBadge({ status }: { status: string }) {
  const statusMap: Record<string, { variant: BadgeVariant; label: string }> = {
    open: { variant: 'danger', label: 'Abierta' },
    in_progress: { variant: 'warning', label: 'En Progreso' },
    resolved: { variant: 'success', label: 'Resuelta' },
    closed: { variant: 'neutral', label: 'Cerrada' },
  };

  const config = statusMap[status] || statusMap.open;

  return (
    <Badge variant={config.variant} dot>
      {config.label}
    </Badge>
  );
}

export function FailureSeverityBadge({ severity }: { severity: string }) {
  const severityMap: Record<string, { variant: BadgeVariant; label: string }> = {
    low: { variant: 'info', label: 'Baja' },
    medium: { variant: 'warning', label: 'Media' },
    high: { variant: 'primary', label: 'Alta' },
    critical: { variant: 'danger', label: 'Crítica' },
  };

  const config = severityMap[severity] || severityMap.medium;

  return <Badge variant={config.variant}>{config.label}</Badge>;
}
