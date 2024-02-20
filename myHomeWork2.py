# # print("hello \n \t this is my first homework")
# # # print("\n" * 4)
# # # print("fill", end="-" "TO:")
# # # num1 = 800
# # # num2 = 80
# # # print(num1 // num2)
# # # print(num1 % num2)
# #
# number = int(input("Enter 4-digit number:"))
# n1 = number // 1000
# n2 = number // 100 % 10
# n3 = number % 100 // 10
# n4 = number % 10
# #
# # result = n1 + n2 + n3 + n4
# # print(f"n1: {n1} n2: {n2} n3: {n3} n4: {n4}")
# # # print(f"Result: {result}")
#
# first_diagonal=int(input("Enter the first diagonal:"))
# second_diagonal = int(input("enter the second diagonal:"))
# area = (first_diagonal * second_diagonal) / 2
# print("Area:", area)
#
# print("hello", "hello","hello", sep="v,", end=" ")
# print("world")
#
#
# print("hello", "hello","hello", sep="v,", end=" ")
# print("world")
# n1 = 10
# n2 = 20
#
# n1, n2 = 10, 20
# print(n1 > n2)
# print(n1 >= n2)
# print(n1 < n2)
# print(n1 <= n2)
# print(n1 == n2)
# print(n1 != n2)
#
# print(1 == 1 and 3 == 3)
# print(1 == 1 or 2 == 3)
#
# is_valid = False
# print(is_valid)
# print(not is_valid)
#
# # print("Hello" in "hello world")
# hours = int(input("enter hours"))
#
# if 12 <= hours <= 23:
#     print("PM")
# elif 0 <= hours < 12:
#     print("AM")
# else:
#     print("incorrect hours!")
film_rating = int(input("Enter the film rating"))
if film_rating > 0 and film_rating <= 5:
    if film_rating == 4 or film_rating == 5:
        print("OK")
    else: print("not OK")
else:
    print("incorrect rating")
print("hi")