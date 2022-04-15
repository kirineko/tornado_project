import os

BASE_DIRS = os.path.dirname(__file__)

# params
options = {
    'port': 9000,
}

# settings
settings = {
    'static_path': os.path.join(BASE_DIRS, 'static'),
    'template_path': os.path.join(BASE_DIRS, 'templates'),
    'debug': True
}
