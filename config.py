import os
from datetime import datetime
from cachelib import RedisCache

def current_datetime():
    return datetime.now().strftime("%Y-%m-%d")

JINJA_CONTEXT_ADDONS = {
    "current_datetime": current_datetime,
    'my_crazy_macro': lambda x: x*2,
}



APP_NAME= "Arcapps D|W "
APP_ICON = "https://arcapps.org/wp-content/uploads/2023/05/dwarcapps.jpg"
FAVICONS = [{"href": "https://arcapps.org/wp-content/uploads/2023/05/dwicon.jpg"}] 


SQL_MAX_ROW = 10000000
SUPERSET_WEBSERVER_TIMEOUT = 600
SQLLAB_TIMEOUT = 600

MAPBOX_API_KEY = "pk.eyJ1Ijoic2hhaWRhem1pbiIsImEiOiJjbGt0azlkMmIwMHNjM2xvanQxcHY4eTg1In0.Avb_8vGjmooMTDxnaWyubQ"

CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_HOST': 'redis',
    'CACHE_REDIS_PORT': 6379,
    'CACHE_REDIS_DB': 1,
    'CACHE_REDIS_URL': 'redis://redis:6379/1'}
SQLALCHEMY_DATABASE_URI = \
    'postgresql+psycopg2://excel:K}QOt_4^cC!u9=V?Vg%J@db:5432/excel_dw'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'Ys8I8WVHIYvBtpKP9enqHmsJ6'
ENABLE_PROXY_FIX = True

SQLLAB_CTAS_NO_LIMIT = True

FEATURE_FLAGS = {
        "ALERT_REPORTS": True,
        "ENABLE_TEMPLATE_PROCESSING": True,
        "THUMBNAILS": True,
      "THUMBNAILS_SQLA_LISTENERS": True,
        'CACHE_TYPE': 'RedisCache',
        'CACHE_DEFAULT_TIMEOUT': 86400,
        'CACHE_KEY_PREFIX': 'superset_filter_',
        'CACHE_REDIS_URL': 'redis://redis:6379/1'
        }
        
# Cache 

DATA_CACHE_CONFIG = {
    "CACHE_TYPE": "SupersetMetastoreCache",
    "CACHE_KEY_PREFIX": "superset_results",  # make sure this string is unique to avoid collisions
    "CACHE_DEFAULT_TIMEOUT": 86400,  # 60 seconds * 60 minutes * 24 hours
}

# On Redis

RESULTS_BACKEND = RedisCache(
    host='redis', port=6379, key_prefix='superset_results')

RESULTS_BACKEND_USE_MSGPACK = False

class CeleryConfig(object):
    BROKER_URL = "redis://redis:6379/0"
    CELERY_IMPORTS = ("superset.sql_lab",)
    CELERY_RESULT_BACKEND = "redis://redis:6379/0"
    CELERY_ANNOTATIONS = {"tasks.add": {"rate_limit": "10/s"}}


CELERY_CONFIG = CeleryConfig
RESULTS_BACKEND = RedisCache(host="redis", port=6379, key_prefix="superset_results")