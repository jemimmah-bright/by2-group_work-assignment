# # # Loops

# # # Basic: Write a Python program that prints all even numbers between 1 and 20 using a for loop.

# def even_numbers ():
#     for even_num in range (1,21):
#      if even_num % 2==0:
#         print (even_num)
# even_numbers ()


# # # APPROACH 2
# # Loop through numbers from 1 to 20
# for num in range(1, 21):
#     # Check if the number is even
#     if num % 2 == 0:
#         print(num)

# # APPROACH 3 USING THE WHILE LOOP
# num = 2
# while num <=20:
#     print (num)
#     num +=2

# # OTHER TRIAL
# # Define the function to print even numbers between 1 and 20
# def print_even_numbers():
#     # Start with the first even number, which is 2
#     num = 2
#  # Continue while the number is less than or equal to 20
#     while num <= 20:
#         print(num)
#         num += 2  #This will help Move to the next even number
# print_even_numbers()


# # Intermediate: Use a while loop to ask the user to input a number until they provide a number greater than 10.

          
# num = 0
# while num <= 10:
#     num = int(input("Enter a number greater than 10     :"))
#     if num <= 10:
#         print (f"The number is smaller than 10 please try again")
#     else:
#         print (f"Thank you. the number entered is greater than 10")


# Advanced: Write a program that prints the multiplication table (from 1 to 10) for numbers
#  from 1 to 5 using nested for loops.
# def multiplication_table(): 
#     for j in range(1,11):
#         for k in range(1,6):
#             print(j*k, end=' \t ')
#         print('\n')
# multiplication_table()


    
# Challenge: Given a list of integers, [4, 7, 2, 9, 12, 15], 
# write a program using a for loop to find the sum of all odd numbers and print the result.
def sum_of_all_odd_numbers ():
    list = [4, 7, 2, 9, 12, 15]
    sum = 0
    for number in  list:

        if number % 2!= 0:
            sum += number
    print(f" The total sum of all odd numbers is {sum}")
sum_of_all_odd_numbers ()



