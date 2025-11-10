# 📦 Guía de Componentes

Esta guía muestra cómo utilizar los componentes y utilidades ya configurados en el proyecto.

## 🎨 Sistema de Temas

### Cambiar tema desde TypeScript/React

```typescript
import { setTheme, getTheme } from '@/utils/theme';

// Cambiar a modo oscuro
setTheme('dark');

// Cambiar a modo claro
setTheme('light');

// Usar preferencias del sistema
setTheme('system');

// Obtener tema actual
const currentTheme = getTheme(); // 'light' | 'dark' | 'system'
```

### Componente ThemeToggle

```tsx
import ThemeToggle from '@/components/ThemeToggle';

export default function Header() {
  return (
    <header>
      <ThemeToggle />
    </header>
  );
}
```

## 🎴 Componente Card

### Uso básico

```tsx
import Card from '@/components/Card';

<Card>
  <h3>Título</h3>
  <p>Contenido de la tarjeta</p>
</Card>
```

### Card con hover

```tsx
<Card hover onClick={() => console.log('Click!')}>
  <h3>Card clickeable</h3>
</Card>
```

### Card completa con Header, Body y Footer

```tsx
import Card, { CardHeader, CardBody, CardFooter } from '@/components/Card';

<Card>
  <CardHeader
    title="Avería #123"
    subtitle="Línea L16 - Máquina XYZ"
    action={<button className="btn-primary">Editar</button>}
  />
  <CardBody>
    <p>Descripción de la avería...</p>
  </CardBody>
  <CardFooter>
    <div className="flex gap-2">
      <button className="btn-secondary">Cancelar</button>
      <button className="btn-primary">Guardar</button>
    </div>
  </CardFooter>
</Card>
```

## 🎨 Clases CSS Predefinidas

### Botones

```html
<!-- Botón primario -->
<button class="btn-primary">Guardar</button>

<!-- Botón secundario -->
<button class="btn-secondary">Cancelar</button>
```

### Inputs

```html
<input type="text" class="input" placeholder="Buscar..." />
```

### Cards

```html
<div class="card">Contenido</div>

<!-- Card con hover -->
<div class="card-hover">Contenido clickeable</div>
```

## 🔌 Cliente API

### Configuración

```typescript
import { apiClient } from '@/utils/api';

// Establecer token de autenticación
apiClient.setToken('tu-jwt-token');

// Limpiar token (logout)
apiClient.clearToken();
```

### Hacer peticiones

```typescript
// GET
const response = await apiClient.get<User[]>('/api/users');
if (response.data) {
  console.log(response.data);
}

// POST
const newUser = await apiClient.post<User>('/api/users', {
  username: 'john',
  email: 'john@example.com',
});

// PUT
const updated = await apiClient.put<User>('/api/users/1', {
  full_name: 'John Doe',
});

// DELETE
await apiClient.delete('/api/users/1');
```

### Manejo de errores

```typescript
const response = await apiClient.get<Failure[]>('/api/failures');

if (response.error) {
  console.error('Error:', response.error);
  console.error('Status:', response.status);
} else {
  console.log('Datos:', response.data);
}
```

## 🛠️ Utilidades

### Formateo de fechas

```typescript
import { formatDate, timeAgo, formatDuration } from '@/utils/helpers';

// Formatear fecha
formatDate('2024-01-15T10:30:00Z'); // "15 ene 2024"
formatDate('2024-01-15T10:30:00Z', true); // "15 ene 2024, 10:30"

// Tiempo transcurrido
timeAgo('2024-01-15T10:30:00Z'); // "hace 2 horas"

// Duración en minutos
formatDuration(90); // "1h 30min"
formatDuration(45); // "45 min"
```

### Colores de estados

```typescript
import { getFailureStatusColor, getFailureSeverityColor } from '@/utils/helpers';

// Obtener clases CSS para el estado
const statusClasses = getFailureStatusColor('open'); // clases Tailwind

// Obtener clases CSS para severidad
const severityClasses = getFailureSeverityColor('critical'); // clases Tailwind
```

### Traducciones

```typescript
import { translateRole, translateSubscriptionTier } from '@/utils/helpers';

translateRole('admin'); // "Administrador"
translateSubscriptionTier('premium'); // "Premium"
```

### Otras utilidades

```typescript
import { truncate, capitalize, getInitials } from '@/utils/helpers';

truncate('Texto muy largo...', 10); // "Texto muy ..."
capitalize('hola mundo'); // "Hola mundo"
getInitials('Juan Pérez García'); // "JP"
```

## 🎨 Colores del Tema

### Colores primarios

```tsx
<div className="bg-primary-600 text-white">Primario</div>
<div className="bg-primary-500 hover:bg-primary-600">Hover</div>
```

### Colores de fondo

```tsx
{/* Light mode backgrounds */}
<div className="bg-light-50">Muy claro</div>
<div className="bg-light-100">Claro</div>
<div className="bg-light-200">Medio</div>

{/* Dark mode backgrounds */}
<div className="dark:bg-dark-950">Muy oscuro</div>
<div className="dark:bg-dark-900">Oscuro</div>
<div className="dark:bg-dark-800">Medio</div>
```

### Colores de texto

```tsx
{/* Light mode text */}
<p className="text-dark-900">Texto primario</p>
<p className="text-dark-600">Texto secundario</p>

{/* Dark mode text */}
<p className="dark:text-dark-50">Texto primario</p>
<p className="dark:text-dark-300">Texto secundario</p>
```

## 📝 Tipos TypeScript

Todos los tipos están disponibles en `@/utils/types`:

```typescript
import type {
  User,
  ProductionLine,
  Machine,
  Failure,
  Solution,
  Manual,
  KPI,
  UserRole,
  SubscriptionTier,
  FailureStatus,
  FailureSeverity,
} from '@/utils/types';
```

## 🔧 Configuración

Accede a la configuración desde `@/utils/config`:

```typescript
import {
  APP_NAME,
  API_BASE_URL,
  API_ENDPOINTS,
  PRODUCTION_LINES,
  USER_ROLES,
} from '@/utils/config';

// Usar endpoints
fetch(API_ENDPOINTS.FAILURES.LIST);
fetch(API_ENDPOINTS.MACHINES.BY_LINE('L16'));
```

## 📱 Layouts

### Usar BaseLayout en páginas Astro

```astro
---
import BaseLayout from '@/layouts/BaseLayout.astro';
---

<BaseLayout title="Mi Página" description="Descripción de la página">
  <main>
    <!-- Tu contenido aquí -->
  </main>
</BaseLayout>
```

## 🎯 Próximos Pasos

Los componentes y utilidades están listos para:
- Fase 2: Componentes de autenticación (Login, Register)
- Fase 3: Componentes de gestión (FailureList, MachineCard, etc.)
- Fase 4: Integración de IA (ChatInterface, SuggestionCard)
- Fase 5: Dashboard y visualizaciones

Todos estos componentes utilizarán la base ya configurada.
