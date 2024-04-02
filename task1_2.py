
def create_a_recipe_dictionary() -> dict[str: list[dict]]:
    cook_book = dict()
    with open('recipes.txt', 'r') as file:
            lines = file.readlines()
        
            i = 0
            while i < len(lines):
                dish_name = lines[i].strip()
                i += 1
                ingredients_count = int(lines[i])
                i += 1
                
                ingredients = []
                for _ in range(ingredients_count):
                    ingredient_info = lines[i].split(' | ')
                    ingredient_name = ingredient_info[0].strip()
                    quantity = int(ingredient_info[1])
                    measure = ingredient_info[2].strip()
                    
                    ingredient = {
                        'ingredient_name': ingredient_name,
                        'quantity': quantity,
                        'measure': measure
                    }
                    ingredients.append(ingredient)
                    
                    i += 1
                
                cook_book[dish_name] = ingredients
                
                i += 1
                
            return cook_book
    
def get_shop_list_by_dishes(dishes: list[str], count_guests: int) -> dict[str: dict]:
    shop_list_by_dishes = dict()
    cook_book = create_a_recipe_dictionary()
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                values = dict(list(ingredient.items())[1:])
                values['quantity'] *= count_guests
                if ingredient_name in shop_list_by_dishes:
                    shop_list_by_dishes[ingredient_name] += values
                else:
                    shop_list_by_dishes[ingredient_name] = values
    return shop_list_by_dishes


def main():
    shop_list_by_dishes = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
    print(shop_list_by_dishes)




if __name__ == '__main__':
    main()

