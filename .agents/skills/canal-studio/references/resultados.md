# Modo 4: Resultados y Modo 5: Revisión

## Modo 4: Registrar resultados

1. Pregunta qué vídeo (o propón los publicados sin métricas en `videos/registro.csv`).
2. Pide las métricas de YouTube Studio. Lo ideal es medir a las **48 h**, **7 días** y **28 días**. Acepta lo que haya; no rellenes lo que falte. Se puede pegar un pantallazo o copiar el texto.
   - Vistas, CTR de impresiones (%), duración media vista, retención media (%), suscriptores ganados, likes, comentarios.
   - En shorts: también % "visto vs deslizado" si lo tienen.
   - Comentarios destacados (cualitativos).
3. Actualiza la fila en `videos/registro.csv` y la sección "Resultados" de `videos/<id>/video.md`.
4. **Veredicto** (`exito | normal | flojo`), comparando con la mediana de los últimos vídeos **del mismo formato** (calcúlala con `python3 scripts/resumen.py`, no a ojo). Con menos de 5 vídeos del formato, pon `normal` salvo que sea muy evidente y dilo.
5. Escribe 1-3 líneas de **por qué** (respuesta a la hipótesis del vídeo). Diferencia lo que es dato de lo que es suposición.
6. Si confirma o descarta algo, apúntalo en `aprendizajes/aprendizajes.md` (ver formato abajo).

## Modo 5: Revisión

Hazla cada ~10 vídeos publicados o cuando lo pidan.

1. Ejecuta `python3 scripts/resumen.py` para ver totales, medianas por formato y mejores/peores vídeos.
2. Busca patrones agrupando por formato, pilar, tipo de título, miniatura, duración, día de publicación. Con pocos datos, habla de **indicios**, no de conclusiones.
3. Actualiza `aprendizajes/aprendizajes.md`:
   - **Confirmado** (≥3 vídeos apuntan lo mismo) → propón el cambio en el archivo de `canal/` correspondiente (modo Ajuste, con confirmación).
   - **Hipótesis** (1-2 vídeos) → propón el próximo experimento para comprobarla.
   - **Descartado** → lo que probamos y no funcionó, para no repetirlo.
4. Propón los 3 próximos experimentos y añade las ideas al `ideas/backlog.md`.
5. Si el canal se acerca a umbrales de monetización, compara con los requisitos vigentes en `canal/11-monetizacion.md` (y recomienda comprobarlos en la web de YouTube, cambian).

## Formato de una entrada en aprendizajes

```
- [AAAA-MM-DD] **<aprendizaje en una frase>** — evidencia: <ids de vídeos y métrica> — acción: <qué cambiamos o probamos>
```
