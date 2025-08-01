
with base as (
  select
    user_id,
    count(*) as total_visits,
    avg(duration_seconds) as avg_duration
  from raw_visits
  group by user_id
)

select * from base
