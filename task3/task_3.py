import http.client
import re
#Search inf
def search_info(key_word, temp):
    result = re.search(key_word, temp)
    start = result.start()
    i = -1
    while True:
        if temp[i+start] == ',':
            break
        print(temp[i+start], end='')
        i += 1
    return temp[result.end():]
conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "2c501bdd53msh281d423c869cf15p18f22cjsn36d828e0f50d",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }
# Choose Country
conn.request("GET", "/api/npm-covid-data/africa", headers=headers)
res = conn.getresponse()
data = res.read()
temp = data.decode("utf-8")
print(data.decode("utf-8"))
result1 = 0
result1 = re.findall("Country", temp)
start = temp
for i in range(len(result1)):
    start1 = search_info("Country", start)
    print("-------",i)
    start2 = search_info("TotalCases", start1)
    print()
    start3 =search_info("TotalDeath", start2)
    print()
    start4 =search_info("TotalRecovered", start3)
    print()
    start5 = search_info("TotalTests",start4)
    print()
    start = start5

