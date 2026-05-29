import plotly.express as px
import streamlit as st

from analytics import delay_by_route, kpi_summary, load_data, monthly_tonnage, revenue_by_route
from rag_search import search_docs

st.set_page_config(page_title="LogisticsForce AI Demo", layout="wide")

st.title("LogisticsForce AI Demo")
st.caption("SQL-style logistics analytics + RAG-style knowledge retrieval over synthetic truck movement data")

try:
    df = load_data()
except FileNotFoundError as exc:
    st.error(str(exc))
    st.stop()

summary = kpi_summary(df)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Shipments", f"{summary['shipments']:,}")
col2.metric("Revenue", f"${summary['revenue_usd']:,.0f}")
col3.metric("Tonnage", f"{summary['tonnage']:,.0f}")
col4.metric("Avg Delay Hours", f"{summary['avg_delay_hours']:.1f}")

st.subheader("Ask a logistics question")
question = st.text_input(
    "Try: total revenue by route, monthly tonnage, route delays, or KPI guide",
    "Show total revenue by route",
)

question_lower = question.lower()

if "delay" in question_lower:
    result = delay_by_route(df)
    st.dataframe(result, use_container_width=True)
    st.plotly_chart(px.bar(result.head(10), x="route", y="avg_delay_hours", title="Average Delay Hours by Route"), use_container_width=True)
elif "month" in question_lower or "tonnage" in question_lower or "volume" in question_lower:
    result = monthly_tonnage(df)
    st.dataframe(result, use_container_width=True)
    st.plotly_chart(px.line(result, x="month", y="tonnage", title="Monthly Tonnage Trend"), use_container_width=True)
elif "guide" in question_lower or "kpi" in question_lower or "knowledge" in question_lower:
    matches = search_docs(question)
    for match in matches:
        st.markdown(f"### {match['title']}")
        st.write(match["excerpt"])
        st.caption(f"Similarity score: {match['score']:.2f}")
else:
    result = revenue_by_route(df)
    st.dataframe(result, use_container_width=True)
    st.plotly_chart(px.bar(result.head(10), x="route", y="revenue_usd", title="Revenue by Route"), use_container_width=True)

st.divider()
st.write("This demo uses synthetic data and simple intent routing. A production version would connect to SQL databases, ERP/TMS systems, and an LLM-backed retrieval layer.")
