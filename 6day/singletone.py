import logger


class SingletonLogger:
    single_instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.single_instance:
            cls.single_instance = super(SingletonLogger, cls).__new__(cls)
        return cls.single_instance

    def __init__(self):
        self.single_instance = self.single_instance


logger1 = SingletonLogger()
logger2 = SingletonLogger()
print(logger1 == logger2)
