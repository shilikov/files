from pprint import pprint
from collections import Counter

from pprint import pprint
from collections import Counter


def dishes(file_name: str) -> dict:
    result: dict = dict()

    with open(file_name) as file:
        for line in file:
            dish = line.strip()
            k = int(file.readline())
            cook_book = []
            for i in range(k):
                ingredient_name, quantity, measure = file.readline().split('|')
                cook_book.append({'ingredient_name': ingredient_name, 'quantyty': int(quantity), 'volume': measure}
                                 )
            result[dish] = cook_book
            file.readline()
    return result


cook_book = dishes('recept.txt')


# pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:
        for ingr in (cook_book[dish]):
            itm_list = dict([(ingr['ingredient_name'], {'volume': ingr['volume'],
                                                        'quantyty': int(ingr['quantyty']) * person_count})])
            if shop_list.get(ingr['ingredient_name']):
                item = (int(shop_list[ingr['ingredient_name']]['quantyty']) +
                              int(itm_list[ingr['ingredient_name']]['quantyty']))
                shop_list[ingr['ingredient_name']]['quantity'] = item

            else:
                shop_list.update(itm_list)

    print(f"из расчета на {person_count} человек необходимо купить:")
    pprint(shop_list)


def program():
    while True:
        print()
        user_input = input('для выбора блюд введите "S"\n'
                           'для выхлжа из прогрпммы введите "Q"\n'
                           'Введите команду - ')
        if user_input == 'S':
            person_count = int(input('Введите количество человек: '))
            dishes = list(input('Введите блюда в расчете '
                                'на одного человека (через запятую): ').split(', '))
            get_shop_list_by_dishes(dishes, person_count=person_count)

        elif user_input == "Q":
            print('рады чnо вы воспользовались нашей программой')
            exit(0)




program()
# get_shop_list_by_dishes(['Запеченный картофель', 'Фахитос'], person_count=5)
# print()
