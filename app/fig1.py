import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
import numpy, scipy.optimize


# Your code that uses argrelextrema

np.random.seed(42)
time = np.linspace(0, 48, 200)
base_prices = 20 + 10 * np.sin((2 * np.pi / 24) * time)
noise = np.random.normal(scale=2, size=len(time))
electricity_prices = base_prices + noise


def fit_sin(tt, yy):
    '''Fit sin to the input time sequence, and return fitting parameters "amp", "omega", "phase", "offset", "freq", "period" and "fitfunc"'''
    tt = numpy.array(tt)
    yy = numpy.array(yy)
    ff = numpy.fft.fftfreq(len(tt), (tt[1]-tt[0]))   # assume uniform spacing
    Fyy = abs(numpy.fft.fft(yy))
    guess_freq = abs(ff[numpy.argmax(Fyy[1:])+1])   # excluding the zero frequency "peak", which is related to offset
    guess_amp = numpy.std(yy) * 2.**0.5
    guess_offset = numpy.mean(yy)
    guess = numpy.array([guess_amp, 2.*numpy.pi*guess_freq, 0., guess_offset])

    def sinfunc(t, A, w, p, c):  return A * numpy.sin(w*t + p) + c
    popt, pcov = scipy.optimize.curve_fit(sinfunc, tt, yy, p0=guess)
    A, w, p, c = popt
    f = w/(2.*numpy.pi)
    fitfunc = lambda t: A * numpy.sin(w*t + p) + c
    return {"amp": A, "omega": w, "phase": p, "offset": c, "freq": f, "period": 1./f, "fitfunc": fitfunc, "maxcov": numpy.max(pcov), "rawres": (guess,popt,pcov)}


N, amp, omega, phase, offset, noise = 500, 1., 2., .5, 4., 3
#N, amp, omega, phase, offset, noise = 50, 1., .4, .5, 4., .2
#N, amp, omega, phase, offset, noise = 200, 1., 20, .5, 4., 1
tt = time
tt2 = time
yy = electricity_prices
yynoise = yy + noise*(numpy.random.random(len(tt))-0.5)

res = fit_sin(tt, yynoise)

maxima_indices = argrelextrema(res["fitfunc"](tt), np.greater)


def fig1():
    plt.plot(tt, yy, "-k", label="y", linewidth=2)
    plt.plot(tt, yynoise, "ok", label="y with noise")
    plt.plot(tt2, res["fitfunc"](tt2), "r-", label="y fit curve", linewidth=2)
    plt.scatter(tt[maxima_indices], res["fitfunc"](tt)[maxima_indices], color='red', label='Local Maxima')
    plt.legend(loc="best")
    #plt.show()


    script_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_path, '../frontend/src/components/assets/fig1.png')
    plt.savefig(file_path, dpi=300)

    plt.close()
    return "./components/assets/fig1.png"

fig1()

    



