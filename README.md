# AI Hiring Intelligence System

**AI-powered resume analysis with Google Gemini, Supabase authentication, persistent candidate history, and Excel reporting.**

[**Live Application**](https://ai-hiring-intelligence-system.streamlit.app/) | [**GitHub Repository**](https://github.com/valentinia-dotcom/AI-Hiring-Intelligence-System)

## Project Overview

AI Hiring Intelligence System is a web application that helps human reviewers examine job-related evidence from resumes.

Users can upload PDF resumes, enter a job description, and generate structured candidate summaries using Google Gemini AI.

The application supports secure user authentication, private candidate analysis history, duplicate resume detection, and downloadable Excel reports.

**Note:** This is a decision-support tool, not an automated hiring or candidate-ranking system. All AI-generated information requires human verification.

## Key Features

- **AI Resume Analysis:** Uses Google Gemini to extract job-relevant evidence from resumes.
- **Multiple Resume Uploads:** Supports up to 20 PDF resumes per analysis.
- **Duplicate Detection:** Uses SHA-256 hashing to identify identical PDFs within an upload batch.
- **Progress Tracking:** Displays analysis progress while resumes are processed.
- **Supabase Authentication:** Supports user registration and email/password sign-in.
- **Persistent Candidate History:** Saves candidate analysis results in Supabase so they remain available after logout.
- **User-Specific Data Access:** Uses Supabase Row Level Security (RLS) policies to restrict access to each user's own results.
- **Excel Export:** Allows users to download candidate results as `.xlsx` files.
- **CSV Export:** Supports CSV downloads.
- **Structured Analysis:** Presents candidate qualifications, experience, projects, education, and reviewer follow-up questions.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend application logic |
| Streamlit | Interactive web application |
| Google Gemini API | AI-powered resume evidence extraction |
| Supabase | Authentication and persistent database storage |
| PostgreSQL | Candidate analysis records |
| Pandas | Data processing and tabular results |
| PyMuPDF | PDF text extraction |
| XlsxWriter | Excel report generation |
| SHA-256 | Duplicate PDF detection |
| GitHub | Source code and version control |
| Streamlit Community Cloud | Application deployment |

## Application Workflow

1. Create an account or sign in.
2. Enter a job title and description.
3. Upload up to 20 PDF resumes.
4. Start the Gemini AI analysis.
5. Review structured candidate evidence in the dashboard.
6. Save the results to Supabase.
7. View saved candidate history after signing in again.
8. Download current or saved results in Excel format.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/valentinia-dotcom/AI-Hiring-Intelligence-System.git
cd AI-Hiring-Intelligence-System
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Supabase

Create a project using the [Supabase Dashboard](https://supabase.com/dashboard).

Enable email/password authentication.

Create the `candidate_results` table in the SQL Editor and enable Row Level Security to restrict users to their own records. The table must match the schema expected by `app.py`.

### 4. Configure Google Gemini

Generate an API key using [Google AI Studio](https://aistudio.google.com/apikey).

### 5. Set Streamlit Secrets

Configure the following values in Streamlit Secrets or in a local `.streamlit/secrets.toml` file:

```toml
SUPABASE_URL = "your_supabase_project_url"
SUPABASE_ANON_KEY = "your_supabase_anon_key"
GEMINI_API_KEY = "your_gemini_api_key"
```

Never commit real API keys or credentials to GitHub. Use the publishable/anon Supabase key rather than the service-role key.

### 6. Run the Application

```bash
streamlit run app.py
```

## Testing Checklist

- Register and sign in using Supabase.
- Upload text-readable PDF resumes.
- Enter a job description and run the Gemini analysis.
- Confirm that duplicate PDFs are skipped within the same batch.
- Verify the candidate evidence table.
- Save results to Supabase.
- Sign out and sign back in.
- Confirm that saved candidate history remains available.
- Download and open an Excel report.
- Sign in with another account and confirm that the first user's results are not visible.

## Security and Privacy

- Supabase handles user authentication.
- Database Row Level Security restricts access to user-specific candidate records.
- API keys are configured through Streamlit Secrets.
- Original PDF files are processed for analysis rather than intentionally stored in the candidate history table.
- Resume information is sent to the configured Gemini API for analysis.

Users should have appropriate permission to process candidate information and follow applicable privacy and employment laws.

## Limitations

- Supports text-readable PDF resumes only; scanned PDFs require OCR, which is not included.
- Supports up to 20 PDFs per batch, with a maximum of 10 MB per PDF.
- AI output may contain inaccuracies and must be independently verified.
- Analysis depends on Gemini API availability, quota limits, and network connectivity.
- Supabase storage and hosting are subject to service limits.
- The system does not score, rank, hire, or reject candidates automatically.

## Live Demo

**[Launch AI Hiring Intelligence System](https://ai-hiring-intelligence-system.streamlit.app/)**

## Future Improvements

- Candidate search and history filters.
- Advanced dashboard analytics.
- Improved downloadable reports.
- Optional OCR support for scanned resumes.
- Additional privacy and data-retention controls.

## Disclaimer

AI Hiring Intelligence System is intended to assist human reviewers by organizing job-related evidence. It does not make employment decisions. Users remain responsible for reviewing source documents and making decisions fairly and lawfully.
