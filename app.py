import streamlit as st
from datetime import datetime

# --- Configuration ---
st.set_page_config(page_title="23 Reasons Why I Love You", layout="centered")
st.title("❤️ 23 Reasons Why I Love You")
st.markdown("### Happy Birthday Max!")

# --- Data ---
reasons = [
{"type": "text", "content": "Because I always feel truly heard by you."},
{"type": "text", "content": "Because even with all the language barriers, you’ve never made me feel stupid."},
{"type": "text", "content": "Because you have a beautiful soul."},
{"type": "text", "content": "Because no matter what it's about, you never give up."},
{"type": "text", "content": "Because I can be completely myself with you."},
{"type": "text", "content": "Because even silence feels warm when I’m with you."},
{"type": "text", "content": "Because with you, even the hardest things in life seem simple."},
{"type": "text", "content": "Because your scent smells like home."},
{"type": "text", "content": "Because when you explain something you care about, your eyes light up."},
{"type": "text", "content": "Because you make every trip we take together feel perfect."},
{"type": "text", "content": "Because you make me laugh even when I don’t want to."},
{"type": "text", "content": "Because you always try to give your best while staying true to who you are."},

# Locked from here (index 12 onwards)
{"type": "text", "content": "Because you share the joy of life with me."},
{"type": "text", "content": "Because you have this rare balance of strength and softness."},
{"type": "text", "content": "Because time with you never feels wasted."},
{"type": "text", "content": "Because you’ve made me believe in a kind of love I didn’t think existed."},
{"type": "text", "content": "Because you don’t talk about your values — you live them."},
{"type": "text", "content": "Because your smile makes me forget all my sorrows."},
{"type": "text", "content": "Because you’re honest, but never cruel."},
{"type": "text", "content": "Because with you, the ordinary becomes extraordinary."},
{"type": "text", "content": "Because your mind is beautiful."},
{"type": "text", "content": "Because every kiss from you still gives me butterflies."},
{"type": "text", "content": "Loving you is the easiest thing I’ve ever done."},
]

unlock_dates = [
    "2025-10-01", "2025-11-01", "2025-12-01", "2026-01-01", "2026-02-01",
    "2026-03-01", "2026-04-01", "2026-05-01", "2026-06-01", "2026-07-01", "2026-08-01"
]

# --- UI ---
st.markdown("---")
cols = st.columns(6)
today = datetime.today().date()

for i, reason in enumerate(reasons):
    col = cols[i % 6]  # distribute hearts across columns
    key = f"heart_{i+1}"

    if i < 12:
        if col.button(f"❤️ {i+1}", key=key):
            if reason["type"] == "text":
                st.success(reason["content"])
            elif reason["type"] == "image":
                st.image(reason["content"], caption=f"Reason {i+1}")

    else:
        unlock_date = datetime.strptime(unlock_dates[i - 12], "%Y-%m-%d").date()
        if today >= unlock_date:
            if col.button(f"❤️ {i+1}", key=key):
                if reason["type"] == "text":
                    st.success(reason["content"])
                elif reason["type"] == "image":
                    st.image(reason["content"], caption=f"Reason {i+1}")
        else:
            col.button(f"🔒 {i+1}", disabled=True, key=key)
            col.caption(f"Opens {unlock_date.strftime('%B %d, %Y')}")

st.markdown("---")
st.caption("Made with love by Esztike 💖")
