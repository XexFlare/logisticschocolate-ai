-- Revenue by route
SELECT route, COUNT(*) AS shipments, SUM(tonnage) AS total_tonnage, SUM(revenue_usd) AS total_revenue
FROM shipments
GROUP BY route
ORDER BY total_revenue DESC;

-- Monthly tonnage trend
SELECT strftime('%Y-%m', shipment_date) AS month, SUM(tonnage) AS total_tonnage
FROM shipments
GROUP BY month
ORDER BY month;

-- Average delay by route
SELECT route, AVG(delay_hours) AS avg_delay_hours
FROM shipments
GROUP BY route
ORDER BY avg_delay_hours DESC;
