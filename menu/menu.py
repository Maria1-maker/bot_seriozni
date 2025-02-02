class Meal:
    def __init__(self, price: int, name: str, ingredients: list[str], describtion: str):
        self.price = price
        self.name = name
        self.ingredients = ingredients
        self.describtion = describtion

    def __str__(self):
        result = f'Название: {self.name}\n'
        result += 'Ингредиенты:\n'
        for ingredient in self.ingredients:
            result += f'\t-{ingredient}\n'
        result += f'Цена: {self.price} рублей\n'
        result += f'Описание: {self.describtion}\n\n'
        return result

class MealContainer:
    def __init__ (self, meals: list[Meal]):
        self.meals = meals

    def write_to_file(self):
        f = open('meals.txt', 'w+', encoding='utf-8' )
        f.write('Блюда:\n')
        for meal in self.meals:
            f.write(str(meal))
        f.close()

kurica = Meal(price =4000, ingredients=['курица', 'я'], name = 'хз', describtion='...')
potato = Meal(price=2000, ingredients=['картошка..?'], name = 'Картошка', describtion='Картошка.')
soup = Meal(price=10000000, ingredients=['вода', 'соль'], name = 'Суп', describtion='aaaaaaaa')
meal_co= MealContainer(meals=[kurica, potato, soup])
meal_co.write_to_file()