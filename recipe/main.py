from recipe import Recipe

# replace redundant code with a creational method
def create_recipe(name, coffee=0, chocolate=0, sugar=0, milk=0, price=0.0):
    recipe = Recipe(name)
    recipe.coffee = coffee
    recipe.chocolate = chocolate
    recipe.sugar = sugar
    recipe.milk = milk
    recipe.price = price
    return recipe


if __name__ == '__main__':
    recipe1 = create_recipe("Coffee with sugar", coffee=4, sugar=2, price=30.0)
    print(recipe1)

    recipe2 = create_recipe("Latte", coffee=3, sugar=2, milk=1, price=40.0)
    print(recipe2)

    recipe3 = create_recipe("Hot Chocolate", coffee=0, chocolate=3, sugar=2, milk=4, price=30.0)
    print(recipe3)
