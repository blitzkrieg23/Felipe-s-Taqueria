x = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0

while True:
    try:
        item = input('Item: ').title()
        if item not in x:
            raise Exception
    except EOFError:
        break
    except:
            continue
    else:
        total += x[item]
        print(f'Total :${total:.2f}')