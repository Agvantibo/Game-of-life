def create2DArray(material, length):
    array = []
    for i in range(length):
        array.append([material] * length)
    return array


def print_red(val):
    print("\033[1;31;49m", end='')
    print(val)
    print("\033[1;30;49m", end='')


class dim_list:
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


def Get_Diagonal_Left(length):
    output_Array = []
    for y in range(length + 1):
        output_Array.append(coordinate(y - 1, y - 1))
    return output_Array


def print2DArray(array, end):
    for i in array:
        for j in i:
            print(j, end=end)
        print()


class coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def GetNeighborIndices(row, col):
    answer = [coordinate(row + 1, col), coordinate(row - 1, col), coordinate(row, col + 1), coordinate(row, col - 1),
              coordinate(row + 1, col + 1), coordinate(row + 1, col - 1), coordinate(row - 1, col + 1),
              coordinate(row - 1, col - 1), ]
    return answer
