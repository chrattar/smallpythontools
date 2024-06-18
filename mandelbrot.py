import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iterations=1000):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iterations:
        z = z*z + c
        n += 1
    return n

def mandelbrot_set(x_min, x_max, y_min, y_max, width, height, max_iterations=1000):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    mandelbrot_data = np.empty((width, height))

    for i in range(width):
        for j in range(height):
            real = x[i]
            imag = y[j]
            c = complex(real, imag)
            mandelbrot_data[i, j] = mandelbrot(c, max_iterations)

    return mandelbrot_data

# Define the region of the complex plane to plot
x_min, x_max = -2.0, 1.0
y_min, y_max = -1.5, 1.5
width, height = 800, 800
max_iterations = 1000

# Calculate the Mandelbrot set data
mandelbrot_data = mandelbrot_set(x_min, x_max, y_min, y_max, width, height, max_iterations)

# Plot the Mandelbrot set
plt.imshow(mandelbrot_data.T, extent=(x_min, x_max, y_min, y_max), cmap='jet', origin='lower')
plt.title("Mandelbrot Set")
plt.colorbar()
plt.show()
