#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    try:
        for i in range(list_length):
            try:
                item1 = my_list_1[i]
                item2 = my_list_2[i]

                if not (isinstance(item1, (int, float)) and isinstance(item2, (int, float))):
                    print("wrong type")
                    result.append(0)
                    continue
                if item2 == 0:
                    print("division by 0")
                    result.append(0)
                else:
                    result.append(item1 / item2)

            except IndexError:
                print("out of range")
                result.append(0)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        return result