import requests
import json

response = requests.get("https://api.corona-zahlen.org/districts")
r_json = response.text

data = json.loads(r_json)

doubleList = ["München", "Passau", "Leipzig"]
cityList = ["Städteregion Aachen", "Rhein-Sieg-Kreis", "Saarpfalz-Kreis", "Minden-Lübbecke", "Berlin Mitte", "Berlin Pankow", "Cottbus", "Erlangen", "Essen", "Hamburg", "Jena", "Kiel", "Köln", "Leipzig", "Lübeck", "Mainz", "München", "Oldenburg", "Passau", "Sankt Augustin", "Tübingen"]
#cityList = input("Von welchen Regionen wollen sie die Inzidenzen wissen?\nSeparieren sie die Regionen mit einem Komma:  ").split(",")

for x in data['data']:
    if data['data'][x]['name'] in cityList:
    #if data['data'][x]['name'][0] == "R":
        if data['data'][x]['name'] == "München" and int(data['data'][x]['population']) >= 1000000:
            print(data['data'][x]['name'], " : ", data['data'][x]['weekIncidence'], " ", data['data'][x]['population'])
        elif data['data'][x]['name'] not in doubleList:
            print(data['data'][x]['name'], " : ", data['data'][x]['weekIncidence'])
        elif data['data'][x]['name'] == "Leipzig" and int(data['data'][x]['population']) >= 500000:
            print(data['data'][x]['name'], " : ", data['data'][x]['weekIncidence'])
        elif data['data'][x]['name'] == "Passau" and int(data['data'][x]['population']) <= 70000:
            print(data['data'][x]['name'], " : ", data['data'][x]['weekIncidence'])
  
