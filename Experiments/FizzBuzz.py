import time

x = 1

while True:
    try:
        y = str()
        if x % 3 == 0:
            y += 'Fizz'
        if x % 5 == 0:
            y += 'Buzz'
        if y == str():
            print(x)
            time.sleep(1)
            x += 1
            continue
        print(y)
        time.sleep(1)
        x += 1
        
    except KeyboardInterrupt:
        print('EXITING CODE.')
        break