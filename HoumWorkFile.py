from pprint import pprint

def get_recipes(recipes_file='./recipes.txt'):
    cook_book = {}
    with open(recipes_file, encoding='utf-8') as receipt_file:
        while len(receipt_file.readline()) > 0:
            dish = receipt_file.readline().rstrip('\n')
            if not dish:
                break
            cook_book[dish] = []
            n = int(receipt_file.readline().rstrip('\n'))
            items = [receipt_file.readline().rstrip('\n').rsplit('|') for _ in range(n)]
            for item in items:
                temp = item[0].replace('  ', ',').split(',')
                cook_book[dish].append({'ingridient_name': temp[0],
                                        'quantity': int(temp[1]),
                                        'measure': temp[2]})
    return cook_book

def get_shop_list_by_dishes(cook_book, dishes, person_count):
    pprint(cook_book)
    shop_list = {}
    shop_list_mq = {}
    for dish in cook_book:
        if dishes == dish:
            for val in cook_book[dish]:
                for products, qual in val.items():
                    if products == 'measure':
                        shop_list_mq.setdefault('measure', str(qual))
                    else:
                        if products == 'quantity':
                            shop_list_mq.setdefault('quantity', int(str(qual)) * int(person_count))
                        else:
                            shop_list.setdefault(val[products], shop_list_mq.copy())
                            shop_list_mq.clear()
    pprint(shop_list)

cook_book = get_recipes()
get_shop_list_by_dishes(cook_book, 'Омлет', 2)
