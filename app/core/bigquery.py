import os

from app.core.config import settings

from google.cloud import bigquery
from google.oauth2 import service_account


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BIGQUERY_CREDENTIALS = os.path.join(BASE_DIR, settings.BIGQUERY_CREDENTIALS_FILE)
credentials = service_account.Credentials.from_service_account_file(BIGQUERY_CREDENTIALS)
client = bigquery.Client(credentials=credentials, project=settings.BIGQUERY_PROJECT_ID)
