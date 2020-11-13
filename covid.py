import requests
from card import make_card

BASE_URL = 'https://disease.sh/v3/covid-19/countries'
QUERY = '?yesterday=true&twoDaysAgo=false&strict=false'


def covid_stats(*args):
    country = ' '.join(args[0:])

    response = requests.get(
        f'{BASE_URL}/{country}{QUERY}')
    result = response.json()

    title = f'Covid-19 Details - {result["country"]}'
    color = 0xF5C518
    thumbnail = result['countryInfo']['flag']
    fields = {
        'Total Cases': result['cases'],
        'Total Recovered': result['recovered'],
        'Total Deaths': result['deaths'],
        'Today Cases': result['todayCases'],
        'Today Recovered': result['todayRecovered'],
        'Today Deaths': result['todayDeaths']
    }
    card = make_card(title=title, color=color, thumbnail=thumbnail, fields=fields)
    return card
