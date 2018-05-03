import requests
import bs4
import collections

weather_report = collections.namedtuple('weather_report',
                                        'loc, temp, temp_unit, condition')


def main():
    print_header()
    zipcode = input("What is your zipcode?" )
    html = get_html(zipcode)
    report = get_weather_information(html)
    print('In {} it is currently {}{} and {}'.format(report.loc, report.temp, report.temp_unit, report.condition))


def print_header():
    print("------------------------------")
    print("         Weather App")
    print("------------------------------")
    print("")


def get_weather_information(url):
    soup = bs4.BeautifulSoup(url, "html.parser")
    loc = soup.find(class_='region-content-header').find('h1').get_text().strip()
    temp = soup.find(class_='wu-value wu-value-to').get_text().strip()
    temp_unit = '°' + soup.find(class_='wu-label').get_text().strip()
    weather_description = soup.find(class_='condition-icon small-6 medium-12 columns').get_text().strip()
    report = weather_report(loc=loc, temp=temp, temp_unit=temp_unit, condition=weather_description)
    return report


def get_html(zipcode):
    url = "https://www.wunderground.com/weather/{}".format(zipcode)
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    main()
