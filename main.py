# -*- coding: utf-8 -*-

import StringIO
import json
import logging
import random
import urllib
import urllib2
import multipart

# стандартные модули для Google Engine
from google.appengine.api import urlfetch
from google.appengine.ext import ndb
import webapp2


# Две следующие строчки необходимы для иморта сторонних библиотек из папки libs
#import sys
#sys.path.insert(0, 'libs')

# Импорт сторонних модулей
# Например
# import vkontakte



#Для удобства все команды можно вывести в словарь
messages = {
            'start_message': ('Мой список команд:\n'
                                +'/about - информация о боте\n'
                                +'/stop - остановить бот\n'),
            'stop_message':('Пока!\n'
                            +'/start - запустить бот'),
            'about_message':  ("Информация о боте\n"
                                +"Автор:        \n"
                                +"Версия:       \n"),

                }


TOKEN = 'ВСТАВЬТЕ ТОКЕН ВАШЕГО БОТА'

BASE_URL = 'https://api.telegram.org/bot' + TOKEN + '/'


# ================================

class EnableStatus(ndb.Model):
    # key name: str(chat_id)
    enabled = ndb.BooleanProperty(indexed=False, default=False)


# ================================

def setEnabled(chat_id, yes):
    es = EnableStatus.get_or_insert(str(chat_id))
    es.enabled = yes
    es.put()

def getEnabled(chat_id):
    es = EnableStatus.get_by_id(str(chat_id))
    if es:
        return es.enabled
    return False


# ================================

class MeHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'getMe'))))


class GetUpdatesHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'getUpdates'))))


class SetWebhookHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        url = self.request.get('url')
        if url:
            self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'setWebhook', urllib.urlencode({'url': url})))))


class WebhookHandler(webapp2.RequestHandler):
    def post(self):
        urlfetch.set_default_fetch_deadline(60)
        body = json.loads(self.request.body)
        logging.info('request body:')
        logging.info(body)
        self.response.write(json.dumps(body))

        update_id = body['update_id']
        message = body['message']
        message_id = message.get('message_id')
        date = message.get('date')
        text = message.get('text')
        fr = message.get('from')
        chat = message['chat']
        chat_id = chat['id']

        if not text:
            logging.info('no text')
            return

        def reply(msg=None, img=None):
            if msg:
                resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
                    'chat_id': str(chat_id),
                    'text': msg.encode('utf-8'),
                    'disable_web_page_preview': 'true',
                    'reply_to_message_id': str(message_id),
                })).read()
            elif img:
                resp = multipart.post_multipart(BASE_URL + 'sendPhoto', [
                    ('chat_id', str(chat_id)),
                    ('reply_to_message_id', str(message_id)),
                ], [
                    ('photo', 'image.jpg', img),
                ])
            else:
                logging.error('no msg or img specified')
                resp = None

            logging.info('send response:')
            logging.info(resp)



############## ОТСЮДА МОЖНО НАЧИНАТЬ КАСТОМИЗИРОВАТЬ ВАШ БОТ ##############

        if text.startswith('/'):

            #СПИСОК КОМАНД ДЛЯ БОТА, НАЧИНАЮЩИХСЯ С /

            if text == '/start':
                reply(messages['start_message'].decode('utf-8'))
                setEnabled(chat_id, True)

            elif text == '/stop':
                mes = 'Пока!\n/start - запустить бот'
                reply(mes.decode('utf-8'))
                setEnabled(chat_id, False)

            elif text == '/about':
                reply(messages['about_message'].decode('utf-8'))
                

            else:
                mes = 'Не уверен, что понимаю, о чем ты...'
                reply(mes.decode('utf-8'))
                

        # Другие команды начинающиеся не с /

        elif 'who are you' in text:
            reply('telegram bot, created by Alexander Osipenko')
        elif 'what time' in text:
            reply('look at the top-right corner of your screen!')
################################################################################
        else:
            if getEnabled(chat_id):
                try:
                    resp1 = json.load(urllib2.urlopen('http://www.simsimi.com/requestChat?lc=en&ft=1.0&req=' + urllib.quote_plus(text.encode('utf-8'))))
                    back = resp1.get('res')
                except urllib2.HTTPError, err:
                    logging.error(err)
                    back = str(err)
                if not back:
                    reply('okay...')
                elif 'I HAVE NO RESPONSE' in back:
                    reply('you said something with no meaning')
                else:
                    reply(back)
            else:
                logging.info('not enabled for chat_id {}'.format(chat_id))


app = webapp2.WSGIApplication([
    ('/me', MeHandler),
    ('/updates', GetUpdatesHandler),
    ('/set_webhook', SetWebhookHandler),
    ('/webhook', WebhookHandler),
], debug=True)
