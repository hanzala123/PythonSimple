from time import sleep
for i in range(10):
    end = '\r'
    if i >8:
        end = '\n'
    print('\r'+'['+('='*i).ljust(9)+']'+'\r', end=end)
    sleep(0.3)
