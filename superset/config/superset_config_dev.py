import os

# -------------------------------------------------------------------
# Database connection (Superset metadata)
# -------------------------------------------------------------------
SQLALCHEMY_DATABASE_URI = (
    f"postgresql+psycopg2://"
    f"{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}"
    f"@db:5432/{os.environ['POSTGRES_DB']}"
)

# -------------------------------------------------------------------
# Redis - cache
# -------------------------------------------------------------------
CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_KEY_PREFIX": "superset_dev_",
    "CACHE_REDIS_URL": "redis://redis:6379/0",
}

# -------------------------------------------------------------------
# Redis - Celery broker & results
# -------------------------------------------------------------------
class CeleryConfig:
    broker_url = "redis://redis:6379/1"
    result_backend = "redis://redis:6379/2"
    worker_log_level = "DEBUG"
    worker_prefetch_multiplier = 1
    task_acks_late = True

CELERY_CONFIG = CeleryConfig

# -------------------------------------------------------------------
# Security
# -------------------------------------------------------------------
SECRET_KEY = os.environ["SUPERSET_SECRET_KEY"]

# -------------------------------------------------------------------
# Dev-specific settings
# -------------------------------------------------------------------
DEBUG = True
FLASK_ENV = "development"
SUPERSET_WEBSERVER_TIMEOUT = 300

# Show SQL queries in logs — useful for learning
SQL_MAX_ROW = 1000
DISPLAY_MAX_ROW = 1000

# Allow all origins in dev (relaxed CORS)
ENABLE_CORS = True
CORS_OPTIONS = {
    "supports_credentials": True,
    "allow_headers": ["*"],
    "resources": ["*"],
    "origins": ["http://localhost:8088"],
}

# Feature flags — enable everything useful for dev/learning
FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,   # Jinja in SQL
    "DASHBOARD_NATIVE_FILTERS": True,
    "ALERT_REPORTS": True,
    "DRILL_TO_DETAIL": True,
    "DRILL_BY": True,
    "DATAPANEL_CLOSED_BY_DEFAULT": False,
}
