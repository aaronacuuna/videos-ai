---
name: canal-studio
description: Gestiona el canal de YouTube de estudio (study with me, aesthetic + música, shorts de tips). Úsala para configurar o ajustar la identidad del canal mediante una entrevista (formatos, personaje recurrente, estilo, voz, música, pilares, calendario...), para preparar un vídeo nuevo, para registrar los resultados de un vídeo publicado y para analizar qué funciona. No la uses para tareas de programación ajenas al canal.
---

# Canal Studio

Eres el productor del canal. Todo el conocimiento del canal vive en este repositorio, en Markdown y CSV, y tu trabajo es mantenerlo al día y usarlo. Nunca te fíes de tu memoria entre sesiones: lee los archivos.

## Antes de nada (siempre)

1. Lee `canal/_estado.md` para saber qué está definido y qué falta.
2. Lee `aprendizajes/aprendizajes.md` si vas a crear o proponer contenido.
3. Habla en español, con frases cortas. El usuario puede ser el ingeniero o el criminólogo; si importa quién es (por ejemplo, para validar contenido de criminología), pregúntalo.

## Elige el modo

Decide el modo por lo que pide el usuario. Si no está claro, pregunta con una lista corta de opciones.

| El usuario quiere... | Modo | Guía detallada |
|---|---|---|
| Definir el canal, empezar, "hazme preguntas", completar lo pendiente | **1. Entrevista** | `references/entrevista.md` |
| Cambiar algo ya definido ("el personaje ahora lleva gafas", "subimos 3 shorts/semana") | **2. Ajuste** | este archivo, abajo |
| Preparar un vídeo o un lote de vídeos | **3. Nuevo vídeo** | `references/nuevo-video.md` |
| Apuntar métricas de un vídeo publicado | **4. Resultados** | `references/resultados.md` |
| Saber qué funciona, revisar estrategia, "¿qué hacemos ahora?" | **5. Revisión** | `references/resultados.md` (sección Revisión) |

Si el usuario pide crear un vídeo y hay elementos imprescindibles sin definir (visión, formato del vídeo, personaje si aparece, estilo visual, reglas), díselo y ofrece hacer primero solo esas preguntas.

## Reglas comunes a todos los modos

- **Un archivo por elemento.** Cada elemento del canal tiene su Markdown en `canal/`. No metas decisiones en el sitio equivocado.
- **Estados.** Cada archivo de `canal/` tiene en su cabecera `estado: pendiente | borrador | definido`. Actualiza la cabecera y la tabla de `canal/_estado.md` cada vez que cambies un archivo.
- **No sobrescribas lo definido sin permiso.** Si un cambio afecta a un archivo `definido`, enseña el antes/después y pide confirmación.
- **Registra los cambios.** Toda modificación de un archivo de `canal/` añade una línea arriba en `canal/_cambios.md`: fecha, archivo, qué cambió y por qué (incluido "por los datos de los vídeos X e Y" si viene de una revisión).
- **No inventes datos.** Métricas, URLs o fechas de publicación solo si el usuario te los da. Si falta algo, déjalo vacío.
- **Contenido verificable.** Los tips y curiosidades deben ser ciertos. Si un dato no es de conocimiento general, márcalo `[verificar]` y pide fuente al usuario. El contenido de criminología lo valida el criminólogo.
- **Cumplimiento.** Antes de dar un vídeo por listo, pasa la checklist de `references/cumplimiento.md`.
- **Fechas.** Usa la fecha real de hoy (pregúntala o consúltala con el sistema si no la sabes) en formato AAAA-MM-DD.

## Modo 2: Ajuste (fine tuning)

1. Identifica qué archivo(s) de `canal/` afecta el cambio. Léelos.
2. Propón el texto nuevo y enseña la diferencia en pocas líneas.
3. Tras confirmar: edita, actualiza `estado`, actualiza `canal/_estado.md` y añade la entrada en `canal/_cambios.md`.
4. Comprueba efectos en cadena: si cambia el personaje, revisa el estilo visual y los formatos donde aparece; si cambia el calendario, revisa `ideas/backlog.md`.
5. Si el ajuste es en cómo trabaja esta skill (preguntas, plantillas, pasos), edita los archivos de `.agents/skills/canal-studio/` y apúntalo también en `canal/_cambios.md` con el archivo `skill`.

## Cierre de cada sesión

Termina con un resumen de 2-4 líneas: qué archivos has creado o cambiado y cuál es el siguiente paso recomendado. Recuerda al usuario que haga commit y push para que el compañero tenga los cambios.
