from flask import Flask, render_template, make_response, jsonify

app = Flask(__name__)

# Cache static files for 1 year (browser caching)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 31536000


@app.after_request
def add_cache_headers(response):
    """Add caching headers to speed up repeat visits."""
    if "text/css" in response.content_type or "javascript" in response.content_type:
        response.headers["Cache-Control"] = "public, max-age=31536000"
    elif "text/html" in response.content_type:
        response.headers["Cache-Control"] = "public, max-age=300"
    return response


@app.route("/health")
def health():
    """Health check endpoint for keep-alive pings."""
    return jsonify(status="ok"), 200


@app.route("/")
def index():
    profile = {
        "name": "Hasmik Hovhannisyan",
        "title": "AI Engineering & Creative Design",
        "tagline": "Wo Technologie auf Kreativität trifft",
        "location": "Messel, Germany",
        "email": "hasmik.hovhannisyan86@gmail.com",
        "phone": "+49 0176 2867 6941",
        "about": (
            "Ich verbinde Technik mit Kreativität. Mit einem Hintergrund in Design "
            "und einer Leidenschaft für Programmierung bringe ich eine einzigartige "
            "Perspektive in die Softwareentwicklung. Derzeit absolviere ich eine "
            "Weiterbildung mit Schwerpunkt auf Python und Web-APIs. Ich denke visuell, "
            "arbeite strukturiert und lerne schnell neue Technologien. Mein Ziel ist es, "
            "Anwendungen zu entwickeln, die nicht nur funktionieren, sondern auch "
            "begeistern."
        ),
        "creative_skills": [
            "Design Thinking", "Visuelle Gestaltung", "UI/UX",
            "Kreative Konzeption", "Ästhetisches Gespür",
        ],
        "technical_skills": [
            "Python", "RESTful APIs", "OOP", "JavaScript",
            "HTML", "CSS", "SQLAlchemy",
        ],
        "soft_skills": [
            "Problemlösungsfähigkeit", "Teamarbeit", "Kommunikationsfähigkeit",
            "Organisationstalent", "Zuverlässigkeit", "Analytisches Denken",
        ],
        "languages": [
            {"name": "Armenisch", "level": "Muttersprache", "percent": 100},
            {"name": "Russisch", "level": "C2", "percent": 95},
            {"name": "Deutsch", "level": "C1", "percent": 85},
            {"name": "Englisch", "level": "B2", "percent": 70},
            {"name": "Spanisch", "level": "A1", "percent": 20},
        ],
        "education": [
            {
                "school": "Masterschool Institute of Technology",
                "degree": "Software Engineering — Weiterbildung",
                "period": "Sep 2025 – Mai 2026",
                "details": [
                    "Full-Stack-Anwendungen mit JavaScript, React, Node.js und SQL entwickelt",
                    "OOP, Test-Driven Development (TDD) sowie Versionskontrolle mit Git und GitHub angewendet",
                    "Skalierbare Anwendungen mit RESTful APIs, Cloud-Services und CI/CD-Pipelines entwickelt",
                ],
            },
            {
                "school": "Hochschule Darmstadt",
                "degree": "Bachelor in Information Science (3. Semester)",
                "period": "2021 – 2023",
                "details": [
                    "Informationsmanagement und Datenorganisation",
                    "Digitale Informationssysteme",
                    "Recherche und Analyse von Informationen",
                ],
            },
            {
                "school": "Technische Universität Darmstadt",
                "degree": "Masterstudium Informatik — Internet und Web-basierte Systeme (3. Semester)",
                "period": "2016 – 2019",
                "details": [
                    "Entwicklung und Analyse moderner Web- und Netzwerksysteme",
                    "Verteilte Systeme, Web-Technologien und digitale Netzwerke",
                ],
            },
            {
                "school": "ERICTA: European Regional Educational Academy",
                "degree": "Diplom Ingenieur — Automated Systems of Information Development",
                "period": "2003 – 2008",
                "details": [
                    "Informationssysteme: Entwicklung, Analyse und Verwaltung automatisierter IT-Systeme",
                    "Datenverarbeitung, Systemarchitektur und softwaregestützte Informationsprozesse",
                ],
            },
        ],
        "experience": [
            {
                "company": "Eyes and More",
                "role": "Kundenberatung",
                "period": "Nov 2024 – Dez 2025",
                "location": "Darmstadt, Deutschland",
                "details": [
                    "Kundenberatung und -betreuung in einem dynamischen Einzelhandelsumfeld",
                    "Starke Führungsqualitäten und herausragenden Kundenservice demonstriert",
                ],
            },
        ],
        "certificates": [
            {
                "name": "Hackathon",
                "issuer": "Masterschool Institute of Technology",
                "date": "November 2025",
            },
        ],
    }
    return render_template("index.html", profile=profile)


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
