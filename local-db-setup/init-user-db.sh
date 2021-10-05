#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER docker password 'my-local-pass';
    CREATE DATABASE docker;
    GRANT ALL PRIVILEGES ON DATABASE docker TO docker;
    \c docker
    CREATE TABLE users (name text not null);
    ALTER TABLE users OWNER TO docker; -- Not clear how to connect as 'docker' user, so this is a slight kludge
    INSERT INTO users (name) values ('John');
EOSQL
