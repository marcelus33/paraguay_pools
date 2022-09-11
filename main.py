import requests

from bs4 import BeautifulSoup


URL_BASE = "https://ipparaguay.com.py/"

def main():
    soup = None
    str_date = "09-de-septiembre-2022"
    uri = "resultados-de-quiniela-teete-del-{}/".format(str_date)
    # TODO THIS SHOULD BE A "GET_POLLS" FUNCTION
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
            polls[poll_index] = [(i + 1, x.get_text()) for i, x in enumerate(list(numbers))]
            index += 1
        return polls
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()
