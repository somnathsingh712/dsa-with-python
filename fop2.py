def toppings(scoop,*menu):
    print(f"\n making a {scoop} scoop ice cream with:")
    for i in menu:
        print(f"- {i}")

toppings(2,'chocolate')
toppings(3,'chocolate','fruits&nuts','butterscotch')
