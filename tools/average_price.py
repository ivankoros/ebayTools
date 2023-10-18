def average_price():
    """Returns the average price of a list of prices and the 10%, 20%, 30%, 40%, and 50% markup of the average price.

    Example:
    Input first price: 10
    Input price # 2: 12
    Input price # 3: 15
    Input price # 4: 11

    Average price is: $12.67
    __________________________________
    10% markup: $13.93
    20% markup: $15.2
    30% markup: $16.47
    40% markup: $17.73
    50% markup: $19.0


    :return: None
    """
    command = input("Input first price:")

    count = 1
    total_value = 0
    while command != "stop":
        command = input(f"Input price # {count + 1}: ")
        try:
            command = float(command)
            total_value += command
            count += 1
        except ValueError:
            if command.lower() in ["stop", "quit"]:
                break
            else:
                print("Invalid input. Please enter a number or 'stop' to stop. ")
                continue

    average = round(total_value / count, 2)

    print(f"\n \nAverage price is: ${average} \n"
          f"__________________________________\n"
          f"10% markup: ${round(average * 1.1, 2)} \n"
          f"20% markup: ${round(average * 1.2, 2)} \n"
          f"30% markup: ${round(average * 1.3, 2)} \n"
          f"40% markup: ${round(average * 1.4, 2)} \n"
          f"50% markup: ${round(average * 1.5, 2)} \n")


if __name__ == "__main__":
    average_price()
