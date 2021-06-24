import telebot
import http.client
import re

lst_country = ["India","Turkey","Indonesia","Iraq","Israel"]
lst_search = ["TotalCases","NewCases","TotalDeaths","NewDeaths","TotalRecovered"]

#Обновление данных или получение первоночальных 
def renew_data():
    conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
    headers = {
    'x-rapidapi-key': "2c501bdd53msh281d423c869cf15p18f22cjsn36d828e0f50d",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }
    conn.request("GET", "/api/npm-covid-data/asia", headers=headers)
    res = conn.getresponse()
    data = res.read()
    tmp = data.decode("utf-8")
    return tmp
global tmp
tmp = renew_data()
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
                if tmp[end_search+i+end_country] =='"':
                    s += ''
                else : 
                    s += tmp[end_search+i+end_country]
                i+=1
            return s
        else: break
def note_res(n,m):
    tmp_s = ""
    for i in range(n):
        tmp_s += lst_country[i]
        tmp_s+='\n'
        for j in range(m):
            tmp_s += search_info(lst_country[i],tmp,lst_search[j])
            tmp_s+='\n'
        tmp_s+='\n'
    return tmp_s
 
bot = telebot.TeleBot('1852394935:AAGRZK-E0ibbEr4xz1Mf1N6oB8WQIgbOLJA')
#START
@bot.message_handler(commands=['start'])
def show_result(message):
    bot.send_message(message.chat.id, note_res(5,5))

#SEARCH
@bot.message_handler(commands=['search'])
def show_result(message):
    if message.text[8:] == 'India':
        bot.send_message(message.chat.id, note_res(1,5))
    elif message.text[8:] == "Turkey":
        bot.send_message(message.chat.id, note_res(2,5))
    elif message.text[8:] == "Indonesia":
        bot.send_message(message.chat.id, note_res(3,5))
    elif message.text[8:] == "Iraq":
        bot.send_message(message.chat.id, note_res(4,5))
    elif message.text[8:] =="Israel":
        bot.send_message(message.chat.id, note_res(5,5))
    else :
        bot.send_message(message.chat.id, "Нет данных по этой стране")    
    
#RENEWDATA
@bot.message_handler(commands=['renewdata'])
def renewdata(message):
    tmp = renew_data()
    bot.send_message(message.chat.id, note_res(5,5))

#HELP
@bot.message_handler(commands=['help'])
def renewdata(message):
    bot.send_message(message.chat.id, "/start запустить бота\n/renewdata обновит данные\n/search поиск по стране\n/txt вернёт текстовый файл")
#TXT
@bot.message_handler(commands=['txt'])
def txt(message):
    f = open('text.txt', 'w')
    tmp_wr = note_res(5,5)
    f.write(tmp_wr)
    f.close()
    file = open('text.txt', 'r')
    bot.send_document(message.chat.id, file)
    file.close()
#run
bot.polling(none_stop=True)
