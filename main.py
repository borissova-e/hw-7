print('Задача 1.')

cook_book = {}
with open('recipes.txt', encoding="utf-8") as f:
    while True:
        name = f.readline().strip()
        if not name:
            break
        amount_of_ingredients = f.readline().strip()
        ingredients = []
        while True:
            ingredient = f.readline().strip()
            if not ingredient:
                break
            ingredient_list = ingredient.split(' | ')
            ingredient_dict = {'ingredient_name': ingredient_list[0], 'quantity': int(ingredient_list[1]),
                               'measure': ingredient_list[2]}
            ingredients.append(ingredient_dict)
        cook_book.setdefault(name, ingredients)

print(cook_book)

print('Задача 2.')


def get_shop_list_by_dishes(dishes, person_count):
    products = {}
    for dish in dishes:
        for cooking in cook_book.keys():
            if dish == cooking:
                for product in cook_book[dish]:
                    product_name = product['ingredient_name']
                    product_quantity = {'measure': product['measure'],
                                        'quantity': product['quantity'] * person_count}
                    if products.get(product_name) is None:
                        products.setdefault(product_name, product_quantity)
                    else:
                        current = products.get(product_name)
                        products[product_name]['quantity'] = products[product_name]['quantity'] + current['quantity']
    return products


print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))
