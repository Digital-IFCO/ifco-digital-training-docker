
import streamlit as st
import pandas as pd
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="pg",
    port=5432,
    database="visits_db",
    user="demo",
    password="demo"
)

# Load data
@st.cache_data
def load_data():
    query = "SELECT * FROM raw_visits;"
    return pd.read_sql(query, conn)

df = load_data()

# Title
st.title("🔍 User Visits Dashboard")

# Metrics
st.metric("Total Users", df["user_id"].nunique())
st.metric("Total Visits", len(df))
st.metric("Average Visit Duration (sec)", round(df["duration_seconds"].mean(), 2))

# Visits per user
visits_per_user = df.groupby("user_id").size().reset_index(name="total_visits")

st.subheader("📊 Total Visits per User")
st.bar_chart(visits_per_user, x="user_id", y="total_visits")

# Optional: Visits over time
df["visit_date"] = pd.to_datetime(df["visit_timestamp"]).dt.date
visits_over_time = df.groupby("visit_date").size().reset_index(name="visits")

st.subheader("📈 Visits Over Time")
st.line_chart(visits_over_time, x="visit_date", y="visits")

# Raw data table
st.subheader("📋 Raw Visit Data")
st.dataframe(df)
