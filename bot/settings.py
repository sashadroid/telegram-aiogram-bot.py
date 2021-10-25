
import os

BOT_TOKEN = '2021251162:AAF8vN_jq005UctlNYnRxerMMnJ__RmdOfY'

HEROKU_APP_NAME = 'https://whoo-am-i.herokuapp.com/'


# webhook settings
WEBHOOK_HOST = HEROKU_APP_NAME
WEBHOOK_PATH = f'/webhook/{BOT_TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(os.getenv('PORT'))