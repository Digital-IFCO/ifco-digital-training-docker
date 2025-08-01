import streamlit as st
import pandas as pd
import psycopg2

# PostgreSQL connection
conn = psycopg2.connect(
    host="pg",
    port=5432,
    database="visits_db",
    user="demo",
    password="demo"
)

# Load data functions
@st.cache_data
def load_raw_visits():
    return pd.read_sql("SELECT * FROM raw_visits;", conn)

@st.cache_data
def load_user_sessions():
    return pd.read_sql("SELECT * FROM user_sessions;", conn)

@st.cache_data
def load_page_stats():
    return pd.read_sql("SELECT * FROM page_stats;", conn)

# Fetch all datasets
df_raw = load_raw_visits()
df_sessions = load_user_sessions()
df_pages = load_page_stats()

# Dashboard Title
st.title("🔍 User Visits Dashboard")

# Metrics from raw_visits
st.metric("Total Users", df_raw["user_id"].nunique())
st.metric("Total Visits", len(df_raw))
st.metric("Avg Visit Duration (sec)", round(df_raw["duration_seconds"].mean(), 2))

# Visits per user
visits_per_user = df_raw.groupby("user_id").size().reset_index(name="total_visits")
st.subheader("👤 Total Visits per User")
st.bar_chart(visits_per_user, x="user_id", y="total_visits")

# Visits over time
df_raw["visit_date"] = pd.to_datetime(df_raw["visit_timestamp"]).dt.date
visits_over_time = df_raw.groupby("visit_date").size().reset_index(name="visits")
st.subheader("🕒 Visits Over Time")
st.line_chart(visits_over_time, x="visit_date", y="visits")

# Table 1: Raw visits
st.subheader("📋 Raw Visit Data")
st.dataframe(df_raw)

# Table 2: Aggregated user sessions (from DBT)
st.subheader("🧠 Aggregated User Sessions")
st.dataframe(df_sessions)

# Table 3: Page statistics (from DBT)
st.subheader("📄 Page Stats")
st.dataframe(df_pages)