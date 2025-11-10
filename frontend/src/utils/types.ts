// Tipos de usuario
export type UserRole = 'admin' | 'technician' | 'operator' | 'viewer';
export type SubscriptionTier = 'free' | 'basic' | 'premium' | 'enterprise';

export interface User {
  id: number;
  email: string;
  username: string;
  full_name: string;
  role: UserRole;
  subscription_tier: SubscriptionTier;
  is_active: boolean;
  is_verified: boolean;
  created_at: string;
  updated_at: string;
}

// Tipos de producción
export type ProductionLineName = 'L16' | 'L20' | 'L33';

export interface ProductionLine {
  id: number;
  name: ProductionLineName;
  description: string;
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

export interface Machine {
  id: number;
  name: string;
  code: string;
  description: string;
  production_line_id: number;
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

// Tipos de averías
export type FailureStatus = 'open' | 'in_progress' | 'resolved' | 'closed';
export type FailureSeverity = 'low' | 'medium' | 'high' | 'critical';

export interface Failure {
  id: number;
  title: string;
  description: string;
  machine_id: number;
  reported_by: number;
  assigned_to?: number;
  status: FailureStatus;
  severity: FailureSeverity;
  resolved_at?: string;
  created_at: string;
  updated_at: string;
}

// Tipos de soluciones
export interface Solution {
  id: number;
  title: string;
  description: string;
  failure_id: number;
  created_by: number;
  time_spent_minutes?: number;
  was_successful: boolean;
  ai_suggested: boolean;
  created_at: string;
  updated_at: string;
}

// Tipos de manuales
export type ManualType = 'maintenance' | 'operation' | 'troubleshooting' | 'safety';

export interface Manual {
  id: number;
  title: string;
  description: string;
  content: string;
  manual_type: ManualType;
  machine_id: number;
  file_url?: string;
  created_by: number;
  created_at: string;
  updated_at: string;
}

// Tipos de KPIs
export interface KPI {
  id: number;
  date: string;
  production_line_id?: number;
  machine_id?: number;
  total_failures: number;
  open_failures: number;
  resolved_failures: number;
  average_resolution_time_minutes?: number;
  mtbf?: number; // Mean Time Between Failures
  mttr?: number; // Mean Time To Repair
  availability_percentage?: number;
  created_at: string;
  updated_at: string;
}

// Tipos de autenticación
export interface LoginRequest {
  username: string;
  password: string;
}

export interface LoginResponse {
  access_token: string;
  refresh_token: string;
  token_type: string;
  user: User;
}

export interface RegisterRequest {
  email: string;
  username: string;
  password: string;
  full_name: string;
}

// Tipos de respuesta paginada
export interface PaginatedResponse<T> {
  items: T[];
  total: number;
  page: number;
  page_size: number;
  pages: number;
}
