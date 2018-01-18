import math

def main():
    total = 0
    for c in '{}'.format(math.factorial(100)): 
        total += int(c)
    print(total)

if __name__ == '__main__':
    main()
