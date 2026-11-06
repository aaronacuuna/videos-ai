# Canal Studio

Repositorio de partida para un canal de YouTube de estudio hecho con ayuda de IA: study with me, vídeos aesthetic con música relajante y shorts de tips y curiosidades.

Aquí vive todo lo que una IA necesita saber para crear vídeos coherentes con el canal, y el histórico de lo que ha funcionado. La skill **canal-studio** os entrevista para definirlo todo, prepara vídeos y aprende de los resultados. Funciona igual en **Codex** y en **Claude Code**.

## Empezar

1. Subid este repo a GitHub (privado) y clonadlo los dos.
2. Abrid Codex o Claude Code en la carpeta del repo.
3. Lanzad la skill:
   - **Codex:** escribe `$canal-studio` (o `/skills` para verla) y di "vamos a configurar el canal".
   - **Claude Code:** `/canal-studio vamos a configurar el canal`.
4. Responded a las preguntas. La entrevista va elemento a elemento y guarda cada uno en `canal/`. Se puede parar y retomar cuando queráis.
5. Al terminar cada sesión: `git add . && git commit -m "..." && git push`, para que el otro tenga los cambios.

## Qué le podéis pedir

| Pide... | Qué hace |
|---|---|
| "Configura el canal" / "sigamos con lo pendiente" | Entrevista: preguntas con opciones hasta definir cada elemento |
| "El personaje ahora lleva una bufanda roja" | Ajuste: cambia el archivo, enseña el antes/después y lo registra |
| "Prepara el próximo study with me" / "3 shorts para esta semana" | Crea `videos/<fecha-slug>/video.md` con guion, prompts, títulos, descripción y checklist |
| "Apunta las métricas del vídeo X" | Actualiza `videos/registro.csv` y el expediente del vídeo, con veredicto |
| "¿Qué está funcionando?" | Revisión: analiza el histórico y actualiza `aprendizajes/` |

## Estructura

```
.agents/skills/canal-studio/   ← la skill (fuente única, la lee Codex)
  SKILL.md
  references/                  ← entrevista, nuevo vídeo, resultados, cumplimiento
.claude/skills/canal-studio/   ← puente para Claude Code (apunta a la de arriba)
AGENTS.md / CLAUDE.md          ← instrucciones generales del repo
canal/                         ← un .md por elemento + _estado.md + _cambios.md
  03-formatos/                 ← un .md por formato
videos/                        ← registro.csv + una carpeta por vídeo
ideas/backlog.md
aprendizajes/aprendizajes.md
assets/                        ← referencias del personaje y licencias
scripts/resumen.py             ← estado del canal y métricas
```

## Mejorar la skill (fine tuning)

La skill es texto, así que se mejora editando:

- **Cambiar qué pregunta la entrevista:** `.agents/skills/canal-studio/references/entrevista.md`.
- **Cambiar cómo se prepara un vídeo:** `references/nuevo-video.md` y `videos/_plantilla/video.md`.
- **Cambiar cómo se analizan los resultados:** `references/resultados.md` y `scripts/resumen.py`.
- **Reglas de YouTube:** `references/cumplimiento.md` (revisadlo cuando cambien las políticas).

También podéis pedírselo a la propia IA: "ajusta la skill para que en la entrevista pregunte también por X". Editad siempre la versión de `.agents/`; la de `.claude/` solo redirige.

## Resumen rápido

```
python3 scripts/resumen.py
```
