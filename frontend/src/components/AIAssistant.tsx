import { useState, useRef, useEffect } from 'react';
import { Send, Bot, User, Copy, RotateCw, Sparkles } from 'lucide-react';
import ReactMarkdown from 'react-markdown';
import { clsx } from 'clsx';
import Button from './Button';
import Textarea from './Textarea';

interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  timestamp: Date;
}

const suggestedPrompts = [
  '¿Cuál es el problema más común en L16?',
  'Sugiere solución para fallo de motor',
  'Historial de averías del último mes',
  'Procedimiento de mantenimiento preventivo',
];

export default function AIAssistant() {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: '1',
      role: 'assistant',
      content: '¡Hola! Soy tu asistente de IA para gestión de averías. Puedo ayudarte a:\n\n- Analizar y diagnosticar problemas\n- Sugerir soluciones basadas en el historial\n- Consultar manuales técnicos\n- Generar informes\n\n¿En qué puedo ayudarte hoy?',
      timestamp: new Date(),
    },
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || isLoading) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      role: 'user',
      content: input.trim(),
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, userMessage]);
    setInput('');
    setIsLoading(true);

    // Simular respuesta de IA (en producción esto llamaría a la API)
    setTimeout(() => {
      const assistantMessage: Message = {
        id: (Date.now() + 1).toString(),
        role: 'assistant',
        content: `He analizado tu consulta sobre "${userMessage.content}".\n\n**Análisis:**\n\nBasándome en el historial de averías y los manuales técnicos disponibles, te puedo proporcionar la siguiente información:\n\n1. Este tipo de problema suele estar relacionado con desgaste de componentes\n2. La solución más común incluye inspección visual y verificación de calibraciones\n3. El tiempo estimado de reparación es de 2-3 horas\n\n**Recomendación:**\n\nRevisa el manual técnico correspondiente en la sección de mantenimiento preventivo. Si el problema persiste, considera contactar al proveedor del equipo.\n\n¿Necesitas más información específica?`,
        timestamp: new Date(),
      };
      setMessages((prev) => [...prev, assistantMessage]);
      setIsLoading(false);
    }, 1500);
  };

  const handlePromptClick = (prompt: string) => {
    setInput(prompt);
    textareaRef.current?.focus();
  };

  const copyMessage = (content: string) => {
    navigator.clipboard.writeText(content);
    // TODO: Mostrar toast de confirmación
  };

  const regenerateResponse = (messageId: string) => {
    // TODO: Implementar regeneración de respuesta
    console.log('Regenerate:', messageId);
  };

  return (
    <div className="flex flex-col h-[calc(100vh-10rem)] max-w-5xl mx-auto">
      {/* Messages Container */}
      <div className="flex-1 overflow-y-auto mb-4 space-y-6 pr-4">
        {messages.map((message) => (
          <div
            key={message.id}
            className={clsx(
              'flex gap-4',
              message.role === 'user' ? 'flex-row-reverse' : 'flex-row'
            )}
          >
            {/* Avatar */}
            <div
              className={clsx(
                'flex-shrink-0 w-10 h-10 rounded-full flex items-center justify-center',
                message.role === 'user'
                  ? 'bg-primary-600 text-white'
                  : 'bg-gradient-to-br from-primary-500 to-primary-700 text-white'
              )}
            >
              {message.role === 'user' ? (
                <User className="w-5 h-5" />
              ) : (
                <Bot className="w-5 h-5" />
              )}
            </div>

            {/* Message Content */}
            <div
              className={clsx(
                'flex-1 max-w-3xl',
                message.role === 'user' ? 'text-right' : 'text-left'
              )}
            >
              <div
                className={clsx(
                  'inline-block p-4 rounded-2xl',
                  message.role === 'user'
                    ? 'bg-primary-600 text-white'
                    : 'bg-white dark:bg-dark-900 border border-light-300 dark:border-dark-700'
                )}
              >
                {message.role === 'assistant' ? (
                  <div className="prose prose-sm dark:prose-invert max-w-none">
                    <ReactMarkdown>{message.content}</ReactMarkdown>
                  </div>
                ) : (
                  <p className="text-sm whitespace-pre-wrap">{message.content}</p>
                )}
              </div>

              {/* Message Actions */}
              {message.role === 'assistant' && (
                <div className="flex gap-2 mt-2">
                  <button
                    onClick={() => copyMessage(message.content)}
                    className="p-1.5 rounded hover:bg-light-200 dark:hover:bg-dark-800 transition-colors"
                    title="Copiar"
                  >
                    <Copy className="w-4 h-4 text-dark-600 dark:text-dark-400" />
                  </button>
                  <button
                    onClick={() => regenerateResponse(message.id)}
                    className="p-1.5 rounded hover:bg-light-200 dark:hover:bg-dark-800 transition-colors"
                    title="Regenerar"
                  >
                    <RotateCw className="w-4 h-4 text-dark-600 dark:text-dark-400" />
                  </button>
                </div>
              )}

              <p className="text-xs text-dark-500 dark:text-dark-500 mt-1">
                {message.timestamp.toLocaleTimeString('es-ES', {
                  hour: '2-digit',
                  minute: '2-digit',
                })}
              </p>
            </div>
          </div>
        ))}

        {isLoading && (
          <div className="flex gap-4">
            <div className="flex-shrink-0 w-10 h-10 rounded-full bg-gradient-to-br from-primary-500 to-primary-700 text-white flex items-center justify-center">
              <Bot className="w-5 h-5" />
            </div>
            <div className="flex-1">
              <div className="inline-block p-4 rounded-2xl bg-white dark:bg-dark-900 border border-light-300 dark:border-dark-700">
                <div className="flex gap-2">
                  <span className="w-2 h-2 bg-primary-600 rounded-full animate-bounce" style={{ animationDelay: '0ms' }} />
                  <span className="w-2 h-2 bg-primary-600 rounded-full animate-bounce" style={{ animationDelay: '150ms' }} />
                  <span className="w-2 h-2 bg-primary-600 rounded-full animate-bounce" style={{ animationDelay: '300ms' }} />
                </div>
              </div>
            </div>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      {/* Suggested Prompts */}
      {messages.length === 1 && (
        <div className="mb-4">
          <div className="flex items-center gap-2 mb-3">
            <Sparkles className="w-4 h-4 text-primary-600" />
            <p className="text-sm font-medium text-dark-700 dark:text-dark-300">
              Sugerencias:
            </p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
            {suggestedPrompts.map((prompt, index) => (
              <button
                key={index}
                onClick={() => handlePromptClick(prompt)}
                className="text-left p-3 rounded-lg border border-light-300 dark:border-dark-700 hover:border-primary-500 dark:hover:border-primary-500 hover:bg-primary-50 dark:hover:bg-primary-900/10 transition-colors text-sm text-dark-700 dark:text-dark-300"
              >
                {prompt}
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Input Form */}
      <form onSubmit={handleSubmit} className="relative">
        <div className="flex gap-2 p-2 bg-white dark:bg-dark-900 border border-light-300 dark:border-dark-700 rounded-xl shadow-medium focus-within:border-primary-500 dark:focus-within:border-primary-500">
          <textarea
            ref={textareaRef}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                handleSubmit(e);
              }
            }}
            placeholder="Escribe tu consulta... (Shift + Enter para nueva línea)"
            className="flex-1 px-4 py-3 bg-transparent outline-none resize-none text-dark-900 dark:text-dark-50 placeholder:text-dark-500 dark:placeholder:text-dark-500 max-h-32"
            rows={1}
            disabled={isLoading}
          />
          <Button
            type="submit"
            variant="primary"
            size="sm"
            disabled={!input.trim() || isLoading}
            loading={isLoading}
            icon={<Send className="w-4 h-4" />}
            className="self-end"
          >
            Enviar
          </Button>
        </div>
      </form>
    </div>
  );
}
