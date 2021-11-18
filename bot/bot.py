import telebot
import requests
import time

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
API_KEY = os.environ.get("API_KEY")
GITHUB_URL = "https://api.github.com/repos/tch-rom/telegram-chatops/actions/runs"
REPO = "tch-rom/telegram-chatops"

payload = {"event_type": "CD triggered via Telegram"}
headers = {'Content-Type': 'application/json', 'Accept': 'application/vnd.github.everest-preview+json', 'Authorization': f'token {GITHUB_TOKEN}'}
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['deploy'])

def deploy(message):
    bot.send_message(message.chat.id, "Hey! Your deployment must start now. Please check the link: https://github.com/tch-rom/telegram-chatops/actions")
    requests.post(f"https://api.github.com/repos/{REPO}/dispatches", json=payload, headers=headers)
    time.sleep(15)
    while True:
        if get_status(headers, GITHUB_URL) == "success" or get_status(headers, GITHUB_URL) == "failure":
            break
        else:
            pass
    bot.send_message(message.chat.id, get_status(headers, GITHUB_URL))

def get_status(headers, url):

    resp = requests.get(url, headers=headers)

    run_numbers = []
    for workflow in resp.json()['workflow_runs']:
        run_numbers.append(workflow['run_number'])

    max_run_num = max(run_numbers)

    for workflow in resp.json()['workflow_runs']:
        if workflow['run_number'] == max_run_num:
            return workflow['conclusion']
        else:
            continue

bot.polling()