import json

from loguru import logger

from app.place.queries import queries
from app.core.bigquery import bigquery


@logger.catch
async def get_places(limit: int, skip: int):
  query_job = await queries.get_places(bigquery.client, limit=limit, offset=skip)
  df = query_job.to_dataframe()
  result = json.loads(df.to_json(orient='records'))

  return result