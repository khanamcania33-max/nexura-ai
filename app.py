import streamlit as st
from data_engine import generate_products
from scorer import calculate_score
from database import save_product, get_saved

# SAFE IMPORT
try:
    from ai_analyzer import analyze_product
except:
    def analyze_product(x):
        return "AI unavailable"

st.set_page_config(layout="wide", page_title="Nexura AI", page_icon="🤖")

st.title("🤖 Nexura AI — Product Intelligence")

# SESSION STATE
if "products" not in st.session_state:
    st.session_state.products = []

# RUN AGENT
if st.button("🚀 Run AI Scan"):
    with st.spinner("AI scanning..."):
        products = generate_products(30)

        for p in products:
            p["score"] = calculate_score(p)

        products = sorted(products, key=lambda x: x["score"], reverse=True)

        st.session_state.products = products

# DISPLAY PRODUCTS
for p in st.session_state.products:
    with st.container():
        col1, col2 = st.columns([3, 1])

        with col1:
            st.subheader(p["name"])
            st.write(f"💰 Price: ${p['price']}")
            st.write(f"[Amazon Link]({p['amazonLink']})")

        with col2:
            st.metric("Score", f"{p['score']}/100")

        # AI ANALYSIS
        if st.button(f"Analyze {p['id']}"):
            result = analyze_product(p["name"])
            st.info(result)

        # SAVE
        if st.button(f"Save {p['id']}"):
            save_product(p["name"], p["score"])
            st.success("Saved!")

        st.markdown("---")

# SIDEBAR SAVED
st.sidebar.title("📊 Saved Products")

saved = get_saved()

for name, score in saved:
    st.sidebar.write(f"{name} ({score})")
