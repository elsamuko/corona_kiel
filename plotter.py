#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import datetime


def plot(data):
    ages = len(data)
    weeks = len(data[0])

    fig = plt.figure(figsize=(15, 10))
    ax = fig.add_subplot()
    im = ax.matshow(data, cmap='rainbow')
    fig.colorbar(im, shrink=0.4)

    age_labels = [str(5+5*x) for x in range(ages)]
    age_labels[-1] = "80+"
    ax.tick_params(axis="y", left=True, right=True,
                   labelright=True, labelleft=True)
    ax.set_yticks(np.arange(ages))
    ax.set_yticklabels(age_labels)

    _, week, _ = datetime.date.today().isocalendar()
    week_labels = [str(1+(53+x-weeks+week) % 53) for x in range(weeks)]
    ax.tick_params(axis="x", top=True, labeltop=True)
    ax.set_xticks(np.arange(weeks))
    ax.set_xticklabels(week_labels)

    plt.savefig("plot.png")


if __name__ == "__main__":
    data = np.random.random((18, 50))
    plot(data)
