from tkinter import *
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

CURR_CONV_API = os.getenv('CURR_CONV_API')

root = Tk()
root.title('Currency Converter')
root.geometry("355x100")


def convert():
    c1 = selected1.get()
    c2 = selected2.get()
    currency2.delete(0, END)

    try:
        api_request = requests.get("https://free.currconv.com/api/v7/convert?q=" + c1 + "_" + c2 + "&compact=ultra&apiKey="+ CURR_CONV_API)
        api = json.loads(api_request.content)
        print(api)
        print(api[c1+'_'+c2])
        print(currency1.get())
        converted = round((float(api[c1+'_'+c2]) * float(currency1.get())), 6)
        print(converted)
        currency2.insert(0, str(converted))
    except Exception as e:
        api = "Error..."


currency_request = requests.get("https://free.currconv.com/api/v7/currencies?apiKey=" + CURR_CONV_API)
currencies = json.loads(currency_request.content)
currency_list = []
for currency in currencies['results'].keys():
    currency_list.append(currency)
currency_sorted = sorted(currency_list)

currency1 = Entry(root, width=10)
currency1.grid(row=0, column=0, padx=10, pady=10)
selected1 = StringVar()
selected1.set("Select")
drop_currency1 = OptionMenu(root, selected1, *currency_sorted)
drop_currency1.grid(row=0, column=1)
equal = Label(root, text="  = ")
equal.grid(row=0, column=2)
currency2 = Entry(root, width=10)
currency2.grid(row=0, column=3, padx=10, pady=10)
selected2 = StringVar()
selected2.set("Select")
drop_currency2 = OptionMenu(root, selected2, *currency_sorted)
drop_currency2.grid(row=0, column=4)



button = Button(root, text="Convert", command=convert)
button.grid(row=1, column=1, columnspan=3, pady=10, padx=10, ipadx=50)





root.mainloop()