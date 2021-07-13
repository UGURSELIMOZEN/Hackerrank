

---- My MS SQL (SQL Server) Solution ---- 


SET NOCOUNT ON;


SELECT price_today.stock_code  FROM price_today , price_tomorrow
WHERE  (price_tomorrow.stock_code = price_today.stock_code) AND (price_tomorrow.price > price_today.price)
ORDER BY stock_code ;


go



