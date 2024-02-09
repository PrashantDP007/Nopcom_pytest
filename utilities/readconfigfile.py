import configparser

config = configparser.RawConfigParser()

config.read("F:\\STUDY\Credence IT\\nopcom_pytest_project\\Configuration\\config.ini")

class Readconfig():

    @staticmethod
    def getEmail():

        Email = config.get('Login Data','email')
        return Email

    @staticmethod
    def getPassword():
        Password = config.get('Login Data', 'password')
        return Password



