class ListDiff:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def calculate_diff(self):
        diff = set(self.list_1) ^ set(self.list_2)
        return list(diff)
