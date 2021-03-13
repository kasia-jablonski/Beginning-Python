from tkinter import *
import requests
import json

# Here's your free API key: f8a120efe37230a78e36
# Example usage:
# https://free.currconv.com/api/v7/convert?q=USD_PHP&compact=ultra&apiKey=f8a120efe37230a78e36

root = Tk()
root.title('Currency Converter')
root.geometry("600x400")

currency_request = requests.get("https://free.currconv.com/api/v7/currencies?apiKey=f8a120efe37230a78e36")
currencies = json.loads(currency_request.content)
currency_list = []
for currency in currencies['results'].keys():
    currency_list.append(currency)
print(currency_list)

currency1 = Entry(root, width=10)
currency1.grid(row=0, column=0)
selected = StringVar()
selected.set("Select")
drop_currency1 = OptionMenu(root, selected, *currency_list)
drop_currency1.grid(row=0, column=1)
try:
    api_request = requests.get("https://free.currconv.com/api/v7/convert?q=PHP_USD&compact=ultra&apiKey=f8a120efe37230a78e36")
    api = json.loads(api_request.content)
    #print(api['PHP_USD'])
except Exception as e:
    api = "Error..."






root.mainloop()