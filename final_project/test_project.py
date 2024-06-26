import pytest
from project import coordinate, distance_to_km, cities_list, aux
def test_coordinate():
    assert(coordinate("são paulo"))==[-23.5506507, -46.6333824]
    assert(coordinate("belo horizonte"))==[-19.9227318, -43.9450948]
def test_distance_to_km():
    assert(distance_to_km([-23.5506507, -46.6333824],[-19.9227318, -43.9450948]))==489
def test_aux():
    assert(aux())== 1
