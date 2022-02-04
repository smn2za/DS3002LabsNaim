# Write a query to get Product name and quantity/unit.
SELECT product_name,quantity_per_unit FROM northwind.products;

# Write a query to get current Product list (Product ID and name).
SELECT id, product_name FROM northwind.products;

# Write a query to get discontinued Product list (Product ID and name).
SELECT id, product_name FROM northwind.products WHERE discontinued="1";

# Write a query to get most expense and least expensive Product list (name and unit price).
SELECT distinct product_name, unit_price FROM northwind.order_details JOIN products ON
products.id = order_details.product_id WHERE unit_price = (SELECT MAX(unit_price) FROM order_details) OR
unit_price= (SELECT MIN(unit_price) FROM order_details);

# Write a query to get Product list (id, name, unit price) where current products cost less than $20. 
SELECT distinct product_id, product_name, unit_price FROM products JOIN order_details ON
products.id = order_details.product_id WHERE unit_price<20;

# Write a query to get Product list (id, name, unit price) where products cost between $15 and $25.
SELECT distinct product_id, product_name, unit_price FROM products JOIN order_details ON
products.id = order_details.product_id WHERE unit_price between 15 and 20;

#Write a query to get Product list (name, unit price) of above average price.
SELECT distinct product_name, unit_price FROM products JOIN order_details ON
products.id = order_details.product_id WHERE unit_price> (SELECT AVG(unit_price) FROM order_details);

#Write a query to get Product list (name, unit price) of ten most expensive products.
SELECT distinct product_name, unit_price from products JOIN order_details ON
products.id = order_details.product_id ORDER by unit_price DESC LIMIT 10;

#Write a query to count current and discontinued products.
SELECT discontinued,COUNT(*) AS "current" FROM northwind.products GROUP BY discontinued;

#Write a query to get Product list (name, units on order, units in stock) of stock is less than the quantity on order.
SELECT distinct product_name, order_details.quantity as order_quantity, inventory_transactions.quantity as inventory_quantity FROM products JOIN
order_details JOIN inventory_transactions ON products.id=order_details.product_id AND order_details.product_id=inventory_transactions.product_id
WHERE inventory_transactions.quantity < order_details.quantity;