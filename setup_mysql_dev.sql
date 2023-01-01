-- a script that prepare mysql server

-- CREATE DATABASE
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- CREATE NEW USER
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- GIVE PRIVILAGE TO hbnb_dev 
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grant SELECT privlage on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- RELOAD AFTER GIVING PRIVILAGES
FLUSH PRIVILEGES;