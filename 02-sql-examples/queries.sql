-- Schema
CREATE TABLE sales (
  date DATE,
  region TEXT,
  product TEXT,
  units INT,
  unit_price NUMERIC
);

-- Sample data
INSERT INTO sales VALUES
('2025-01-01','Marmara','Phone',12,350),
('2025-01-01','Akdeniz','Laptop',5,900),
('2025-01-02','Ege','Tablet',9,250),
('2025-01-02','Marmara','Phone',8,350),
('2025-01-03','İç Anadolu','Headphones',20,60),
('2025-01-04','Akdeniz','Phone',7,350),
('2025-01-04','Ege','Laptop',3,900),
('2025-01-05','Marmara','Tablet',10,250),
('2025-01-05','İç Anadolu','Laptop',4,900),
('2025-01-06','Akdeniz','Headphones',15,60);

-- KPIs
-- Total revenue
SELECT SUM(units * unit_price) AS total_revenue
FROM sales;

-- Revenue by product
SELECT product, SUM(units * unit_price) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC;

-- Top region by revenue
SELECT region, SUM(units * unit_price) AS revenue
FROM sales
GROUP BY region
ORDER BY revenue DESC
LIMIT 1;

-- Region revenue share (%)
SELECT
  region,
  ROUND(100.0 * SUM(units*unit_price) /
        (SELECT SUM(units*unit_price) FROM sales), 1) AS revenue_share_pct
FROM sales
GROUP BY region
ORDER BY revenue_share_pct DESC;

-- Daily revenue time series
SELECT date, SUM(units * unit_price) AS daily_revenue
FROM sales
GROUP BY date
ORDER BY date;
