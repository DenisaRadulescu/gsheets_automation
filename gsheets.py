import gspread
from google.oauth2.service_account import Credentials


class GoogleSheets:

    def __init__(self, scopes, credentials_path, excel_key):
        self.scopes = scopes
        self.creds = Credentials.from_service_account_file(credentials_path, scopes=self.scopes)
        self.client = gspread.authorize(self.creds)
        self.excel = client.open_by_key(excel_key)
        self.working_sheet = self.excel.sheet1

    def insert_words(self):
        pass

    def modify_cell(self):
        pass

    def get_values(self):
        return self.working_sheet.get_all_records()



scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)

client = gspread.authorize(creds)

full_excel = client.open_by_key("1VQuQKR1E_4_Xq0UrGjp8WasxA71YyISsFWqJgpRrjlc")
working_sheet = full_excel.sheet1
values = working_sheet.get_all_records()
print(values)
# working_sheet.update("C5", "test")
# values = working_sheet.get_all_values()
# print(values)

# working_sheet.format("A1:F1", {'textFormat': {'bold': True}})
# working_sheet.insert_row(["Gigel", "o adresa", "231", "3232", "1232"])
