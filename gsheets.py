import json

import gspread
from google.oauth2.service_account import Credentials


class GoogleSheets:

    def __init__(self, scopes, credentials_path, excel_key):
        self.scopes = scopes
        self.creds = Credentials.from_service_account_file(credentials_path, scopes=self.scopes)
        self.client = gspread.authorize(self.creds)
        self.excel = self.client.open_by_key(excel_key)
        self.working_sheet = self.excel.sheet1

    def insert_rows(self, values, index=1):
        self.working_sheet.insert_row(values, index)

    def modify_cell(self, row, col, value):
        self.working_sheet.update_cell(row, col, value)

    def get_values(self):
        return self.working_sheet.get_all_records()

    def add_worksheet(self, title, rows=100, cols=20):
        return self.excel.add_worksheet(title=title, rows=rows, cols=cols)

    def select_worksheet(self, title):
        self.working_sheet = self.excel.worksheet(title)

# scopes = [
#     "https://www.googleapis.com/auth/spreadsheets"
# ]
# creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
#
# client = gspread.authorize(creds)
#
# full_excel = client.open_by_key("1VQuQKR1E_4_Xq0UrGjp8WasxA71YyISsFWqJgpRrjlc")
# working_sheet = full_excel.sheet1
# values = working_sheet.get_all_records()
# print(values)


if __name__ == '__main__':

    with open("config.json", "r") as f:
        gsheets_config = json.loads(f.read())

    excel = GoogleSheets(scopes=gsheets_config["scopes"],
                         credentials_path='credentials.json',
                         excel_key=gsheets_config["excel_id"])

    excel.insert_rows(["Anca Popescu", "anca_popescu@example.com", "Marketing","-", "-", "01/01/2025"], index=5)
    excel.modify_cell(1, 1, "Updated Name")
    new_sheet = excel.add_worksheet("Departments")
    excel.select_worksheet("Departments")

    employees = excel.get_values()
    print(employees)