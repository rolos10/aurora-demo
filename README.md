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

Configura la variable de entorno **`ANTHROPIC_API_KEY`** en el dashboard de Vercel (Settings → Environment Variables) para que Aurora y el resumen de historia clínica funcionen.

## Instalar como app en el celular (PWA)

La demo se puede **instalar con icono en la pantalla de inicio**, sin App Store ni Play Store.

### Android (Chrome)

1. Abra la URL en **Chrome**.
2. Aparecerá el aviso **Instalar Aurora** (o menú ⋮ → **Instalar aplicación**).
3. Confirme. Quedará el icono **Aurora** en el launcher.
4. Al abrirla, corre a pantalla completa como una app.

### iPhone (Safari)

1. Abra la URL en **Safari** (no Chrome).
2. Toque **Compartir** (cuadrado con flecha).
3. Elija **Agregar a pantalla de inicio**.
4. Confirme el nombre **Aurora** y toque **Agregar**.

### Qué incluye la PWA

- `manifest.webmanifest` — nombre, colores, iconos, modo `standalone`
- `sw.js` — service worker para instalación y cache offline básico
- `icons/` — iconos en varios tamaños (192, 512, etc.)
- Layout adaptado cuando se abre instalada (pantalla completa, sin marco de “teléfono demo”)

> **Tip para la demo:** genere un QR con la URL de Vercel para que el cliente instale la app en su celular en segundos.

## Antes de la demo al prospecto

La API key de Anthropic debe estar configurada en **Vercel** (`ANTHROPIC_API_KEY`). No se expone en el código ni en el navegador del usuario.

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
- **PWA** instalable (`manifest.webmanifest` + service worker)
- Web Speech API (reconocimiento + síntesis del navegador)
- Anthropic Messages API vía proxy serverless (`api/chat.js`, Claude Sonnet 4)
- `localStorage` para persistir citas

## Notas para el prospecto

- En producción la voz se puede subir a **ElevenLabs Conversational AI** para que suene más natural (la TTS del navegador es decente pero limitada)
- Aurora puede integrarse con el sistema de citas real de Clínica Genezen vía webhook
- El backend de citas puede correr en Vercel Edge Functions o el sistema actual de la clínica
