from pprint import pprint

from src.classes import Category, Product
from src.utils import load_data


def main():
    data = load_data()
    categories = []
    for unit in data:
        list_products = [un for un in unit['products']]

        category = Category(unit['name'], unit['description'], unit['products'])

        categories.append(f'{category.get_name()}\n'
                          f'{category.get_description()}\n'
                          f'{category.get_products()}\n'
                          )
        result = []
        for element in list_products:
            product = Product(element['name'], element['description'], element['price'], element['quantity'])
            result.append(f'{product.get_title()}\n'
                          f'{product.get_description()}\n'
                          f'{product.get_price}\n'
                          f'{product.get_quantity_in_stock()}\n\n'
                          )
    pprint(categories)


if __name__ == '__main__':
    main()
