import configuration
import data
import requests


def post_new_order(order_body):  # создание нового заказа
    return requests.post(configuration.BASE_URL + configuration.CREATE_ORDERS_PATH,  # указываем полный URL
                         json=data.order_body,
                         headers=data.headers)


response = post_new_order(data.order_body);
print(response.status_code)


def get_new_order_track():  # получение номера заказа
    return post_new_order(data.order_body).json()["track"]


track_number = get_new_order_track()
print(track_number)


def get_order():  # получение заказа по его номеру
    return requests.get(configuration.BASE_URL + configuration.ORDERS_PATH + "?t=" + str(track_number))


response = get_order()
