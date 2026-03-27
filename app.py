import streamlit as st
from data_engine import generate_products
from scorer import calculate_score
from database import save_product, unsave_product, get_saved_ids

try:
    from ai_analyzer import analyze_product
except:
    def analyze_product(x):
        return "AI unavailable"

st.set_page_config(layout="wide", page_title="Nexura AI", page_icon="🤖")

st.title("🤖 Nexura AI — Elite Product Research Agent")

# SESSION
if "products" not in st.session_state:
    st.session_state.products = []

# RUN
if st.button("🚀 Run AI Scan"):
    products = generate_products(40)

    for p in products:
        p["score"] = calculate_score(p)

    products = sorted(products, key=lambda x: x["score"], reverse=True)
    st.session_state.products = products

# LOAD SAVED
saved_ids = get_saved_ids()

# DISPLAY
for p in st.session_state.products:

    with st.container():
        col1, col2 = st.columns([3,1])

        with col1:
            st.subheader(f"🔗 [{p['name']}]({p['amazonLink']})")
            st.write(f"💰 Price: ${p['price']}")
            st.write(f"📊 Revenue: ${p['monthlyRevenue']}")
            st.write(f"🔍 Search: {p['searchVolume']}")
            st.write(f"⭐ Reviews: {p['reviews']}")

        with col2:
            st.metric("Score", f"{p['score']}/100")

        st.write(f"📦 Weight: {p['weight']}kg | 📈 Trend: {p['trend']}")
        st.write(f"💵 Margin: {p['margin']}% | Profit: ${p['profit']}")

        # AI
        if st.button(f"Analyze {p['id']}"):
            st.info(analyze_product(p["name"]))

        # SAVE / UNSAVE
        if p["id"] in saved_ids:
            if st.button(f"❌ Unsave {p['id']}"):
                unsave_product(p["id"])
                st.rerun()
        else:
            if st.button(f"❤️ Save {p['id']}"):
                save_product(p["id"], p["name"], p["score"])
                st.rerun()

        st.markdown("---")
