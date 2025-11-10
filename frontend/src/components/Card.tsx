import type { ReactNode } from 'react';

interface CardProps {
  children: ReactNode;
  className?: string;
  hover?: boolean;
  onClick?: () => void;
}

export default function Card({ children, className = '', hover = false, onClick }: CardProps) {
  const baseClasses = 'card p-6';
  const hoverClasses = hover ? 'card-hover cursor-pointer' : '';
  const combinedClasses = `${baseClasses} ${hoverClasses} ${className}`.trim();

  return (
    <div className={combinedClasses} onClick={onClick}>
      {children}
    </div>
  );
}

interface CardHeaderProps {
  title: string;
  subtitle?: string;
  action?: ReactNode;
}

export function CardHeader({ title, subtitle, action }: CardHeaderProps) {
  return (
    <div className="flex items-start justify-between mb-4">
      <div>
        <h3 className="text-xl font-semibold text-dark-900 dark:text-dark-50">
          {title}
        </h3>
        {subtitle && (
          <p className="text-sm text-dark-600 dark:text-dark-400 mt-1">
            {subtitle}
          </p>
        )}
      </div>
      {action && <div>{action}</div>}
    </div>
  );
}

interface CardBodyProps {
  children: ReactNode;
  className?: string;
}

export function CardBody({ children, className = '' }: CardBodyProps) {
  return (
    <div className={`text-dark-700 dark:text-dark-300 ${className}`}>
      {children}
    </div>
  );
}

interface CardFooterProps {
  children: ReactNode;
  className?: string;
}

export function CardFooter({ children, className = '' }: CardFooterProps) {
  return (
    <div className={`mt-6 pt-4 border-t border-light-300 dark:border-dark-700 ${className}`}>
      {children}
    </div>
  );
}
