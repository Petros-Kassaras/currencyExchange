from tkinter import *
from tkinter.ttk import *

import requests
from ttkthemes import ThemedTk

screen = ThemedTk(theme="adapta")
screen.configure(themebg="adapta")
screen.title("Parathyro") #titlos
screen.geometry('510x100')#parathyro megethos
screen.resizable(width=False,height=False)
import requests, json

def convert ():
    global baseUrl
    global mainUrl

    fromcurrency = cmb1.get()
    tocurrency = cmb2.get()

    apiKey = "K3MQO5ISZGAYC6NI" # Your API key for making requests

    baseUrl = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE" # Base URL for the currency exchange API

    mainUrl = baseUrl + "&from_currency=" + fromcurrency + "&to_currency=" + tocurrency + "&apikey=" + apiKey # Construct the full API request URL with the selected currencies and the API key
    print(mainUrl)

    req_obj = requests.get(mainUrl) # Make the API request to get the exchange rate data
    result = req_obj.json()  # Parse the JSON response from the API
    exchange_rate = float(result["Realtime Currency Exchange Rate"]["5. Exchange Rate"]) # Extract the exchange rate from the response
    print(exchange_rate)

    amount=float(entr.get())
    result=round(amount*exchange_rate,2)
    lblre.config(text=str(result))



lbltitle = Label(screen,text="Currency Exchange")
lblamount = Label(screen,text="Amount")
lblfrom = Label(screen,text="From")
lblto = Label(screen,text="To")
entr = Entry(screen)
cmb1 = Combobox(screen,state='readonly')
cmb1['values']=('EUR','USD','JBP','GBP','CAD')
cmb1.current(1)
cmb2 = Combobox(screen,state='readonly')
cmb2['values']=('EUR','USD','JBP','GBP','CAD')
cmb2.current(1)
btn = Button(screen,text="Convert",command=convert)
lblre = Label(screen)

lbltitle.grid(column=0,row=0,columnspan=4)
lblamount.grid(column=0,row=1)
lblfrom.grid(column=1,row=1)
lblamount.grid(column=2,row=1)
lblto.grid(column=3,row=1)
entr.grid(column=0,row=2)
cmb1.grid(column=1,row=2)
cmb2.grid(column=2,row=2)
btn.grid(column=3,row=2)
lblre.grid(column=3,row=3)

screen.mainloop() #kleinei programma