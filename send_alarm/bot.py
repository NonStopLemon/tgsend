import telebot as tb
import simplejson as json
from . import config as cfg
from . import errors
from datetime import datetime


class Bot:

    def __init__(self, site_name, error, url):
        self.__bot = tb.TeleBot(cfg.token)
        self.__message = str()
        self.__site_name = site_name
        self.__error = error
        self.__url = url

    def create_message(self):

        self.err_full = errors.enum_rror[self.__error]
        self.__message = "Сервис:{site}\nОшибка:{err}\nТекст ошибки:{full_err}\nСсылка:{url}\nВремя:{time}".format(site=self.__site_name,
                                                                                                                   err=self.__error,
                                                                                                                   full_err=self.err_full,
                                                                                                                   url=self.__url,
                                                                                                                   time=datetime.now())

    def sends(self):
        self.__bot.send_message(cfg.chat_id, self.__message)
