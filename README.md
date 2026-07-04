# Markdown to HTML Converter

## Description

This is a beginner-friendly Python project that converts a simple Markdown file into an HTML file.

The program reads a Markdown file (`sample.md`), converts headings, paragraphs, and bold text into HTML, and saves the result as `output.html`.

## Internship Details
- Name : Simranjit Kaur
- Intern ID : CITS3897
- Organistation : CODTECH

## Features

- Convert Heading 1 (#)
- Convert Heading 2 (##)
- Convert Heading 3 (###)
- Convert Bold Text (**text**)
- Convert Paragraphs
- Save output as HTML

## Project Structure

```
markdown-to-html-converter/
│── converter.py
│── sample.md
│── output.html
│── README.md
│── requirements.txt
```

## Requirements

- Python 3.x

No external libraries are required.

## How to Run

1. Open the project in VS Code.
2. Open the terminal.
3. Run:

```bash
python converter.py
```

4. The HTML file (`output.html`) will be created automatically.

## Example Markdown

```markdown
# Hello

Welcome to Python.

## About

Learning is fun.

**Thank You**
```

## Output

```html
<h1>Hello</h1>
<p>Welcome to Python.</p>
<h2>About</h2>
<p>Learning is fun.</p>
<p><b>Thank You</b></p>
```
