import config as cfg
import hug
import logging
import logging.config

from falcon import HTTP_200, HTTP_500

# load config
logging.config.fileConfig('{path}/logging.conf'.format(path=cfg.path_name))

# create logger
logger = logging.getLogger('strings_api')


@hug.post('/strings/basic', versions=1)
@hug.local()
def strings_basic(body, hug_timer=3, response=None):
    pass


@hug.post('/strings/intermediate', versions=1)
@hug.local()
def strings_intermediate(body, hug_timer=3, response=None):
    pass
