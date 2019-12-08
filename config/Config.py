import configparser
import os
from pathlib import Path

from service.GuardpianService import GuardpianService
from util.Camera import Camera
from util.Gpio import Gpio


class Config:
    def __init__(self):
        config = self.__read_config()
        settings = self.__get(config, 'settings')
        print(settings)
        debug = settings['debug'] == 'true'
        if debug:
            print('Debug mode enabled')
        self.camera = Camera(debug)
        self.gpio = Gpio(debug)
        self.guardpian_service = GuardpianService(self.camera, self.gpio)

    def __read_config(self):
        config = configparser.RawConfigParser()
        filePath = str(Path(__file__).parent.parent.absolute()) + '/config.properties'
        config.read(filePath)
        return config

    def __get(self, config, section):
        return dict(config.items(section))
