import sys
import os

if __name__ == '__main__':
    sys.path.append('..')
    year = input('Enter year: ')
    filetype = input('Enter filetype: ')
    # create folders for the days and the py files
    for i in range(1, 26):
        if not os.path.exists(year + '/Day' + str(i)):
            os.makedirs(year + '/Day' + str(i) + '/src')
            f = open(year + '/Day' + str(i) + '/src/main.' + filetype, 'w')
            f.close()
            f = open(year + '/Day' + str(i) + '/input.txt', 'w')
            f.close()
