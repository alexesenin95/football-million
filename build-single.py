#!/usr/bin/env python3
"""Сборка игры в один самодостаточный HTML-файл.

Зачем: обычная версия ссылается на questions.js и шрифты из assets/, что удобно
для правок и для git. Но иногда нужен ровно один файл — мгновенное превью,
отправка ссылкой, публикация там, где нельзя выложить папку. Скрипт вшивает
базу вопросов и шрифты (как data:URI) прямо в HTML.

Использование:
    python3 build-single.py                      # -> dist/football-million.html
    python3 build-single.py путь/имя.html        # свой путь
    python3 build-single.py --bare имя.html      # без <!DOCTYPE>/<html>/<head>/<body>
                                                 # (для площадок, которые оборачивают сами)

Результат не коммитится: *.html в dist/ — сборочный артефакт.
"""
import base64
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = [
    "assets/fonts/unbounded-cyrillic-c86556.woff2",
    "assets/fonts/unbounded-latin-06f2e4.woff2",
    "assets/fonts/nunito-cyrillic-373a90.woff2",
    "assets/fonts/nunito-latin-798ec6.woff2",
]


def build(bare=False):
    src = open(os.path.join(HERE, "index.html"), encoding="utf-8").read()

    # Шрифты -> data:URI.
    for rel in FONTS:
        raw = open(os.path.join(HERE, rel), "rb").read()
        uri = "data:font/woff2;base64," + base64.b64encode(raw).decode()
        if "url(%s)" % rel not in src:
            raise SystemExit("в index.html нет ссылки на шрифт %s" % rel)
        src = src.replace("url(%s)" % rel, "url(%s)" % uri)

    # База вопросов -> инлайн.
    questions = open(os.path.join(HERE, "questions.js"), encoding="utf-8").read()
    tag = '<script src="questions.js"></script>'
    if tag not in src:
        raise SystemExit("в index.html нет подключения questions.js")
    src = src.replace(tag, "<script>\n" + questions + "\n</script>")

    # Подключённая графика из ASSETS (пути вида "assets/...") -> data:URI.
    # В репозитории игра ссылается на файлы, но одиночный файл должен нести их в себе.
    MIME = {".webp": "image/webp", ".png": "image/png", ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg", ".svg": "image/svg+xml", ".gif": "image/gif",
            ".mp3": "audio/mpeg", ".ogg": "audio/ogg"}
    def inline_asset(m):
        rel = m.group(1)
        path = os.path.join(HERE, rel)
        ext = os.path.splitext(rel)[1].lower()
        if ext in (".woff2",):                       # шрифты уже вшиты выше
            return m.group(0)
        if not os.path.isfile(path):
            raise SystemExit("в ASSETS указан несуществующий файл: %s" % rel)
        if ext not in MIME:
            raise SystemExit("неизвестный тип файла в ASSETS: %s" % rel)
        data = base64.b64encode(open(path, "rb").read()).decode()
        return '"data:%s;base64,%s"' % (MIME[ext], data)
    src = re.sub(r'"(assets/[^"]+)"', inline_asset, src)

    if bare:
        # Снимаем обвязку документа: <title> должен остаться первой строкой.
        src = re.sub(r'^<!DOCTYPE html>\s*<html lang="ru">\s*<head>\s*', "", src)
        src = src.replace('<meta charset="utf-8">\n', "")
        for name in ("viewport", "theme-color"):
            src = re.sub(r'<meta name="%s"[^>]*>\n' % name, "", src)
        src = re.sub(r'<link rel="icon"[^>]*>\n', "", src)
        src = src.replace("</head>\n<body>\n", "").replace("</body>\n</html>\n", "")
        src = src.strip() + "\n"
        if not src.startswith("<title>"):
            raise SystemExit("после снятия обвязки <title> должен быть первой строкой")

    # Ничего внешнего остаться не должно — иначе одиночный файл не самодостаточен.
    # Подстановки вида src="${url}" — это шаблонные строки JS, а не ссылки на файлы.
    external = [
        u for u in re.findall(r'(?:src|href)="([^"]+)"', src)
        if not u.startswith("data:") and "${" not in u
    ]
    if external:
        raise SystemExit("остались внешние ссылки: %s" % ", ".join(external))
    return src


def main():
    args = [a for a in sys.argv[1:]]
    bare = "--bare" in args
    args = [a for a in args if a != "--bare"]
    out = args[0] if args else os.path.join(HERE, "dist", "football-million.html")
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    html = build(bare=bare)
    open(out, "w", encoding="utf-8").write(html)
    print("собрано: %s (%.0f КБ%s)" % (out, os.path.getsize(out) / 1024, ", без обвязки" if bare else ""))


if __name__ == "__main__":
    main()
