def max_number(numbers):
   max = numbers[0]
   for element in numbers:
      if element > max:
         max = element
      return max


numbers = [100, 1, 5, 80, 69, 76, 102, 33, 20]

print("Largest element of the list is:", max_number(numbers))

