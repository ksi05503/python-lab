class PermutationGenerator:
    table = {}

    def __init__(self, str):
        self.str = str
        self.init_table()

    def get_table(self):
        return self.table

    def init_table(self):
        self._recursive(self.str)

    def _recursive(self, current, result=''):
        # escape
        if len(self.str) == len(result):
            self.table[result] = True
            return result

        # rescursion
        for i in range(len(current)):
            self._recursive(_delete_char(current, i), result + current[i])

# util
def _delete_char(str, i):
    return str[:i] + str[i + 1:]

def main():
    p = PermutationGenerator('ABCDE')
    print(p.get_table())


if __name__ == '__main__':
    main()