import pytest

from src.classes import Category, Product

@pytest.fixture
def class_product():
    return Product('Samsung Galaxy C23 Ultra',
                   '256GB, Серый цвет, 200MP камера',
                   180000.0,
                   5)
@pytest.fixture
def class_category():
    list_of_products = [Product]
    return Category('Смартфоны',
                    'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для '
                    'удобства жизни',
                    list_of_products)


def test_category_init(class_category):
    assert class_category.title == 'Смартфоны'
    assert class_category.description == ('Смартфоны, как средство не только коммуникации, но и получение '
                                          'дополнительных функций для удобства жизни')

    assert class_category.total_numbers_of_category == 1
    assert class_category.unique_products == 1


def test_get_name(class_category):
    assert class_category.get_name() == 'Смартфоны'


def test_get_description(class_category):
    assert class_category.get_description() == ('Смартфоны, как средство не только коммуникации, но и получение '
                                                'дополнительных функций для удобства жизни')

def test_category_len(class_category):
    assert class_category.__len__() == 1

def test_category_str(class_category):
    assert class_category.__str__() == 'Смартфоны, количество продуктов: 1 шт.'

def test_product_init(class_product):
    assert class_product.name == 'Samsung Galaxy C23 Ultra'
    assert class_product.description == '256GB, Серый цвет, 200MP камера'
    assert class_product.price == 180000.0
    assert class_product.quantity_in_stock == 5

def test_product_str(class_product):
    assert class_product.__str__() == 'Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.'


def test_get_title(class_product):
    assert class_product.get_title() == 'Samsung Galaxy C23 Ultra'


def test_get_description(class_product):
    assert class_product.get_description() == '256GB, Серый цвет, 200MP камера'


def test_get_price(class_product):
    assert class_product.price == 180000.0


def test_get_quantity_in_stock(class_product):
    assert class_product.get_quantity_in_stock() == 5

def test_add(class_product):
    other = Product('name', 'desc', 50000, 2)
    assert class_product + other == 1000000