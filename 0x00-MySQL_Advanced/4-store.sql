-- 4-store.sql
-- This script creates a trigger that decreases the quantity of an item
-- in the `items` table whenever a new order is added to the `orders` table.

DELIMITER $$

CREATE TRIGGER decrease_quantity_after_insert
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END$$

DELIMITER ;
