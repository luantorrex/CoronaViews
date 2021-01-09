from app import app
from app.covid_data import get_covid_data

@app.route('/')
def index():
    return 'Welcome to CoronaViews, type a contry (in english) at the URL like this: http://127.0.0.1:5000/usa and get corona numbers about this country.'


@app.route('/<pais>')
def covid_data(pais):
    data = get_covid_data(pais)
    
    output = 'Confirmed: % s ' % data[0] + \
        'Recovered: % s ' % data[1] + \
        'Deaths: % s ' % data[2] + \
        'Last Update: % s' % data[3]

    return output