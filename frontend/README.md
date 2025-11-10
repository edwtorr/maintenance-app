# Frontend - Gestión de Averías

Frontend de la aplicación construido con Astro, React y Tailwind CSS.

## Características

- SSR (Server-Side Rendering) habilitado para autenticación
- Componentes React para interactividad
- Tailwind CSS con tema personalizado (light/dark mode)
- Sistema de temas inspirado en Claude
- TypeScript para type safety

## Estructura

```
frontend/
├── src/
│   ├── components/    # Componentes React reutilizables
│   ├── layouts/       # Layouts de Astro
│   ├── pages/         # Rutas de la aplicación
│   ├── styles/        # Estilos globales y Tailwind
│   └── utils/         # Utilidades (config, theme, etc.)
├── public/            # Assets estáticos
└── astro.config.mjs   # Configuración de Astro
```

## Scripts Disponibles

```bash
# Desarrollo
npm run dev

# Build
npm run build

# Preview
npm run preview
```

## Configuración de Tema

El tema se puede cambiar mediante el sistema de temas ubicado en `src/utils/theme.ts`:

- **Light**: Modo claro
- **Dark**: Modo oscuro
- **System**: Sigue las preferencias del sistema

## Variables de Entorno

Ver `.env.example` para las variables requeridas.

```env
PUBLIC_API_URL=http://localhost:8000
PUBLIC_APP_NAME=Gestión de Averías
```

## Componentes Base

Los componentes base (btn, input, card) están definidos en `src/styles/global.css` usando @layer components de Tailwind.

## Próximos Pasos (Fase 2+)

- Componentes de autenticación
- Dashboard principal
- Gestión de averías
- Integración con IA
- Visualización de KPIs
