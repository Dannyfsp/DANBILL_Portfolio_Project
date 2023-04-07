#!/usr/bin/python3
from os import getenv

APP_MYSQL_USER = getenv('APP_MYSQL_USER')
APP_MYSQL_PWD = getenv('APP_MYSQL_PWD')
APP_MYSQL_HOST = getenv('APP_MYSQL_HOST')
APP_MYSQL_DB = getenv('APP_MYSQL_DB')
APP_API_HOST = getenv('APP_API_HOST')
APP_API_PORT = getenv('APP_API_PORT')

print(APP_MYSQL_USER)
print(APP_MYSQL_PWD)
print(APP_MYSQL_HOST)
print(APP_MYSQL_DB)
print(APP_API_HOST)
print(APP_API_PORT)
