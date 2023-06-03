import requests

#DELETE

REVIEW_ID = 10
URL = f'http://127.0.0.1:8000/api/v1/reviews/{REVIEW_ID}'

response = requests.delete(URL)

if response.status_code == 200:
    print('Delete made successfully')

    print(response.json())

else:
    print(response.content)

"""
#PUT

REVIEW_ID = 10
URL = f'http://127.0.0.1:8000/api/v1/reviews/{REVIEW_ID}'

REVIEW = {
    'review': 'New review. We update the content',
    'score': 1
}

response = requests.put(URL, json=REVIEW)

if response.status_code == 200:
    print('Request made successfully')

    print(response.json())"""

"""
#POST

URL = 'http://127.0.0.1:8000/api/v1/reviews'
REVIEW = {
    'user_id': 1,
    'movie_id': 1,
    'review': 'Review created with requests',
    'score': 3
}

response = requests.post(URL, json=REVIEW)

if response.status_code == 200:
    print('Request made successfully')

    print(response.json()['id'])

else:
    print(
        response.content
        )"""

"""
#GET

URL = 'http://127.0.0.1:8000/api/v1/reviews'
HEADERS = { 'accept': 'application/json' }
QUERYSET = {'page': 2, 'limit':1}

response = requests.get(URL, headers=HEADERS, params=QUERYSET )


if response.status_code == 200:
    print('Request made successfully')

if response.headers.get('content-type') == 'application/json':

    reviews = response.json()
    for review in reviews:
        
        print(f"score: {review['score']} - {review['review']}")"""