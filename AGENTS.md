# Instrucciones para agentes (Codex, Claude Code y otros)

Este repositorio es el "cerebro" de un canal de YouTube de estudio (study with me, aesthetic + música relajante, shorts de tips y curiosidades). No es un proyecto de software: es conocimiento en Markdown y CSV que guía la creación de vídeos con IA.

## Usa la skill
Para cualquier tarea del canal usa la skill **canal-studio** (`.agents/skills/canal-studio/SKILL.md`). Sigue sus modos: entrevista, ajuste, nuevo vídeo, resultados y revisión.

## Mapa del repo
- `canal/` — un Markdown por elemento del canal (visión, audiencia, formatos, personaje, estilo, voz, música, pilares, calendario, herramientas, monetización, reglas). `_estado.md` dice qué está definido; `_cambios.md` es el historial.
- `videos/` — `registro.csv` (histórico con métricas) y una carpeta por vídeo con su `video.md`.
- `ideas/backlog.md` — ideas pendientes.
- `aprendizajes/aprendizajes.md` — lo que dicen los datos.
- `assets/` — referencias del personaje y licencias (solo archivos ligeros).
- `scripts/resumen.py` — resumen de estado y métricas.

## Reglas
- Responde en español.
- Lee `canal/_estado.md` al empezar.
- No inventes métricas, URLs ni fechas.
- No cambies un archivo `definido` de `canal/` sin confirmación, y registra todo cambio en `canal/_cambios.md`.
- No publiques nada en YouTube sin aprobación humana.
- No subas claves de API ni archivos pesados al repo.
