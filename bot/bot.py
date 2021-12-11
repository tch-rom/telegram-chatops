import telebot
import requests
import time
import os 

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
API_KEY = os.environ.get("API_KEY")
GITHUB_URL = "https://api.github.com/repos/tch-rom/telegram-chatops/actions/runs"
REPO = "tch-rom/telegram-chatops"
busy = False

vm_count = 0
headers = {'Content-Type': 'application/json', 'Accept': 'application/vnd.github.everest-preview+json', 'Authorization': f'token {GITHUB_TOKEN}'}
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['deploy'],)

def deploy(message):

    global busy
    payload = {"event_type": "app_deployment"}

    if busy == False :
        bot.send_message(message.chat.id, "Hey! Your deployment must start now. Please check the link: https://github.com/tch-rom/telegram-chatops/actions")
        requests.post(f"https://api.github.com/repos/{REPO}/dispatches", json=payload, headers=headers)
        busy = True
        time.sleep(15)
        while True:
            if get_status(headers, GITHUB_URL) == "success" or get_status(headers, GITHUB_URL) == "failure":
                break
            else:
                pass
        bot.send_message(message.chat.id, get_status(headers, GITHUB_URL))
        busy = False
    else:
        bot.send_message(message.chat.id, "Hey! You are running a deployment already. Wait till the end (status sharing) and you can run it again.")


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

@bot.message_handler(commands=['vm_create'])

def vm_create(message):

    global busy
    global vm_count
    payload = {"event_type": "vm_create"}
    print(payload)

    if busy == False and vm_count == 0:
        bot.send_message(message.chat.id, "Hey! Let's create you some DO droplet. Please check the link: https://github.com/tch-rom/telegram-chatops/actions")
        requests.post(f"https://api.github.com/repos/{REPO}/dispatches", json=payload, headers=headers)
        vm_count = 1
        busy = True
        time.sleep(15)
        while True:
            if get_status(headers, GITHUB_URL) == "success" or get_status(headers, GITHUB_URL) == "failure":
                break
            else:
                pass
        bot.send_message(message.chat.id, get_status(headers, GITHUB_URL))
        busy = False
    elif vm_count != 0:
        bot.send_message(message.chat.id, "Sorry mate! DO doesn't let us to make more than 1 droplet... Unfortunately. Destroy vm to create the new one")
    else:
        bot.send_message(message.chat.id, "Hey! Hold on, buddy. Our little bot is busy right now.")


@bot.message_handler(commands=['vm_destroy'])

def vm_destroy(message):

    global busy
    global vm_count
    payload = {"event_type": "vm_destroy"}

    if busy == False and vm_count == 1:
        bot.send_message(message.chat.id, "Hey! Let's destroy you some DO droplet. Please check the link: https://github.com/tch-rom/telegram-chatops/actions")
        print(payload)
        requests.post(f"https://api.github.com/repos/{REPO}/dispatches", json=payload, headers=headers)
        vm_count = 0
        busy = True
        time.sleep(15)
        while True:
            if get_status(headers, GITHUB_URL) == "success" or get_status(headers, GITHUB_URL) == "failure":
                break
            else:
                pass
        bot.send_message(message.chat.id, get_status(headers, GITHUB_URL))
        busy = False
    elif vm_count == 0:
        bot.send_message(message.chat.id, "What happened, buddy? You want to destroy nothing?")
    else:
        bot.send_message(message.chat.id, "Hey! Hold on, buddy. Our little bot is busy right now.")

@bot.message_handler(commands=['vm_show_version'])

def vm_show_version(message):
    global event_type
    event_type = "vm_show_version"
    bot.send_message(message.chat.id, "Hey! Here will be your vm_show_version functionality")

@bot.message_handler(commands=['vm_kde_patch'])

def vm_kde_patch(message):
    global event_type
    event_type = "vm_kde_patch"
    bot.send_message(message.chat.id, "Hey! Here will be your vm_kde_patch functionality")

bot.polling()