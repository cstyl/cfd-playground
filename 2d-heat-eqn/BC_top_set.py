# Copyright 2022 cstyl
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from common import set_IC, set_BC, calculate


def animate(k):
    plotheatmap(u[k], k)


def plotheatmap(u_k, k):
    # Clear the current plot figure
    plt.clf()

    plt.title(f"Temperature at t = {k*delta_t:.3f} unit time")
    plt.xlabel("x")
    plt.ylabel("y")

    # This is to plot u_k (u at time-step k)
    plt.pcolormesh(u_k, cmap=plt.cm.jet, vmin=0, vmax=100)
    plt.colorbar()

    return plt


PLATE_LENGTH = 50
MAX_ITER_TIME = 1000

alpha = 2.0
delta_x = 1

delta_t = (delta_x ** 2) / (4 * alpha)
gamma = (alpha * delta_t) / (delta_x ** 2)

# Initial condition everywhere inside the grid
u_initial = np.zeros((PLATE_LENGTH, PLATE_LENGTH))

# Boundary conditions
u_top = 100.0
u_left = 0.0
u_bottom = 0.0
u_right = 0.0

# The grid of u(k, i, j)
u = np.empty((MAX_ITER_TIME, PLATE_LENGTH, PLATE_LENGTH))

u = set_IC(u_initial, u)
u = set_BC(u_top, u_left, u_bottom, u_right, u, lx=PLATE_LENGTH, ly=PLATE_LENGTH)
u = calculate(
    gamma,
    u,
    max_iter=MAX_ITER_TIME,
    delta_x=delta_x,
    delta_y=delta_x,
    lx=PLATE_LENGTH,
    ly=PLATE_LENGTH,
)

anim = animation.FuncAnimation(
    plt.figure(), animate, interval=1, frames=MAX_ITER_TIME, repeat=False,
)
anim.save("BC_top_100.gif")
