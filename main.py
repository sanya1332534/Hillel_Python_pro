from urllib.parse import urlparse, parse_qs


def parse(query: str) -> dict:
    parsed_url = urlparse(query)
    query_params = parse_qs(parsed_url.query)
    param_dict = {key: value[0] for key, value in query_params.items()}
    return param_dict


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=John') == {'name': 'John'}


def parse_cookie(query: str) -> dict:
    cookie_data = {}
    items = query.split(';')
    for item in items:
        parts = item.split('=')
        key = parts[0].strip()
        value = '='.join(parts[1:]).strip()
        if key:
            cookie_data[key] = value
    return cookie_data


if __name__ == '__main__':
    assert parse_cookie('name=John;') == {'name': 'John'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=John;age=28;') == {'name': 'John', 'age': '28'}
    assert parse_cookie('name=John=User;age=28;') == {'name': 'John=User', 'age': '28'}
