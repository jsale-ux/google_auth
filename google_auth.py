import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KEY_FILE = os.path.join(BASE_DIR, "keys.json")

CREDS = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE, SCOPE)
client = gspread.authorize(CREDS)

sheet = client.open("BUS472")
worksheet = sheet.sheet1

print("Accessible Spreadsheets..BUS472")
