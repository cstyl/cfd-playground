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


def set_IC(u_initial, u):
    """
    Set the initial conditions on the four sides of the plate and inside.

    Parameters
    ----------
    u_initial : 2D array
        Initial condition values.
    u : array
        Numpy array representing the grid domain.
    """
    u[0, :, :] = u_initial

    return u


def set_BC(u_top, u_left, u_bottom, u_right, u, lx=50, ly=50):
    """
    Set the boundary conditions on the four sides of the plate.

    Parameters
    ----------
    u_top : float
        Boundary condition of the top side.
    u_left : float
        Boundary condition of the left side.
    u_bottom : float
        Boundary condition of the bottom side.
    u_right : float
        Boundary condition of the right side.
    u : array
        Numpy array representing the grid domain.
    """
    u[:, (ly - 1) :, :] = u_top
    u[:, :, :1] = u_left
    u[:, :1, 1:] = u_bottom
    u[:, :, (lx - 1) :] = u_right

    return u


def calculate(gamma, u, max_iter=1000, delta_x=1, delta_y=1, lx=50, ly=50):
    for k in range(0, max_iter - 1, 1):
        for j in range(1, ly - 1, delta_y):
            for i in range(1, lx - 1, delta_x):
                u[k + 1, j, i] = (
                    gamma
                    * (
                        u[k][j][i + 1]
                        + u[k][j][i - 1]
                        + u[k][j + 1][i]
                        + u[k][j - 1][i]
                        - 4 * u[k][j][i]
                    )
                    + u[k][j][i]
                )

    return u
