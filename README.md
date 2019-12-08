# The Guardpian

This small project uses a Raspberry Pi 3B+, a Camera and a PIR Sensor and it is used as a Security Camera.

## Requirements

- [Raspberry Pi](https://www.raspberrypi.org/) - Any version of Raspberry Pi will work.
- [PIR Motion Sensor](https://www.amazon.co.uk/gp/product/B00NFXBPU8) - A PIR motion sensor and linked to GPIO 4.
- [Pi Camera](https://www.amazon.co.uk/gp/product/B07TWHB8B4)
- Python 
- GIT (to clone this repo)

## How it works

When the PIR Sensor captures any motion, it will trigger a camera shot to be saved.

To make it work on your own Raspberry Pi, you will need Python and Git installed on your raspberry.

Plug the camera to your Raspberry and the PIR Motion Sensor using GPIO 4. 

To start The Guardpian, clone this repo and then use Python to run it.

```
git clone https://github.com/jpadilladev/the-guardpian.git

python the-guardpian/theguardpian/main.py
```

It is recommended to add the starting script at Raspberry boot.

## Settings
You can change the default settings using `config.properties.sample`, removing the `.sample` suffix and using your own as `config.properties`

## Debugging

You can enable debug mode in config.properties under settings section, using `debug = true`

(WIP)


