import json

from loguru import logger

from app.core import bigquery
from app.place import queries


# TODO: add types
@logger.catch
def get_places():
  # Perform a query.
  query_job = bigquery.client.query(queries.get_places_query)  # API request

  df = query_job.to_dataframe()
  result = json.loads(df.to_json(orient='records'))

  return result