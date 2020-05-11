import requests


def request(coords, size, typee=False):

    text_coords = ','.join(([str(i) for i in coords]))
    if typee:
        map_request = \
            "http://static-maps.yandex.ru/1.x/?ll={},{}&spn={},{}&l=map&pt={},round".format(coords[0], coords[1],
                                                                                            size, size, text_coords)
    else:
        map_request = \
            "http://static-maps.yandex.ru/1.x/?ll={},{}&spn={},{}&l=map".format(coords[0], coords[1],
                                                                                size, size)
    response = requests.get(map_request)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    return map_file


def get_coord(text):
    """Получает координаты по адресу объекта
    text - адресс
    return x, y"""
    x, y = None, None
    toponym_to_find = text

    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"
    }
    response = requests.get(geocoder_api_server, params=geocoder_params)
    if not response:
        return x, y
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    x, y = toponym_coodrinates.split(" ")
    return x, y
