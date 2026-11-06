# Modo 1: Entrevista

Objetivo: llegar a que cada elemento del canal esté `definido`, con decisiones concretas que otra IA pueda seguir sin preguntar.

## Cómo preguntar

- **Un elemento cada vez**, en el orden de la tabla de abajo, salvo que el usuario elija otro. Retoma por el primer elemento `pendiente` o `borrador` de `canal/_estado.md`.
- **2-4 preguntas por mensaje**, nunca un formulario largo.
- **Ofrece opciones** con una recomendada (marcada con ⭐) y deja siempre abierta la respuesta libre. Las personas deciden mejor eligiendo que redactando desde cero.
- **Propón por defecto.** Si el usuario dice "no sé" o "lo que veas", propón algo coherente con lo ya definido, explícalo en una línea y pide un sí/no.
- **Repregunta lo vago.** "Aesthetic" o "relajante" no son decisiones: pide ejemplos (canales, colores, una imagen de referencia, una canción).
- **Resume y confirma** antes de escribir: "Esto es lo que voy a guardar: ... ¿Correcto?".
- **Escribe al terminar cada elemento**, no al final de todo. Rellena la plantilla del archivo, borra los comentarios `<!-- PENDIENTE -->` resueltos, pon `estado: definido` (o `borrador` si quedaron dudas, listadas en la sección "Dudas abiertas") y actualiza `_estado.md` y `_cambios.md`.
- Al acabar un elemento, di cuántos quedan y pregunta si seguir o parar. Es normal hacerlo en varias sesiones.

**Modo rápido:** si el usuario quiere ir rápido, haz solo las preguntas marcadas con (★) de cada elemento, genera todos los archivos como `borrador` y deja las demás preguntas en "Dudas abiertas".

## Orden y banco de preguntas

Usa estas preguntas como guía, no como guion literal. Adapta según las respuestas previas y salta lo que ya esté respondido.

### 1. Visión → `canal/01-vision.md`
- (★) ¿Nombre del canal (o ideas)? ¿Idioma(s)?
- (★) En una frase: ¿para quién es el canal y qué gana viéndolo?
- (★) ¿Nicho amplio (estudiantes en general) o estrecho (criminología, derecho, oposiciones, selectividad...)? ⭐ Recomendado: estrecho, aprovechando la formación del criminólogo.
- ¿Objetivo a 6 y 12 meses (suscriptores, horas, ingresos)?
- ¿Cuántas horas semanales puede dedicar cada uno?
- 3 canales de referencia y qué copiaríais / evitaríais de cada uno.

### 2. Audiencia → `canal/02-audiencia.md`
- (★) Edad, nivel de estudios, país/idioma.
- (★) ¿Qué problema tienen? (concentración, procrastinación, soledad al estudiar, ansiedad de exámenes...)
- ¿Cuándo y dónde nos ven? (de fondo en el portátil, en el móvil entre clases...)
- ¿Qué NO quieren ver?

### 3. Formatos → `canal/03-formatos/<formato>.md` (uno por formato)
Primero: (★) ¿qué formatos tendremos? Opciones: study with me (largo), aesthetic + música (largo), shorts de tips, shorts de curiosidades, otro. Crea un archivo por formato elegido a partir de `canal/03-formatos/_plantilla-formato.md` y borra los que no se usen. Para cada formato:
- (★) Duración y estructura (p. ej. pomodoro 50/10 con temporizador visible, 4 bloques).
- (★) Qué se ve en pantalla minuto a minuto o escena a escena.
- ¿Aparece el personaje? ¿Qué hace?
- ¿Hay voz, texto en pantalla, ambos o nada?
- Elementos fijos (intro, temporizador, marca de agua, cierre) y elementos que varían.
- Cómo se diferencia cada vídeo del anterior (clave para no ser contenido repetitivo: escenario, estación, asignatura, hora del día, reto...).
- Título y miniatura: patrón base.

### 4. Personaje recurrente → `canal/04-personaje.md`
- (★) ¿Habrá personaje? ¿Humano, animal, estilizado (anime, 3D, acuarela)?
- (★) Rasgos fijos que NUNCA cambian: edad aparente, pelo, ojos, complexión, rasgo distintivo (gafas, pecas, un accesorio).
- Nombre y personalidad (aunque no hable: cómo se mueve, qué estudia, manías).
- Vestuario: fijo o variable por estación/tema. Qué piezas se mantienen siempre.
- Entornos habituales (habitación, biblioteca, cafetería, tren...).
- ¿Tiene voz? Si sí, características y herramienta.
- Imágenes de referencia: pide que se guarden en `assets/personaje/` y anota su nombre.
- Prohibiciones: no parecerse a una persona real ni a un personaje con derechos de autor.
Con las respuestas, redacta un **prompt base** (en inglés si la herramienta de imagen funciona mejor así) + **prompt negativo** + qué partes se sustituyen por vídeo (`{escenario}`, `{ropa}`, `{hora}`, `{accion}`).

### 5. Estilo visual → `canal/05-estilo-visual.md`
- (★) Paleta (3-5 colores, en hex si es posible) y ambiente (cálido, nocturno, lluvia, minimalista...).
- (★) Estilo de imagen (ilustración, foto realista, pixel art, anime...).
- Tipografías y texto en pantalla.
- Animación: estática, loop sutil (lluvia, vapor, parpadeo), cámara lenta.
- Miniaturas: composición, cuánto texto, si sale la cara del personaje.

### 6. Voz y tono → `canal/06-voz-y-tono.md`
- (★) ¿Tuteo? ¿Cercano, motivador, de "compañero de biblioteca", académico?
- Palabras o expresiones de marca; palabras prohibidas.
- Uso de emojis en títulos y descripciones.
- Voz en off: humana (de quién) o sintética. ⭐ Recomendado: voz humana en los shorts, refuerza la aportación original.

### 7. Música y audio → `canal/07-musica-y-audio.md`
- (★) Géneros (lofi, piano, ambient, jazz, sonidos de lluvia/cafetería...) y si hay sonidos de ambiente.
- (★) Fuente de la música y licencia: biblioteca de audio de YouTube, librería de pago, generación con IA (qué servicio y qué plan permite uso comercial), composición propia. Pide que la licencia se guarde en `assets/licencias/`.
- Volumen y mezcla; ¿avisos sonoros en descansos del pomodoro?

### 8. Pilares de contenido → `canal/08-pilares-contenido.md`
- (★) 3-5 temas que el canal cubre siempre (técnicas de estudio, organización, salud del estudiante, curiosidades de criminología...).
- ¿Qué aporta cada socio? (el criminólogo valida contenido de su área, el ingeniero la automatización...)
- Temas prohibidos o delicados (crímenes reales con víctimas identificables, consejos médicos...).
- Rellena al menos 10 ideas iniciales en `ideas/backlog.md`.

### 9. Calendario → `canal/09-calendario.md`
- (★) Frecuencia por formato (p. ej. 1 largo/semana + 3 shorts).
- Días y horas de publicación (zona horaria de la audiencia).
- Quién hace qué y cuándo (revisión, aprobación, subida).
- Temporadas: exámenes, vuelta a clase, vacaciones.

### 10. Herramientas → `canal/10-herramientas.md`
- (★) Qué herramienta para: guion, imagen, animación, música, voz, montaje, miniatura, subida.
- Qué está automatizado y qué es manual. ⭐ Recomendado: automatizar producción y dejar la publicación con aprobación humana.
- Presupuesto mensual máximo.
- Dónde viven los archivos pesados (no en este repo: Drive, disco, S3...).

### 11. Monetización → `canal/11-monetizacion.md`
- (★) Fuentes previstas: anuncios (YPP), afiliados, productos digitales (plantillas, planners), patrocinios, membresías.
- Qué ofrecer y cuándo (antes de llegar a YPP también se puede vender).
- Cómo repartís ingresos y gastos (recomienda dejarlo por escrito).

### 12. Reglas y líneas rojas → `canal/12-reglas.md`
- (★) Qué nunca haremos (clickbait engañoso, imitar a otros canales, datos sin verificar...).
- Proceso de aprobación antes de publicar.
- Cómo declaramos el uso de IA.
Parte de `references/cumplimiento.md` y añade las reglas propias.

## Al terminar la entrevista completa

1. Comprueba coherencia entre archivos (personaje ↔ estilo visual ↔ formatos ↔ voz) y señala contradicciones.
2. Resume el canal en 5 líneas en `canal/01-vision.md`, sección "Resumen ejecutivo".
3. Propón el primer lote de vídeos con el modo 3.
