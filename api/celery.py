from celery import Celery
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

# Initialize Celery app
celery_app = Celery(
    "blog_api_tasks",
    broker=os.getenv("CELERY_BROKER_URL"),
    backend=os.getenv("CELERY_RESULT_BACKEND"),
    include=['api.tasks.email']  # Add specific task modules
)

# Configure Celery
celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='Europe/Istanbul',
    enable_utc=True,
    task_track_started=True,
    task_time_limit=30 * 60,
    worker_prefetch_multiplier=1,
    worker_max_tasks_per_child=50
)

# Discover tasks in the api package
celery_app.autodiscover_tasks(['api'])