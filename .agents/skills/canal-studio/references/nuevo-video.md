# Modo 3: Nuevo vídeo

Objetivo: dejar en `videos/` una carpeta con todo lo necesario para producir y publicar un vídeo, coherente con el canal y con lo aprendido.

## Pasos

1. **Lee el contexto:** `canal/01-vision.md`, el archivo del formato en `canal/03-formatos/`, `canal/04-personaje.md` (si aparece), `canal/05-estilo-visual.md`, `canal/06-voz-y-tono.md`, `canal/07-musica-y-audio.md`, `canal/12-reglas.md`, `aprendizajes/aprendizajes.md` y las últimas 10 filas de `videos/registro.csv`.
2. **Elige la idea.** Si el usuario no trae una, propón 3 del `ideas/backlog.md` (o nuevas) justificando cada una con un aprendizaje o un pilar. Evita repetir el tema, escenario o título de los últimos vídeos del mismo formato.
3. **Pregunta solo lo imprescindible** (máx. 3 preguntas): formato si no está claro, fecha prevista, algún requisito especial.
4. **Crea la carpeta** `videos/AAAA-MM-DD-slug-corto/` (fecha prevista de publicación) copiando `videos/_plantilla/video.md` como `video.md`.
5. **Rellena `video.md`:**
   - Frontmatter: `id` (= nombre de la carpeta), formato, fecha prevista, estado `idea → guion → produccion → listo → publicado`, pilar, hipótesis.
   - **Hipótesis:** qué esperamos aprender con este vídeo ("miniatura con la cara del personaje vs sin cara", "tema de oposiciones atrae más que selectividad"). Cada vídeo es un experimento pequeño; cambia una variable cada vez.
   - **Guion / escaleta** según la estructura del formato.
   - **Prompts de imagen/animación:** parte del prompt base del personaje y rellena solo las variables (`{escenario}`, `{ropa}`, `{hora}`, `{accion}`). No modifiques los rasgos fijos.
   - **Música:** pistas o prompt de generación + licencia.
   - **Título** (3 opciones, recomienda una), **descripción**, **tags**, **capítulos** si es largo.
   - **Miniatura:** descripción y prompt.
   - **Qué lo hace distinto** de los vídeos anteriores (una línea; obligatorio).
6. **Pasa la checklist** de `references/cumplimiento.md` y márcala en el archivo.
7. **Añade la fila** a `videos/registro.csv` con id, fecha, formato, título elegido, pilar, hipótesis y el resto vacío.
8. **Actualiza** `ideas/backlog.md` (mueve la idea a "En producción").

## Lotes

Si piden varios vídeos de golpe, crea uno por carpeta y asegúrate de que varían entre sí (tema, escenario, ropa, título). Muestra una tabla resumen antes de escribir los archivos y pide confirmación.

## Automatización

Si existe un pipeline (ver `canal/10-herramientas.md`), deja los datos que necesite en el bloque `pipeline:` del frontmatter con los nombres que use el script. No publiques nada directamente: el estado `listo` requiere aprobación humana registrada en el campo `aprobado_por`.
