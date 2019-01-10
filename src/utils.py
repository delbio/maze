
def rotate_counterclockwise(array_2d):
    list_of_tuples = zip(*array_2d[::])
    return [list(elem) for elem in list_of_tuples]

def rotate_clockwise(array_2d):
    """
    Code copied by: https://stackoverflow.com/a/48444999/3753724
    """
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]
