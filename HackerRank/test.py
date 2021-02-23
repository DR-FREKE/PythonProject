def fizzBuzz(n):
    for num in range(n + 1):
        if num != 0:
            if(num % 3 == 0 and num % 5 != 0):
                print('fizz')
            elif num % 5 == 0 and num % 3 != 0:
                print('buzz')
            elif num % 5 == 0 and num % 3 == 0:
                print('fizzBuzz')
            else:
                print(num)


fizzBuzz(15)
