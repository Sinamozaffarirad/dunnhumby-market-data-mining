CREATE LOGIN market WITH PASSWORD='StrongPass123!';
CREATE DATABASE marketdb;
CREATE USER market FOR LOGIN market;
ALTER ROLE db_owner ADD MEMBER market;

SELECT @@SERVERNAME;          -- should show LENOVO\SQLEXPRESS
SELECT name FROM sys.server_principals WHERE type_desc = 'SQL_LOGIN';

IF NOT EXISTS (SELECT * FROM sys.server_principals WHERE name = 'market')
BEGIN
    CREATE LOGIN market WITH PASSWORD = 'StrongPass123!', CHECK_POLICY = OFF;
END
GO

/* ②  Create the database if it doesn't exist */
IF DB_ID('marketdb') IS NULL
BEGIN
    CREATE DATABASE marketdb;
END
GO

/* ③  Map the login to the database and grant rights */
USE marketdb;
IF NOT EXISTS (SELECT * FROM sys.database_principals WHERE name = 'market')
BEGIN
    CREATE USER market FOR LOGIN market;
END
/* give full rights during development */
ALTER ROLE db_owner ADD MEMBER market;
GO

