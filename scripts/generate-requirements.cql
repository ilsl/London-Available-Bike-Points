CREATE KEYSPACE requirements WITH REPLICATION = {'class': 'SimpleStrategy','replication_factor':1};
CREATE TABLE requirements.stats (packages text PRIMARY KEY);
COPY requirements.stats(packages) FROM '/home/requirements.txt' WITH DELIMITER=',' AND HEADER=FALSE;
SELECT * FROM requirements.stats;