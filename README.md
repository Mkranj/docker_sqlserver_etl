# Docker SQL Server with Python script template  

A simple set up to run an SQL Server database in a docker container, along with a Python script to run an ETL process against it.
You can run and populate a database without installing external software.  

After the ETL finishes, you can access the database in your DB tool of choice, like DBVisualiser, DBeaver etc. The database will run on localhost port 1433 by default and has the following user credentials that **should be changed**:  

* User: *sa*  
* Password: *CHANGEpass1!*  

Remember to change the credentials in docker-compose.yml and etl.py accordingly.  

## Requirements  
Docker has to be installed. On Windows, install Docker Desktop.  

## How to run  
To run the example, execute `docker compose up` in root folder.  

## Customise for your project 
Customise `sql_server/setup_init_db.sql` to create desired tables and/or databases on the server. **This SQL will be run first.**  It creates a *test_init* database with a single empty *fTest* table by default.  

The `etl/etl.py` file will be run after the SQL server is setup. By default it inserts a single row in the *test_init.dbo.fTest* table.  
Here is where you should create your ETL pipeline, read and transform external files, etc.  

Your data source files should go in the `etl/data` folder, which is designated as a volume for the python etl container. It comes with an *example.log* whose contents get printed to the console during ETL.  
It is bound to the `/data/` folder in the container, so the files will be available to your Python script at that location.  
