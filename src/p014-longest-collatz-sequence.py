# The following iterative sequence is defined for the set of positive integers:
#
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

class CollatzSequence():
    def __init__(self):
        self.sequences = {}

    def getSequenceLen(self, number):
        start = number
        counter = 1

        while number != 1:
            loaded_counter = 0
#            print('number = {}, counter = {}'.format(number, counter))
            if number in self.sequences:
#                print('Found existing sequence: {}, len = {}'.format(number, self.sequences[number]))
                counter += self.sequences[number] - 1
                loaded_counter = self.sequences[number]
                break
            elif number % 2 == 0:
                number = number / 2
            else:
                number = 3 * number + 1
            counter += 1
        if loaded_counter + 5 < counter:
            self.sequences[start] = counter
 #       print('Sequence length for {} is {}'.format(start, counter))
        return counter


def main():
    print('Starting.')
    longest = 0
    number = 0

    stuff = CollatzSequence()
    for i in range(2, 1000000):
        temp = stuff.getSequenceLen(i)
        if temp > longest:
            longest = temp
            number = i
        if i % 100000 == 0:
            print('Longest sequence under {} is {}, {} long. Stored amount={}'.format(i, number, longest, len(stuff.sequences)))

if __name__ == '__main__':
    main()
