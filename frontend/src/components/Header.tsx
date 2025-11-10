import { useState } from 'react';
import { Search, Bell, Moon, Sun, Monitor, Menu, LogOut } from 'lucide-react';
import { clsx } from 'clsx';
import { getTheme, setTheme, type Theme } from '@/utils/theme';
import Button from './Button';

interface HeaderProps {
  onMenuClick?: () => void;
  showMenuButton?: boolean;
}

export default function Header({ onMenuClick, showMenuButton = false }: HeaderProps) {
  const [searchOpen, setSearchOpen] = useState(false);
  const [userMenuOpen, setUserMenuOpen] = useState(false);
  const [notificationsOpen, setNotificationsOpen] = useState(false);
  const [currentTheme, setCurrentTheme] = useState<Theme>(getTheme());

  const handleThemeChange = (theme: Theme) => {
    setTheme(theme);
    setCurrentTheme(theme);
  };

  // Mock user data - esto vendrá del contexto de autenticación en Fase 3
  const user = {
    name: 'Usuario Demo',
    email: 'demo@maintenance.com',
    avatar: null,
    role: 'Técnico',
  };

  // Mock notifications
  const notifications = [
    { id: 1, message: 'Nueva avería en L16', time: 'Hace 5 min', unread: true },
    { id: 2, message: 'Avería #123 resuelta', time: 'Hace 1 hora', unread: true },
    { id: 3, message: 'Mantenimiento programado L20', time: 'Hace 2 horas', unread: false },
  ];

  const unreadCount = notifications.filter(n => n.unread).length;

  return (
    <header className="fixed top-0 right-0 left-0 lg:left-64 h-16 bg-white dark:bg-dark-900 border-b border-light-300 dark:border-dark-800 z-30">
      <div className="h-full flex items-center justify-between px-4 lg:px-6">
        {/* Left Side */}
        <div className="flex items-center gap-4 flex-1">
          {/* Menu button for mobile */}
          {showMenuButton && (
            <button
              onClick={onMenuClick}
              className="lg:hidden p-2 rounded-lg hover:bg-light-200 dark:hover:bg-dark-800"
            >
              <Menu className="w-5 h-5" />
            </button>
          )}

          {/* Search */}
          <div className="relative flex-1 max-w-md">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-dark-500 dark:text-dark-400" />
            <input
              type="text"
              placeholder="Buscar averías, máquinas, manuales..."
              className="w-full pl-10 pr-4 py-2 rounded-lg bg-light-100 dark:bg-dark-800 border border-transparent focus:border-primary-500 focus:bg-white dark:focus:bg-dark-900 outline-none transition-colors text-sm"
              onFocus={() => setSearchOpen(true)}
              onBlur={() => setTimeout(() => setSearchOpen(false), 200)}
            />
          </div>
        </div>

        {/* Right Side */}
        <div className="flex items-center gap-2">
          {/* Theme Switcher */}
          <div className="hidden sm:flex items-center gap-1 p-1 rounded-lg bg-light-200 dark:bg-dark-800">
            <button
              onClick={() => handleThemeChange('light')}
              className={clsx(
                'p-1.5 rounded transition-colors',
                currentTheme === 'light'
                  ? 'bg-white dark:bg-dark-700'
                  : 'hover:bg-light-300 dark:hover:bg-dark-700'
              )}
              title="Modo claro"
            >
              <Sun className="w-4 h-4" />
            </button>
            <button
              onClick={() => handleThemeChange('system')}
              className={clsx(
                'p-1.5 rounded transition-colors',
                currentTheme === 'system'
                  ? 'bg-white dark:bg-dark-700'
                  : 'hover:bg-light-300 dark:hover:bg-dark-700'
              )}
              title="Sistema"
            >
              <Monitor className="w-4 h-4" />
            </button>
            <button
              onClick={() => handleThemeChange('dark')}
              className={clsx(
                'p-1.5 rounded transition-colors',
                currentTheme === 'dark'
                  ? 'bg-white dark:bg-dark-700'
                  : 'hover:bg-light-300 dark:hover:bg-dark-700'
              )}
              title="Modo oscuro"
            >
              <Moon className="w-4 h-4" />
            </button>
          </div>

          {/* Notifications */}
          <div className="relative">
            <button
              onClick={() => setNotificationsOpen(!notificationsOpen)}
              className="relative p-2 rounded-lg hover:bg-light-200 dark:hover:bg-dark-800 transition-colors"
            >
              <Bell className="w-5 h-5" />
              {unreadCount > 0 && (
                <span className="absolute top-1 right-1 w-2 h-2 bg-red-500 rounded-full" />
              )}
            </button>

            {/* Notifications Dropdown */}
            {notificationsOpen && (
              <div className="absolute right-0 mt-2 w-80 bg-white dark:bg-dark-900 rounded-lg shadow-strong border border-light-300 dark:border-dark-800">
                <div className="p-4 border-b border-light-300 dark:border-dark-800">
                  <h3 className="font-semibold text-dark-900 dark:text-dark-50">
                    Notificaciones
                  </h3>
                </div>
                <div className="max-h-96 overflow-y-auto">
                  {notifications.map((notification) => (
                    <div
                      key={notification.id}
                      className={clsx(
                        'p-4 border-b border-light-300 dark:border-dark-800 hover:bg-light-100 dark:hover:bg-dark-800 cursor-pointer',
                        notification.unread && 'bg-primary-50 dark:bg-primary-900/10'
                      )}
                    >
                      <p className="text-sm text-dark-900 dark:text-dark-50">
                        {notification.message}
                      </p>
                      <p className="text-xs text-dark-600 dark:text-dark-400 mt-1">
                        {notification.time}
                      </p>
                    </div>
                  ))}
                </div>
                <div className="p-2">
                  <Button variant="ghost" fullWidth size="sm">
                    Ver todas
                  </Button>
                </div>
              </div>
            )}
          </div>

          {/* User Menu */}
          <div className="relative">
            <button
              onClick={() => setUserMenuOpen(!userMenuOpen)}
              className="flex items-center gap-2 p-1.5 pr-3 rounded-lg hover:bg-light-200 dark:hover:bg-dark-800 transition-colors"
            >
              <div className="w-8 h-8 rounded-full bg-primary-600 flex items-center justify-center text-white font-medium text-sm">
                {user.name.charAt(0)}
              </div>
              <div className="hidden md:block text-left">
                <p className="text-sm font-medium text-dark-900 dark:text-dark-50">
                  {user.name}
                </p>
                <p className="text-xs text-dark-600 dark:text-dark-400">{user.role}</p>
              </div>
            </button>

            {/* User Dropdown */}
            {userMenuOpen && (
              <div className="absolute right-0 mt-2 w-56 bg-white dark:bg-dark-900 rounded-lg shadow-strong border border-light-300 dark:border-dark-800">
                <div className="p-4 border-b border-light-300 dark:border-dark-800">
                  <p className="font-medium text-dark-900 dark:text-dark-50">{user.name}</p>
                  <p className="text-sm text-dark-600 dark:text-dark-400">{user.email}</p>
                </div>
                <div className="p-2">
                  <a
                    href="/profile"
                    className="flex items-center gap-2 px-3 py-2 text-sm rounded-lg hover:bg-light-200 dark:hover:bg-dark-800 text-dark-900 dark:text-dark-50"
                  >
                    <Bell className="w-4 h-4" />
                    Perfil y Configuración
                  </a>
                  <button
                    className="w-full flex items-center gap-2 px-3 py-2 text-sm rounded-lg hover:bg-light-200 dark:hover:bg-dark-800 text-red-600 dark:text-red-400"
                  >
                    <LogOut className="w-4 h-4" />
                    Cerrar Sesión
                  </button>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </header>
  );
}
