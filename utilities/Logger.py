import logging

class LogGenerator:

    @staticmethod
    def log_gen():

        logger = logging.getLogger() # to get log
        logfile = logging.FileHandler("F:\\STUDY\\Credence IT\\nopcom_pytest_project\\Logs\\test_Userlogin.log") # to set path of log file

        log_formate = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s ") # creating a formate
        logfile.setFormatter(log_formate) # applying formate to logfile

        logger.addHandler(logfile) # add logs to the logfile everytime of execution to the same file
        logger.setLevel(logging.INFO) # set the log level ( INFO ,WARNING , ERROR , CRITICAL , DEBUG)

        return logger