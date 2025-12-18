#!/bin/bash

# early exit on any error
set -e

# If the "success" file exists in saved volume, remove it for now
rm -f /var/opt/mssql/.initialized

# Start SQL Server in background
/opt/mssql/bin/sqlservr &

# Wait for SQL Server to be ready
echo "Waiting for SQL Server to start..."
sleep 20

# -C: Trust Server Certificate

# Run initialization scripts
/opt/mssql-tools18/bin/sqlcmd \
    -S localhost \
    -U sa \
    -P "$SA_PASSWORD" \
	-C \
    -i /opt/sql/setup_init_db.sql

# Signal readiness
touch /var/opt/mssql/.initialized

echo "Initialization complete, /mssql/.initialized created."

# Bring SQL Server back to foreground
wait
