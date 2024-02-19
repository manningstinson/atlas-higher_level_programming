-- Create database hbtn_0d_2 if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user user_0d_2 if it does not exist and grant SELECT privilege in hbtn_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
