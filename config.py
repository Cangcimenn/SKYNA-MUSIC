# yooo guiz Herox 
import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "SKYNA MUSIC")
API_ID = int(getenv("API_ID", "12345678"))
API_HASH = getenv("API_HASH", "")
OWNER_NAME = getenv("OWNER_NAME", "S K Y")
ALIVE_NAME = getenv("ALIVE_NAME", "SKYNA MUSIC")
BOT_USERNAME = getenv("BOT_USERNAME", "SkynaMusicBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "SkynaAsisstant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ilusi_kata")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ilusi_kata")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5366532807").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/1c0582e56a00290a96f2a.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Cangcimenn/SKYNA-MUSIC")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/592db7e73a2990094e544.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/92e8c83e9148c6fea5f3b.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/92e8c83e9148c6fea5f3b.png")
