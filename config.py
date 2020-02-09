from configparser import ConfigParser


class Config():

    config = ConfigParser()
    config.read('data.ini')

    instance = config.getint('main', 'instance')
    status = config.get('main', 'status')

    instance += 1  # increase instance integer by 1 on launch

    config.set('main', 'instance', str(instance))

    def write():
        with open('data.ini', 'w+') as configfile:
            config.write(configfile)

    write()
