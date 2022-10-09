from bs4 import BeautifulSoup
import requests

from config import URL_BASE


def uri_from_date(date):
    # TODO convert date to letters i.e: "09-de-septiembre-2022"
    str_date = date
    uri = "resultados-de-quiniela-teete-del-{}/".format(str_date)
    return uri


def scrap_pool_results(uri):
    try:
        soup = BeautifulSoup(
            requests.get(URL_BASE + uri, timeout=10,
                         headers={'user-agent': 'Mozilla/5.0'}, verify=False).text, "html.parser")
        polls_soup = soup.select("ol")
        polls = {}
        polls_indexes = ['morning', 'evening', 'night']
        index = 0
        for poll in polls_soup:
            numbers = poll.select("li")
            poll_index = polls_indexes[index]
            polls[poll_index] = [(i + 1, x.get_text())
                                 for i, x in enumerate(list(numbers))]
            index += 1
        return polls
    except Exception as e:
        print(str(e))
        return []


def save_results_to_db(results):
    # TODO finish this
    morning = results.get('morning')
    evening = results.get('evening')
    night = results.get('night')
    for n in morning:
        order = n[0]
        number = int(n[1])
