# Engineer_Abuibraheem — AI Personal Website (Replit-ready)

This project is a simple personal website with an AI-powered assistant and a secure contact form.
Built for: Engineer_Abuibraheem

## Features
- Home, Projects, and AI Tools pages
- AI Text Assistant (calls OpenAI ChatCompletion)
- Secure contact form that sends messages to your email via SMTP

## Setup (Replit)
1. Create a new Python Repl and upload this project folder.
2. In Replit Secrets (the lock icon), set the following keys:
   - OPENAI_API_KEY : your OpenAI API key
   - EMAIL_USER : your SMTP email (e.g., your Gmail address)
   - EMAIL_PASS : your SMTP app password (for Gmail use an app password)
   - EMAIL_TO : your email address to receive contact form messages
3. Click Run. The app will be available at `https://<your-repl>.repl.co`

## Notes
- Do NOT commit your real API keys to public repos.
- If you prefer Google Gemini instead of OpenAI, you can replace the `/generate` logic with Gemini API calls.
