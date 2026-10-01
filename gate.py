"""Opening screens: blank password page -> beating heart -> the gift."""
import re

import streamlit as st
import streamlit.components.v1 as components

import gift_data as g

GATE_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600&display=swap');
#MainMenu, footer, header, [data-testid="stToolbar"], [data-testid="stDecoration"] { display:none !important; }
.stApp, [data-testid="stAppViewContainer"] { background:#fff8f1 !important; }
.block-container { max-width:520px; padding-top:16vh !important; text-align:center; }
html, body, p, label, div { font-family:'Nunito',sans-serif; color:#4b3f58; }
.stButton>button, .stFormSubmitButton>button {
    background:#f8d7e0; color:#4b3f58; border:none; border-radius:999px; padding:.5rem 1.6rem; }
.stFormSubmitButton>button:hover, .stButton>button:hover { background:#e3d9f5; color:#4b3f58; }
[data-testid="stForm"] { border:none; padding:0; }
</style>
"""

HEART_HTML = """
<style>
  html,body{margin:0;height:100%;background:transparent;overflow:hidden;font-family:sans-serif}
  .wrap{height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center}
  #heart{width:190px;height:190px;cursor:pointer;touch-action:manipulation;
         filter:drop-shadow(0 10px 20px rgba(240,120,160,.45));animation:beat 1.3s ease-in-out infinite}
  @keyframes beat{0%,100%{transform:scale(1)}15%{transform:scale(1.14)}30%{transform:scale(1)}45%{transform:scale(1.09)}}
  .cap{margin-top:18px;color:#7a6590;font-size:15px}
  .mini{position:fixed;pointer-events:none;user-select:none;z-index:9}
</style>
<div class="wrap">
  <svg id="heart" viewBox="0 0 32 29.6"><path fill="#f48fb1" d="M23.6,0c-3.4,0-6.3,2.7-7.6,5.6C14.7,2.7,11.8,0,8.4,0C3.8,0,0,3.8,0,8.4c0,9.4,9.5,11.9,16,21.2c6.1-9.3,16-12.1,16-21.2C32,3.8,28.2,0,23.6,0z"/></svg>
  <div class="cap">__CAPTION__</div>
</div>
<script>
  const faces = ['💗','💖','💕','💞','🩷','💓'];
  let last = 0;
  function burst(x, y){
    for(let i=0;i<16;i++){
      const s = document.createElement('span');
      s.className = 'mini';
      s.textContent = faces[Math.floor(Math.random()*faces.length)];
      s.style.left = x+'px'; s.style.top = y+'px';
      s.style.fontSize = (10 + Math.random()*16)+'px';
      document.body.appendChild(s);
      const a = Math.random()*Math.PI*2, d = 50 + Math.random()*110;
      s.animate([
        {transform:'translate(-50%,-50%) scale(.4)', opacity:1},
        {transform:`translate(calc(-50% + ${Math.cos(a)*d}px), calc(-50% + ${Math.sin(a)*d - 30}px)) scale(1.1)`, opacity:0}
      ], {duration: 900 + Math.random()*600, easing:'ease-out'}).onfinish = () => s.remove();
    }
  }
  const h = document.getElementById('heart');
  ['pointerenter','pointerdown','pointermove'].forEach(ev => h.addEventListener(ev, e => {
    const now = Date.now();
    if (ev === 'pointermove' && now - last < 250) return;
    last = now; burst(e.clientX, e.clientY);
  }));
</script>
"""


def _same_date(a, b):
    nums = lambda t: [int(x) for x in re.findall(r"\d+", t)]
    return nums(a) == nums(b)


def run_gate():
    """Returns True once the person is past the password + heart screens."""
    stage = st.session_state.get("stage", "lock")
    if stage == "gift":
        return True

    st.markdown(GATE_CSS, unsafe_allow_html=True)

    if stage == "lock":
        st.markdown(f"<p>{g.LOCK_HINT}</p>", unsafe_allow_html=True)
        with st.form("lock"):
            pw = st.text_input("Password", placeholder="dd/mm/yyyy", label_visibility="collapsed")
            submitted = st.form_submit_button("Kholo 💗")
        if submitted:
            if _same_date(pw, g.PASSWORD):
                st.session_state["stage"] = "heart"
                st.rerun()
            else:
                st.caption("Hmm, ye sahi nahi hai. Ek baar aur try karo 🙂")
        return False

    components.html(HEART_HTML.replace("__CAPTION__", g.HEART_CAPTION), height=340)
    mid = st.columns([1, 2, 1])[1]
    if mid.button("Apna gift kholo 💗", use_container_width=True):
        st.session_state["stage"] = "gift"
        st.rerun()
    return False
