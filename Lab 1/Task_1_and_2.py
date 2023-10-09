# author: David Kromka

import time


def taskA(input_str):
    start_time = time.perf_counter()  # Record the start time
    input_str = input_str.upper()  # Convert the input string to uppercase
    result_order = ""
    result_reverse = ""
    result_reverse_array = []

    for char in input_str:
        if char.isalpha():  # Check if the character is a letter
            # Convert the letter to a number in order
            number_in_order = ord(char) + 1 - ord('A')
            # Convert the letter to a number in reverse order
            number_in_reverse = 26 - (ord(char) - ord('A'))
            result_reverse_array.append(number_in_reverse - 1)

            # Append the numbers to the result strings
            result_order += str(number_in_order) + " "
            result_reverse += str(number_in_reverse) + " "

        else:
            # If it's not a letter, just append it as is
            result_order += char
            result_reverse += char
            result_reverse_array.append(char)
    end_time = time.perf_counter()  # Record the end time
    execution_time = (end_time - start_time) * 1000  # Calculate the execution time
    return result_order, result_reverse, numbers_to_letters(result_reverse_array), execution_time


def taskB(input_str):
    start_time = time.perf_counter()  # Record the start time
    input_str = input_str.upper()  # Convert the input string to uppercase
    b_result_array = []

    for char in input_str:
        if char.isalpha():  # Check if the character is a letter
            # Convert the letter to a number in reverse order
            number_in_reverse = 26 - (ord(char) - ord('A'))
            if (ord(char) + 1 - ord('A')) <= 13:
                half_number = 13 - (ord(char) + 1 - ord('A'))
            else:
                half_number = number_in_reverse + 12
            b_result_array.append(half_number)
        else:
            b_result_array.append(char)
    end_time = time.perf_counter()  # Record the end time
    execution_time = (end_time - start_time) * 1000  # Calculate the execution time
    return numbers_to_letters(b_result_array), b_result_array, execution_time


def taskC(input_str, k):
    start_time = time.perf_counter()  # Record the start time
    input_str = input_str.upper()  # Convert the input string to uppercase
    c_result_array = []

    for char in input_str:
        if char.isalpha():  # Check if the character is a letter
            if k == 0:
                k = ord(char) - ord('A') + 1
            if (k + ord(char) - ord('A') + 1) > 26:
                c_result_array.append(k + ord(char) - ord('A') - 26)
            else:
                c_result_array.append(k + ord(char) - ord('A'))
        else:
            c_result_array.append(char)
    end_time = time.perf_counter()  # Record the end time
    execution_time = (end_time - start_time) * 1000  # Calculate the execution time
    return numbers_to_letters(c_result_array), c_result_array, execution_time


def taskA_decrypt(input_string):
    start_time = time.perf_counter()  # Record the start time
    input_numbers = input_string.split()
    decrypt_array = []
    for num in input_numbers:
        decrypt_array.append(26 - int(num))
    end_time = time.perf_counter()  # Record the end time
    execution_time = (end_time - start_time) * 1000  # Calculate the execution time
    return numbers_to_letters(decrypt_array), execution_time


def taskB_decrypt(input_string):
    start_time = time.perf_counter()  # Record the start time
    input_numbers = input_string.split()
    decrypt_array = []
    for num in input_numbers:
        if int(num) <= 13:
            decrypt_array.append(13 - int(num))
        else:
            decrypt_array.append(13 - int(num) + 26)
    end_time = time.perf_counter()  # Record the end time
    execution_time = (end_time - start_time) * 1000  # Calculate the execution time
    return numbers_to_letters(decrypt_array), execution_time


def taskC_decrypt(input_string, k):
    start_time = time.perf_counter()  # Record the start time
    input_numbers = input_string.split()
    decrypt_array = []
    for num in input_numbers:
        if int(num) - k > 0:
            decrypt_array.append(int(num) - k - 1)
        else:
            decrypt_array.append(25 + int(num) - k)
    end_time = time.perf_counter()  # Record the end time
    execution_time = (end_time - start_time) * 1000  # Calculate the execution time
    return numbers_to_letters(decrypt_array), execution_time


def numbers_to_letters(result_reverse_array):
    return ''.join(chr(int(item) + ord('A')) for item in result_reverse_array)


def encrypt(input_string):
    # Task A
    result_order, result_reverse, result_reverse_string, execution_time = taskA(input_string)
    print("Task A:")
    print("Result in order:", result_order)
    print("Result in reverse order:", result_reverse)
    print("Letters from reverse order:", result_reverse_string)
    print("Execution Time: ", round(execution_time, 4), "milliseconds \n")

    # Task B
    b_result, b_result_array, execution_time = taskB(input_string)
    print("Task B:")
    print("Result:", b_result)
    print("Numbers result:", ' '.join(map(lambda x: str(x + 1), b_result_array)))
    print("Execution Time: ", round(execution_time, 4), "milliseconds \n")

    # Task C
    # My K number from lecture is 11
    # c_result, execution_time = taskC(input_string, 0)
    c_result_k, c_result_k_array, execution_time_k = taskC(input_string, 11)
    print("Task C:")
    # print("Result with k = first letter : ", c_result)
    # print("Execution Time:", round(execution_time, 4), "milliseconds \n")
    print("Result with k = 11: ", c_result_k)
    print("Numbers result with k = 11: ", ' '.join(map(lambda x: str(x + 1), c_result_k_array)))
    print("Execution Time : ", round(execution_time_k, 4), "milliseconds \n")


def decrypt(input_string):
    # Task A
    a_decrypt, execution_time = taskA_decrypt(input_string)
    print("Task A decryption: ", a_decrypt)
    print("Execution Time : ", round(execution_time, 4), "milliseconds \n")

    # Task B
    b_decrypt, execution_time = taskB_decrypt(input_string)
    print("Task B decryption: ", b_decrypt)
    print("Execution Time : ", round(execution_time, 4), "milliseconds \n")

    # Task C
    c_decrypt, execution_time = taskC_decrypt(input_string, 11)
    print("Task C decryption: ", c_decrypt)
    print("Execution Time : ", round(execution_time, 4), "milliseconds \n")


def main():
    # Get input from the user
    input_string = input("Enter a string to encrypt or space separated numbers to decrypt: ")

    # Split the input string into words and check if all words are numbers
    all_numbers = all(word.isdigit() for word in input_string.split())
    print(all_numbers)
    # Output the result
    if all_numbers:
        decrypt(input_string)
    else:
        encrypt(input_string)


while True:
    main()
