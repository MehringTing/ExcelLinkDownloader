import numpy as np
import pandas as pd

from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.size'] = 10
plt.rcParams['axes.unicode_minus'] = False


def line_chart(df, x, y, title='', x_name='', y_name='', legend_position='best', fmt='%g', wh=(8, 8)):
    fig, ax = plt.subplots(1, 1, figsize=wh)

    labels = df[x]
    y1 = df[y[0]]
    y2 = df[y[1]]

    x = np.arange(len(labels))  # the label locations

    ax.plot(x, y1, label=y[0])
    ax.plot(x, y2, label=y[1])

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_title(title)
    ax.set_xticks(x, labels)
    ax.set_ylabel(y_name)
    ax.legend(loc=legend_position, framealpha=0.5)

    # ax.grid(True, linestyle='-.', linewidth=0.5, color='#dfdfdf')

    fig.tight_layout()

    plt.show()


if __name__ == '__main__':
    data = {
        'year': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        'men': [20, 34, 30, 35, 27, 23, 45, 22, 43, 12, 33, 15],
        'women': [25, 32, 34, 20, 25, 23, 54, None, None, None, None,None],
    }

    df = pd.DataFrame(data)
    # print(df.columns)
    # cols = list(df.columns)[1:]
    # print(cols)
    # cols.reverse()
    # print(cols)
    # print(df)
    line_chart(df, 'year', ['men', 'women'], title='图标一', y_name='万元')
