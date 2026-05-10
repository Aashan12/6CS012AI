from pathlib import Path
import json
import pickle
import re
import shutil
import string
import tempfile

import contractions
import nltk
import streamlit as st

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer


BASE_DIR = Path(__file__).resolve().parent


st.set_page_config(
    page_title="Sarcasm Detector",
    page_icon="🎭",
    layout="wide",
)


st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        /* ── Page background ── */
        .stApp {
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            min-height: 100vh;
        }

        /* ── Sidebar ── */
        [data-testid="stSidebar"] {
            background: rgba(255, 255, 255, 0.04);
            border-right: 1px solid rgba(255, 255, 255, 0.08);
        }

        [data-testid="stSidebar"] * {
            color: #e2e8f0 !important;
        }

        [data-testid="stSidebar"] .stButton > button {
            background: rgba(139, 92, 246, 0.18);
            border: 1px solid rgba(139, 92, 246, 0.35);
            border-radius: 10px;
            color: #c4b5fd !important;
            font-weight: 600;
            font-size: 0.88rem;
            padding: 0.55rem 1rem;
            transition: all 150ms ease;
            width: 100%;
        }

        [data-testid="stSidebar"] .stButton > button:hover {
            background: rgba(139, 92, 246, 0.35);
            border-color: #8b5cf6;
            color: #fff !important;
            transform: translateX(3px);
        }

        /* ── Main content container ── */
        .block-container {
            max-width: 900px;
            padding: 2.5rem 2rem 3rem;
        }

        /* ── Hero header ── */
        .hero {
            text-align: center;
            padding: 1rem 0 1.8rem;
        }

        .hero-badge {
            display: inline-block;
            background: rgba(139, 92, 246, 0.2);
            border: 1px solid rgba(139, 92, 246, 0.4);
            border-radius: 999px;
            color: #c4b5fd;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            padding: 0.3rem 0.9rem;
            text-transform: uppercase;
            margin-bottom: 1rem;
        }

        .hero-title {
            font-size: clamp(2.4rem, 6vw, 3.8rem);
            font-weight: 800;
            background: linear-gradient(135deg, #a78bfa, #60a5fa, #f472b6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            line-height: 1.1;
            margin: 0 0 1rem;
        }

        .hero-sub {
            color: #94a3b8;
            font-size: 1.05rem;
            max-width: 560px;
            margin: 0 auto;
            line-height: 1.65;
        }

        /* ── Input card ── */
        .stTextArea textarea {
            background: rgba(15, 12, 41, 0.7) !important;
            border: 1px solid rgba(139, 92, 246, 0.35) !important;
            border-radius: 12px !important;
            color: #f1f5f9 !important;
            font-size: 1rem !important;
            line-height: 1.6 !important;
            padding: 0.85rem 1rem !important;
            transition: border-color 200ms ease, box-shadow 200ms ease !important;
        }

        .stTextArea textarea:focus {
            border-color: #8b5cf6 !important;
            box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.2) !important;
            outline: none !important;
        }

        .stTextArea textarea::placeholder {
            color: #475569 !important;
        }

        /* Remove red focus ring Streamlit adds */
        .stTextArea [data-baseweb="textarea"]:focus-within {
            border-color: #8b5cf6 !important;
            box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.2) !important;
        }

        .stTextArea [data-baseweb="base-input"] {
            background: transparent !important;
        }

        /* ── Form container acts as the card ── */
        div[data-testid="stForm"] {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 1.6rem;
            backdrop-filter: blur(12px);
        }

        div[data-testid="stForm"] label {
            color: #e2e8f0 !important;
            font-weight: 600 !important;
            font-size: 0.95rem !important;
        }
        div[data-testid="stForm"] .stButton > button,
        .stButton > button[kind="primaryFormSubmit"] {
            background: linear-gradient(135deg, #7c3aed, #4f46e5) !important;
            border: none !important;
            border-radius: 12px !important;
            color: #fff !important;
            font-size: 1rem !important;
            font-weight: 700 !important;
            height: 3rem !important;
            letter-spacing: 0.02em;
            transition: all 180ms ease !important;
            box-shadow: 0 4px 20px rgba(124, 58, 237, 0.4) !important;
        }

        div[data-testid="stForm"] .stButton > button:hover,
        .stButton > button[kind="primaryFormSubmit"]:hover {
            background: linear-gradient(135deg, #6d28d9, #4338ca) !important;
            box-shadow: 0 6px 28px rgba(124, 58, 237, 0.55) !important;
            transform: translateY(-2px) !important;
        }

        /* ── Result cards ── */
        .result-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.2rem;
            margin-top: 1.5rem;
        }

        .result-card {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 1.5rem;
            backdrop-filter: blur(12px);
        }

        .result-card-sarcastic {
            border-color: rgba(239, 68, 68, 0.4);
            background: rgba(239, 68, 68, 0.07);
        }

        .result-card-normal {
            border-color: rgba(34, 197, 94, 0.4);
            background: rgba(34, 197, 94, 0.07);
        }

        .card-eyebrow {
            color: #64748b;
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            margin-bottom: 0.6rem;
        }

        .verdict {
            font-size: 2.2rem;
            font-weight: 800;
            line-height: 1.1;
            margin: 0 0 0.3rem;
        }

        .verdict-sarcastic { color: #f87171; }
        .verdict-normal    { color: #4ade80; }

        .verdict-emoji {
            font-size: 1.8rem;
            margin-right: 0.4rem;
        }

        .confidence-label {
            color: #94a3b8;
            font-size: 0.88rem;
            margin-top: 0.8rem;
            margin-bottom: 0.35rem;
        }

        .confidence-value {
            color: #e2e8f0;
            font-size: 1.5rem;
            font-weight: 700;
        }

        /* ── Progress bar override ── */
        .stProgress > div > div > div > div {
            background: linear-gradient(90deg, #7c3aed, #ec4899) !important;
            border-radius: 999px !important;
        }

        .stProgress > div > div > div {
            background: rgba(255,255,255,0.08) !important;
            border-radius: 999px !important;
            height: 10px !important;
        }

        /* ── Score card ── */
        .score-card {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 1.5rem;
            backdrop-filter: blur(12px);
        }

        .score-number {
            font-size: 3rem;
            font-weight: 800;
            background: linear-gradient(135deg, #a78bfa, #60a5fa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            line-height: 1;
            margin: 0.4rem 0;
        }

        .score-hint {
            color: #64748b;
            font-size: 0.82rem;
            margin-top: 0.5rem;
        }

        /* ── Cleaned text ── */
        .cleaned-card {
            background: rgba(15, 12, 41, 0.7);
            border: 1px solid rgba(139, 92, 246, 0.25);
            border-radius: 16px;
            padding: 1.4rem 1.6rem;
            margin-top: 1.2rem;
        }

        .cleaned-title {
            color: #94a3b8;
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            margin-bottom: 0.75rem;
        }

        .cleaned-text {
            color: #a5f3fc;
            font-family: 'Courier New', Consolas, monospace;
            font-size: 0.97rem;
            line-height: 1.65;
            word-break: break-word;
        }

        /* ── Word count pill ── */
        .word-pill {
            display: inline-block;
            background: rgba(139, 92, 246, 0.15);
            border: 1px solid rgba(139, 92, 246, 0.3);
            border-radius: 999px;
            color: #a78bfa;
            font-size: 0.82rem;
            font-weight: 600;
            padding: 0.25rem 0.75rem;
            margin-top: 0.5rem;
        }

        /* ── Sidebar section headers ── */
        .sidebar-section {
            color: #64748b !important;
            font-size: 0.72rem !important;
            font-weight: 700 !important;
            letter-spacing: 0.1em !important;
            text-transform: uppercase !important;
            margin-bottom: 0.6rem !important;
        }

        .file-chip {
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 8px;
            color: #94a3b8 !important;
            font-family: 'Courier New', monospace;
            font-size: 0.8rem;
            padding: 0.4rem 0.7rem;
            margin-bottom: 0.4rem;
            display: block;
        }

        /* ── Divider ── */
        hr {
            border-color: rgba(255,255,255,0.08) !important;
        }

        /* ── Streamlit default overrides ── */
        .stAlert {
            border-radius: 12px !important;
        }

        [data-testid="stMetricValue"] {
            color: #e2e8f0 !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ── NLTK + model loading ──────────────────────────────────────────────────────

@st.cache_resource(show_spinner=False)
def load_nltk_resources():
    resources = {
        "stopwords": "corpora/stopwords",
        "punkt": "tokenizers/punkt",
        "punkt_tab": "tokenizers/punkt_tab",
        "wordnet": "corpora/wordnet",
        "omw-1.4": "corpora/omw-1.4",
    }
    for package, resource_path in resources.items():
        try:
            nltk.data.find(resource_path)
        except (LookupError, OSError):
            nltk.download(package, quiet=True)

    return set(stopwords.words("english")), WordNetLemmatizer()


def normalize_keras_h5_config(obj):
    drop_keys = {"optional", "quantization_config"}
    if isinstance(obj, dict):
        if obj.get("class_name") == "DTypePolicy":
            return obj.get("config", {}).get("name", "float32")
        config = obj.get("config")
        if obj.get("class_name") == "InputLayer" and isinstance(config, dict):
            if "batch_shape" in config:
                config["batch_input_shape"] = config.pop("batch_shape")
        return {k: normalize_keras_h5_config(v) for k, v in obj.items() if k not in drop_keys}
    if isinstance(obj, list):
        return [normalize_keras_h5_config(v) for v in obj]
    return obj


def make_compatible_h5_copy(model_path):
    import h5py
    version_key = int(model_path.stat().st_mtime)
    compat_path = Path(tempfile.gettempdir()) / f"{model_path.stem}_tfkeras_{version_key}.h5"
    if compat_path.exists():
        return compat_path
    shutil.copy2(model_path, compat_path)
    with h5py.File(compat_path, "r+") as h5_file:
        raw_config = h5_file.attrs["model_config"]
        if isinstance(raw_config, bytes):
            raw_config = raw_config.decode("utf-8")
        model_config = normalize_keras_h5_config(json.loads(raw_config))
        h5_file.attrs.modify("model_config", json.dumps(model_config))
    return compat_path


def load_best_model(model_path):
    try:
        return load_model(str(model_path), compile=False)
    except TypeError as error:
        message = str(error)
        if "batch_shape" not in message and "quantization_config" not in message:
            raise
        compatible_model_path = make_compatible_h5_copy(model_path)
        return load_model(str(compatible_model_path), compile=False)


class TokenizerUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == "keras.src.legacy.preprocessing.text" and name == "Tokenizer":
            return Tokenizer
        return super().find_class(module, name)


@st.cache_resource(show_spinner=False)
def load_saved_artifacts():
    model = load_best_model(BASE_DIR / "best_sarcasm_model.h5")
    with open(BASE_DIR / "tokenizer.pkl", "rb") as f:
        tokenizer = TokenizerUnpickler(f).load()
    with open(BASE_DIR / "max_length.pkl", "rb") as f:
        max_length = pickle.load(f)
    return model, tokenizer, max_length


stop_words, lemmatizer = load_nltk_resources()
model, tokenizer, max_length = load_saved_artifacts()


# ── Text processing ───────────────────────────────────────────────────────────

def clean_text(text):
    text = text.lower()
    text = contractions.fix(text)
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    text = re.sub(r"@\w+|#\w+", "", text)
    text = re.sub(r"\d+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()
    words = word_tokenize(text)
    cleaned_words = [lemmatizer.lemmatize(w) for w in words if w not in stop_words]
    return " ".join(cleaned_words)


def predict_sarcasm(text):
    cleaned = clean_text(text)
    sequence = tokenizer.texts_to_sequences([cleaned])
    padded = pad_sequences(sequence, maxlen=max_length, padding="post", truncating="post")
    raw = model.predict(padded, verbose=0)[0][0]
    label = "Sarcastic" if raw >= 0.5 else "Not Sarcastic"
    return label, float(raw), cleaned


# ── Example sentences ─────────────────────────────────────────────────────────

EXAMPLES = {
    "😏  Sarcastic headline": "Local man thrilled to spend weekend resetting all his passwords.",
    "📰  Normal headline":    "The city council approved a new public library downtown.",
    "💼  Office sentence":    "Great, another meeting that definitely could not have been an email.",
}


def set_example(example):
    st.session_state["user_input"] = example


# ── Sidebar ───────────────────────────────────────────────────────────────────

with st.sidebar:
    st.markdown('<p class="sidebar-section">Try an example</p>', unsafe_allow_html=True)
    st.caption("Fills the input box — your model still makes the prediction.")
    st.write("")

    for title, example in EXAMPLES.items():
        st.button(title, on_click=set_example, args=(example,), use_container_width=True)

    st.divider()

    st.markdown('<p class="sidebar-section">Model files</p>', unsafe_allow_html=True)
    for chip in ["best_sarcasm_model.h5", "tokenizer.pkl", "max_length.pkl"]:
        st.markdown(f'<span class="file-chip">📄 {chip}</span>', unsafe_allow_html=True)

    st.divider()
    st.markdown('<p class="sidebar-section">How it works</p>', unsafe_allow_html=True)
    st.caption(
        "Text is cleaned, tokenised, and padded before being passed to an "
        "LSTM model trained on the News Headlines Dataset for Sarcasm Detection."
    )


# ── Hero ──────────────────────────────────────────────────────────────────────

st.markdown(
    """
    <div class="hero">
        <div class="hero-badge">🎭 LSTM · Word2Vec · NLP</div>
        <h1 class="hero-title">Sarcasm Detection</h1>
        <p class="hero-sub">
            Paste any headline, tweet, or sentence and let the model decide
            whether it's dripping with sarcasm — or perfectly sincere.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


# ── Input form ────────────────────────────────────────────────────────────────

with st.form("sarcasm_form"):
    user_input = st.text_area(
        "Enter text to classify",
        key="user_input",
        height=130,
        placeholder="e.g. 'Oh great, the printer is out of ink again — what a surprise.'",
    )

    word_count = len(user_input.split()) if user_input.strip() else 0
    st.markdown(
        f'<span class="word-pill">✏️ {word_count} word{"s" if word_count != 1 else ""}</span>',
        unsafe_allow_html=True,
    )

    st.write("")

    submitted = st.form_submit_button("🔍  Analyse Text", use_container_width=True)


# ── Results ───────────────────────────────────────────────────────────────────

if submitted:
    if not user_input.strip():
        st.warning("⚠️  Please enter some text before running the model.")
    else:
        with st.spinner("Running model…"):
            label, probability, cleaned = predict_sarcasm(user_input)

        confidence = probability if label == "Sarcastic" else 1 - probability
        is_sarcastic = label == "Sarcastic"

        verdict_emoji  = "😏" if is_sarcastic else "😊"
        card_class     = "result-card-sarcastic" if is_sarcastic else "result-card-normal"
        verdict_class  = "verdict-sarcastic"     if is_sarcastic else "verdict-normal"
        bar_color_note = "rgba(239,68,68,0.8)"   if is_sarcastic else "rgba(34,197,94,0.8)"

        col_verdict, col_score = st.columns(2, gap="medium")

        # ── Verdict card ──
        with col_verdict:
            st.markdown(
                f"""
                <div class="result-card {card_class}">
                    <div class="card-eyebrow">Prediction</div>
                    <div class="verdict {verdict_class}">
                        <span class="verdict-emoji">{verdict_emoji}</span>{label}
                    </div>
                    <div class="confidence-label">Model confidence</div>
                    <div class="confidence-value">{confidence * 100:.1f}%</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.write("")
            st.progress(confidence)

        # ── Score card ──
        with col_score:
            st.markdown(
                f"""
                <div class="score-card">
                    <div class="card-eyebrow">Raw sarcasm score</div>
                    <div class="score-number">{probability:.3f}</div>
                    <div class="score-hint">
                        Threshold: <strong>0.500</strong> — scores above this are classified as sarcastic.
                    </div>
                    <br/>
                    <div class="card-eyebrow">Confidence bar</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.progress(probability)

        # ── Cleaned text ──
        st.markdown(
            f"""
            <div class="cleaned-card">
                <div class="cleaned-title">🧹 Cleaned &amp; tokenised input</div>
                <div class="cleaned-text">{cleaned or "⚠️ No tokens remained after preprocessing."}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
