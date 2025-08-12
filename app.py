import streamlit as st
from db_utils import init_db, get_all_policies
from collections import Counter
import re

st.set_page_config(page_title="Gov360", layout="wide")
st.title("🇮🇳 Gov360 - Indian Government Policies Explorer")

init_db()
policies = get_all_policies()

# Sidebar filters
st.sidebar.header("🔍 Filter Policies")
sectors = sorted(set(p["sector"] for p in policies))
years = sorted(set(str(p["year"]) for p in policies))

sector_filter = st.sidebar.selectbox("Filter by Sector", ["All"] + sectors)
year_filter = st.sidebar.selectbox("Filter by Year", ["All"] + years)
search_term = st.sidebar.text_input("Search by keyword")

# Keyword Suggestions
st.sidebar.markdown("### 💡 Suggested Keywords")
all_text = " ".join(p["summary"] + " " + p["title"] for p in policies)
words = re.findall(r'\b[a-zA-Z]{4,}\b', all_text.lower())
common_keywords = [w for w, c in Counter(words).most_common(30) if w not in {"india", "government", "policy"}]

with st.sidebar.expander("📌 Top Keywords"):
    for kw in common_keywords[:15]:
        if st.button(kw.capitalize()):
            search_term = kw

# Filter logic
filtered = []
for p in policies:
    if (sector_filter == "All" or p["sector"] == sector_filter) and \
       (year_filter == "All" or str(p["year"]) == year_filter) and \
       (search_term.lower() in p["title"].lower() or search_term.lower() in p["summary"].lower()):
        filtered.append(p)

# Show policies
st.subheader(f"📋 Showing {len(filtered)} policies")
if not filtered:
    st.warning("🚫 No matching policies found.")
else:
    for policy in filtered:
        with st.expander(f"{policy['title']} ({policy['year']})"):
            st.markdown(f"**Sector:** {policy['sector']}")
            st.markdown(f"**Summary:** {policy['summary']}")
            st.markdown(f"**Details:** {policy['details']}")
            st.markdown(f"[🔗 Official Link]({policy['url']})")