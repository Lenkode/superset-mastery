import os

# -------------------------------------------------------------------
# Database connection
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
    "CACHE_KEY_PREFIX": "superset_preprod_",
    "CACHE_REDIS_URL": "redis://redis:6379/0",
}

# -------------------------------------------------------------------
# Redis - Celery
# -------------------------------------------------------------------
class CeleryConfig:
    broker_url = "redis://redis:6379/1"
    result_backend = "redis://redis:6379/2"
    worker_log_level = "INFO"
    worker_prefetch_multiplier = 1
    task_acks_late = True

CELERY_CONFIG = CeleryConfig

# -------------------------------------------------------------------
# Security
# -------------------------------------------------------------------
SECRET_KEY = os.environ["SUPERSET_SECRET_KEY"]

# -------------------------------------------------------------------
# Preprod-specific settings
# -------------------------------------------------------------------
DEBUG = False
FLASK_ENV = "production"
SUPERSET_WEBSERVER_TIMEOUT = 120

SQL_MAX_ROW = 10000
DISPLAY_MAX_ROW = 1000

ENABLE_CORS = True
CORS_OPTIONS = {
    "supports_credentials": True,
    "allow_headers": ["*"],
    "resources": ["*"],
    "origins": ["http://localhost:8089"],
}

FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
    "DASHBOARD_NATIVE_FILTERS": True,
    "ALERT_REPORTS": True,
    "DRILL_TO_DETAIL": True,
    "DRILL_BY": True,
    "DATAPANEL_CLOSED_BY_DEFAULT": False,
}

# Row limits
ROW_LIMIT = 50000
SQL_MAX_ROW = 50000
DISPLAY_MAX_ROW = 50000

# Row limits
ROW_LIMIT = 300000
SQL_MAX_ROW = 300000
DISPLAY_MAX_ROW = 300000
