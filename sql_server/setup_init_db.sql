/*
** Copyright Microsoft, Inc. 1994 - 2000
** All Rights Reserved.
*/


-- Create and use test_init database

CREATE DATABASE test_init
GO

USE test_init
GO

-- Default schema is dbo.

SET NOCOUNT ON
GO

set quoted_identifier on
GO

/* Set DATEFORMAT so that the date strings are interpreted correctly regardless of
   the default DATEFORMAT on the server.
*/
SET DATEFORMAT mdy
GO

/*
Create a single sample fTest table
*/

DROP TABLE IF EXISTS fTest
GO


CREATE TABLE "fTest" (
	"testID" "int" IDENTITY (1, 1) NOT NULL ,
	"LastName" nvarchar (20) NOT NULL ,
	"FirstName" nvarchar (10) NOT NULL ,
	CONSTRAINT "PK_Test" PRIMARY KEY  CLUSTERED 
	(
		"testID"
	)
)
GO

 CREATE  INDEX "LastName" ON "dbo"."fTest"("LastName")
GO