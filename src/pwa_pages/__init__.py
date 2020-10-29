"""A collection of tools that can be used in the Jupyter notebooks."""

from typing import Callable, Optional, Sequence, SupportsFloat, Tuple

import matplotlib.pyplot as plt
import numpy as np


def plot(
    function: Callable[[SupportsFloat], Sequence[float]],
    plot_range: Tuple[float, float],  # pylint: disable=redefined-builtin
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
) -> None:
    x_1, x_2 = plot_range
    n_steps = 100
    x_values = np.linspace(x_1, x_2, n_steps)
    y_values = function(x_values)
    plt.plot(x_values, y_values)

    if title is not None:
        plt.title(title)
    if xlabel is not None:
        plt.xlabel(xlabel)
    if ylabel is not None:
        plt.ylabel(ylabel)
    plt.ylabel("$|M(E)|^2$")
