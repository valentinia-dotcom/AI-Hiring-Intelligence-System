


"""
AI Hiring Intelligence System
Midnight Aurora — Frontend Theme

Visual styling only.
Does not modify Gemini, Supabase, authentication,
candidate history, or Excel exports.
"""

import base64
from pathlib import Path
from textwrap import dedent

import streamlit as st


COLORS = {
    "background": "#070D1D",
    "surface": "#101A33",
    "surface_alt": "#172341",
    "border": "#29395E",
    "text": "#F3F6FF",
    "muted": "#A8B6D3",
    "violet": "#7856F7",
    "purple": "#A044F7",
    "blue": "#38A8FF",
    "green": "#32D6A0",
}


# --------------------------------------------------
# OFFICIAL LOGO (the PNG already uploaded to GitHub)
# --------------------------------------------------
# Keep this filename unchanged unless the file is renamed in GitHub.
LOGO_FILE = Path(__file__).resolve().parent / "AI Hiring Intelligence Logo (1).png"


def logo_data_uri():
    """Load the existing repository PNG; provide a readable fallback if missing."""
    try:
        image_bytes = LOGO_FILE.read_bytes()
        return "data:image/png;base64," + base64.b64encode(image_bytes).decode("ascii")
    except OSError:
        return None


# --------------------------------------------------
# APPLY THEME
# --------------------------------------------------

def apply_theme():
    """Apply Midnight Aurora styling to Streamlit."""

    css = """
    <style>

    :root {
        --bg: #070D1D;
        --surface: #101A33;
        --surface-alt: #172341;
        --border: #29395E;
        --text: #F3F6FF;
        --muted: #A8B6D3;
        --violet: #7856F7;
        --blue: #38A8FF;
    }

    /* MAIN BACKGROUND */

    html, body,
    [data-testid="stApp"] {
        color: var(--text);
        font-family: "Inter", "Segoe UI",
                     Arial, sans-serif;
    }

    [data-testid="stApp"] {
        background:
            radial-gradient(
                ellipse at 90% 0%,
                rgba(120,86,247,0.14),
                transparent 45%
            ),
            radial-gradient(
                ellipse at 0% 25%,
                rgba(56,168,255,0.08),
                transparent 40%
            ),
            #070D1D;
        background-attachment: fixed;
    }

    .block-container {
        width: 100%;
        max-width: 1200px;
        box-sizing: border-box;
        padding: 5rem clamp(1rem, 3vw, 2rem) 4rem !important;
        margin-inline: auto;
    }

    /* Prevent text or widgets from stretching the entire app horizontally. */
    [data-testid="stAppViewContainer"] {
        overflow-x: clip;
    }

    /* TYPOGRAPHY */

    h1, h2, h3, h4 {
        color: #F3F6FF !important;
        letter-spacing: -0.025em;
        font-weight: 700 !important;
    }

    p, label {
        line-height: 1.6;
    }

    [data-testid="stCaptionContainer"] {
        color: #A8B6D3;
    }

    /* SIDEBAR */

    [data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #101A34,
                #080F20
            );
        border-right: 1px solid #29395E;
    }

    [data-testid="stSidebar"] .stButton button {
        width: 100%;
    }

    /* FORMS */

    [data-testid="stForm"] {
        background:
            linear-gradient(
                145deg,
                rgba(23,35,65,0.95),
                rgba(12,20,41,0.96)
            );
        border: 1px solid #29395E;
        border-radius: 20px;
        padding: 1.5rem;
    }

    /* INPUTS */

    div[data-baseweb="input"] > div,
    div[data-baseweb="textarea"] > div {
        background-color: #172341 !important;
        border: 1px solid #29395E !important;
        border-radius: 12px !important;
    }

    div[data-baseweb="input"] input,
    div[data-baseweb="textarea"] textarea {
        color: #F3F6FF !important;
        -webkit-text-fill-color: #F3F6FF;
    }

    div[data-baseweb="input"]:focus-within > div,
    div[data-baseweb="textarea"]:focus-within > div {
        border-color: #7856F7 !important;
        box-shadow:
            0 0 0 2px rgba(120,86,247,0.12);
    }

    /* PRIMARY BUTTONS */

    .stButton button[kind="primary"],
    .stFormSubmitButton button[kind="primary"] {
        background:
            linear-gradient(
                100deg,
                #367AF5,
                #7856F7,
                #A044F7
            ) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 650 !important;
        min-height: 2.8rem;
        box-shadow:
            0 5px 20px rgba(120,86,247,0.15);
        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease;
    }

    .stButton button[kind="primary"]:hover,
    .stFormSubmitButton button[kind="primary"]:hover {
        transform: translateY(-1px);
        box-shadow:
            0 8px 24px rgba(120,86,247,0.28);
    }

    /* SECONDARY BUTTONS */

    .stButton button[kind="secondary"],
    .stFormSubmitButton button[kind="secondary"] {
        background: #172341 !important;
        color: #F3F6FF !important;
        border: 1px solid #35466B !important;
        border-radius: 12px !important;
    }

    .stButton button[kind="secondary"]:hover,
    .stFormSubmitButton button[kind="secondary"]:hover {
        border-color: #7856F7 !important;
    }

    /* DOWNLOAD BUTTONS */

    .stDownloadButton button {
        background:
            linear-gradient(
                105deg,
                #225DBB,
                #6550DC
            ) !important;
        color: white !important;
        border: 1px solid #6677DA !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
    }

    .stDownloadButton button:hover {
        filter: brightness(1.12);
    }

    /* FILE UPLOADER */

    [data-testid="stFileUploaderDropzone"] {
        background:
            linear-gradient(
                135deg,
                rgba(56,168,255,0.07),
                rgba(120,86,247,0.09)
            ) !important;
        border: 1px dashed #6278C4 !important;
        border-radius: 16px !important;
    }

    /* DATAFRAMES AND TABLES */

    [data-testid="stDataFrame"],
    [data-testid="stTable"] {
        background: #101A33;
        border: 1px solid #29395E;
        border-radius: 15px;
        overflow: hidden;
    }

    /* TABS */

    button[data-baseweb="tab"] {
        color: #A8B6D3;
        font-weight: 600;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        color: #AC9AFF !important;
    }

    /* METRICS */

    [data-testid="stMetric"] {
        background:
            linear-gradient(
                145deg,
                #172341,
                #101A33
            );
        border: 1px solid #29395E;
        border-radius: 16px;
        padding: 1.2rem;
    }

    /* EXPANDERS */

    [data-testid="stExpander"] {
        background: rgba(23,35,65,0.75);
        border: 1px solid #29395E;
        border-radius: 14px;
    }

    /* BRAND HEADER */

    .aurora-brand {
        display: flex;
        align-items: center;
        gap: 16px;
        max-width: 100%;
        min-width: 0;
        margin-bottom: 1.5rem;
    }

    .aurora-brand > div:last-child {
        min-width: 0;
    }

    /* Show the icon area of the original wide PNG, hiding its dark wordmark.
       No extra logo image or image-processing dependency is required. */
    .aurora-brand-logo {
        width: 72px;
        height: 76px;
        flex-shrink: 0;
        background-size: 185px auto;
        background-repeat: no-repeat;
        background-position: -1px -36px;
        filter: drop-shadow(0 0 10px rgba(56,168,255,0.24));
    }

    .aurora-brand-name {
        font-size: clamp(
            1.4rem, 2.7vw, 2rem
        );
        font-weight: 750;
        line-height: 1.2;
        letter-spacing: -0.04em;
        overflow-wrap: anywhere;
        background:
            linear-gradient(
                100deg,
                #FFFFFF,
                #BDA8FF 52%,
                #56BBFF
            );
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .aurora-brand-subtitle {
        color: #A8B6D3;
        font-size: 0.9rem;
        margin-top: 5px;
    }

    /* HERO PANEL */

    .aurora-hero {
        position: relative;
        overflow: hidden;
        width: 100%;
        max-width: 100%;
        min-width: 0;
        box-sizing: border-box;
        padding: clamp(1.25rem, 3vw, 2rem);
        margin: 1.2rem 0 2rem;

        background:
            radial-gradient(
                ellipse at 92% 0%,
                rgba(129,72,249,0.22),
                transparent 55%
            ),
            radial-gradient(
                ellipse at 10% 95%,
                rgba(38,129,250,0.17),
                transparent 55%
            ),
            #101A33;

        border: 1px solid #344674;
        border-radius: 22px;
    }

    .aurora-eyebrow {
        font-size: 0.76rem;
        color: #8EBEFF;
        font-weight: 750;
        text-transform: uppercase;
        letter-spacing: 0.17em;
        margin-bottom: 1rem;
    }

    .aurora-hero h2 {
        font-size: clamp(1.35rem, 2.5vw, 2rem) !important;
        line-height: 1.25 !important;
        letter-spacing: -0.02em;
        max-width: 780px;
        white-space: normal !important;
        overflow-wrap: anywhere;
        margin: 0 0 0.9rem;
    }

    .aurora-hero p {
        font-size: clamp(0.95rem, 1.2vw, 1.05rem) !important;
        color: #B5C2DF;
        line-height: 1.65;
        max-width: 740px;
        white-space: normal !important;
        overflow-wrap: anywhere;
        margin: 0;
    }

    /* RESPONSIVE */

    @media (max-width: 768px) {
        .block-container {
            padding: 4.25rem 1rem 3rem !important;
        }

        .aurora-brand {
            gap: 10px;
        }

        .aurora-brand-name {
            font-size: clamp(1.1rem, 5vw, 1.55rem);
        }

        .aurora-hero h2 {
            font-size: clamp(1.25rem, 5vw, 1.6rem) !important;
        }

        .aurora-hero {
            padding: 1.4rem;
            border-radius: 17px;
        }

        .aurora-brand-logo {
            width: 58px;
            height: 62px;
            background-size: 150px auto;
            background-position: -1px -29px;
        }

        [data-testid="stForm"] {
            padding: 1rem;
        }
    }

    @media (prefers-reduced-motion: reduce) {
        .stButton button,
        .stFormSubmitButton button {
            transition: none !important;
            transform: none !important;
        }
    }

    </style>
    """

    st.markdown(dedent(css), unsafe_allow_html=True)


# --------------------------------------------------
# RENDER LOGO + BRAND NAME
# --------------------------------------------------

def render_brand():
    """Display the official uploaded PNG icon and accessible Aurora brand title."""
    logo = logo_data_uri()
    # CSS clips the icon from the original combined icon-and-wordmark PNG.
    # Display the title separately so its lettering stays legible on navy.
    icon = (
        f'<div class="aurora-brand-logo" role="img" '
        f'aria-label="AI Hiring Intelligence logo icon" '
        f'style="background-image: url(\'{logo}\');"></div>'
        if logo else '<div aria-hidden="true" style="font-size:2.4rem">◈</div>'
    )
    html = (
        '<div class="aurora-brand">'
        + icon
        + '<div><div class="aurora-brand-name">AI Hiring Intelligence System</div>'
        '<div class="aurora-brand-subtitle">Intelligent resume evidence analysis</div>'
        '</div></div>'
    )
    st.markdown(html, unsafe_allow_html=True)


# --------------------------------------------------
# RENDER AURORA WELCOME PANEL
# --------------------------------------------------

def render_hero():
    """Display the branded welcome panel without Markdown code-block parsing."""

    # Keep the HTML tags on one logical line so Streamlit's Markdown
    # renderer cannot interpret indented lines as a code block.
    hero_html = (
        '<section class="aurora-hero">'
        '<div class="aurora-eyebrow">INTELLIGENT RESUME ANALYSIS</div>'
        '<h2>Turn Resumes Into Clear, Job-Relevant Insights</h2>'
        '<p>Analyze PDF resumes using AI, review job-related evidence, '
        'securely save candidate history, and export Excel reports. '
        'Built to support informed human review.</p>'
        '</section>'
    )
    st.markdown(hero_html, unsafe_allow_html=True)
