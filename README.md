# AI Hiring Intelligence — Supabase, Gemini and per-user Google Sheets

This version **does not need n8n**. It analyzes up to 20 text-based PDF resumes per run using Gemini, provides factual, job-related evidence for human review, saves users' default spreadsheet links in Supabase, and lets each person authorize their own Google account to create/append to their own Sheets.

## 1. Upload project files to GitHub

Replace your existing `app.py` and `requirements.txt` with the files in this folder. Keep `supabase_setup.sql` and `SECRETS_EXAMPLE.toml` for reference; **do not commit credentials**. Deploy the `main` branch, `app.py` entry point, on Streamlit Community Cloud.

## 2. Supabase setup

1. Create a project at https://supabase.com/dashboard .
2. In **SQL Editor**, run `supabase_setup.sql`. The `user_settings` table uses row-level security, and each user can read and modify only their own settings.
3. In **Project Settings / API**, copy your project URL and *publishable/anon* key (not the service-role key).
4. Under **Authentication / Providers / Email**, enable email/password. For production enable email verification, password recovery and rate limits, and review abuse protection.
5. Consider disabling public registrations once your intended users have joined.

## 3. Google Cloud OAuth setup

1. Create a Google Cloud project: https://console.cloud.google.com/ .
2. Enable **Google Sheets API**.
3. Configure Google Auth Platform / OAuth consent screen. Add the sensitive scope `https://www.googleapis.com/auth/spreadsheets` and publish or add test users as appropriate. External apps may require Google verification before broad public use. While in Testing, refresh tokens for this scope generally expire after 7 days. Users must reauthorize when needed.
4. Create **OAuth Client ID**, Application type **Web application**, with **Authorized redirect URI** exactly equal to your deployed Streamlit root URL, e.g. `https://my-hiring-app.streamlit.app/`. Use precisely the same URI in `GOOGLE_REDIRECT_URI` and in Google Cloud (including trailing slash if present).
5. Copy OAuth client ID and client secret to your Streamlit Secrets.
6. Users click **Connect my Google account**, consent to Sheets access, then they can create their own spreadsheet or paste an existing Sheet URL. Only spreadsheets that the authorized user can edit can be updated.

OAuth authentication is different from Streamlit/Supabase sign-in: the app uses Supabase for account identity and Google OAuth only when accessing that account's Google Sheets. The app encrypts Google refresh tokens before storage in its Supabase table; keep the encryption key secret and backed up. Do not change the key after users connect unless migrating existing encrypted tokens. A compromised Streamlit process could still expose Google tokens, so protect hosting/admin access and restrict the OAuth scope. Disconnect in the app deletes the stored credential but does not revoke previously issued Google tokens; users can revoke access in Google account security settings.

## 4. Gemini API key and Streamlit Secrets

Get a Gemini key from https://aistudio.google.com/apikey . In Streamlit Cloud → Settings → Secrets, paste the values from `SECRETS_EXAMPLE.toml` with real credentials. Generate the encryption key *locally* using:

```python
from cryptography.fernet import Fernet
print(Fernet.generate_key().decode())
```

Never upload filled secrets files or print secrets to logs. Gemini API costs/quotas and data handling policies depend on your account/settings; get consent to send resumes to Gemini.

## 5. Test checklist

- Register a test user and sign in (confirm email if enabled).
- Connect user Google account; authorize Sheets access.
- Use **Create a new Google Sheet in my Drive** or paste an existing URL and **Save as my default sheet**.
- Upload two small text-readable PDF resumes and enter the job description.
- Review the evidence summaries, then click **Append these results to my default Google Sheet**.
- Open the Sheet link and verify the `Candidate Results` tab contains one row per resume.
- Sign out and sign in again; the default Sheet URL persists. Check with a different user to verify isolation.

## Important limitations

- Only text PDFs are supported (no OCR for scans). File size max 10 MB each, 20 files per run.
- Candidate summaries are **not suitability scores, rankings, automatic hiring or rejection decisions**. Human reviewers should verify claims against source documents and ensure applicable employment/privacy compliance.
- CSV export is available even without Google authorization.
- To reduce accidental duplicates, saving the same analysis twice is blocked for the current Streamlit session; durable deduplication across browser sessions is not implemented.
- The service needs internet access, Google API enablement, valid OAuth consent, and Supabase. OAuth redirect handling assumes the authorization starts and finishes in the same Streamlit session. Some browser privacy settings or a reboot during consent can invalidate the temporary OAuth state; retry connection in that case.
