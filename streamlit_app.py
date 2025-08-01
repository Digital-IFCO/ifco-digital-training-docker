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

# Load data
@st.cache_data
def load_raw_visits():
    return pd.read_sql("SELECT * FROM raw_visits;", conn)

@st.cache_data
def load_user_sessions():
    return pd.read_sql("SELECT * FROM user_sessions;", conn)

# Fetch data
df_raw = load_raw_visits()
df_sessions = load_user_sessions()

# Title
st.title("🔍 User Visits Dashboard")

# Metrics from raw_visits
st.metric("Total Users", df_raw["user_id"].nunique())
st.metric("Total Visits", len(df_raw))
st.metric("Avg Visit Duration (sec)", round(df_raw["duration_seconds"].mean(), 2))

# Visits per user (from raw)
visits_per_user = df_raw.groupby("user_id").size().reset_index(name="total_visits")
st.subheader("📊 Total Visits per User")
st.bar_chart(visits_per_user, x="user_id", y="total_visits")

# Time trend
df_raw["visit_date"] = pd.to_datetime(df_raw["visit_timestamp"]).dt.date
visits_over_time = df_raw.groupby("visit_date").size().reset_index(name="visits")
st.subheader("📈 Visits Over Time")
st.line_chart(visits_over_time, x="visit_date", y="visits")

# Raw visit data
st.subheader("📋 Raw Visit Data")
st.dataframe(df_raw)

# User sessions table
st.subheader("🧾 Aggregated User Sessions")
st.dataframe(df_sessions)