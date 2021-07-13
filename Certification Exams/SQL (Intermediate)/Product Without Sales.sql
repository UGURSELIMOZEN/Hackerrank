

------ My MS SQL (SQL Server) Solution -----

SET NOCOUNT ON;


SELECT  DISTINCT Product.sku , Product.product_name FROM Product 
LEFT JOIN Invoice_Item ON Product.id = Invoice_Item.product_id
WHERE Invoice_Item.product_id IS NULL
ORDER BY Product.sku ASC ;

go
