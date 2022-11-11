cook_book = {}

with open("recipes.txt", "rt", encoding="utf-8") as file:
    
    for l in file:
        name_dish = l.strip()
        ingredient_count = file.readline().strip()
        cook_book[name_dish] = []
        for i in range(int(ingredient_count)):
            ingredient = file.readline()
            ingredient_name, quantity, measure = ingredient.strip().split(" | ")
            cook_book[name_dish].append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        file.readline()

def get_shop_list_by_dishes(dishes, person_count):
    compound_dishes = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                meas_quan_list = {}
                meas_quan_list['measure'] = ingredient['measure']
                meas_quan_list['quantity'] = int(ingredient['quantity']) * int(person_count)
                compound_dishes[ingredient['ingredient_name']] = meas_quan_list
        else:
            print('Такого блюда нет в меню')
    return compound_dishes

total = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(cook_book, end="\n\n\n")
print(total)
