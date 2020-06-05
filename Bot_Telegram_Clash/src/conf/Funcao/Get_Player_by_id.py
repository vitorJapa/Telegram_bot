import requests

playerid = 'RLPQU99C'
url = "https://api.clashofclans.com/v1/players/ "+playerid
headers = {
    "Authorization" : "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImNkOTczYTAzLTJlZmUtNDJhMi05ODQ0LWE5MWU3NGZmOTMwNSIsImlhdCI6MTU5MDk3MTI2Miwic3ViIjoiZGV2ZWxvcGVyLzk4N2JlYjY3LTUxMjItOWIwMy0yNWU0LTNkNTczZTMxNjExMiIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjIwMS4yNi4xMjEuMjI0Il0sInR5cGUiOiJjbGllbnQifV19.6v0_9ocMhnjfsfp_Ey0P4mXOYu5ocheYZOVmaops24-2gA9gt2S_kPjwEUsAiRxUGnUMIZTQaFC5ARfu8JFCFQ"
}

response = requests.get(url=url, headers=headers)

if response.status_code >= 200 and response.status_code <= 299:
    #sucesso
    #print(response.status_code)
    #print(response.reason)
    response_data = response.json()
    print('Nome:',response_data['name'])
    print('Tag:',response_data['tag'])
    print('Centro de vila:',response_data['townHallLevel'])
    print('Level:',response_data['expLevel'])
    tropas = response_data['troops']
    aux = list(filter(lambda x: "builderBase", tropas))

    for n in aux:
        #broto = n['name']['level']['maxLevel']
        #if (tropas in aux):
        print(n)
        #print(n['village'])
               # print(aux)
            #else:
             #   exit()
    else:
           exit()

    #erros
    #print(count, n['name'], 'Level:',n['level'],'Tag:', n['maxLevel'])
    print(response.status_code)
    print(response.reason)
    response_data = response.json()
    print(response_data)


