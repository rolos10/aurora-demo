# Aurora · Clínica Genezen — Demo

Demo interactivo de la app móvil de Clínica Genezen con **agendamiento por voz** (Aurora) y flujo manual de citas.

## Qué incluye

- **Login** con cédula
- **Home** con accesos rápidos y próxima cita
- **🎙️ Agendar por voz** (Aurora) — conversación natural en español
- **🗓️ Agendar Cita** — flujo manual de 4 pasos (especialidad → médico → horario → confirmar)
- **📋 Historia Clínica** con resumen inteligente por IA
- **🔔 Notificaciones**

## Deploy en Vercel (30 segundos)

### Opción A — CLI

```bash
cd aurora-demo
npx vercel --prod
```

Sigue las instrucciones; Vercel detecta el `index.html` y lo sirve como sitio estático.

### Opción B — Drag & drop

1. Entra a [vercel.com/new](https://vercel.com/new)
2. Arrastra la carpeta `aurora-demo/` completa
3. Click en **Deploy** (sin tocar nada — no requiere build)

Vercel te da una URL pública tipo `https://aurora-demo-xxxx.vercel.app`.

## Antes de la demo al prospecto

La primera vez que abras la URL en el dispositivo de demo:

1. Toca **🔑 API** arriba a la derecha (visible una vez logueado)
2. Pega tu API key de Anthropic (`sk-ant-...`) — la consigues en [console.anthropic.com/settings/keys](https://console.anthropic.com/settings/keys)
3. Guardar

La key queda en `localStorage` del navegador del dispositivo de demo. No queda expuesta en el código ni en el deploy.

> **Importante:** para producción real conviene poner un proxy serverless en Vercel (`api/chat.js`) que oculte la key. Para el demo de prospecto con un dispositivo controlado, este enfoque es suficiente.

## Requisitos del navegador del demo

- **Chrome desktop / Android** ✅ funciona completo
- **Safari iOS** ✅ funciona completo (asegurarse de aceptar permiso de micrófono)
- **Firefox** ⚠️ no soporta `webkitSpeechRecognition` para reconocimiento de voz
- **HTTPS obligatorio** — Vercel lo provee por defecto

## Cómo funciona Aurora (flujo por voz)

El paciente ya está autenticado en la app (Carlos Alberto Ruiz), por lo que Aurora solo le pregunta:

1. **Especialidad** ("¿Para qué especialidad necesita?")
2. **Motivo** breve de consulta
3. **Fecha y hora** preferidas
4. Repite todo y pide confirmación

Una vez confirmado, la cita queda guardada en `localStorage` y aparece en la Historia Clínica con el código `AUR-XXXXX`.

## Stack técnico

- Una sola página: `index.html` (sin build step)
- React 18 + Babel Standalone vía CDN
- Web Speech API (reconocimiento + síntesis del navegador)
- Anthropic Messages API directamente desde browser (Claude Sonnet 4)
- `localStorage` para persistir citas y API key

## Notas para el prospecto

- En producción la voz se puede subir a **ElevenLabs Conversational AI** para que suene más natural (la TTS del navegador es decente pero limitada)
- Aurora puede integrarse con el sistema de citas real de Clínica Genezen vía webhook
- El backend de citas puede correr en Vercel Edge Functions o el sistema actual de la clínica
