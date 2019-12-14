from config.Config import Config
import logging as log


def main():
    log.info('Starting The Guardpian...')
    config = Config()
    config.guardpian_service.start()


if __name__ == '__main__':
    main()
