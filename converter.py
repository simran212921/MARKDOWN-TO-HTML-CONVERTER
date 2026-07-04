def convert_markdown_to_html(markdown_text):
    html = []

    lines = markdown_text.split("\n")

    for line in lines:

        # Heading 1
        if line.startswith("# "):
            html.append(f"<h1>{line[2:]}</h1>")

        # Heading 2
        elif line.startswith("## "):
            html.append(f"<h2>{line[3:]}</h2>")

        # Heading 3
        elif line.startswith("### "):
            html.append(f"<h3>{line[4:]}</h3>")

        # Bold
        elif line.startswith("**") and line.endswith("**"):
            text = line[2:-2]
            html.append(f"<p><b>{text}</b></p>")

        # Normal paragraph
        elif line.strip() != "":
            html.append(f"<p>{line}</p>")

    return "\n".join(html)


# Read markdown file
with open("sample.md", "r") as file:
    markdown = file.read()

# Convert
html = convert_markdown_to_html(markdown)

# Save HTML
with open("output.html", "w") as file:
    file.write(html)

print("HTML file created successfully!")
