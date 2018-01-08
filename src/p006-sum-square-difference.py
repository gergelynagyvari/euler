
class SumSquare:
    def __init__(self):
        pass


def main():
    ss = SumSquare()

    s1 = 0
    s2 = 0
    for v in range(101):
        s1 += v*v
        s2 += v
        print('v = {}, s1 = {}, s2 = {}'.format(v, s1, s2))

    print('s1={}, s2={}, s22={}, diff={}'.format(s1, s2, s2*s2, s2*s2-s1))

if __name__ == '__main__':
    main()



