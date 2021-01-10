import json
import requests


def get_covid_data(country):
    data_request = requests.get('https://covid19.mathdro.id/api/countries/' + country)
    data_json = data_request.json()

    try:
        confirmed = data_json['confirmed']['value']
        recovered = data_json['recovered']['value']
        deaths = data_json['deaths']['value']
        last_update = data_json['lastUpdate'][0:10]

        covid_data = [confirmed, recovered, deaths, last_update]

    except:
        covid_data = 'Sorry, we didnt find any data with this parameter.'

    return covid_data


def get_covid_daily_data(country_name, day):
    data_request = requests.get('https://covid19.mathdro.id/api/daily/' + day)
    data_json = data_request.json()

    covid_data = []

    for each_row in range(0, len(data_json), 1):
        if data_json[each_row]['countryRegion'] != country_name.capitalize():
            continue
        else:
            confirmed = data_json[each_row]['confirmed']
            recovered = data_json[each_row]['recovered']
            deaths = data_json[each_row]['deaths']
            last_update = data_json[each_row]['lastUpdate'][0:10]
            country = data_json[each_row]['countryRegion']
            
            covid_data = [confirmed, recovered, deaths, last_update, country]
        
    return covid_data