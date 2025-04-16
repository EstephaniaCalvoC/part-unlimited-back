#!/bin/bash

DB_NAME="parts_unlimited_dev.db"

if [ -f "$DB_NAME" ]; then
    echo "Removing existing database file..."
    rm "$DB_NAME"
fi

sqlite3 "$DB_NAME" < ./scripts/part_schema.sql

echo "Database initialized successfully!"
