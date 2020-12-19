import numpy as np

def flatten(iterable):
    try:
        iterator = iter(iterable)
    except TypeError:
        yield iterable
    else:
        for element in iterator:
            yield from flatten(element)

num_samples = 128

t = np.linspace(0, 0.5, num_samples)
real_data = np.sin(t)

imag_data = np.array([0] * num_samples)
data = real_data + 1j * imag_data

print("-----------BEGIN Raw Data-----------")
print(data)
print("-----------END Raw Data-----------" + "\n")

print("-----------BEGIN Raw Results-----------")
print(np.fft.fft(data))
print("-----------END Raw Results-----------" + "\n")

print("-----------BEGIN Magnitude-----------")
print(np.absolute(np.fft.fft(data)))
print("-----------END Magnitude-----------" + "\n")

print("-----------BEGIN Data for Numerical Recipes FFT routine-----------")
print([round(x, 5) for x in flatten([[x, 0] for x in real_data])])
print("-----------END Raw Data-----------" + "\n")

