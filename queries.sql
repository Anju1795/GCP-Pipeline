-- Busiest pickup station
SELECT start_station_name, COUNT(*) AS rides
FROM `your_project.bike_analysis.bike_cleaned`
GROUP BY start_station_name
ORDER BY rides DESC
LIMIT 5;

-- Average trip duration per day
SELECT day_of_week, AVG(duration_min) as avg_duration
FROM `your_project.bike_analysis.bike_cleaned`
GROUP BY day_of_week
ORDER BY avg_duration DESC;
