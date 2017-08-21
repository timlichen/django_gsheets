from django.shortcuts import render
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
# Create your views here.
def index(request):
    # Put in name of sheet
    # Add Don't forget to put back client_secret.json
    sheet = client.open("####").sheet1
    list_of_hashes = sheet.get_all_records()
    print(list_of_hashes)

    return render(request, "index.html")
