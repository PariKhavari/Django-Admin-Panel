# Django-Admin-Panel

Ein robustes, erweiterbares Admin-Backend auf Basis von **Django** und **Django Admin**. 
Dieses Projekt liefert eine saubere Grundstruktur für Authentifizierung, Rollen & Berechtigungen, 
Konfiguration, Tests, CI/CD sowie Deployment (lokal, Docker, Cloud).

---

## Inhaltsverzeichnis
- [Überblick](#überblick)
- [Technischer Stack](#technischer-stack)
- [Schnellstart](#schnellstart)
- [Voraussetzungen](#voraussetzungen)
- [Installation & Einrichtung](#installation--einrichtung)
  - [1) Projekt klonen](#1-projekt-klonen)
  - [2) Virtuelle Umgebung](#2-virtuelle-umgebung)
  - [3) Abhängigkeiten installieren](#3-abhängigkeiten-installieren)
  - [4) Umgebungsvariablen](#4-umgebungsvariablen)
  - [5) Datenbank vorbereiten](#5-datenbank-vorbereiten)
  - [6) Superuser anlegen](#6-superuser-anlegen)
  - [7) Dev-Server starten](#7-dev-server-starten)
- [Nützliche Befehle](#nützliche-befehle)
- [Struktur des Projekts](#struktur-des-projekts)
- [Berechtigungen & Rollen](#berechtigungen--rollen)
- [Fixtures & Demo-Daten](#fixtures--demo-daten)
- [Tests & Qualitätssicherung](#tests--qualitätssicherung)
- [Docker & Container](#docker--container)
- [Deployment](#deployment)
- [Sicherheit](#sicherheit)
- [Troubleshooting](#troubleshooting)
- [Beitragende & Richtlinien](#beitragende--richtlinien)
- [Lizenz](#lizenz)
- [Changelog (Beispiel)](#changelog-beispiel)

---

## Überblick

**Ziel**: Ein zentrales Admin-Panel für interne Teams mit sicheren Login-Flows, 
rollenbasierten Berechtigungen, auditierbaren Änderungen (Log-Entries) und stabiler Basis für Erweiterungen 
(z. B. eigene Admin-Aktionen, Custom-ModelAdmins, Inlines, Filter).

**Highlights**:
- Django Admin hartgehärtet (Sicherheits-Header, CSP, CSRF, sichere Cookies)
- Role-Based Access Control (RBAC) via Gruppen & Berechtigungen
- Settings nach Umgebungen getrennt (dev/stage/prod)
- Out-of-the-box CI-Test-Setup und Linters
- Optionales Docker-Setup für reproduzierbare Runs

---

## Technischer Stack

- **Python** ≥ 3.11
- **Django** ≥ 5.x
- **PostgreSQL** (empfohlen) oder SQLite (lokal)
- **Django Admin** + Erweiterungen (Filter, Actions, AdminSite-Branding)
- **pytest** + **coverage** für Tests
- **ruff** / **flake8** (alternativ) für Linting, **black** für Formatierung
- **Docker**/**docker-compose** (optional)

---

## Schnellstart

```bash
# 1) Abhängigkeiten
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -U pip

# 2) Install
pip install -r requirements.txt

# 3) Env
cp .env.example .env        # passe Werte an

# 4) DB & Migrations
python manage.py migrate

# 5) Superuser
python manage.py createsuperuser

# 6) Start
python manage.py runserver 0.0.0.0:8000

# Admin aufrufen
# http://127.0.0.1:8000/admin/
```

---

## Voraussetzungen

- Python 3.11+ installiert
- Optional: Docker, docker-compose
- Optional: PostgreSQL 14+ (lokal oder remote)
- Git

---

## Installation & Einrichtung

### 1) Projekt klonen

```bash
git clone https://example.com/your-org/django-admin-panel.git
cd django-admin-panel
```

### 2) Virtuelle Umgebung

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell
# .venv\Scripts\Activate.ps1
```

### 3) Abhängigkeiten installieren

```bash
pip install -U pip
pip install -r requirements.txt
# Optional: Dev-Extras
pip install -r requirements-dev.txt
```

### 4) Umgebungsvariablen

Lege eine `.env` an (oder nutze `.env.example` als Vorlage):

```ini
# .env
DJANGO_SETTINGS_MODULE=config.settings.dev
SECRET_KEY=wechsel-mich-unbedingt
DEBUG=True

# Datenbank (PostgreSQL empfohlen)
DB_ENGINE=django.db.backends.postgresql
DB_NAME=adminpanel
DB_USER=adminpanel
DB_PASSWORD=adminpanel
DB_HOST=127.0.0.1
DB_PORT=5432

# Sicherheit / Cookies
SESSION_COOKIE_SECURE=False
CSRF_COOKIE_SECURE=False
ALLOWED_HOSTS=127.0.0.1,localhost

# E-Mail (Konsole in dev)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend

# Timezone/Language
TIME_ZONE=Europe/Berlin
LANGUAGE_CODE=de
```

**Hinweis:** In Produktion `DEBUG=False`, sichere Cookies aktivieren und `ALLOWED_HOSTS` korrekt setzen.

### 5) Datenbank vorbereiten

```bash
python manage.py migrate
```

### 6) Superuser anlegen

```bash
python manage.py createsuperuser
```

### 7) Dev-Server starten

```bash
python manage.py runserver 0.0.0.0:8000
```

Admin-Login unter `http://127.0.0.1:8000/admin/`.

---

## Nützliche Befehle

```bash
# Statische Dateien sammeln (prod)
python manage.py collectstatic --noinput

# Benutzer & Gruppen verwalten (Beispiele via manage.py shell, s. unten)
python manage.py shell

# DB-Seed (falls implementiert)
python manage.py loaddata fixtures/base.json
```

---

## Struktur des Projekts

```text
django-admin-panel/
├─ config/
│  ├─ settings/
│  │  ├─ base.py         # gemeinsame Basiseinstellungen
│  │  ├─ dev.py          # Entwicklungsmodus
│  │  ├─ prod.py         # Produktionsmodus
│  ├─ urls.py            # URL-Routing (inkl. /admin/)
│  ├─ wsgi.py            # WSGI entrypoint
│  ├─ asgi.py            # ASGI entrypoint (optional)
├─ apps/
│  ├─ core/              # Basismodelle, Utilities
│  ├─ accounts/          # Benutzer, Gruppen, Rollen
│  └─ ...
├─ templates/
│  └─ admin/             # Branding/Overrides für Django Admin
├─ static/
│  └─ admin/             # custom CSS/JS für Admin
├─ manage.py
├─ requirements.txt
├─ requirements-dev.txt
├─ .env.example
└─ README.md
```

---

## Berechtigungen & Rollen

- **Empfohlen:** Rechte über **Gruppen** vergeben (RBAC).
- Beispiel (in `manage.py shell`):
  ```python
  from django.contrib.auth.models import Group, Permission, User
  editors, _ = Group.objects.get_or_create(name="Editors")
  perms = Permission.objects.filter(codename__in=["add_user", "change_user", "view_user"])
  editors.permissions.add(*perms)

  u = User.objects.create_user("editor1", password="change-me")
  u.groups.add(editors)
  ```
- Custom-AdminSite nutzen, um Branding und Zugriff einzuschränken.
- Eigene **Admin-Aktionen** und **ModelAdmins** implementieren (Filter, list_display, search_fields).

---

## Fixtures & Demo-Daten

- Lege JSON-Fixtures in `fixtures/` ab und lade sie mit:
  ```bash
  python manage.py loaddata fixtures/base.json
  ```
- Für Produktivsysteme: nur minimal benötigte Seeds (z. B. Gruppen/Rollen).

---

## Tests & Qualitätssicherung

```bash
# Unit-/Integrationstests
pytest -q

# Coverage
coverage run -m pytest
coverage html  # Report in htmlcov/index.html

# Linting & Formatierung
ruff check .
black --check .
black .         # zum Formatieren
```

Optionales `pre-commit`-Setup (Auszug aus `.pre-commit-config.yaml`):

```yaml
repos:
  - repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: v0.6.9
    hooks:
      - id: ruff
  - repo: https://github.com/psf/black
    rev: 24.8.0
    hooks:
      - id: black
```

---

## Docker & Container

**docker-compose.yml (Beispielauszug):**
```yaml
services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    env_file: .env
    depends_on:
      - db

  db:
    image: postgres:16
    environment:
      POSTGRES_DB: adminpanel
      POSTGRES_USER: adminpanel
      POSTGRES_PASSWORD: adminpanel
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

**Docker Quickstart:**
```bash
docker compose up --build
# Admin: http://localhost:8000/admin/
```

---

## Deployment

- **Empfohlen:** WSGI/ASGI-Server (gunicorn/uvicorn) hinter Nginx/Apache.
- **Statische Dateien** via `collectstatic` bereitstellen.
- **Env**: `DEBUG=False`, sichere Cookies, konkrete `ALLOWED_HOSTS`, starke `SECRET_KEY`.
- Datenbank-Verbindungen, Caches (Redis/Memcached) und E-Mail-Provider konfigurieren.
- Health-Checks und Backups einrichten.
- Beispiel Gunicorn (systemd):
  ```ini
  [Unit]
  Description=gunicorn daemon
  After=network.target

  [Service]
  User=www-data
  Group=www-data
  WorkingDirectory=/srv/django-admin-panel
  ExecStart=/srv/django-admin-panel/.venv/bin/gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3

  [Install]
  WantedBy=multi-user.target
  ```

---

## Sicherheit

- Setze **SECURE_HSTS_SECONDS**, **SECURE_SSL_REDIRECT**, **SESSION_COOKIE_SECURE**, **CSRF_COOKIE_SECURE** in Prod.
- Nutze **Content Security Policy (CSP)**, z. B. über `django-csp`.
- Aktiviere **X-Content-Type-Options**, **X-Frame-Options**, **Referrer-Policy**.
- Verwende starke Passwörter, 2FA (z. B. per `django-otp`) für sensible Admins.
- Begrenze Login-Versuche (z. B. `django-axes`) und aktiviere Logging/Auditing.
- Regelmäßige Updates/Dependencies prüfen (Dependabot, pip-audit).

---

## Troubleshooting

- **`DisallowedHost`:** `ALLOWED_HOSTS` korrekt setzen.
- **`OperationalError (db)`:** DB-Verbindung checken, Migrations ausführen.
- **Statische Dateien fehlen:** `collectstatic` und Nginx-Config prüfen.
- **Admin-Branding nicht sichtbar:** `TEMPLATES`-Pfad & Caches leeren.
- **`CSRF`-Fehler:** korrekte Domäne/HTTPS & Cookies prüfen.

---

## Beitragende & Richtlinien

- Feature-Branches nutzen, PRs mit Tests.
- Konventionen: PEP8, Type Hints wo sinnvoll.
- Commits im Imperativ, kleine, nachvollziehbare Änderungen.
- PR-Template & Issue-Templates verwenden (falls vorhanden).
- Code-Reviews erwünscht.

---

## Lizenz

Dieses Projekt steht unter der **MIT-Lizenz** (oder Organisation entsprechend anpassen). 
Siehe `LICENSE`-Datei.

---

## Changelog (Beispiel)

### [Unreleased]
- ✨ Neue Admin-Aktion: Export als CSV
- 🛠️ Refactor: Konsistentes Logging
- 🐛 Fix: Pagination im Benutzer-Admin

### 0.1.0 – Initial Release
- Grundgerüst mit Django 5, Admin, RBAC-Basis, Tests & Docker
