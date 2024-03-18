import gspread
from google.oauth2.service_account import Credentials

class SheetsModel():
    def __init__(self):
        try:
            scopes = ["https://www.googleapis.com/auth/spreadsheets"]
            creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
            self.client = gspread.authorize(creds)
            self.sheet_id = "1b_WuKh0xKlkv8CGN89jBWpQkTDEDOAOEeteiewMkNZ0"
            self.workbook=self.client.open_by_key(self.sheet_id)
            self.sheet = self.workbook.worksheet("Sheet1")
        except Exception as e:
            print("Error:", e)

    def update_sheet(self, column_values):
        try:
            self.sheet.clear()
            print()
            self.sheet.update(f"A1:L{len(column_values)}", column_values)
            # self.sheet.format("A1:M1", {"textFormat": {"bold": True}})
            print("Sheet updated successfully")
        except Exception as e:
            print("Error updating sheet:", e)
