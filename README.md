# Recipe Recommendation System

An AI-powered recipe generation web app built with Django and the OpenAI API. Users register an account, enter ingredients they have on hand, and the app uses OpenAI's API to generate a custom recipe that gets saved to their account history.

# Deployed Site Link: (add your Vercel URL here after deploying)

## Features

- User registration and authentication
- AI recipe generation via the OpenAI API (model configurable, currently GPT-6 Luna)
- Recipe saved to user account on each generation
- PostgreSQL database in production (SQLite for local dev)
- Static file serving with WhiteNoise

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.12, Django 5.2 |
| AI | OpenAI API (GPT-6 Luna by default) |
| Database | PostgreSQL on Neon (prod), SQLite (dev) |
| Deployment | Vercel |
| Static Files | WhiteNoise |

## Local Setup

**Prerequisites:** Python 3.10+, pip

```bash
# Clone the repo
git clone https://github.com/bprestholdt/Recipe-Recommendation-System.git
cd Recipe-Recommendation-System

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
| `OPENAI_MODEL` | Optional; OpenAI model to use (default `gpt-6-luna`) |
| `DATABASE_URL` | PostgreSQL connection string (Neon) |

See [.env.example](.env.example) for the full template.

## Deployment (Vercel + Neon)

1. Create a free Postgres database on [Neon](https://neon.com) and copy its connection string
2. Import this repo as a new project in [Vercel](https://vercel.com); it detects Django from `manage.py`
3. Set environment variables in the Vercel project:
   - `DATABASE_URL` — the Neon connection string
   - `SECRET_KEY` — generate one at [djecrety.ir](https://djecrety.ir/)
   - `OPENAI_API_KEY` — your OpenAI key
   - `DEBUG` — `False`
   - `ALLOWED_HOSTS` — `.vercel.app`
4. Deploy. Each build runs `python manage.py migrate` (set in `pyproject.toml`), and Vercel collects and serves static files automatically

## Running Tests

```bash
pytest
```

## Author

Braden Prestholdt — [GitHub](https://github.com/bprestholdt) · [LinkedIn](https://linkedin.com/in/your-profile)
