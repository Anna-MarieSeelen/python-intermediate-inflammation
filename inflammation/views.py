"""Module containing code for plotting inflammation data."""

from matplotlib import pyplot as plt
import numpy as np


def visualize(data_dict):
    """Display plots of basic statistical properties of the inflammation data.

    :param data_dict: Dictionary of name -> data to plot
    """
    # TODO(lesson-design) Extend to allow saving figure to file

    num_plots = len(data_dict)
    fig = plt.figure(figsize=((3 * num_plots) + 1, 3.0))

    for i, (name, data) in enumerate(data_dict.items()):
        axes = fig.add_subplot(1, num_plots, i + 1)

        axes.set_ylabel(name)
        axes.plot(data)

    fig.tight_layout()

    plt.show()

def make_line_graph_daily_sd(daily_sd):
    """Display lineplot of daily sd

    :param daily_sd: np array with daily s.d.
    """
    # define data values
    x = np.arange(len(daily_sd))
    y = daily_sd  # Y-axis points

    plt.plot(x, y)  # Plot the chart
    plt.show()  # display