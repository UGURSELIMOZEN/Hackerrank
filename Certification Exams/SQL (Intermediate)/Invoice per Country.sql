


------ My MS SQL (SQL Server) Solution -----



SET NOCOUNT ON;


SELECT country.country_name , COUNT(invoice.invoice_number) ,ROUND(AVG(invoice.total_price) ,6) FROM country
JOIN city ON country.id = city.country_id
JOIN customer ON customer.city_id = city.id
JOIN invoice ON invoice.customer_id = customer.id
GROUP BY country.country_name
HAVING   ROUND(AVG(invoice.total_price) ,6) >  COUNT(invoice.invoice_number) * ROUND(AVG(invoice.total_price) ,6) / COUNT(country.country_name) ;

go
