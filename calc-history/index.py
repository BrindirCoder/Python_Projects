history = []

while True:
    print("\nEnter calculation (or type 'exit')")
    expr = input(">>> ")

    if expr.lower() == "exit":
        break

    try:
        result = eval(expr)
        print("Result:", result)

        history.append(f"{expr} = {result}")

    except:
        print("Invalid calculation")

    print("\nHistory:")
    for item in history:
        print(item)

    
