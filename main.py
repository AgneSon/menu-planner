from dishes import DISHES

print(DISHES)


def find_the_dish(list):
    answer_1 = input("Choose your carb, protein, type "
                     "of diet of dish name: ").lower()
    list_of_dishes = []
    for dish in list:
        if answer_1 in dish.values():
            list_of_dishes.append(dish['name'])

    if len(list_of_dishes) > 0:
        return list_of_dishes
    else:
        return "Sorry. No valid matches."


print(find_the_dish(DISHES))
