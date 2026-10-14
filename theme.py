"""
Midnight Aurora — AI Hiring Intelligence System
Frontend theme only.
Includes:
- Midnight navy and Aurora gradient styling
- Geometric diamond logo
- Streamlit button, form, and input styling
- Candidate evidence table styling
- Sidebar and download button styling
- Responsive spacing
This module does not modify authentication, AI analysis,Supabase data, or Excel exports.
"""

import base64
import streamlit as st

# BRAND COLORS
 
COLORS = {
    "background": "#070D1D",
    "surface": "#0E1730",
    "surface_alt": "#131F3B",
    "border": "#283659",
    "text": "#F3F6FF",
    "muted": "#9BAACB",
    "violet": "#7856F7",
    "purple": "#A044F7",
    "blue": "#38A8FF",
    "green": "#32D6A0",
}

# GEOMETRIC DIAMOND LOGO

LOGO_SVG = """
<svg xmlns="http://www.w3.org/2000/svg"
     width="120" height="120" viewBox="0 0 120 120"
     role="img" aria-label="AI Hiring Intelligence logo">

  <defs>
    <linearGradient id="auroraA"
        x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#38A8FF"/>
      <stop offset="100%" stop-color="#7856F7"/>
    </linearGradient>

    <linearGradient id="auroraB"
        x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#A044F7"/>
      <stop offset="100%" stop-color="#4C59ED"/>
    </linearGradient>
  </defs>

  <polygon points="60,5 93,55 60,115 27,55"
           fill="#121A39"/>

  <polygon points="60,5 60,60 27,55"
           fill="url(#auroraA)"/>

  <polygon points="60,5 93,55 60,60"
           fill="#9360FF"/>

  <polygon points="27,55 60,60 60,115"
           fill="#275CCF"/>

  <polygon points="93,55 60,115 60,60"
           fill="url(#auroraB)"/>

  <polygon points="60,5 60,60 93,55"
           fill="none" stroke="#B0A3FF"
           stroke-width="1.3" opacity="0.6"/>
</svg>
"""


def logo_data_uri():
    """Return the brand logo as an embeddable SVG image URI."""
    encoded = base64.b64encode(
        LOGO_SVG.encode("utf-8")
    ).decode("ascii")
    return f"data:image/svg+xml;base64,{encoded}"


 
# MAIN THEME
 

def apply_theme():
    """Apply the Midnight Aurora visual theme to Streamlit."""

    st.markdown(
        """
        <style>

        /*  GLOBAL PAGE */

        :root {
            --midnight: #070D1D;
            --surface: #0E1730;
            --surface-alt: #131F3B;
            --border: #283659;
            --text: #F3F6FF;
            --muted: #9BAACB;
            --violet: #7856F7;
            --purple: #A044F7;
            --blue: #38A8FF;
            --success: #32D6A0;
        }

        html, body,
        [data-testid="stApp"] {
            background-color: var(--midnight);
            color: var(--text);
            font-family: "Inter", "Segoe UI", Arial, sans-serif;
        }

        [data-testid="stApp"] {
            background-image:
                radial-gradient(
                    ellipse at 85% 0%,
                    rgba(120, 86, 247, 0.15),
                    transparent 42%
                ),
                radial-gradient(
                    ellipse at 5% 22%,
                    rgba(56, 168, 255, 0.09),
                    transparent 38%
                );
            background-attachment: fixed;
        }

        .block-container {
            max-width: 1450px;
            padding-top: 2rem;
            padding-bottom: 4rem;
        }

        /* ---------------------------------------------
           TYPOGRAPHY
        --------------------------------------------- */

        h1, h2, h3, h4 {
            color: var(--text) !important;
            font-weight: 700 !important;
            letter-spacing: -0.025em;
        }

        h1 {
            font-size: clamp(1.8rem, 3vw, 2.7rem) !important;
        }

        p, li, label {
            color: var(--text);
        }

        [data-testid="stCaptionContainer"] {
            color: var(--muted);
        }

        /* ---------------------------------------------
           SIDEBAR
        --------------------------------------------- */

        [data-testid="stSidebar"] {
            background:
                linear-gradient(
                    180deg,
                    #0C1530 0%,
                    #080F23 100%
                );
            border-right: 1px solid var(--border);
        }

        [data-testid="stSidebar"] .stButton > button {
            width: 100%;
        }

        /* ---------------------------------------------
           INPUT FIELDS
        --------------------------------------------- */

        div[data-baseweb="input"] > div,
        div[data-baseweb="textarea"] > div {
            background: #0D1831 !important;
            border: 1px solid var(--border) !important;
            border-radius: 11px !important;
            color: var(--text) !important;
        }

        div[data-baseweb="input"] input,
        div[data-baseweb="textarea"] textarea {
            color: var(--text) !important;
        }

        div[data-baseweb="input"]:focus-within > div,
        div[data-baseweb="textarea"]:focus-within > div {
            border-color: var(--blue) !important;
            box-shadow:
                0 0 0 2px rgba(56, 168, 255, 0.14);
        }

        /* ---------------------------------------------
           FORMS AND PANELS
        --------------------------------------------- */

        [data-testid="stForm"] {
            background:
                linear-gradient(
                    145deg,
                    rgba(19, 31, 59, 0.95),
                    rgba(10, 19, 40, 0.95)
                );
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: 1.4rem;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            border-radius: 17px;
        }

        /* ---------------------------------------------
           PRIMARY BUTTONS
        --------------------------------------------- */

        .stButton > button[kind="primary"],
        .stFormSubmitButton > button[kind="primary"] {
            background:
                linear-gradient(
                    100deg,
                    #367AF5 0%,
                    #7856F7 55%,
                    #A044F7 100%
                ) !important;

            color: white !important;
            border: 0 !important;
            border-radius: 11px !important;
            font-weight: 650 !important;
            min-height: 2.8rem;

            box-shadow:
                0 5px 20px rgba(120, 86, 247, 0.18);

            transition:
                transform 0.2s ease,
                box-shadow 0.2s ease;
        }

        .stButton > button[kind="primary"]:hover,
        .stFormSubmitButton > button[kind="primary"]:hover {
            transform: translateY(-1px);
            box-shadow:
                0 8px 25px rgba(120, 86, 247, 0.3);
        }

        /* ---------------------------------------------
           SECONDARY BUTTONS
        --------------------------------------------- */

        .stButton > button[kind="secondary"],
        .stFormSubmitButton > button[kind="secondary"] {
            background: #121D39 !important;
            border: 1px solid #35466B !important;
            color: var(--text) !important;
            border-radius: 11px !important;
            min-height: 2.7rem;
        }

        .stButton > button[kind="secondary"]:hover,
        .stFormSubmitButton > button[kind="secondary"]:hover {
            border-color: var(--blue) !important;
        }

        /* ---------------------------------------------
           DOWNLOAD BUTTONS
        --------------------------------------------- */

        .stDownloadButton > button {
            background:
                linear-gradient(
                    105deg,
                    #174A9C,
                    #5E47D9
                ) !important;
            border: 1px solid #6677DA !important;
            color: white !important;
            border-radius: 11px !important;
            font-weight: 600 !important;
        }

        .stDownloadButton > button:hover {
            border-color: #89B8FF !important;
            filter: brightness(1.1);
        }

        /* ---------------------------------------------
           FILE UPLOADER
        --------------------------------------------- */

        [data-testid="stFileUploaderDropzone"] {
            background:
                linear-gradient(
                    145deg,
                    rgba(56, 168, 255, 0.07),
                    rgba(120, 86, 247, 0.08)
                ) !important;

            border: 1px dashed #6178C2 !important;
            border-radius: 15px !important;
        }

        /* ---------------------------------------------
           TABLES
        --------------------------------------------- */

        [data-testid="stDataFrame"] {
            background: #0D1730;
            border: 1px solid var(--border);
            border-radius: 14px;
            overflow: hidden;
        }

        [data-testid="stTable"] {
            border-radius: 14px;
            overflow: hidden;
        }

        /* ---------------------------------------------
           TABS
        --------------------------------------------- */

        button[data-baseweb="tab"] {
            color: var(--muted);
            font-weight: 600;
        }

        button[data-baseweb="tab"][aria-selected="true"] {
            color: #AC9AFF !important;
        }

        /* ---------------------------------------------
           METRIC CARDS
        --------------------------------------------- */

        [data-testid="stMetric"] {
            background:
                linear-gradient(
                    145deg,
                    #14213E,
                    #0D1730
                );
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 1.1rem;
        }

        [data-testid="stMetricValue"] {
            color: #F4F6FF;
        }

        /* ---------------------------------------------
           EXPANDERS
        --------------------------------------------- */

        [data-testid="stExpander"] {
            background: rgba(19, 31, 59, 0.7);
            border: 1px solid var(--border);
            border-radius: 13px;
        }

        /* ---------------------------------------------
           DIVIDERS
        --------------------------------------------- */

        hr {
            border-color: var(--border) !important;
            opacity: 0.7;
        }

        /* ---------------------------------------------
           CUSTOM BRAND HEADER
        --------------------------------------------- */

        .aurora-brand {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 1.8rem;
            padding: 0.5rem 0;
        }

        .aurora-brand-logo {
            width: 58px;
            height: 58px;
            flex-shrink: 0;
            filter:
                drop-shadow(
                    0 0 14px rgba(120, 86, 247, 0.35)
                );
        }

        .aurora-brand-name {
            margin: 0;
            font-size: clamp(1.35rem, 2.7vw, 2rem);
            font-weight: 750;
            letter-spacing: -0.04em;
            line-height: 1.2;
            background:
                linear-gradient(
                    100deg,
                    #FFFFFF,
                    #BDA8FF 52%,
                    #56BBFF
                );
            background-clip: text;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .aurora-brand-subtitle {
            color: #AAB9DB;
            font-size: 0.89rem;
            margin-top: 5px;
        }

        /* ---------------------------------------------
           AURORA HERO
        --------------------------------------------- */

        .aurora-hero {
            position: relative;
            overflow: hidden;

            background:
                radial-gradient(
                    ellipse at 90% 0%,
                    rgba(129, 72, 249, 0.22),
                    transparent 55%
                ),
                radial-gradient(
                    ellipse at 10% 95%,
                    rgba(38, 129, 250, 0.17),
                    transparent 50%
                ),
                #0E1730;

            border: 1px solid #2D3B69;
            border-radius: 22px;
            padding: 2rem;
            margin: 1rem 0 2rem 0;
        }

        .aurora-hero h2 {
            font-size: clamp(1.45rem, 2.5vw, 2.2rem);
            margin-bottom: 0.6rem;
        }

        .aurora-hero p {
            color: #B5C2DF;
            line-height: 1.7;
            max-width: 720px;
        }

        .aurora-eyebrow {
            color: #8EBEFF;
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.17em;
            margin-bottom: 0.7rem;
        }

        /* ---------------------------------------------
           RESPONSIVE DESIGN
        --------------------------------------------- */

        @media (max-width: 768px) {

            .block-container {
                padding: 1.2rem 0.9rem 3rem;
            }

            .aurora-hero {
                padding: 1.3rem;
                border-radius: 16px;
            }

            .aurora-brand-logo {
                width: 44px;
                height: 44px;
            }

            [data-testid="stForm"] {
                padding: 0.95rem;
            }
        }

        @media (prefers-reduced-motion: reduce) {
            .stButton > button,
            .stFormSubmitButton > button {
                transition: none !important;
                transform: none !important;
            }
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


# BRAND HEADER WITH LOGO
 

def render_brand():
    """Display the application name and custom geometric logo."""

    logo = logo_data_uri()

    st.markdown(
        f"""
        <div class="aurora-brand">
            <img
                class="aurora-brand-logo"
                src="{logo}"
                alt="AI Hiring Intelligence geometric logo"
            />
            <div>
                <div class="aurora-brand-name">
                    AI Hiring Intelligence System
                </div>
                <div class="aurora-brand-subtitle">
                    Intelligent resume evidence analysis
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# OPTIONAL HERO PANEL
 

def render_hero():
    """Display the Midnight Aurora welcome panel."""

    st.markdown(
        """
<section class="aurora-hero">
    <div class="aurora-eyebrow">POWERED BY GOOGLE GEMINI</div>
    <h2>Turn Resumes Into Clear, Job-Relevant Insights</h2>
    <p>
        Analyze PDF resumes using AI, review job-related
        evidence, securely save candidate history,
        and export Excel reports.
        Built to support informed human review.
    </p>
</section>
        """,
        unsafe_allow_html=True,
    )

      


