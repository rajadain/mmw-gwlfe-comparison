-- These queries were used to get the data stored in my local computer's
-- core_job table of various MapShed runs

SELECT DISTINCT ON (model_input)
       model_input, result::json
FROM core_job
WHERE model_input LIKE '{''wkaoi'':%' -- MapShed Input with Saved Shape
  AND result LIKE '{"n38":%' -- MapShed Output (excludes Subbasin)
  AND status = 'complete';
