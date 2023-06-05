import numpy as np
import pandas as pd

from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.size'] = 10
plt.rcParams['axes.unicode_minus'] = False


def group_bar_chart(df, x, y, title='', x_name='', y_name='', legend_position='best', fmt='%g'):
    fig, ax = plt.subplots()

    labels = df[x]
    y1 = df[y[0]]
    y2 = df[y[1]]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    bar1 = ax.bar(x - width / 2, y1, width, label=y[0], color='green', alpha=0.7)
    bar2 = ax.bar(x + width / 2, y2, width, label=y[1], alpha=0.7)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_title(title)
    ax.set_xticks(x, labels)
    ax.set_ylabel(y_name)
    ax.legend(loc=legend_position)

    ax.bar_label(bar1, padding=3, fmt=fmt)
    ax.bar_label(bar2, padding=3, fmt=fmt)

    fig.tight_layout()

    plt.show()


if __name__ == '__main__':
    data = {
        'year': [2018, 2019, 2020, 2021, 2022],
        'men': [20, 34, 30, 35, 27],
        'women': [25, 32, 34, 20, 25],
    }
    df = pd.DataFrame(data)
    print(df)
    print(df.iloc[:, 1])
    df.iloc[:, 1] = df.iloc[:, 1].astype('float')
    print(df.dtypes)
    print(df.info)
    # print(df.columns)
    # cols = list(df.columns)[1:]
    # print(cols)
    # cols.reverse()
    # print(cols)
    # print(df)
    group_bar_chart(df, 'year', ['men', 'women'], title='图标一', y_name='万元')
