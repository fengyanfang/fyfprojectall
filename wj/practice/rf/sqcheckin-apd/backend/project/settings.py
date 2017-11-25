#-*- coding:utf-8 -*-

from settings_common import *

# django 容器（如 gunicorn, cherrypy） web服务地址
WEB_SERVER_LISTEN_ADDR = ('0.0.0.0',80)




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
DEBUG=True






CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'TIMEOUT':  30*60, # 30 minutes cache will be deleted
        'OPTIONS': {
            'MAX_ENTRIES': 1000 # not effective for memcached
        }
    },

    'onedaycache': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake2',
        'TIMEOUT':  86400,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}

# FATAL = CRITICAL = 50 ERROR = 40  WARN = WARNING = 30 INFO = 20 DEBUG = 10 NOTSET = 0
LOG_LEVEL = 'INFO'

django_sys_log_setting = {
                            'handlers': ['django_file','console'],
                            'level': LOG_LEVEL,
                            'propagate': False,
                         }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(message)s',
            'datefmt': '%m%d_%H:%M:%S'
        },
        'simple': {
            'format': '%(message)s'
        },
    },
    'handlers': {
        'null': {
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': LOG_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'django_file': {
            'level': LOG_LEVEL,
            'class': 'logging.handlers.RotatingFileHandler',#'logging.FileHandler',
            'filename': BASE_DIR + '/log/django.log',
            'maxBytes' : 1024*1024*10, # 10MB
            'backupCount' : 50,
            'formatter': 'verbose'
        },
        'mgr_file': {
            'level': LOG_LEVEL,
            'class': 'logging.handlers.RotatingFileHandler',#'logging.FileHandler',
            'filename': BASE_DIR + '/log/mgr.log',
            'maxBytes' : 1024*1024*10, # 10MB
            'backupCount' : 50,
            'formatter': 'verbose'
        },

        'teacher_file': {
            'level': LOG_LEVEL,
            'class': 'logging.handlers.RotatingFileHandler',#'logging.FileHandler',
            'filename': BASE_DIR + '/log/teacher.log',
            'maxBytes' : 1024*1024*10, # 10MB
            'backupCount' : 50,
            'formatter': 'verbose'
        },

        'student_file': {
            'level': LOG_LEVEL,
            'class': 'logging.handlers.RotatingFileHandler',#'logging.FileHandler',
            'filename': BASE_DIR + '/log/student.log',
            'maxBytes' : 1024*1024*10, # 10MB
            'backupCount' : 50,
            'formatter': 'verbose'
        },
        'datamodel_file': {
            'level': LOG_LEVEL,
            'class': 'logging.handlers.RotatingFileHandler',#'logging.FileHandler',
            'filename': BASE_DIR + '/log/model.log',
            'maxBytes' : 1024*1024*10, # 10MB
            'backupCount' : 50,
            'formatter': 'verbose'
        },
        'stats_file': {
            'level': LOG_LEVEL,
            'class': 'logging.handlers.RotatingFileHandler',#'logging.FileHandler',
            'filename': BASE_DIR + '/log/stats.log',
            'maxBytes' : 1024*1024*10, # 10MB
            'backupCount' : 50,
            'formatter': 'verbose'
        },
        'sms_file': {
            'level': LOG_LEVEL,
            'class': 'logging.handlers.RotatingFileHandler',#'logging.FileHandler',
            'filename': BASE_DIR + '/log/sms.log',
            'maxBytes' : 1024*1024*10, # 10MB
            'backupCount' : 50,
            'formatter': 'verbose'
        },
        'util_file': {
            'level': LOG_LEVEL,
            'class': 'logging.handlers.RotatingFileHandler',#'logging.FileHandler',
            'filename': BASE_DIR + '/log/util.log',
            'maxBytes' : 1024*1024*10, # 10MB
            'backupCount' : 20,
            'formatter': 'verbose'
        },
    },

    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': LOG_LEVEL,
        },
        'django.request':     django_sys_log_setting,
        'django.security':    django_sys_log_setting,
        'py.warnings':        django_sys_log_setting,
        'django.db.backends': django_sys_log_setting,

        'mgr': {
            'handlers': ['mgr_file','console'],
            'level': LOG_LEVEL,
        },

        'teacher': {
            'handlers': ['teacher_file','console'],
            'level': LOG_LEVEL,
        },

        'student': {
            'handlers': ['student_file','console'],
            'level': LOG_LEVEL,
        },

        'datamodel': {
            'handlers': ['datamodel_file','console'],
            'level': LOG_LEVEL,
        },

        'stats': {
            'handlers': ['stats_file'],
            'level': LOG_LEVEL,
        },
        'sms': {
            'handlers': ['sms_file','console'],
            'level': LOG_LEVEL,
        },
        'util': {
            'handlers': ['util_file'],
            'level': LOG_LEVEL,
        },
    }
}