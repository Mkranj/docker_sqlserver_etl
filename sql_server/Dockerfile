FROM mcr.microsoft.com/mssql/server:2022-latest


# Accept license agreement
ENV ACCEPT_EULA=Y
# SAMPLE PASS
ENV SA_PASSWORD=Vjezbe123!

USER root

COPY ./setup_init_db.sql /opt/sql/setup_init_db.sql

# Script to start up the server and execute the initialization SQL
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]