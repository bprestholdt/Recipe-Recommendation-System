# Recipe Recommendation System

An AI-powered recipe generation web app built with Django and the OpenAI API. Users register an account, enter ingredients they have on hand, and the app uses GPT-3.5 to generate a custom recipe that gets saved to their account history.

# Deployed Site Link: https://web-production-fb7b2.up.railway.app/

> First load may take a moment if the service has been idle.

## Features

- User registration and authentication
- AI recipe generation via OpenAI GPT-3.5 Turbo
- Recipe saved to user account on each generation
- PostgreSQL database in production (SQLite for local dev)
- Static file serving with WhiteNoise

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.12, Django 5.0 |
| AI | OpenAI GPT-3.5 Turbo |
| Database | PostgreSQL (prod), SQLite (dev) |
| Deployment | Railway |
| Static Files | WhiteNoise |

## Local Setup

**Prerequisites:** Python 3.10+, pip

```bash
# Clone the repo
git clone https://github.com/your-username/recipe-rec-system.git
cd recipe-rec-system

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Create your .env file
cp .env.example .env
# Edit .env and add your SECRET_KEY and OPENAI_API_KEY

# Run migrations
python manage.py migrate

# Start the dev server
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## Environment Variables

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | `True` for development, `False` for production |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hostnames |
| `OPENAI_API_KEY` | Your OpenAI API key |
| `DATABASE_URL` | PostgreSQL connection string (set automatically by Railway) |

See [.env.example](.env.example) for the full template.

## Deployment (Railway)

1. Push this repo to GitHub
2. Go to [railway.app](https://railway.app) and create a new project from your GitHub repo
3. Add a **PostgreSQL** plugin to the project (Railway sets `DATABASE_URL` automatically)
4. Set environment variables in Railway's dashboard:
   - `SECRET_KEY` — generate one at [djecrety.ir](https://djecrety.ir/)
   - `OPENAI_API_KEY` — your OpenAI key
   - `DEBUG` — `False`
   - `ALLOWED_HOSTS` — `your-app.up.railway.app`
5. Railway runs `gunicorn RecipeRecSystem.wsgi:application` via the Procfile
6. Run the release command once: `python manage.py migrate`

## Running Tests

```bash
pytest
```

## Author

Braden Prestholdt — [GitHub](https://github.com/your-username) · [LinkedIn](https://linkedin.com/in/your-profile)
