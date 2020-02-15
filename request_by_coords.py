import requests


def request(coords):
    size = 0.5
    map_request = \
        "http://static-maps.yandex.ru/1.x/?ll={}%{}&spn={},{}&l=map".format(coords, size, size)
    response = requests.get(map_request)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    return file