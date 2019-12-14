import logging as log

import requests


class IftttClient:
    def __init__(self, debug, url, event_on, event_off):
        self.debug = debug
        self.url = url
        self.event_on = event_on
        self.event_off = event_off

    def send_event_on(self):
        if not self.debug:
            requests.get(self.url.replace("{event}", self.event_on))
        log.info("IFTTT Event: " + self.event_on)

    def send_event_off(self):
        if not self.debug:
            requests.get(self.url.replace("{event}", self.event_off))
        log.info("IFTTT Event: " + self.event_off)
