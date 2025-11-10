import { useState } from 'react';
import {
  Home,
  Bot,
  ClipboardList,
  BarChart3,
  BookOpen,
  Archive,
  Settings,
  User,
  ChevronLeft,
  ChevronRight,
} from 'lucide-react';
import { clsx } from 'clsx';

interface NavItem {
  label: string;
  icon: React.ReactNode;
  href: string;
  badge?: number;
}

const navItems: NavItem[] = [
  { label: 'Dashboard', icon: <Home className="w-5 h-5" />, href: '/dashboard' },
  { label: 'Asistente IA', icon: <Bot className="w-5 h-5" />, href: '/ai-assistant' },
  { label: 'Registro de Averías', icon: <ClipboardList className="w-5 h-5" />, href: '/failures' },
  { label: 'Visualización de KPIs', icon: <BarChart3 className="w-5 h-5" />, href: '/kpis' },
  { label: 'Manuales', icon: <BookOpen className="w-5 h-5" />, href: '/manuals' },
  { label: 'Históricos', icon: <Archive className="w-5 h-5" />, href: '/history' },
  { label: 'Configuración', icon: <Settings className="w-5 h-5" />, href: '/config' },
  { label: 'Perfil', icon: <User className="w-5 h-5" />, href: '/profile' },
];

interface SidebarProps {
  currentPath?: string;
}

export default function Sidebar({ currentPath = '/' }: SidebarProps) {
  const [collapsed, setCollapsed] = useState(false);

  const isActive = (href: string) => {
    if (href === '/dashboard' && currentPath === '/') return true;
    return currentPath.startsWith(href);
  };

  return (
    <aside
      className={clsx(
        'fixed left-0 top-0 h-screen bg-white dark:bg-dark-900 border-r border-light-300 dark:border-dark-800',
        'transition-all duration-300 ease-in-out z-40',
        collapsed ? 'w-16' : 'w-64'
      )}
    >
      {/* Logo */}
      <div className="h-16 flex items-center justify-between px-4 border-b border-light-300 dark:border-dark-800">
        <div className={clsx('flex items-center gap-3', collapsed && 'justify-center')}>
          <div className="w-8 h-8 bg-primary-600 rounded-lg flex items-center justify-center text-white font-bold">
            GA
          </div>
          {!collapsed && (
            <span className="font-semibold text-dark-900 dark:text-dark-50">
              Gestión Averías
            </span>
          )}
        </div>
      </div>

      {/* Navigation */}
      <nav className="flex flex-col py-4 px-2 gap-1">
        {navItems.map((item) => (
          <a
            key={item.href}
            href={item.href}
            className={clsx(
              'flex items-center gap-3 px-3 py-2.5 rounded-lg transition-colors group relative',
              isActive(item.href)
                ? 'bg-primary-100 dark:bg-primary-900/20 text-primary-700 dark:text-primary-400'
                : 'text-dark-700 dark:text-dark-300 hover:bg-light-200 dark:hover:bg-dark-800',
              collapsed && 'justify-center'
            )}
            title={collapsed ? item.label : ''}
          >
            {item.icon}
            {!collapsed && <span className="text-sm font-medium">{item.label}</span>}
            {!collapsed && item.badge && (
              <span className="ml-auto bg-primary-600 text-white text-xs font-semibold px-2 py-0.5 rounded-full">
                {item.badge}
              </span>
            )}

            {/* Tooltip cuando está colapsado */}
            {collapsed && (
              <div className="absolute left-full ml-2 px-2 py-1 bg-dark-900 dark:bg-dark-800 text-white text-sm rounded opacity-0 pointer-events-none group-hover:opacity-100 transition-opacity whitespace-nowrap">
                {item.label}
              </div>
            )}
          </a>
        ))}
      </nav>

      {/* Toggle Button */}
      <button
        onClick={() => setCollapsed(!collapsed)}
        className={clsx(
          'absolute -right-3 top-20 w-6 h-6 bg-white dark:bg-dark-900 border border-light-300 dark:border-dark-800',
          'rounded-full flex items-center justify-center text-dark-600 dark:text-dark-400',
          'hover:bg-light-100 dark:hover:bg-dark-800 transition-colors'
        )}
      >
        {collapsed ? (
          <ChevronRight className="w-4 h-4" />
        ) : (
          <ChevronLeft className="w-4 h-4" />
        )}
      </button>
    </aside>
  );
}
