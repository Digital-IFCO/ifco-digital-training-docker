-- dbt/models/page_stats.sql

SELECT
  page,
  COUNT(*) AS total_visits,
  AVG(duration_seconds) AS avg_duration
FROM raw_visits
GROUP BY page