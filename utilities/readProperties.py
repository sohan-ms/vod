import configparser

config = configparser.RawConfigParser()
config.read(r".//Configurations/config.ini")


class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('Hostname', 'baseURL')
        return url

    @staticmethod
    def getEmail():
        email = config.get('Hostname', 'username')
        return email

    @staticmethod
    def getPassword():
        password = config.get('Hostname', 'password')
        return password
