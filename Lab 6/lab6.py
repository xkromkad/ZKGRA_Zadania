#author: David Kormka
DES_IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

DES_FP = [40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41, 9, 49, 17, 57, 25]

INTEL_IP = [6, 14, 22, 30, 38, 46, 54,
            62, 4, 12, 20, 28, 36, 44, 52,
            60, 2, 10, 18, 26, 34, 42, 50,
            58, 0, 8, 16, 24, 32, 40, 48, 56,
            7, 15, 23, 31, 39, 47, 55, 63, 5,
            13, 21, 29, 37, 45, 53, 61, 3, 11,
            19, 27, 35, 43, 51, 59, 1, 9, 17,
            25, 33, 41, 49, 57]

SBOX = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
       [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
       [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
       [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
#Task 1

def tab_values():

    intel_values = [14, 23, 61, 6]
    for item in intel_values:
        index = INTEL_IP.index(item)
        print(f"Intel x86 initial value: {item}, DES initial value: {DES_IP[index]}, DES final value: {DES_FP[index]}")

#Task 2
def sbox(binary_number):

    # Extracting first and last digits
    first_last_digits = binary_number[0] + binary_number[-1:]

    # Extracting middle four digits
    middle_digits = binary_number[1:5]

    # Converting binary to decimal
    outer_decimal = int(first_last_digits, 2)
    middle_decimal = int(middle_digits, 2)
    return outer_decimal, middle_decimal



print("Task 1")
tab_values()

print("Task 2")
letter_counter = ord('a')
binary_numbers = ["011010", "001111", "110110", "110011"]
for binary_number in binary_numbers:
    outer, inter = sbox(binary_number)
    result = SBOX[outer][inter]
    letter = chr(letter_counter)
    print(f"{letter}: {result}")
    letter_counter += 1
