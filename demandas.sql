CREATE EXTERNAL TABLE IF NOT EXISTS demandas (
  legajo STRING,
  anio_nacimiento INT,
  dni STRING,
  persona STRING,
  id STRING,
  nombre STRING
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = '1'
)
LOCATION 's3://project-demandas-raw-argentina/';

--SELECT * FROM demandas;
