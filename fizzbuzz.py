def fizzbuzz():
    for i in list(range(1,100)): 
        if i % 15 == 0:
            print('Fizzbuzz')
        elif i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0:
            print('Fizz')
        else:
            print(i)

fizzbuzz()