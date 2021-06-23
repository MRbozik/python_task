import http.client
from tkinter import *
import re
import sys
import os
# Поиск информации по стране, ключ-слову в tmp
def search_info(country,tmp,key_word):
    result_country = re.search(country, tmp)
    end_country = result_country.end() #поиск начала поиска по стране
    result_search = re.search(key_word, tmp[end_country:])
    end_search = result_search.end() # поиск по ключслову
    s = key_word
    while True:
       # print(end_search)
        if tmp[end_search+end_country+1] == ":":
            i=1
            while tmp[end_search+i+end_country] != ",":
                s += tmp[end_search+i+end_country]
                i+=1
            return s
        else: break


conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "2c501bdd53msh281d423c869cf15p18f22cjsn36d828e0f50d",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }
conn.request("GET", "/api/npm-covid-data/asia", headers=headers)
res = conn.getresponse()
data = res.read()
tmp = data.decode("utf-8")
lst_country = ["India","Turkey","Indonesia","Iraq","Israel"]
lst_search = ["TotalCases","NewCases","TotalDeaths","NewDeaths","TotalRecovered"]
#Show
root = Tk()
root.title("Covid Asia")
root.geometry("600x1600")
for i in range(len(lst_country)):
    lab_country = Label(root, text = lst_country[i],font ="Arial 14",fg = "black" )
    lab_country.place(x = 20, y = 50*i*4)
    for j in range (len(lst_search)):
        lab_search = Label(root, text = search_info(lst_country[i],tmp,lst_search[j]),font ="Arial 14",fg = "green" )
        lab_search.place(x = 20, y = 50*i*4+30*(j+1))
#Перезапуск программы для обновления данных 
def restartProgram():
    os.execl(sys.executable, os.path.abspath('task_3.py'), *sys.argv)         
restartButton = Button(text = "RESTART", command = restartProgram)
restartButton.place(x = 400, y = 100, width = 200, height = 40)
root.mainloop()
