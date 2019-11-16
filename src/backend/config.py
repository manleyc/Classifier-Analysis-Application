class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "B\xb2?.\xdf\x9f\xa7m\xf8\x8a%,\xf7\xc4\xfa\x91"

    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
	DEBUG = True

	SQLALCHEMY_DATABASE_URI = 'sqlite:///C:\\Users\\cmanl\\Documents\\College\\2019-ca400-manleyc4\\src\\backend\\filestorage.db'
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	SESSION_COOKIE_SECURE = False

