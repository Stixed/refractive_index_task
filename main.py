import numpy as np
from scipy.optimize import newton

global T

class Material:
    thick = 90
    freqRange = np.linspace(0,1,1001)
    transOmega = 1
    nOmega = np.zeros(freqRange.shape, dtype = complex)
    def display_info(self):
        print("The thickness of the layer is ", self.thick)

    def getRefrIndex():
        self.nOmega = newton(func, omega0, fprime=funcDerivative)


def func(n):

    return

def funcDerivative(n):

    return 

def loadSignal(fname):
    importedSignal = np.loadtxt(fname)
    
    return signalIn, signalOut

material1 = Material()
