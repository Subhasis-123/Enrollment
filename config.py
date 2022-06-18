import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xa8.8\xcc\xdft2\xd7H\xf8,\xe9\x87\xe86'

    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment' }


    