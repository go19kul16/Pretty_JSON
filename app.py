import streamlit as st
import json

st.set_page_config(page_title="JSON Pretty Printer", layout="wide")

st.title("🧾 JSON Pretty Printer")

st.write(
    "Paste your **raw or unformatted JSON** below. "
    "The app will validate it and display a **pretty-printed version**."
)

raw_json = st.text_area(
    "Raw JSON Input",
    height=300,
    placeholder='{"a":1,"b":{"c":2,"d":[3,4]}}'
)

if st.button("Pretty Print JSON"):
    if not raw_json.strip():
        st.warning("Please paste some JSON first.")
    else:
        try:
            parsed_json = json.loads(raw_json)
            pretty_json = json.dumps(parsed_json, indent=4, ensure_ascii=False)

            st.subheader("Pretty Printed JSON")
            st.code(pretty_json, language="json")

        except json.JSONDecodeError as e:
            st.error("Invalid JSON ❌")
            st.write(f"**Error:** {e}")
