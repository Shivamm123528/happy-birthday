import base64
import os
import random

import streamlit as st

import gift_data as g
from gate import run_gate

st.set_page_config(page_title="For Chhaya 💗", page_icon="💗", layout="centered")

BASE = os.path.dirname(os.path.abspath(__file__))


def p(rel):
    return os.path.join(BASE, rel)


@st.cache_data
def to_b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def background_css():
    """Uses assets/background.(jpg|jpeg|png|webp); falls back to a pastel gradient."""
    for ext, mime in (("jpg", "jpeg"), ("jpeg", "jpeg"), ("png", "png"), ("webp", "webp")):
        path = p(f"assets/background.{ext}")
        if os.path.exists(path):
            try:
                return (
                    "linear-gradient(rgba(248,215,224,0.38), rgba(212,233,247,0.30)), "
                    f'url("data:image/{mime};base64,{to_b64(path)}") 65% 75% / cover no-repeat'
                )
            except Exception:
                pass
    return "linear-gradient(160deg,#fde2ea 0%,#e6dcf7 50%,#d6ebfa 100%)"


CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,400;0,600;1,400&family=Nunito:wght@400;600&display=swap');
:root { --blush:#f8d7e0; --lav:#e3d9f5; --sky:#d4e9f7; --cream:#fff8f1; --ink:#4b3f58; }
.stApp, [data-testid="stAppViewContainer"] { background: transparent !important; }
.stApp::before { content:""; position:fixed; inset:0; z-index:-1; background: %BG%; }
#MainMenu, footer, header, [data-testid="stToolbar"], [data-testid="stDecoration"] { display:none !important; visibility:hidden; }
.block-container {
    background: rgba(255,248,241,0.84);
    backdrop-filter: blur(6px);
    border-radius: 28px;
    padding: 2.2rem 1.8rem 3rem !important;
    margin-top: 1.5rem; margin-bottom: 1.5rem;
    max-width: 760px;
    box-shadow: 0 8px 40px rgba(120,90,150,0.18);
}
html, body, p, li, label, div { font-family:'Nunito',sans-serif; color:var(--ink); line-height:1.65; }
h1, h2, h3 { font-family:'Fraunces',serif !important; color:#5a4670 !important; font-weight:600; }
h1 { text-align:center; font-size:2.3rem !important; }
h2 { margin-top:2.4rem !important; font-size:1.5rem !important; }
[data-testid="stExpander"] { background:rgba(248,215,224,0.45); border:1px solid #efc6d3; border-radius:18px; margin-bottom:.6rem; }
[data-testid="stExpander"] summary:hover { color:#9a5a7a; }
.card { background:rgba(227,217,245,0.55); border-radius:18px; padding:.9rem 1.1rem; margin-bottom:.8rem; height:100%; }
.card b { font-family:'Fraunces',serif; font-size:1.05rem; }
.wish { background:rgba(212,233,247,0.6); border-radius:18px; padding:.9rem 1.1rem; margin-bottom:.8rem; }
.smile { background:rgba(248,215,224,0.7); border-radius:18px; padding:1rem 1.2rem; text-align:center; font-size:1.1rem; }
.script { font-style:italic; opacity:.85; }
.center { text-align:center; }
.stButton>button { background:#e3d9f5; color:#4b3f58; border:none; border-radius:999px; padding:.5rem 1.4rem; }
.stButton>button:hover { background:#f8d7e0; color:#4b3f58; }
@media (max-width:640px) {
    .block-container { padding:1.4rem 1rem 2rem !important; margin-top:.5rem; border-radius:20px; }
    h1 { font-size:1.8rem !important; }
}
</style>
"""
if not run_gate():
    st.stop()

st.markdown(CSS.replace("%BG%", background_css()), unsafe_allow_html=True)

# ---------- Splash ----------
if not st.session_state.get("welcomed"):
    st.balloons()
    st.session_state["welcomed"] = True

st.title(g.SPLASH_TITLE)
for line in g.SPLASH_LINE:
    st.markdown(f"<p class='center'>{line}</p>", unsafe_allow_html=True)

# ---------- Open when ----------
st.header("Open when...")
for env in g.ENVELOPES:
    with st.expander(env["title"]):
        for line in env["lines"]:
            st.markdown(line)
        if env.get("show_call"):
            st.markdown(f"[📞 Call Mom](tel:{g.MOM_PHONE})")

# ---------- Voice notes ----------
st.header("Voice notes")
for note in g.VOICE_NOTES:
    st.subheader(note["title"])
    audio_path = p(note["file"])
    if os.path.exists(audio_path):
        try:
            st.audio(audio_path)
        except Exception:
            pass
    st.markdown(f"<p class='script'>{note['script']}</p>", unsafe_allow_html=True)

# ---------- Memories ----------
st.header("Our little map")
cols = st.columns(2)
for i, (title, text) in enumerate(g.MEMORIES):
    with cols[i % 2]:
        st.markdown(f"<div class='card'><b>{title}</b><br>{text}</div>", unsafe_allow_html=True)

# ---------- Grateful ----------
st.header("Why I'm grateful")
st.markdown(g.GRATEFUL_INTRO)
for item in g.GRATEFUL:
    st.markdown(f"- {item}")
st.subheader(g.LOVE_LIST_TITLE)
for item in g.LOVE_LIST:
    st.markdown(f"- {item}")

# ---------- Next ----------
st.header("Things we'll do next")
checked = [st.checkbox(item, key=f"next_{i}") for i, item in enumerate(g.NEXT_UP)]
if all(checked):
    st.toast(g.NEXT_UP_DONE, icon="💗")
    st.success(g.NEXT_UP_DONE)

# ---------- Smile ----------
st.header("Need a smile?")
if st.button("Make me smile 😊"):
    st.session_state["smile"] = random.choice(g.SMILE_MEMORIES)
if st.session_state.get("smile"):
    st.markdown(f"<div class='smile'>{st.session_state['smile']}</div>", unsafe_allow_html=True)

# ---------- Wishes ----------
st.header("Wishes for you this year")
for title, text in g.WISHES:
    st.markdown(f"<div class='wish'><b>{title}</b><br>{text}</div>", unsafe_allow_html=True)

# ---------- Photos ----------
available = [ph for ph in g.PHOTOS if os.path.exists(p(ph))]
if available:
    st.header("Photo wall")
    cols = st.columns(2)
    for i, ph in enumerate(available):
        try:
            cols[i % 2].image(p(ph), use_container_width=True)
        except Exception:
            pass

# ---------- Closing ----------
st.header("One last thing")
for line in g.CLOSING:
    st.markdown(line)
st.markdown(f"<h3 class='center'>{g.CLOSING_LINE}</h3>", unsafe_allow_html=True)
