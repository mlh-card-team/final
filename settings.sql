-- settings.sql
CREATE DATABASE card_maker;
CREATE USER card_makeruser WITH PASSWORD 'card_maker';
GRANT ALL PRIVILEGES ON DATABASE card_maker TO card_makeruser;