
numbers_list = [1,2,3]



def return_number():
    for number in numbers_list:
        if number == 2:
            new_num = number + 1
            return new_num

final_number = return_number()

print(final_number)


# def return_number_simple():
#     newest_number = numbers_list[1] + 1
#     return newest_number

# print(newest_number)