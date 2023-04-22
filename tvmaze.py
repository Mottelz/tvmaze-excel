import requests

BASE_URL = 'https://api.tvmaze.com'


def search_for_show(query):
    res = requests.get(f'{BASE_URL}/search/shows', params={'q': query})
    return parse_show_results(res.json())


def parse_show_results(raw_results):
    processed = []
    for result in raw_results:
        show_data = result.get('show')
        if show_data:
            processed.append({
                'name': show_data.get('name'),
                'id': show_data.get('id'),
                'language': show_data.get('language'),
                'genres': ' '.join(show_data.get('genres')),
                'status': show_data.get('status'),
                'averageRuntime': show_data.get('averageRuntime'),
                'premiered': show_data.get('premiered'),
                'summary': show_data.get('summary')
            })
    return processed
