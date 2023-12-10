import sender_stand_request
# Виолетта Абахтимова, 11-я когорта - Финальный проект. Инженер по тестированию плюс

def test_order_from_track_number():
    response = sender_stand_request.get_order()
    assert response.status_code == 200
