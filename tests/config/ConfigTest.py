from theguardpian.config.Config import Config


def test_config_debug_is_true():
    config = Config()
    assert config.camera.debug
    assert config.gpio.debug


if __name__ == '__main__':
    test_config_debug_is_true()
    print('All tests passed.')
