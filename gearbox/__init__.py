def create_2d_array(material, length):
    array = []
    for i in range(length):
        array.append([material] * length)
    return array


def print_red(val):
    print("\033[1;31;49m", end='')
    print(val)
    print("\033[1;30;49m", end='')


class Smartlist:
    def __init__(self, array):
        self.array = array

    def write(self, location, symbol):
        symbol = str(symbol)
        try:
            self.array[location.x][location.y] = symbol
        except IndexError:
            print_red('Something is wrong with the indices')

    def get(self, location):
        try:
            ans = self.array[location.x][location.y]
        except IndexError:
            return None
        return ans

    def print(self, separator):
        for i in self.array:
            for j in i:
                print(j, end=separator)
            print()
        print()

    def convert_to(self, input_array):
        self.array = input_array

    def convert_from(self):
        return self.array

    def append_b(self, row, element):
        self.array[row].append(element)

    def n_row(self):
        self.array.append([])


def print_2d_array(array, end):
    for i in array:
        for j in i:
            print(j, end=end)
        print()


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def get_neighbor_indices(row, col):
    answer = [Coordinate(row + 1, col), Coordinate(row - 1, col), Coordinate(row, col + 1), Coordinate(row, col - 1),
              Coordinate(row + 1, col + 1), Coordinate(row + 1, col - 1), Coordinate(row - 1, col + 1),
              Coordinate(row - 1, col - 1), ]
    return answer
