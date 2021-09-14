import json

from loguru import logger

from app.place.queries import queries
from app.core.bigquery import bigquery
# from app.place.models.place import Place


@logger.catch
async def get_places(limit: int = 1, skip: int = 0):
  query_job = await queries.get_places(bigquery.client, limit=limit, offset=skip)
  df = query_job.to_dataframe()
  result = json.loads(df.to_json(orient='records'))

  # I can format the response
  # places = []

  # for place in result:
  #   places.append(Place(**place))

  # return places