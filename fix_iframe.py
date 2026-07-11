with open("index.html", "r") as f:
    content = f.read()

content = content.replace('<iframe src="assets/resume.pdf" title="Resume" style="width: 100%; height: 600px; border: none;">\n                    Preview unavailable — use the download link below.\n                </iframe>', '<object data="assets/resume.pdf" type="application/pdf" width="100%" height="600px" title="Resume">\n                    <p>Preview unavailable — use the download link below.</p>\n                </object>')

with open("index.html", "w") as f:
    f.write(content)
