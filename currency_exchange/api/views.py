import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response

ENDPOINT = 'https://www.cbr-xml-daily.ru/daily_json.js'
PREVIOUS_REQUESTS = []


class RequestResponseError(Exception):
    """Исключение для ошибок при запросе."""

    pass


@api_view(['GET'])
def currency_exchange_api(request):
    try:
        api_answer = requests.get(ENDPOINT).json()
        response_dict = {
            'Date': api_answer.get('Date'),
            'Currency': api_answer.get('Valute').get('USD')
        }
        PREVIOUS_REQUESTS.append(response_dict)
        context = {
            'current currency rate': response_dict,
            'previous rates': PREVIOUS_REQUESTS,
        }
        if len(PREVIOUS_REQUESTS) > 10:
            del PREVIOUS_REQUESTS[0]
    except requests.RequestException as error:
        raise RequestResponseError(f'Request {api_answer} failed '
                                   f'Error: {error}.')
    return Response(context)
