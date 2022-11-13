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

def rewrite_sort_file(name_f1 = "1.txt", name_f2 = "2.txt", name_f3 = "3.txt"):
    os.chdir("sorted") # Переходим в директорию папки sorted
    rewrite_file = "rewrite_file.txt" # Наименование перезаписываемого файла
    files = {}
    for file in os.listdir(): # пробегаемся по директории с файлами и формируем словарь (название файла-количество строк)
        with open(os.path.join(os.getcwd(), file), 'r', encoding = "utf-8") as f:
            files[file] = len(f.readlines())

    with open(os.path.join(os.getcwd(), rewrite_file), 'w', encoding='utf-8') as ff:
        for i in sorted(files.items(), key=lambda para: para[1]):
            ff.write(i[0] + "\n")
            ff.write(str(i[1]) + "\n")
            with open(os.path.join(os.getcwd(), i[0]), 'r', encoding="utf-8") as f:
                file = f.readlines()
            ff.writelines(file)
                
rewrite_sort_file()
