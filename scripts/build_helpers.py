"""Shared HTML helpers for build.py and pages.py."""
import html


def esc(text):
    return html.escape(text, quote=True)


def table(columns, rows):
    """columns[0] labels the row header; rows are lists of plain-text or HTML cells."""
    head = "".join(
        f'<th scope="col">{c}</th>' if i else f'<th scope="col"><span class="sr-only">{c}</span></th>'
        for i, c in enumerate(columns)
    )
    body = ""
    for row in rows:
        cells = "".join(f'<td data-label="{esc(columns[i + 1])}">{cell}</td>' for i, cell in enumerate(row[1:]))
        body += f'<tr><th scope="row">{row[0]}</th>{cells}</tr>\n'
    return f'<table class="compare"><thead><tr>{head}</tr></thead>\n<tbody>\n{body}</tbody></table>'
