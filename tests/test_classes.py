import pytest

from src.classes import Category, Product


@pytest.fixture
def class_category():
    return Category('Смартфоны',
                    'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни',
                    {
                        "name": "Samsung Galaxy C23 Ultra",
                        "description": "256GB, Серый цвет, 200MP камера",
                        "price": 180000.0,
                        "quantity": 5
                    })


def test_category_init(class_category):
    assert class_category.title == 'Смартфоны'
    assert class_category.description == 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни'
    assert class_category.products == {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    }
    assert class_category.total_numbers_of_category == 1
    assert class_category.unique_products == 1


def test_get_name(class_category):
    assert class_category.get_name() == 'Смартфоны'


def test_get_description(class_category):
    assert class_category.get_description() == 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни'


def test_get_products(class_category):
    assert class_category.get_products() == {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    }


@pytest.fixture
def class_product():
    return Product('Samsung Galaxy C23 Ultra',
                   '256GB, Серый цвет, 200MP камера',
                   180000.0,
                   5)


def test_product_init(class_product):
    assert class_product.title == 'Samsung Galaxy C23 Ultra'
    assert class_product.description == '256GB, Серый цвет, 200MP камера'
    assert class_product.price == 180000.0
    assert class_product.quantity_in_stock == 5


def test_get_title(class_product):
    assert class_product.get_title() == 'Samsung Galaxy C23 Ultra'


def test_get_description(class_product):
    assert class_product.get_description() == '256GB, Серый цвет, 200MP камера'


def test_get_price(class_product):
    assert class_product.get_price() == 180000.0


def test_get_quantity_in_stock(class_product):
    assert class_product.get_quantity_in_stock() == 5
