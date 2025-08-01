
# 🐳 Docker Data Pipeline (PySpark + dbt + Postgres + Streamlit)

This project demonstrates a simple end-to-end data pipeline for Data Engineers using Docker.

## ✅ Stack Overview

| Component     | Description                        |
|---------------|------------------------------------|
| **PostgreSQL**| Stores raw and transformed data    |
| **PySpark**   | Reads & processes input CSV        |
| **dbt**       | Transforms data in the database    |
| **Streamlit** | Visualizes the final data output   |

---

## 📋 Prerequisites

Before getting started, make sure you have **Docker Desktop** installed on your system:

- **Docker Desktop**: Download and install from [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)

---

## 🚀 Getting Started

### 1. Clone or unzip the project

```bash
cd docker
```

### 2. Build and start the containers

```bash
docker-compose build
docker-compose up -d
```

---

## 🧪 Run Data Pipeline Steps

### 1. Run PySpark Job (loads CSV into PostgreSQL)

```bash
docker exec -it spark spark-submit /opt/spark/spark_job.py
```

### 2. Run dbt Transformation

```bash
docker exec -it dbt bash
cd /usr/app
dbt run --profiles-dir profiles
exit
```

### 3. Open the Streamlit Dashboard

Visit 👉 [http://localhost:8501](http://localhost:8501)

---

## 📁 Project Structure

```text
.
├── data/
│   └── input.csv                 # Input data file
├── dbt/
│   ├── models/
│   │   └── user_sessions.sql     # dbt model
│   ├── profiles/
│   │   └── profiles.yml          # dbt connection config
│   └── dbt_project.yml
├── custom_spark/
│   ├── Dockerfile                # Custom Spark image
│   └── postgresql-42.2.5.jar     # JDBC Driver (add manually)
├── spark_job.py                  # PySpark transformation script
├── streamlit_app.py              # Streamlit dashboard
└── docker-compose.yml
```

---

## ✨ What You Can Show

- How Spark processes data from CSV and loads it into a warehouse
- How dbt runs transformations in a reproducible way
- How Streamlit creates real-time, interactive dashboards
- How Docker makes the entire pipeline portable and consistent

---

Happy presenting! 🚀
