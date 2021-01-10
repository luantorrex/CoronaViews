from app import app
from app.covid_data import (
    get_covid_data, 
    get_covid_daily_data
    )


@app.route('/')
def index():
    
    output_phrase = 'Welcome to CoronaViews, <br><br>' + \
    'General numbers per country: <br>' + \
    'I.E.: <b> http://127.0.0.1:5000/country/usa</b><br>'+ \
    '(Confirmed cases, Recovered people & Deaths).' + \
    '<br><br>' + \
    'General daily cases per country: <br>' + \
    'I.E.: <b> http://127.0.0.1:5000/daily/usa/01-01-2021</b><br>' + \
    '(Confirmed cases, Recovered people & Deaths).'

    return output_phrase


@app.route('/country/<country>/')
def covid_data(country):
    cases_data = get_covid_data(country)

    if isinstance(cases_data, str):
        country_data = cases_data
    else:
        country_data = 'Confirmed: % s ' % cases_data[0] + '<br>' + \
            'Recovered: % s ' % cases_data[1] + '<br>' + \
            'Deaths: % s ' % cases_data[2] + '<br>' + \
            'Last Update: % s' % cases_data[3]

    output_phrase = country.capitalize() + '<br>' + \
                    'General Cases' + '<br><br>' + \
                    country_data

    return output_phrase


@app.route('/daily/<country>/<day>/')
def daily_covid_data(country, day):
    cases_data = get_covid_daily_data(country, day)

    if len(cases_data) == 0:
        country_data = 'Sorry, we didnt find any data with these parameters.'
    else:
        country_data = 'Confirmed: % s ' % cases_data[0] + '<br>' + \
            'Recovered: % s ' % cases_data[1] + '<br>' + \
            'Deaths: % s ' % cases_data[2] + '<br>' + \
            'Last Update: % s' % cases_data[3]

    output_phrase = country.capitalize() + '<br>' + \
                    day + '<br><br>' + \
                    country_data

    return output_phrase