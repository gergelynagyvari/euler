# Starting in the top left corner of a 2+2 grid, and only being able to
# move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20+20 grid?

class LatticePath():
    def __init__(self):
        pass

    def countPaths(self, m, n):
        print('Start counting paths for a {}x{} matrix'.format(m, n))

        count = [[0 for x in range(m)] for y in range(n)]

        for i in range(m):
            count[i][0] = 1

        for j in range(n):
            count[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                count[i][j] = count[i-1][j] + count[i][j-1]

        print(repr(count))


def main():
    pathFinder = LatticePath()

    pathFinder.countPaths(2, 2)
    pathFinder.countPaths(3, 3)
    pathFinder.countPaths(21, 21)


if __name__ == '__main__':
    main()
