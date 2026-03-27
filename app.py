import streamlit as st
from data_engine import generate_products
from scorer import calculate_score
from database import save_product, unsave_product, get_saved_ids

try:
    from ai_analyzer import analyze_product
except:
    def analyze_product(x): return "AI unavailable"

st.set_page_config(layout="wide", page_title="Nexura AI", page_icon="🤖")

# 🔥 PREMIUM CSS
st.markdown("""
<style>
body {background-color:#0e1117;color:white;}
.card {
    background:#161b22;
    padding:20px;
    border-radius:12px;
    margin-bottom:15px;
    border:1px solid #30363d;
}
.card:hover {border:1px solid #58a6ff;}
</style>
""", unsafe_allow_html=True)

st.title("🤖 Nexura AI — Elite Product Finder")

# SESSION
if "products" not in st.session_state:
    st.session_state.products = []

# FILTERS UI 🔥
st.sidebar.header("🔍 Filters")

min_price = st.sidebar.slider("Min Price", 10, 100, 20)
max_price = st.sidebar.slider("Max Price", 20, 200, 40)
max_reviews = st.sidebar.slider("Max Reviews", 100, 5000, 1500)
min_margin = st.sidebar.slider("Min Margin %", 10, 50, 15)

# RUN
if st.button("🚀 Run AI Scan"):
    products = generate_products(50)

    for p in products:
        p["score"] = calculate_score(p)

    st.session_state.products = products

saved_ids = get_saved_ids()

# FILTER APPLY
filtered = [
    p for p in st.session_state.products
    if min_price <= p["price"] <= max_price
    and p["reviews"] <= max_reviews
    and p["margin"] >= min_margin
]

# SORT
filtered = sorted(filtered, key=lambda x: x["score"], reverse=True)

# DISPLAY
for p in filtered:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader(f"🔗 [{p['name']}]({p['amazonLink']})")
    st.write(f"💰 Price: ${p['price']} | ⭐ Reviews: {p['reviews']}")
    st.write(f"📊 Search: {p['searchVolume']} | 📦 Weight: {p['weight']}kg")
    st.write(f"💵 Margin: {p['margin']}% | Profit: ${p['profit']}")
    st.metric("Score", f"{p['score']}/100")

    col1, col2 = st.columns(2)

    with col1:
        if st.button(f"Analyze {p['id']}"):
            st.info(analyze_product(p["name"]))

    with col2:
        if p["id"] in saved_ids:
            if st.button(f"❌ Unsave {p['id']}"):
                unsave_product(p["id"])
                st.rerun()
        else:
            if st.button(f"❤️ Save {p['id']}"):
                save_product(p["id"], p["name"], p["score"])
                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
