import configparser
import logging as log
from pathlib import Path

from service.EmailSender import EmailSender
from service.GuardpianService import GuardpianService
from util.Camera import Camera
from util.Gpio import Gpio


class Config:
    def __init__(self):
        log.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',level=log.INFO)
        config = self.__read_config()
        settings = self.__get(config, 'settings')
        debug = settings['debug'] == 'true'
        if debug:
            log.info('Debug mode enabled')
        smtp = self.__get(config, 'smtp')
        email_sender = EmailSender(debug, smtp['smtp_server'], smtp['smtp_port'], smtp['from_mail'],
                                        smtp['from_password'], smtp['recipients'], smtp['subject'])
        self.guardpian_service = GuardpianService('/home/pi/Desktop/', Camera(debug), Gpio(debug), email_sender)

    def __read_config(self):
        config = configparser.RawConfigParser()
        file_path = str(Path(__file__).parent.parent.absolute()) + '/config.properties'
        config.read(file_path)
        return config

    def __get(self, config, section):
        return dict(config.items(section))
