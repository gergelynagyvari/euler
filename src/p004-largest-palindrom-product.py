
class Palindrome:
    def __init__(self):
        pass

    def isPalindrome(self, number):
        text='{}'.format(number)
        for i in range(len(text)/2):
            #print('text[{}]={}, text[{}]={}'.format(i, text[i], -(i+1), text[-(i+1)]))
            if text[i] != text[-(i+1)]:
                return False
        return True

    def generateProducts(self, start, end):
        return {a*b:[a,b] for a in range(start, end) for b in range(start, end)}

def main():
    checker = Palindrome()
    products = checker.generateProducts(900, 999)

    for k,v in sorted(products.iteritems(), reverse = True):
        if checker.isPalindrome(k):
            print('{} = product({})'.format(k, repr(v)))
            return


    #print(checker.isPalindrome(121))


if __name__ == '__main__':
    main()



