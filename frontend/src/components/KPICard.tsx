import { type ReactNode } from 'react';
import { TrendingUp, TrendingDown, Minus } from 'lucide-react';
import { clsx } from 'clsx';

interface KPICardProps {
  title: string;
  value: string | number;
  subtitle?: string;
  icon?: ReactNode;
  trend?: 'up' | 'down' | 'neutral';
  trendValue?: string;
  color?: 'primary' | 'success' | 'warning' | 'danger' | 'info';
}

export default function KPICard({
  title,
  value,
  subtitle,
  icon,
  trend,
  trendValue,
  color = 'primary',
}: KPICardProps) {
  const colorClasses = {
    primary: 'bg-primary-50 dark:bg-primary-900/20 text-primary-600 dark:text-primary-400',
    success: 'bg-green-50 dark:bg-green-900/20 text-green-600 dark:text-green-400',
    warning: 'bg-yellow-50 dark:bg-yellow-900/20 text-yellow-600 dark:text-yellow-400',
    danger: 'bg-red-50 dark:bg-red-900/20 text-red-600 dark:text-red-400',
    info: 'bg-blue-50 dark:bg-blue-900/20 text-blue-600 dark:text-blue-400',
  };

  const getTrendIcon = () => {
    switch (trend) {
      case 'up':
        return <TrendingUp className="w-4 h-4" />;
      case 'down':
        return <TrendingDown className="w-4 h-4" />;
      case 'neutral':
        return <Minus className="w-4 h-4" />;
      default:
        return null;
    }
  };

  const getTrendColor = () => {
    switch (trend) {
      case 'up':
        return 'text-green-600 dark:text-green-400';
      case 'down':
        return 'text-red-600 dark:text-red-400';
      case 'neutral':
        return 'text-dark-600 dark:text-dark-400';
      default:
        return '';
    }
  };

  return (
    <div className="card p-6">
      <div className="flex items-start justify-between mb-4">
        <div className="flex-1">
          <p className="text-sm font-medium text-dark-600 dark:text-dark-400 mb-1">
            {title}
          </p>
          <p className="text-3xl font-bold text-dark-900 dark:text-dark-50">
            {value}
          </p>
          {subtitle && (
            <p className="text-xs text-dark-500 dark:text-dark-500 mt-1">
              {subtitle}
            </p>
          )}
        </div>

        {icon && (
          <div className={clsx('p-3 rounded-lg', colorClasses[color])}>
            {icon}
          </div>
        )}
      </div>

      {trend && trendValue && (
        <div className={clsx('flex items-center gap-1 text-sm', getTrendColor())}>
          {getTrendIcon()}
          <span className="font-medium">{trendValue}</span>
          <span className="text-dark-600 dark:text-dark-400">vs mes anterior</span>
        </div>
      )}
    </div>
  );
}
