from gsheets import GoogleSheets
from mail import Mail

# o sa avem un google sheet ce va contine nume, mail, data expirare parola
# vom face automatizare care trimite mailuri angajatilor carora urmeaza sa le expire parola



if __name__ == '__main__':
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets"
    ]
    excel_key = '"1VQuQKR1E_4_Xq0UrGjp8WasxA71YyISsFWqJgpRrjlc"'

    mail = Mail("denisa.r95@gmail.com")
    google_sheets = GoogleSheets(scopes, 'credentials.json', excel_key)

    