import os

class Config(object):
    BOT_TOKEN = os.environ.get("5159393792:AAEkeGYIvbR7YSk0vt_ycXZldwrvIyk8tpQ", "")

    API_ID = int(os.environ.get("9244035", 123456))

    API_HASH = os.environ.get("66c62a85cfbf593a991ea680223a0549", "")
    
    API_KEY = os.environ.get("mx1Xtbpav1m18HUn4hWp", "")

    # AUTH_USERS = set(str(x) for x in os.environ.get("AUTH_USERS", "").split())

    # PRIVATE = bool(os.environ.get("PRIVATE", ""))
