from mcrcon import MCRcon
from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("RCON_HOST")
PORT = int(os.getenv("RCON_PORT"))
PASSWORD = os.getenv("RCON_PASSWORD")


def command(cmd):
    with MCRcon(HOST, PASSWORD, port=PORT) as mcr:
        return mcr.command(cmd)