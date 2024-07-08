
class Azure():
    def __init__(self):
        pass

    def ms_connect(self):
        pass

    def ms_login(self):
        pass

    def ms_sendData(self):
        pass

    def ms_receiveData(self):
        pass

    def ms_disconnect(self):
        pass

class Aws():
    def aws_conn(self, id, pass):
        pass

    def aws_setData(self):
        pass

    def aws_getData(self):
        pass

    def aws_bye(self):
        pass

def run(za:Azure):
    az.ms_connect()
    az.ms_login("KFC",'1234')
    az.ms_send_data()
    az.ms_disconnect()

def client():
    run(Azure())