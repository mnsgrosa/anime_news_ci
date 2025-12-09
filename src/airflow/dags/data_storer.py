import hashlib
import json
import os
from datetime import datetime, timedelta
from typing import Dict, List

import httpx
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.hooks.gcs import GCSHook
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from api.anime import AnimeHandler
from dotenv import load_dotenv
from google.cloud import aiplatform, storage
from handler.chunker import prepare_synopsis

from airflow import DAG

load_dotenv()

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 1, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


def extract_upcoming_api(**context):
    anime_handler = AnimeHandler()
    upcoming_data = anime_handler.get_upcoming_season()
    context["ti"].xcom_push(key="upcoming_data", value=upcoming_data)
