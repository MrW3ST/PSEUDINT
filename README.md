# PSEUDINT

> **Usage légal uniquement / Legal use only**

Un outil OSINT pour rechercher un pseudo sur plus de 30 plateformes simultanément.
An OSINT tool to search a username across 30+ platforms simultaneously.

---

## Français

### Présentation

**PSEUDINT** est un outil de renseignement en source ouverte (OSINT) permettant de vérifier en quelques secondes si un nom d'utilisateur est enregistré sur une trentaine de plateformes populaires : réseaux sociaux, plateformes de développement, jeux vidéo, streaming, forums, etc.

L'interface possède une esthétique rétro-terminal avec un thème sombre (Dracula) et un thème clair disponibles.

### Fonctionnalités

- Scan simultané de **30+ plateformes** (réseaux sociaux, dev, gaming, streaming...)
- Résultats en **temps réel** avec indicateurs visuels (trouvé / absent / erreur)
- **Export des résultats** : copie de toutes les URLs trouvées dans le presse-papier
- **Deux thèmes** : sombre (Dracula) et clair (vintage), sauvegardés localement
- Interface **responsive** (mobile-friendly)
- Détection intelligente par code HTTP et/ou analyse du corps de réponse

### Plateformes couvertes

| Catégorie | Plateformes |
|---|---|
| Réseaux sociaux | Twitter/X, Instagram, Facebook, TikTok, LinkedIn, Pinterest, Snapchat |
| Contenu & Forums | YouTube, Reddit, Medium, Tumblr, Patreon, OnlyFans |
| Développement | GitHub, GitLab, npm, PyPI, Hacker News, Dev.to, Replit |
| Gaming & Streaming | Twitch, Steam, Roblox, Chess.com, Lichess, Xbox |
| Adulte | Pornhub, Cam4, Stripchat, Chaturbate |

### Prérequis

- Python 3.8+
- pip

### Installation

```bash
git clone <repo-url>
cd osint-tool
pip install -r requirements.txt
```

### Utilisation

```bash
python app.py
```

Le serveur démarre sur `http://localhost:8000` et ouvre automatiquement votre navigateur.

1. Entrez un pseudo dans le champ de recherche
2. Cliquez sur **Rechercher**
3. Les résultats s'affichent en direct au fil du scan
4. Cliquez sur **Copier les résultats** pour exporter les URLs trouvées

### Structure du projet

```
osint-tool/
├── app.py              # Backend FastAPI (API + serveur)
├── platforms.py        # Définition des 30+ plateformes
├── requirements.txt    # Dépendances Python
└── static/
    └── index.html      # Interface utilisateur (HTML/CSS/JS)
```

### Stack technique

- **Backend** : Python, FastAPI, uvicorn, httpx
- **Frontend** : HTML5, CSS3, JavaScript vanilla

---

## English

### Overview

**PSEUDINT** is an open-source intelligence (OSINT) tool that checks in seconds whether a username is registered on 30+ popular platforms: social networks, developer platforms, gaming, streaming, forums, and more.

The interface features a retro terminal aesthetic with a dark (Dracula) and a light theme available.

### Features

- Simultaneous scan of **30+ platforms** (social, dev, gaming, streaming...)
- **Real-time results** with visual indicators (found / not found / error)
- **Export results**: copy all found URLs to clipboard in one click
- **Two themes**: dark (Dracula) and light (vintage), saved locally
- **Responsive** interface (mobile-friendly)
- Smart detection via HTTP status codes and/or response body analysis

### Covered Platforms

| Category | Platforms |
|---|---|
| Social Networks | Twitter/X, Instagram, Facebook, TikTok, LinkedIn, Pinterest, Snapchat |
| Content & Forums | YouTube, Reddit, Medium, Tumblr, Patreon, OnlyFans |
| Development | GitHub, GitLab, npm, PyPI, Hacker News, Dev.to, Replit |
| Gaming & Streaming | Twitch, Steam, Roblox, Chess.com, Lichess, Xbox |
| Adult | Pornhub, Cam4, Stripchat, Chaturbate |

### Requirements

- Python 3.8+
- pip

### Installation

```bash
git clone <repo-url>
cd osint-tool
pip install -r requirements.txt
```

### Usage

```bash
python app.py
```

The server starts on `http://localhost:8000` and automatically opens your browser.

1. Enter a username in the search field
2. Click **Rechercher** (Search)
3. Results appear live as each platform is checked
4. Click **Copier les résultats** to export all found URLs

### Project Structure

```
osint-tool/
├── app.py              # FastAPI backend (API + server)
├── platforms.py        # 30+ platform definitions
├── requirements.txt    # Python dependencies
└── static/
    └── index.html      # User interface (HTML/CSS/JS)
```

### Tech Stack

- **Backend**: Python, FastAPI, uvicorn, httpx
- **Frontend**: HTML5, CSS3, Vanilla JavaScript

### How It Works

The backend sends concurrent HTTP requests to all platforms simultaneously using `asyncio`. Each platform uses one of two detection methods:

- **status** — checks the HTTP response code (200 = found, 404 = not found)
- **body** — scans the response HTML for platform-specific "not found" strings

Results are returned as JSON and the frontend updates each card in real time.

---

## License / Licence

For **legal use only**. The author is not responsible for any misuse of this tool.
Pour **usage légal uniquement**. L'auteur décline toute responsabilité en cas d'utilisation abusive.
