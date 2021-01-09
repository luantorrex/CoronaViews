import json
import requests

def get_covid_data(country):
    data = requests.get('https://covid19.mathdro.id/api/countries/' + country)
    data = data.json()

    confirmed = data['confirmed']['value']
    recovered = data['recovered']['value']
    deaths = data['deaths']['value']
    last_update = data['lastUpdate'][0:10]

    covid_data = [confirmed, recovered, deaths, last_update]

    return covid_data