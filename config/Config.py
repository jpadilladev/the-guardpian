import configparser
import logging as log
from pathlib import Path

from service.EmailSender import EmailSender
from service.GuardpianService import GuardpianService
from service.IftttClient import IftttClient
from util.Camera import Camera
from util.Gpio import Gpio


class Config:
    def __init__(self):
        self.__log_settings()
        config = self.__read_config()
        settings = self.__get(config, 'settings')
        ifttt_settings = self.__get(config, 'ifttt')
        debug = settings['debug'] == 'true'
        if debug:
            log.info('Debug mode enabled')
        email_sender = self.__create_email_sender(config, debug)
        self.guardpian_service = GuardpianService(
            '/home/pi/Desktop/', Camera(debug), Gpio(debug, int(settings['pin'])), email_sender,
            int(settings['ifttt']) == 'true',
            IftttClient(debug, ifttt_settings['webhooks_url'], ifttt_settings['event_name_on'],
                        ifttt_settings['event_name_off']))

    def __create_email_sender(self, config, debug):
        smtp = self.__get(config, 'smtp')
        email_sender = EmailSender(debug, smtp['smtp_server'], smtp['smtp_port'], smtp['from_mail'],
                                   smtp['from_password'], smtp['recipients'], smtp['subject'])
        return email_sender

    def __log_settings(self):
        log.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=log.INFO)

    def __read_config(self):
        config = configparser.RawConfigParser()
        file_path = str(Path(__file__).parent.parent.absolute()) + '/config.properties'
        config.read(file_path)
        return config

    def __get(self, config, section):
        return dict(config.items(section))
