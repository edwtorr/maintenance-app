import KPICard from '@/components/KPICard';
import Card, { CardHeader, CardBody } from '@/components/Card';
import { FailureStatusBadge, FailureSeverityBadge } from '@/components/Badge';
import Button from '@/components/Button';
import { Clock, AlertCircle, Activity, Wrench, TrendingUp } from 'lucide-react';

// Datos de ejemplo
const kpis = {
  mttr: { value: '2.3h', subtitle: 'Tiempo medio de reparación', trend: 'down' as const, trendValue: '-15%' },
  mtbf: { value: '45.2h', subtitle: 'Tiempo medio entre fallos', trend: 'up' as const, trendValue: '+8%' },
  availability: { value: '94.5%', subtitle: 'Disponibilidad total', trend: 'up' as const, trendValue: '+2.1%' },
  openFailures: { value: '12', subtitle: 'Averías abiertas actualmente', trend: 'down' as const, trendValue: '-3' },
};

const recentFailures = [
  {
    id: 1,
    title: 'Fallo en motor principal',
    machine: 'Máquina XZ-100',
    line: 'L16',
    status: 'open' as const,
    severity: 'critical' as const,
    time: 'Hace 15 min',
  },
  {
    id: 2,
    title: 'Sensor de temperatura desajustado',
    machine: 'Máquina AB-250',
    line: 'L20',
    status: 'in_progress' as const,
    severity: 'medium' as const,
    time: 'Hace 1 hora',
  },
  {
    id: 3,
    title: 'Fuga hidráulica menor',
    machine: 'Máquina CD-320',
    line: 'L33',
    status: 'in_progress' as const,
    severity: 'low' as const,
    time: 'Hace 2 horas',
  },
  {
    id: 4,
    title: 'Calibración necesaria',
    machine: 'Máquina EF-450',
    line: 'L16',
    status: 'resolved' as const,
    severity: 'medium' as const,
    time: 'Hace 3 horas',
  },
];

const lineStatus = [
  { name: 'L16', status: 'warning', availability: '91%', activeFailures: 2, color: 'text-yellow-600 dark:text-yellow-400' },
  { name: 'L20', status: 'operational', availability: '96%', activeFailures: 1, color: 'text-green-600 dark:text-green-400' },
  { name: 'L33', status: 'operational', availability: '95%', activeFailures: 1, color: 'text-green-600 dark:text-green-400' },
];

export default function DashboardContent() {
  return (
    <>
      {/* Page Header */}
      <div className="mb-6">
        <h1 className="text-3xl font-bold text-dark-900 dark:text-dark-50 mb-2">
          Dashboard
        </h1>
        <p className="text-dark-600 dark:text-dark-400">
          Resumen general del estado de las líneas de producción
        </p>
      </div>

      {/* KPI Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
        <KPICard
          title="MTTR"
          value={kpis.mttr.value}
          subtitle={kpis.mttr.subtitle}
          icon={<Clock className="w-6 h-6" />}
          trend={kpis.mttr.trend}
          trendValue={kpis.mttr.trendValue}
          color="primary"
        />
        <KPICard
          title="MTBF"
          value={kpis.mtbf.value}
          subtitle={kpis.mtbf.subtitle}
          icon={<Activity className="w-6 h-6" />}
          trend={kpis.mtbf.trend}
          trendValue={kpis.mtbf.trendValue}
          color="success"
        />
        <KPICard
          title="Disponibilidad"
          value={kpis.availability.value}
          subtitle={kpis.availability.subtitle}
          icon={<TrendingUp className="w-6 h-6" />}
          trend={kpis.availability.trend}
          trendValue={kpis.availability.trendValue}
          color="info"
        />
        <KPICard
          title="Averías Abiertas"
          value={kpis.openFailures.value}
          subtitle={kpis.openFailures.subtitle}
          icon={<AlertCircle className="w-6 h-6" />}
          trend={kpis.openFailures.trend}
          trendValue={kpis.openFailures.trendValue}
          color="warning"
        />
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Recent Failures */}
        <div className="lg:col-span-2">
          <Card>
            <CardHeader title="Averías Recientes" subtitle="Últimas averías reportadas">
              <Button variant="outline" size="sm" href="/failures">
                Ver todas
              </Button>
            </CardHeader>
            <CardBody>
              <div className="space-y-3">
                {recentFailures.map((failure) => (
                  <div
                    key={failure.id}
                    className="flex items-start justify-between p-3 rounded-lg bg-light-100 dark:bg-dark-800 hover:bg-light-200 dark:hover:bg-dark-700 transition-colors cursor-pointer"
                  >
                    <div className="flex-1">
                      <div className="flex items-center gap-2 mb-1">
                        <h4 className="font-medium text-dark-900 dark:text-dark-50">
                          {failure.title}
                        </h4>
                        <FailureSeverityBadge severity={failure.severity} />
                      </div>
                      <p className="text-sm text-dark-600 dark:text-dark-400 mb-2">
                        {failure.machine} • {failure.line}
                      </p>
                      <div className="flex items-center gap-3 text-xs text-dark-500 dark:text-dark-500">
                        <FailureStatusBadge status={failure.status} />
                        <span>{failure.time}</span>
                      </div>
                    </div>
                    <Button variant="ghost" size="sm">
                      Ver
                    </Button>
                  </div>
                ))}
              </div>
            </CardBody>
          </Card>
        </div>

        {/* Production Lines Status */}
        <div>
          <Card>
            <CardHeader title="Estado de Líneas" subtitle="Líneas de producción" />
            <CardBody>
              <div className="space-y-4">
                {lineStatus.map((line) => (
                  <div key={line.name} className="p-4 rounded-lg bg-light-100 dark:bg-dark-800">
                    <div className="flex items-center justify-between mb-2">
                      <h4 className="text-lg font-semibold text-dark-900 dark:text-dark-50">
                        {line.name}
                      </h4>
                      <span className={`flex items-center gap-1 text-sm font-medium ${line.color}`}>
                        <span className="w-2 h-2 rounded-full bg-current"></span>
                        {line.status === 'operational' ? 'Operativa' : 'Atención'}
                      </span>
                    </div>
                    <div className="space-y-1">
                      <div className="flex justify-between text-sm">
                        <span className="text-dark-600 dark:text-dark-400">Disponibilidad</span>
                        <span className="font-medium text-dark-900 dark:text-dark-50">{line.availability}</span>
                      </div>
                      <div className="flex justify-between text-sm">
                        <span className="text-dark-600 dark:text-dark-400">Averías activas</span>
                        <span className="font-medium text-dark-900 dark:text-dark-50">{line.activeFailures}</span>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </CardBody>
          </Card>

          {/* Quick Actions */}
          <Card className="mt-4">
            <CardHeader title="Acciones Rápidas" />
            <CardBody>
              <div className="space-y-2">
                <Button variant="primary" fullWidth href="/failures/new" icon={<Wrench className="w-4 h-4" />}>
                  Reportar Avería
                </Button>
                <Button variant="secondary" fullWidth href="/ai-assistant" icon={<Activity className="w-4 h-4" />}>
                  Asistente IA
                </Button>
                <Button variant="outline" fullWidth href="/manuals">
                  Ver Manuales
                </Button>
              </div>
            </CardBody>
          </Card>
        </div>
      </div>
    </>
  );
}
