# NEXYRA Hackathon Website

A responsive hackathon landing page built with HTML/CSS/JavaScript and a Flask + SQLite backend.

## Run locally

1. Install Python 3.10+.
2. Open a terminal in this folder.
3. Create a virtual environment (optional):
   `python -m venv .venv`
4. Activate it:
   Windows: `.venv\Scripts\activate`
5. Install dependencies:
   `pip install -r requirements.txt`
6. Start:
   `python app.py`
7. Open: http://127.0.0.1:5000

Registrations are stored in `nexyra.db`.

## Important before public deployment

- Add authentication to `/api/registrations`.
- Move secrets/configuration to environment variables.
- Use a production WSGI server instead of Flask debug mode.
- Add server-side validation, rate limiting and email/OTP verification if required.
- Replace the Register form with your official registration/payment workflow if one already exists.
