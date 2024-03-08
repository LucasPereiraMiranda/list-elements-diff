from list_diff import ListDiff


def handle():
    list_1 = ['1', '2', '3']
    list_2 = ['1', '2']

    list_diff = ListDiff(list_1, list_2)
    result = list_diff.calculate_diff()
    print('list_1:',list_1)
    print('list_2:',list_2)
    print('diff:',result)

    print('list_1 len:', len(list_1))
    print('list_2 len:', len(list_2))
    print('diff len:', len(result))


if __name__ == '__main__':
    handle()
