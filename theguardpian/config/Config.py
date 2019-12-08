import configparser

from theguardpian.service.GuardpianService import GuardpianService
from theguardpian.util.Camera import Camera
from theguardpian.util.Gpio import Gpio


class Config:
    def __init__(self):
        config = self.__read_config()
        settings = self.__get(config, 'settings')
        self.camera = Camera(settings['debug'])
        self.gpio = Gpio(settings['debug'])
        self.guardpian_service = GuardpianService(self.camera, self.gpio)

    def __read_config(self):
        config = configparser.RawConfigParser()
        config.read('../config.properties')
        return config

    def __get(self, config, section):
        return dict(config.items(section))
