#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    try:
        for i in range(list_length):
            try:
                number1 = my_list_1[i] if i < len(my_list_1) else 0
                number2 = my_list_2[i] if i < len(my_list_2) else 0

                if not (isinstance(number1, (int, float)) and isinstance(number2, (int, float))):
                    print("Wrong type")
                    return
                if number2 == 0:
                    print("division by 0")
                    return
                result.append(number1 / number2)
            except IndexError:
                print("out of range")
                return
    except Exception as e:
        print("Oops.. An error occured", e)
    finally:
        return (result)
