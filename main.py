from config.Config import Config


def main():
    print('Starting The Guardpian...')
    config = Config()
    service = config.guardpian_service
    service.start()


if __name__ == '__main__':
    main()
