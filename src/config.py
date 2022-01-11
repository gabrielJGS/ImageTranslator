import tweepy
import logging
import os
# from os.path import join, dirname
# from dotenv import load_dotenv

# dotenv_path = join(dirname(__file__), '../.env')
# load_dotenv(dotenv_path)

logger = logging.getLogger()

def create_api():
    CONSUMER_KEY = os.environ("CONSUMER_KEY")
    CONSUMER_SECRET = os.environ("CONSUMER_SECRET")
    ACCESS_TOKEN = os.environ("ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.environ("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api

def langs():
    return ['af','sq','am','ar','hy','az','eu','be','bn','bs','bg','ca','ceb','ny','zh-cn','zh-tw','co','hr','cs','da','nl','en','eo','et','tl','fi','fr','fy','gl','ka','de','el','gu','ht','ha','haw','iw','he','hi','hmn','hu','is','ig','id','ga','it','ja','jw','kn','kk','km','ko','ku','ky','lo','la','lv','lt','lb','mk','mg','ms','ml','mt','mi','mr','mn','my','ne','no','or','ps','fa','pl','pt','pa','ro','ru','sm','gd','sr','st','sn','sd','si','sk','sl','so','es','su','sw','sv','tg','ta','te','th','tr','uk','ur','ug','uz','vi','cy','xh','yi','yo','zu']