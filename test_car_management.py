"""Tests for the Car class (write these BEFORE car_management.py - red first!)."""
import pytest
from car_management import Car

@pytest.fixture(autouse=True)
def reset_car_class():
    Car.all_cars = {}
    Car.total_cars = 0
    Car._next_id = 1

def test_new_car_stores_its_details():
    car = Car("Toyota", "Corolla", 2020, 15000)
    assert car.make == "Toyota"
    assert car.model == "Corolla"
    assert car.year == 2020
    assert car.mileage == 15000
    assert car.services == []


def test_mileage_defaults_to_zero():
    assert Car("Honda", "Civic", 2024).mileage == 0


def test_class_attributes_start_empty():
    assert Car.total_cars == 0
    assert Car.all_cars == {}

# ---- Piece 2: ids and counting ----
def test_ids_rise_by_one():
    first = Car("Toyota", "Corolla", 2020)
    second = Car("Honda", "Civic", 2021)
    assert first.id == 1
    assert second.id == 2


def test_id_cannot_be_changed():
    car = Car("Toyota", "Corolla", 2020)
    with pytest.raises(AttributeError):
        car.id = 99


def test_total_cars_counts_every_car():
    Car("Toyota", "Corolla", 2020)
    Car("Honda", "Civic", 2021)
    assert Car.total_cars == 2


def test_all_cars_stores_every_car():
    car = Car("Toyota", "Corolla", 2020)
    assert Car.all_cars[car.id] is car