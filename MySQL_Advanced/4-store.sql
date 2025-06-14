-- This SQL script creates a database for a store, including tables for items, orders, and customers.
CREATE TRIGGER decrease_quantity AFTER INSERT ON orders
FOR EACH ROW UPDATE items
SET
quantity = quantity - NEW.number
WHERE name = NEW.item_name;