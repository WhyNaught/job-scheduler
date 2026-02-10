#!/bin/bash
set -e
set -a
source .env
set +a

echo "Starting MySQL container:"
echo "  DB_NAME=$DB_NAME"
echo "  DB_PORT=$DB_PORT"

sudo docker pull mysql:latest

sudo docker rm -f "$DB_NAME" 2>/dev/null || true

sudo docker run \
  --name "$DB_NAME" \
  -e MYSQL_ROOT_PASSWORD="$DB_PASSWORD" \
  -e MYSQL_DATABASE="$DB_NAME" \
  -p "$DB_PORT:3306" \
  -v "$(pwd)/build/mysql-init:/docker-entrypoint-initdb.d" \
  -d mysql:latest
