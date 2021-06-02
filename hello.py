
def greet(people):
    printout = []
    for p in people:
        to_print = 'hello {}'.format(p)
        printout.append(to_print)
        print(to_print)
    return printout


if __name__ == '__main__':

    everybody = [
        'colin',
        'pierre'
    ]
    greet(everybody)
