from src.html_parsing.parse import get_quote_list
from src.models.quote_model import Quotes
from src.requests.req import get_by_page


def get_quotes():
    object_list = []
    i = 1

    while i != 0:
        request = get_by_page(f'page/{i}')
        quote_list = get_quote_list(request)

        for q in quote_list:
            tag_list = {}

            tags = q.findAll('a', class_='tag')

            for t in tags:
                tag_list[t.text] = t.get('href')

            author = q.small.text
            quote = q.span.text

            object_list.append(Quotes(quote, author, tag_list))

        i += 1
        if len(quote_list) == 0:
            i = 0
    return object_list
