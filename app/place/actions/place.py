import json
from app.core import bigquery

# TODO: find a better way to maintain this
get_places_query = ('SELECT * FROM `oceana_twitter.twitter_place` LIMIT 1')


# TODO: add types
def get_places():
  # Perform a query.
  query_job = bigquery.client.query(get_places_query)  # API request
  # rows = query_job.result()  # Waits for query to finish

  # print(rows)
  # return rows
  # for row in rows:
  #   print(row.name)

  df = query_job.to_dataframe()
  result = json.dumps(json.loads(df.to_json(orient='records')), indent=2)
  # result = df.to_json(orient='records')
  print(type(result))
  return result