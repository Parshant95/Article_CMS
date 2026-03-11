import os
import urllib.parse

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'images11'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'ENTER_STORAGE_KEY'
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'dbcms.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'dbadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'ENTER_SQL_PASSWORD'

    SQLALCHEMY_DATABASE_URI = (
        "mssql+pyodbc://"
        + SQL_USER_NAME
        + ":"
        + urllib.parse.quote_plus(SQL_PASSWORD)
        + "@"
        + SQL_SERVER
        + ":1433/"
        + SQL_DATABASE
        + "?driver=ODBC+Driver+18+for+SQL+Server"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CLIENT_SECRET = os.environ.get('CLIENT_SECRET') or 'ENTER_CLIENT_SECRET'
    CLIENT_ID = os.environ.get('CLIENT_ID') or 'ENTER_CLIENT_ID'

    AUTHORITY = "https://login.microsoftonline.com/common"

    REDIRECT_PATH = "/getAToken"

    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"