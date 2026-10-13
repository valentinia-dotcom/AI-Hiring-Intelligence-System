# AI Hiring Intelligence — Streamlit without n8n

This version directly uses Google Gemini for job-related **evidence extraction**, not automatic hiring decisions. It accepts up to 20 text PDFs, reviews each against a job description, and displays/downloads the results. It can save results to **the signed-in user's Google Sheets**.

## 1. GitHub

Replace your current repository root `app.py` and `requirements.txt` with the attached versions, leaving your original n8n workflow JSON untouched. Never commit credentials.

## 2. Gemini API key

Get a Gemini API key from Google AI Studio. In Streamlit Community Cloud, open your app's Settings → Secrets, and enter:

```toml
GEMINI_API_KEY = "YOUR_KEY"
```

This is sufficient to run resume analysis and download a CSV. No n8n webhook is needed.

## 3. Optional: allow each user to save into their own Google Drive

In Google Cloud Console:

1. Create/select a project.
2. Enable **Google Sheets API** (and ensure the OAuth consent screen is configured).
3. Configure the OAuth branding/consent screen, with **External** audience if you will allow outside users. While in testing, add permitted test accounts. Production usage can require Google's app verification, depending on audience and scopes.
4. Create an **OAuth client ID**, application type **Web application**.
5. Add your Streamlit app URL (including trailing `/`) as an **Authorized redirect URI**. It MUST match your `redirect_uri` secret exactly.
6. Copy client ID and secret to Streamlit's private Secrets settings, using `SECRETS_EXAMPLE.toml` as template. Set a unique, long, random `oauth_state_secret` and the real app redirect URL.
7. Restart/redeploy the app. Users click **Sign in with Google** before running analysis to connect Sheets for that browser session.

The app requests the `spreadsheets` OAuth scope. Users can create a new spreadsheet in their own Google Drive or append to an existing compatible spreadsheet they have permission to edit. A newly created sheet includes the `Candidate Results` tab and 11 headers.

**Returning user:** after reopening the app, sign in again, select **Append to an existing spreadsheet**, and paste its URL. A new sheet is NOT required. To retain a persistent default for a particular user across sessions, add a separate user settings store in the future.

Google Sheets permissions still apply: users cannot modify sheets they cannot access. Candidate information is sensitive; review your privacy notice, retention practices, and API data-handling terms before deploying publicly.

## 4. Limitations

- Text PDFs only: scanned-image PDFs require OCR.
- Google Sheets saving requires Cloud OAuth setup and a Google sign-in each session; no global service account or n8n.
- Gemini API usage may have costs or quotas.
- Gemini can make mistakes; results include evidence summaries but no automatic hire/reject decision or numeric candidate ranking.
- Simultaneous sessions and one-off failures should be tested on your deployment. The duplicate-save prevention covers the current Streamlit session only; it is not a persistent deduplication database.
- For a production, public multi-user product, add an authentication and consent policy and a durable database to track user sheet choices, audit logs and deduplication.
