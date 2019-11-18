
import sys

import numpy as np
import scipy.io.wavfile as wf



def main():
    args= sys.argv

    rate1, data1 = wf.read('loop1.wav')
    rate2, data2 = wf.read('strings.wav')
    rate3, data3 = wf.read('fanfare.wav')
    if rate1 != rate2 or rate2 != rate3:
        raise ValueError('Sampling_rate_Error')

    mix_1 = data1 * 0.6 + data2 * 0.3 + data3 * 0.1
    mix_2 = data1 * 0.3 + data2 * 0.2 + data3 * 0.5
    mix_3 = data1 * 0.1 + data2 * 0.5 + data3 * 0.4
    y = [mix_1, mix_2, mix_3]
    y = [(y_i * 32767 / max(np.absolute(y_i))).astype(np.int16) for y_i in np.asarray(y)]

    wf.write('mix_1.wav', rate1, y[0])
    wf.write('mix_2.wav', rate2, y[1])
    wf.write('mix_3.wav', rate3, y[2])


if __name__ == '__main__':
    main()
