
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

np.random.seed(42)
time = np.linspace(0, 48, 200)
base_prices = 20 + 10 * np.sin((2 * np.pi / 24) * time)
noise = np.random.normal(scale=2, size=len(time))
electricity_prices = base_prices + noise

import numpy, scipy.optimize

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

opposite_line = 40 - res["fitfunc"](tt)

# Find indices of local maxima in the opposite line
maxima_indices_opposite = argrelextrema(opposite_line, np.greater)

def fig2(): 
    print("Starting fig2...")
    plt.plot(tt, yy, "-k", label="y", linewidth=2)
    plt.plot(tt, res["fitfunc"](tt), "r-", label="y fit curve", linewidth=2)
    plt.plot(tt, opposite_line, "b--", label="Opposite Line", linewidth=2)
    plt.scatter(tt[maxima_indices_opposite], opposite_line[maxima_indices_opposite], color='green', label='Local Maxima in Opposite Line')
    plt.legend(loc="best")

    script_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_path, '../frontend/src/components/assets/fig2.png')
    plt.savefig(file_path, dpi=300)
    print("Completed fig2...")
    return "./components/assets/fig2.png"

fig2()
    
