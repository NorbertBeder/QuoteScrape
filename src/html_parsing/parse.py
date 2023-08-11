from bs4 import BeautifulSoup


def get_quote_list(request):
    soup = BeautifulSoup(request.content, 'html.parser')
    quote_list = soup.find_all('div', class_='quote')

    return quote_list
