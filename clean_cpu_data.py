import numpy as np
import matplotlib.pyplot as plt


def CartoAnalysis(processID: str, typeOfProcess='mapping'):
    '''
    @param: processID
    @param: typeOfProcess: str ('mapping' or 'localization')
    '''
    lst = []
    with open(f"carto_{typeOfProcess}.txt", mode='r') as in_f:
        for line in in_f:
            if line.strip():
                beatiful_line = line.lstrip()
                if beatiful_line.startswith(processID):
                    lst_words = beatiful_line.split()
                    lst.append(float(lst_words[8].replace(',', '.')))


    beautiful_array = np.array(lst)
    print('average: ' + str(np.average(beautiful_array)))
    print('max: ' + str(np.max(beautiful_array)))
    print('min: ' + str(np.min(beautiful_array)))
    print(f'Execution time: {len(beautiful_array) * 3} s')


    with open(f"{typeOfProcess}_result.txt", 'w') as out_f:
        out_f.write(f'------------ {typeOfProcess} phase analysis ------------\n')
        out_f.write('Average: ' + str(np.average(beautiful_array)) + ' %\n')
        out_f.write('Max: ' + str(np.max(beautiful_array)) + ' %\n')
        out_f.write('Min: ' + str(np.min(beautiful_array)) + ' %\n')
        out_f.write(f'Execution time: {len(beautiful_array) * 3} s' + '\n')


    plt.figure(figsize=(8, 6))
    plt.plot(beautiful_array)
    plt.xlabel('Time stamp - split 3 second')
    plt.ylabel("%CPU usage")
    plt.title(f'CPU usage of Cartographer during {typeOfProcess} on Intel® Core™ i7-7700HQ CPU @ 2.80GHz x 8 ')
    plt.savefig(f"{typeOfProcess}.pdf", bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    CartoAnalysis('66562', 'localization')