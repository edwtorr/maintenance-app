import { type InputHTMLAttributes, forwardRef, type ReactNode } from 'react';
import { clsx } from 'clsx';

interface InputProps extends InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  error?: string;
  hint?: string;
  fullWidth?: boolean;
  icon?: ReactNode;
  iconPosition?: 'left' | 'right';
}

const Input = forwardRef<HTMLInputElement, InputProps>(
  (
    {
      label,
      error,
      hint,
      fullWidth = false,
      icon,
      iconPosition = 'left',
      className,
      ...props
    },
    ref
  ) => {
    return (
      <div className={clsx('flex flex-col gap-1.5', fullWidth && 'w-full')}>
        {label && (
          <label className="text-sm font-medium text-dark-900 dark:text-dark-50">
            {label}
            {props.required && <span className="text-red-500 ml-1">*</span>}
          </label>
        )}

        <div className="relative">
          {icon && iconPosition === 'left' && (
            <div className="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none text-dark-500 dark:text-dark-400">
              {icon}
            </div>
          )}

          <input
            ref={ref}
            className={clsx(
              'w-full px-4 py-2 rounded-lg',
              'bg-white dark:bg-dark-900',
              'border border-light-300 dark:border-dark-700',
              'text-dark-900 dark:text-dark-50',
              'placeholder:text-light-500 dark:placeholder:text-dark-500',
              'focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent',
              'disabled:opacity-50 disabled:cursor-not-allowed',
              'transition-all duration-200',
              icon && iconPosition === 'left' && 'pl-10',
              icon && iconPosition === 'right' && 'pr-10',
              error && 'border-red-500 focus:ring-red-500',
              className
            )}
            {...props}
          />

          {icon && iconPosition === 'right' && (
            <div className="absolute inset-y-0 right-0 flex items-center pr-3 pointer-events-none text-dark-500 dark:text-dark-400">
              {icon}
            </div>
          )}
        </div>

        {hint && !error && (
          <p className="text-xs text-dark-600 dark:text-dark-400">{hint}</p>
        )}

        {error && (
          <p className="text-xs text-red-600 dark:text-red-400">{error}</p>
        )}
      </div>
    );
  }
);

Input.displayName = 'Input';

export default Input;
