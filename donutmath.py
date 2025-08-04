import os
import sys
import math
import time

# Screen size
width, height = 80, 24
theta_spacing = 0.07
phi_spacing = 0.02

# Precompute luminance characters
chars = ".,-~:;=!*#$@"

A, B = 0, 0
while True:
    z = [0] * (width * height)
    b = [' '] * (width * height)
    for j in range(0, 628, int(theta_spacing * 100)):  # theta from 0 to 2pi
        for i in range(0, 628, int(phi_spacing * 100)):  # phi from 0 to 2pi
            c = math.sin(i * 0.01)
            d = math.cos(j * 0.01)
            e = math.sin(A)
            f = math.sin(j * 0.01)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i * 0.01)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(width / 2 + 30 * D * (l * h * m - t * n))
            y = int(height / 2 + 15 * D * (l * h * n + t * m))
            o = int(x + width * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if height > y > 0 and 0 < x < width and D > z[o]:
                z[o] = D
                b[o] = chars[max(0, N)]
    os.system('cls' if os.name == 'nt' else 'clear')
    sys.stdout.write(''.join(b))
    sys.stdout.flush()
    A += 0.04
    B += 0.08
    time.sleep(0.03)
