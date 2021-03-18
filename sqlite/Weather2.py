from tkinter import *
import requests
import json
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API = os.getenv('WEATHER_API')


root = Tk()
root.title('Air Quality')
root.geometry("600x300")

conn = sqlite3.connect('weather.db')
c = conn.cursor()

# Create table
'''
c.execute("""CREATE TABLE weather (
		zipcode integer,
		city text,
		quality integer,
		category integer
		)""")
'''

# Create Zipcode Lookup function
def zipLookup():
    # zip.get()
    # zipLabel = Label(root, text=zip.get())
    # zipLabel.grid(row=1, column=0, columnspan=2)

    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=" + WEATHER_API)
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"

        root.configure(background=weather_color)
        myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20), background = weather_color)
        myLabel.grid(row=1, column=0, columnspan=2)

        conn = sqlite3.connect('weather.db')
        c = conn.cursor()

        # Insert into table
        # c.execute("INSERT INTO weather VALUES (:zipcode, :city, :quality, :category)", 
        #         {
        #             'zipcode': zip.get(),
        #             'city': city,
        #             'quality': quality,
        #             'category': category
        #         })
        my_data = (zip.get(), city, quality, category)
        my_query = "INSERT INTO weather values(?,?,?,?)"
        conn.execute(my_query, my_data)
        conn.commit()
        query()
    except Exception as e:
        api = "Error..."

def show():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    # Query the database
    c.execute("SELECT *, oid FROM weather")
    records = c.fetchall()
    print(records)
    print_records = ''
    # for record in records:
    #     print_records += str(record[0]) + " " + str(record[1]) + "\t" + str(record[2]) +"\n"

    for i in range(len(records)-1, len(records)-6, -1):
        print_records += str(records[i][0]) + " " + str(records[i][1]) + "\t" + str(records[i][2]) +"\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=2, column=0, columnspan=2)

    conn.commit()

zip = Entry(root)
zip.grid(row=0, column=0, stick=W+E+N+S)
zipButton = Button(root, text="Lookup Zipcode", command=zipLookup)
zipButton.grid(row=0, column=1, stick=W+E+N+S)

show_button = Button(root,text="Show Recent Searches", command=show)
show_button.grid(row=0, column=2)

def query():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    # Query the database
    c.execute("SELECT *, oid FROM weather")
    records = c.fetchall()
    print(records)

    # print_records = ''
    # for record in records:
    #     print_records += str(record[0]) + " " + str(record[1]) + "\t" + str(record[6]) +"\n"

    # query_label = Label(root, text=print_records)
    # query_label.grid(row=12, column=0, columnspan=2)

#     conn.commit()
#     conn.close()

query()
conn.commit()
conn.close()

root.mainloop()