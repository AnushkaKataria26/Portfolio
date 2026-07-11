import re

with open("index.html", "r") as f:
    content = f.read()

# Title and Logo
content = content.replace("<title>[Your Name] — Portfolio</title>", "<title>Anushka Kataria — Portfolio</title>")
content = content.replace('<div class="logo">[Your Name]</div>', '<div class="logo">Anushka Kataria</div>')

# Hero
content = content.replace("<h1>[Your Name]</h1>", "<h1>Anushka Kataria</h1>")
content = content.replace('<p>[One-line positioning: e.g. "Final-year CS student building ML and backend systems"]</p>', '<p>Software Developer and Machine Learning Enthusiast focused on backend development and scalable server-side systems</p>')

photo_html = '<div class="photo-placeholder"><img src="assets/photo.webp" alt="Anushka Kataria" class="photo" style="width: 100%; height: 100%; object-fit: cover;"></div>'
content = re.sub(r'<div class="photo-placeholder".*?</div>', photo_html, content, flags=re.DOTALL)

# CTA Buttons
content = content.replace('<a href="#projects" class="btn">[View Projects]</a>', '<a href="#projects" class="btn">View Projects</a>')
content = content.replace('<a href="#resume" class="btn">[Download Resume]</a>', '<a href="assets/resume.pdf" class="btn" download>Download Resume</a>')

# About
about_text = "Software Developer and Machine Learning Enthusiast proficient in Data Structures and Algorithms. I am passionate about solving complex problems through technology and critical thinking. My focus lies primarily in backend development and building robust, scalable server-side systems, complemented by a strong interest in applied machine learning."
content = content.replace('<p>[Placeholder bio: replace with 3-5 sentences covering background, focus area, and goals]</p>', f'<p>{about_text}</p>')

# Skills
skills_html = """
            <h3>Languages</h3>
            <ul>
                <li>Python</li>
                <li>C++</li>
            </ul>

            <h3>Machine Learning</h3>
            <ul>
                <li>Machine Learning & Deep Learning</li>
                <li>NLP</li>
                <li>scikit-learn & PyTorch</li>
                <li>Transformers (DistilBERT)</li>
            </ul>

            <h3>Backend/Systems</h3>
            <ul>
                <li>FastAPI</li>
                <li>SQL & PostgreSQL</li>
                <li>System Design</li>
                <li>Operating Systems & Computer Networks</li>
            </ul>

            <h3>Tools & Platforms</h3>
            <ul>
                <li>Git & GitHub</li>
                <li>MLflow</li>
                <li>Docker</li>
            </ul>
"""
content = re.sub(r'<h3>Languages</h3>.*?</ul>.*?<h3>Machine Learning</h3>.*?</ul>.*?<h3>Backend/Systems</h3>.*?</ul>.*?<h3>Tools & Platforms</h3>.*?</ul>', skills_html.strip(), content, flags=re.DOTALL)

# Projects
projects_html = """
            <div class="project-grid">
                
                <article class="project-card">
                    <div class="project-thumb"></div>
                    <h3>NexTrace</h3>
                    <p>Real Time Log Analytics & Search Platform with a custom inverted-index search engine.</p>
                    <ul class="tech-tags">
                        <li>C++</li>
                        <li>Python</li>
                        <li>SQL</li>
                    </ul>
                    <div class="project-links">
                        <a href="https://github.com/AnushkaKataria26/NexTrace" target="_blank" rel="noopener noreferrer">View Code</a>
                    </div>
                </article>

                <article class="project-card">
                    <div class="project-thumb"></div>
                    <h3>AsyncFlow</h3>
                    <p>Distributed Task Queue & Worker Processing Platform with lease-based dequeue.</p>
                    <ul class="tech-tags">
                        <li>C++</li>
                        <li>Python</li>
                        <li>PostgreSQL</li>
                    </ul>
                    <div class="project-links">
                        <a href="https://github.com/AnushkaKataria26/AsyncFlow" target="_blank" rel="noopener noreferrer">View Code</a>
                    </div>
                </article>

                <article class="project-card">
                    <div class="project-thumb"></div>
                    <h3>FactRadar</h3>
                    <p>Fake news classifier evaluating class-imbalance robustness and benchmarking DistilBERT.</p>
                    <ul class="tech-tags">
                        <li>Machine Learning</li>
                        <li>NLP</li>
                        <li>Transformers</li>
                    </ul>
                    <div class="project-links">
                        <a href="https://github.com/AnushkaKataria26/FactRadar" target="_blank" rel="noopener noreferrer">View Code</a>
                    </div>
                </article>

                <article class="project-card">
                    <div class="project-thumb"></div>
                    <h3>TruthLens</h3>
                    <p>Multimodal deepfake detection platform (Top 100 nationwide, AMD Slingshot Hackathon 2026).</p>
                    <ul class="tech-tags">
                        <li>Generative AI</li>
                        <li>Deep Learning</li>
                        <li>Multimodal AI</li>
                    </ul>
                    <div class="project-links">
                        <a href="https://github.com/AnushkaKataria26/TruthLens" target="_blank" rel="noopener noreferrer">View Code</a>
                    </div>
                </article>

            </div>
"""
content = re.sub(r'<div class="project-grid">.*?</div>\s*</section>', projects_html.strip() + '\n        </section>', content, flags=re.DOTALL)

# Experience & Education
experience_html = """
            <div class="timeline">
                
                <div class="timeline-entry">
                    <h3>Machine Learning Intern</h3>
                    <p class="timeline-meta">IPCA Laboratories · Jun 2026 – Jul 2026</p>
                    <p>Built a text preprocessing and entity extraction pipeline in Python using rule-based NLP (spaCy). Trained a supervised binary classifier to triage ADR vs. non-ADR intake records.</p>
                </div>

                <div class="timeline-entry">
                    <h3>Machine Learning Intern | FactRadar</h3>
                    <p class="timeline-meta">IBM PBEL Virtual Internship · Jun 2025 – Jul 2025</p>
                    <p>Built a fake news classifier using TF-IDF and Logistic Regression/SVM. Fine-tuned a DistilBERT transformer over the classical baseline.</p>
                </div>

                <div class="timeline-entry">
                    <h3>Bachelor of Technology - Computer Science and Engineering</h3>
                    <p class="timeline-meta">Mody University of Science and Technology · Aug 2023 – Present</p>
                    <p>CGPA: 7.67. Focused on Data Structures, Algorithms, and Core CS principles.</p>
                </div>

                <div class="timeline-entry">
                    <h3>Intermediate (XII)</h3>
                    <p class="timeline-meta">Pragati Convent H.S. School · Jul 2021 – Apr 2022</p>
                    <p>MP Board; Percentage: 88.2%</p>
                </div>

            </div>
"""
content = re.sub(r'<div class="timeline">.*?</div>\s*</section>', experience_html.strip() + '\n        </section>', content, flags=re.DOTALL)

# Resume
resume_html = """
            <h2>Resume</h2>
            <div class="resume-embed">
                <iframe src="assets/resume.pdf" title="Resume" style="width: 100%; height: 600px; border: none;">
                    <p>Preview unavailable — use the download link below.</p>
                </iframe>
            </div>
            <a href="assets/resume.pdf" class="btn" download>Download Resume PDF</a>
"""
content = re.sub(r'<h2>Resume</h2>.*?<a href="#" class="btn">\[Download Resume PDF\]</a>', resume_html.strip(), content, flags=re.DOTALL)

# Contact
contact_html = """
            <h2>Contact</h2>
            <p><a href="mailto:anushkakataria26@gmail.com">anushkakataria26@gmail.com</a></p>
            <div class="social-links">
                <a href="https://github.com/AnushkaKataria26" target="_blank" rel="noopener noreferrer">GitHub</a>
                <a href="https://linkedin.com/in/anushkakataria" target="_blank" rel="noopener noreferrer">LinkedIn</a>
            </div>
"""
content = re.sub(r'<h2>Contact</h2>.*?</div>', contact_html.strip(), content, flags=re.DOTALL)

# Footer
content = content.replace("© [Year] [Your Name]", "© 2026 Anushka Kataria")

with open("index.html", "w") as f:
    f.write(content)
