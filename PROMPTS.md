# Промпты на графику

Готовые запросы для генератора изображений под каждый слот игры. Технические требования
(размеры, форматы, куда какой файл кладётся) — в [ASSETS.md](ASSETS.md), здесь только творческая
часть: что должно быть в кадре и как это попросить.

Промпты написаны по-английски: Midjourney, DALL·E, Flux и Stable Diffusion понимают английский
заметно лучше. Если генератор русскоязычный (Кандинский, Шедеврум) — переводите дословно, смысл
не потеряется. Пример перевода — в конце файла.

---

## Как этим пользоваться

**1. К каждому промпту приклеивайте один и тот же стилевой блок.** Это главное: разнобой стиля
заметнее, чем средний уровень исполнения. Копируйте его без изменений в каждый запрос.

```
STYLE: polished semi-realistic 3D casual game art, mobile game production quality in the spirit
of Playrix. Night football stadium lighting — cool dark ambient with warm floodlight rim light
from above and behind, soft volumetric haze, gentle bloom. Rich saturated colours, smooth
surfaces, clean readable silhouette. Colour palette: deep graphite #050A10, pitch green #0D6B31
and #0F7A38, acid lime accent #C8FF2E, gold #FFCF3D. No text anywhere in the image.
```

**2. И один и тот же негативный промпт.**

```
NEGATIVE: text, letters, words, numbers, captions, watermark, signature, logo, brand marks,
real club crests, recognisable real footballers, sponsor lettering on kits, UI elements, borders,
frame, flat lighting, muddy desaturated colours, cluttered background, extra limbs, deformed hands
```

**3. Весь набор — за один заход, одной моделью.** Не возвращайтесь к недостающей иконке через
неделю другим сервисом: она будет выбиваться, и это будет видно.

---

## Четыре запрета

- **Никакого текста в кадре.** Генераторы пишут абракадабру, а весь текст в игре и так рисует
  движок поверх картинки. Любая надпись на майке, табло или баннере — брак.
- **Никаких реальных эмблем клубов и узнаваемых лиц футболистов.** Это товарные знаки и права
  на изображение, Яндекс.Игры такое модерируют. Все формы, гербы и лица — вымышленные.
- **Жёлтый и красный — только карточки.** В игре эти два цвета означают предупреждение и
  удаление. Если они появятся на иконке фланга или на форме игрока, игрок будет читать это как
  сигнал тревоги. Единственное осознанное исключение — иконка «Россия» с триколорным шарфом:
  там красный приглушите.
- **Ничего мелкого в мелких ассетах.** Иконка живёт на экране размером 20–50 пикселей. Всё, что
  тоньше крупного пятна, там исчезнет. Проверка простая: уменьшите картинку до 24 px и посмотрите,
  читается ли она.

---

# 1. Заставка

**Слоты:** `ASSETS.sky`, `ASSETS.skyPortrait` · **Размеры:** 1920×1080 и 1080×1920 · **Альфа:** не нужна

Это фон под всеми экранами игры сразу — и меню, и матча. Отсюда единственное жёсткое требование:
**центр кадра должен быть тёмным, спокойным и пустым.** Поверх него лежат панель вопроса,
карточки ответов и табло. Забитый деталями центр убьёт читаемость, и никакая красота этого не
искупит. Весь свет, блеск и детали — в верхние углы, куда смотрят прожекторы.

### Горизонтальный кадр

```
Wide establishing shot of a modern football stadium at night, seen from pitch level. Empty green
pitch with mown stripes across the lower third, packed dark stands rising left and right, four
floodlight towers glowing warm white against a deep blue-black sky, visible light haze in the
beams. The centre of the frame is deliberately dark, quiet and empty — no players, no ball, no
objects — while all sparkle and bright detail sits in the upper corners. Cinematic, atmospheric,
slightly wide-angle lens. Aspect ratio 16:9.
```

### Вертикальный кадр

Не кроп горизонтального: на телефоне видно верхнюю треть экрана, и там должны быть трибуны,
а не пустое небо.

```
Vertical composition of the same modern football stadium at night. Two floodlight towers and a
tall wall of packed dark stands fill the upper half of the frame, a sliver of green pitch with
mown stripes at the very bottom, deep blue-black sky between the towers. The middle band of the
image is dark and empty so interface panels can sit on it. Cinematic, atmospheric.
Aspect ratio 9:16.
```

---

# 2. Карточки амплуа

**Слот:** `ASSETS.pos.gk` / `.def` / `.mid` / `.fwd` · **Размер:** 500×900 (вертикальный) · **Альфа:** обязательна

Четыре фигуры игроков на карточки выбора амплуа в меню. Фигура встаёт в правую часть карточки,
текст ужимается сам — код это уже умеет.

**Три требования ко всему набору сразу:**

- **Одна форма на всех троих полевых.** Иначе на одном экране окажутся игроки четырёх разных
  клубов. Вратарь — единственный в другой форме, как и положено.
- **Одинаковый рост фигуры в кадре и одинаковый отступ снизу.** Иначе на карточках они запрыгают.
  Проще всего добиться, генерируя все четыре одним заходом с одинаковой формулировкой кадрирования.
- **Кадр вертикальный и в обтяжку по фигуре.** Не квадрат: карточка в меню низкая и широкая,
  и квадратный холст с прозрачными полями по бокам заезжает на текст. Фигура должна заполнять
  кадр по высоте от края до края, пустых полей по бокам — минимум.
- **Позы разные и говорящие.** Карточка должна читаться до того, как игрок дочитает подпись.

### Вратарь

```
Full-body 3D character of a male football goalkeeper in a confident ready stance, knees slightly
bent, gloved hands open at hip height, weight on the toes. Bright orange goalkeeper kit with dark
graphite trim, thick padded gloves, plain fictional design without any markings. Warm floodlight
rim light from the upper left, cool fill from the right. Isolated on a fully transparent
background, no ground, no cast shadow. Full figure head to boots, centred, facing camera in
three-quarter view. Tall portrait canvas, figure filling the frame from top to bottom, tight crop with minimal empty margin at the sides.
```

### Защитник

```
Full-body 3D character of a male football defender standing like a wall — wide planted stance,
arms slightly away from the body, chest forward, calm determined face. Deep teal and graphite
outfield kit with acid lime trim, plain fictional design without any markings. Warm floodlight
rim light from the upper left, cool fill from the right. Isolated on a fully transparent
background, no ground, no cast shadow. Full figure head to boots, centred, facing camera in
three-quarter view. Tall portrait canvas, figure filling the frame from top to bottom, tight crop with minimal empty margin at the sides.
```

### Полузащитник

```
Full-body 3D character of a male football midfielder in a poised upright stance, one foot resting
on top of a football, head up as if scanning the pitch for a pass. Deep teal and graphite outfield
kit with acid lime trim, plain fictional design without any markings. Warm floodlight rim light
from the upper left, cool fill from the right. Isolated on a fully transparent background, no
ground, no cast shadow. Full figure head to boots, centred, facing camera in three-quarter view. Tall portrait canvas, figure filling the frame from top to bottom, tight crop with minimal empty margin at the sides.
```

### Нападающий

```
Full-body 3D character of a male football striker caught mid-stride in an explosive forward-leaning
sprint start, shoulders low, arms driving. Deep teal and graphite outfield kit with acid lime trim,
plain fictional design without any markings. Warm floodlight rim light from the upper left, cool
fill from the right. Isolated on a fully transparent background, no ground, no cast shadow. Full
figure head to boots, centred, facing camera in three-quarter view. Tall portrait canvas, figure filling the frame from top to bottom, tight crop with minimal empty margin at the sides.
```

---

# 3. Карточки «куда развиваем атаку»

Сначала о формате. Флангов одиннадцать: семь категорий и четыре ролевых. Полноценный арт на
каждую карточку — это одиннадцать больших картинок, которые игрок видит по три штуки на каждом
шаге, то есть до пятнадцати раз за матч. Такой объём и приедается, и весит.

**Поэтому: иконка на карточке, а не полноэкранный арт.** Карточка уже отрисована движком —
рамка, подсветка, подписи, свечение при наведении. От графики нужен один выразительный предмет
в центре. Это и дешевле, и работает лучше.

**Слоты:** `ASSETS.cat.*` (семь) и `ASSETS.role.*` (четыре) · **Размер:** 192×192 · **Альфа:** обязательна

К каждому промпту этого раздела добавьте общий кусок про иконки:

```
ICON FRAME: single centred 3D icon object, matte plastic and brushed metal look, chunky readable
silhouette, soft studio lighting with a warm rim, isolated on a fully transparent background,
nothing touching the canvas edges, identical object scale across the whole icon set. Square canvas.
```

### Семь категорий

| Слот | Фланг | Промпт (к нему — стилевой блок, негатив и ICON FRAME) |
|---|---|---|
| `world` | Сборные и мундиали | `A stylised globe whose surface is made of football panel stitching, tilted on its axis, thin acid lime meridian lines glowing faintly.` |
| `euro` | Еврокубки | `A tall silver and gold cup trophy with two big curved handles, generic fictional design, polished metal with warm reflections.` |
| `leagues` | Европейские лиги | `A blank rounded club crest shield with bold vertical stripes, no emblem and no lettering, slight metallic bevel on the edge.` |
| `players` | Игроки и рекорды | `A single golden football boot standing on a small round pedestal, laces detailed, gold with warm highlights.` |
| `rules` | Правила и судейство | `A chrome referee whistle on a short braided lanyard, coiled beneath it.` |
| `tactics` | Тактика и термины | `A small tactics board with acid lime arrows and dots drawn on a dark green surface, no lettering, slight perspective.` |
| `russia` | Российский футбол | `A coiled knitted supporters scarf in white, muted blue and muted red stripes, with a football tucked into the coil.` |

По «Правилам» осознанно взят один свисток без карточек: жёлтый и красный в этой игре означают
предупреждение и удаление, и на иконке фланга они читались бы как тревога.

### Четыре ролевых фланга

Эти карточки в игре подписаны золотом и стоят рядом с обычными. Значит, иконки должны читаться
как отдельная, «своя» линейка: та же геометрия и та же толщина, но теплее и золотистее.
Добавьте к промпту `warmer gold-tinted palette, distinctly warmer than the rest of the icon set`.

| Слот | Фланг | Промпт |
|---|---|---|
| `gk` | Вратари | `A pair of goalkeeper gloves standing upright side by side, thick padded backs, textured palms.` |
| `def` | Защитники | `A rounded heraldic shield with a faint football panel pattern embossed on its face, thick bevelled rim.` |
| `mid` | Полузащитники | `A metal gear wheel with a football set into its centre hub.` |
| `fwd` | Нападающие | `A football boot caught at the moment of striking a ball, with a short curved motion trail behind it.` |

---

# 4. Куда ещё — по убыванию отдачи

## 4.1 Вратарь для пенальти — шесть кадров

**Слоты:** `ASSETS.keeper.idle` / `.leanL` / `.leanR` / `.diveL` / `.diveR` / `.diveC`
**Размер:** 1200×550 каждый, **один и тот же холст** · **Альфа:** обязательна

Самое слабое место игры сейчас и одновременно пиковый момент матча. Здесь есть нюанс, ради
которого движок специально переделан: **все шесть кадров рисуются на общем холсте размером
ворот, поза уже внутри кадра.** Код не крутит и не двигает картинку — он меняет кадр целиком.
Поэтому в кадре «прыжок влево» вратарь уже нарисован в левом углу в полёте, и тело может
выходить за пределы створа.

Форма — яркая, но **не зелёная и не лаймовая**: он на фоне газона и рядом с лаймовым
интерфейсом. Оранжевый, бирюзовый или фуксия читаются идеально.

Общий кусок для всех шести:

```
KEEPER FRAME: wide 1200x550 canvas matching a football goal mouth, camera straight on from the
penalty spot, the goalkeeper drawn in place inside this frame at correct scale. Bright orange
goalkeeper kit with dark trim and padded gloves, plain fictional design without markings. Isolated
on a fully transparent background — no goal, no net, no pitch, no cast shadow. Identical character,
identical kit, identical camera and identical canvas across all six frames.
```

| Кадр | Промпт |
|---|---|
| `idle` | `Goalkeeper standing centred in the goal mouth in a ready stance, feet apart, arms out and low, focused straight at the camera.` |
| `leanL` | `Goalkeeper still on his feet but clearly leaning and shifting weight to his left, shoulders tilted, one foot loading — a readable pre-dive tell.` |
| `leanR` | `Goalkeeper still on his feet but clearly leaning and shifting weight to his right, shoulders tilted, one foot loading — a readable pre-dive tell.` |
| `diveL` | `Goalkeeper in a full horizontal dive to his left, body almost parallel to the ground, both arms stretched out, legs trailing.` |
| `diveR` | `Goalkeeper in a full horizontal dive to his right, body almost parallel to the ground, both arms stretched out, legs trailing.` |
| `diveC` | `Goalkeeper staying central, exploding straight upward with both arms stretched high above his head, feet just off the ground.` |

Наклоны — это подсказка игроку перед ударом. Если они не читаются издалека, механика чтения
вратаря не работает, и мини-игра превращается в лотерею. Это важнее анатомической точности.

## 4.2 Ворота

**Слот:** `ASSETS.goal` · **Размер:** 1200×550, тот же холст, что у вратаря · **Альфа:** обязательна

```
A football goal seen straight on from the penalty spot: white goal frame with crossbar and two
posts, taut semi-transparent netting behind, slight sag in the net. The background behind the net
is fully transparent so the scene shows through. No pitch, no grass, no ground line at the bottom.
Wide canvas matching the goal proportions.
```

Нижнюю кромку не рисуйте: под ворота код подставляет свою полосу газона.

## 4.3 Мяч

**Слот:** `ASSETS.ball` · **Размер:** 128×128 · **Альфа:** обязательна

Один файл на всё: и на лестницу зон, где он размером 18 пикселей, и на пенальти. Значит, крупные
контрастные пятна и никакой мелкой графики.

```
A classic football with bold black pentagon panels on white, three-quarter view, clean and simple,
strong top light with a soft highlight, slight gloss. Isolated on a fully transparent background,
no shadow. The panel pattern must stay readable when the image is scaled down to 18 pixels.
```

## 4.4 Комментатор

**Слоты:** `ASSETS.host.idle` / `.ok` / `.bad` / `.card` / `.win` · **Размер:** 400×400 · **Альфа:** не нужна

Самый недооценённый ассет: он превращает текстовую строку внизу экрана в живого человека,
который радуется и расстраивается вместе с игроком. Кадр обрезается в круг диаметром около
40 пикселей — значит, лицо крупно и по центру, эмоция читается по одному лицу, без жестов.

```
HOST FRAME: chest-up portrait of a friendly male football commentator in a headset, seated in a
dark stadium commentary box with blurred floodlights behind him. Face large and centred in the
frame, warm key light. Identical character, identical clothing, identical camera and framing
across all five portraits — only the facial expression changes. Square canvas.
```

| Кадр | Эмоция |
|---|---|
| `idle` | `Calm and attentive, neutral professional expression.` |
| `ok` | `Pleased and approving, warm smile, eyebrows up.` |
| `bad` | `Disappointed, wincing, hand half-raised toward his face.` |
| `card` | `Stern and serious, frowning, lips pressed together.` |
| `win` | `Ecstatic, mouth wide open mid-shout, both fists up in celebration.` |

## 4.5 Карточки

**Слоты:** `ASSETS.card.y`, `ASSETS.card.r` · **Размер:** 500×735 · **Альфа:** обязательна

Показываются на весь экран, детали видно.

```
A referee's [yellow / red] card held up at a slight angle, plain plastic surface with a subtle
grain, a bright specular glare sweeping across it, softly rounded corners. Isolated on a fully
transparent background. No hand, no arm, no text on the card. Portrait canvas.
```

Жёлтая — `#FFD60A`, красная — `#FF3B30`, ровно те же, что в интерфейсе.

## 4.6 Логотип

**Слот:** `ASSETS.logo` · **Размер:** 1440×440 · **Альфа:** обязательна

Единственное исключение из запрета на текст — здесь надпись и есть содержание. Но генератор
буквы всё равно испортит, поэтому просите **только знак**, а типографику соберите отдельно
в редакторе. Либо закажите локап живому дизайнеру.

```
Emblem for a football quiz game: a bold shield-and-ball badge, gold and acid lime on deep
graphite, with fifteen small chevrons rising along its edge like steps. Metallic, glossy,
game-logo style, centred, isolated on a fully transparent background. No text, no letters.
```

Пятнадцать шевронов — это пятнадцать шагов, тот самый счётчик из названия.

## 4.7 Кубок на экран победы

**Слот:** `ASSETS.trophy` · **Размер:** 300×300 · **Альфа:** обязательна

```
A golden football trophy cup with a small globe on top, ornate but clean, brilliant warm gold with
strong specular highlights and a faint glow, tiny sparkles around it. Isolated on a fully
transparent background. Square canvas.
```

## 4.8 Газон

**Слот:** `ASSETS.turf` · **Размер:** 640×1440 · **Альфа:** не нужна

Подстилается под лестницу зон вместо CSS-полос.

```
Top-down texture of a perfectly mown football pitch, alternating light and dark green stripes
running across the short side, fine grass detail, soft even lighting, no markings, no lines, no
objects. Seamless and even across the whole image. Vertical canvas.
```

Разметку не рисуйте: штрафные, круг и линии код накладывает сверху сам.

## 4.9 Иконки инструментов

**Слоты:** `ASSETS.tool.*` · **Размер:** 96×96 · **Альфа:** обязательна

На экране они около 20 пикселей, поэтому силуэт максимально простой, почти монохромный.
Собирайте одним заходом с тем же `ICON FRAME`, добавив `flat monochrome silhouette style,
single colour, no small details`.

| Слот | Кнопка | Промпт |
|---|---|---|
| `offside` | Офсайд (50:50) | `A linesman's flag raised on a short pole, simple bold silhouette.` |
| `coach` | Тренер | `A coach's clipboard with a whistle hanging over its corner.` |
| `stands` | Трибуны | `A megaphone pointing up and to the right, simple bold silhouette.` |
| `var` | VAR | `A small monitor screen on a stand, seen at a slight angle.` |
| `time` | Добавленное время | `A fourth official's electronic substitution board held up, blank display.` |
| `attack` | Атака | `A thick arrow surging forward and upward, with a short speed trail.` |
| `cash` | Удержание | `A closed padlock with a football resting against its base.` |

## 4.10 Иконка и обложка для каталога Яндекс.Игр

Это нужно для публикации независимо от того, что происходит внутри игры. **Актуальные размеры
берите прямо в Консоли разработчика** — они менялись, и полагаться на память тут нельзя.

Иконка:

```
App icon for a football quiz game: a football and a golden number-shaped trophy on a deep graphite
background with a subtle acid lime glow, bold centred composition, strong silhouette that stays
readable at 64 pixels, slight vignette. No text. Square canvas.
```

Обложка каталога:

```
Wide key art banner for a football quiz game: a night stadium under floodlights, a football
resting on the pitch in the lower left, a golden trophy glowing in the upper right, dramatic
lighting, deep graphite and green with acid lime and gold accents, wide empty space in the centre
left for a title to be placed later. No text. Wide banner canvas.
```

Промо-скриншоты для карточки игры генерировать не надо — их снимают с самой игры.

---

## 4.11 Фоны экрана загрузки и стартового экрана

**Слоты:** `ASSETS.loading` и `ASSETS.splash` · **Размер:** 1920×1080 · **Альфа:** не нужна

Оба экрана уже работают: загрузка показывает реальный прогресс, стартовый экран — большая
кнопка «ИГРАТЬ». Пока свои фоны не положены, под ними виден общий фон стадиона — уже неплохо,
так что эти два файла опциональны. Если делать, требование то же, что у главного фона:
**центр и нижняя треть тёмные и пустые** — там логотип, полоса прогресса и кнопка.

Экран загрузки — уместен кадр «до матча»: тоннель, раздевалка, газон крупно:

```
View from inside a stadium players' tunnel at night, looking out toward a brightly lit football
pitch in the distance, dark tunnel walls framing the shot, warm golden light spilling in from the
pitch. The centre and lower half of the frame are dark and empty for interface elements.

Style: polished semi-realistic 3D casual game art, premium mobile game quality, warm golden
lighting, soft haze, rich saturated colours.

Do not include: text, letters, numbers, watermark, logos, real club crests, people, players.

Aspect ratio 16:9.
```

Стартовый экран — праздничный кадр, можно с золотым дождём конфетти по краям:

```
A night football stadium seen from the centre circle, camera low over the grass, packed glowing
stands all around, four floodlight towers blazing, thin streams of golden confetti falling at the
left and right edges of the frame. The centre of the frame is dark and empty for a logo and a
button.

Style: polished semi-realistic 3D casual game art, premium mobile game quality, warm golden
lighting, soft haze, rich saturated colours, celebratory mood.

Do not include: text, letters, numbers, watermark, logos, real club crests, people, players.

Aspect ratio 16:9.
```

# Что можно добавить потом

Слотов под это сейчас нет, но добавить их — работа на десять минут, если решите, что нужно:

- **Экран загрузки.** Отдельный кадр с логотипом и полосой прогресса, пока грузится игра.
  На Яндекс.Играх это первое, что видит человек.
- **Фон экрана итога.** Раздевалка или выходной тоннель под результатами матча — сейчас там
  просто размытая игра.
- **Кадр выхода из тоннеля** на старте матча, как заставка перед первым вопросом.

---

# Приёмка

Прежде чем считать набор готовым:

- [ ] Ни на одной картинке нет текста, цифр и подписей.
- [ ] Нет реальных клубных эмблем и узнаваемых лиц.
- [ ] Все иконки уменьшены до 24 px и всё ещё читаются.
- [ ] Центр заставки тёмный и пустой — панель вопроса на нём читается.
- [ ] Шесть кадров вратаря на одинаковом холсте, наклоны различимы издалека.
- [ ] Четыре фигуры амплуа одного роста и в одной форме, кроме вратаря.
- [ ] Жёлтый и красный не встречаются нигде, кроме карточек.
- [ ] Всё, что должно быть с альфой, — с альфой, без белой подложки.
- [ ] После раскладки файлов `document.documentElement.className` в консоли показывает
      ожидаемые `has-*`.

---

# Пример для русскоязычного генератора

Если пользуетесь Кандинским или Шедеврумом, переводите дословно — структура та же:

```
Широкий кадр современного футбольного стадиона ночью, вид с уровня поля. Пустой зелёный газон
полосами в нижней трети, тёмные заполненные трибуны слева и справа, четыре мачты прожекторов
светят тёплым белым на фоне глубокого сине-чёрного неба, в лучах видна дымка. Центр кадра
намеренно тёмный, спокойный и пустой — без игроков, без мяча, без предметов, — а весь блеск и
детали в верхних углах. Кинематографично, атмосферно, лёгкий широкий угол.

Стиль: сочная полуреалистичная 3D-графика казуальной мобильной игры, ночное стадионное
освещение, тёплый контровой свет, мягкая дымка, насыщенные цвета. Палитра: тёмный графит,
сочный зелёный газон, кислотный лайм, золото. Без текста.

Не надо: текста, букв, цифр, водяных знаков, логотипов, реальных клубных эмблем, узнаваемых
футболистов, плоского света, мутных цветов, захламлённого кадра.
```
