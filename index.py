# -*- coding: utf-8 -*-
import tweepy
import logging
import time
from src.config import create_api
from src.config import langs
from src.translate import translate
import json
from types import SimpleNamespace
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
langtypes = langs()

def check_mentions(api, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,tweet_mode='extended', since_id=since_id).items():
        tweetText = tweet.full_text.lower()
        selectLang = 0
        selLang = ""
        for lan in langtypes:
            selectLang = tweetText.find("-"+lan)
            if(selectLang > 0):
                selLang = tweetText[selectLang+1:selectLang+1+len(lan)]
                break
        if('media' in tweet.entities):
            for med in tweet.entities['media']:
                message = translate(med['media_url'], selLang)
                message = [message[i:i+(279-len(tweet.user.screen_name)-2)] for i in range(0, len(message)-len(tweet.user.screen_name)-2, (279-len(tweet.user.screen_name)-2))]
                threadParentId = tweet.id
                for msg in message:
                    logger.info("Answering to "+tweet.user.name)
                    
                    threadParentId = api.update_status(
                        status="@"+tweet.user.screen_name+" "+msg,
                        in_reply_to_status_id=threadParentId,
                    ).id
        else:
            logger.info("Answering noMedia "+ tweet.user.screen_name)

            # api.update_status(
            #     status="Você não anexou nenhum arquivo!\n" +
            #     str(datetime.now()),
            #     in_reply_to_status_id=tweet.id,
            # )
        new_since_id = max(tweet.id, new_since_id)
        print(new_since_id)
    return new_since_id

def main():
    # Abre arquivo
    idfile = open('lastid.txt', 'r+')
    since_id = int(idfile.read())

    api = create_api()
    while True:
        since_id = check_mentions(api, since_id)
        idfile.seek(0)
        idfile.write(str(since_id))
        idfile.truncate()
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()
