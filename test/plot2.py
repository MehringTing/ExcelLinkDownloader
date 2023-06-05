import numpy as np
import pandas as pd

from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.size'] = 10
plt.rcParams['axes.unicode_minus'] = False


def group_bar_chart(df, x, y, title='', x_name='', y_name='', legend_position='best', fmt='%g'):
    fig, axs = plt.subplots(1, 2, sharey=True)

    labels = df[x]
    y1 = df[y[0]]
    y2 = df[y[1]]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    bar1 = axs[0].barh(x - width / 2, y1, width, label=y[0])
    bar2 = axs[0].barh(x + width / 2, y2, width, label=y[1])

    # Add some text for labels, title and custom x-axis tick labels, etc.
    axs[0].set_title(title)
    # axs[0].set_xticks(x, labels)
    axs[0].set_yticks(x, labels)
    axs[0].set_ylabel(y_name)
    axs[0].yaxis.tick_right()
    axs[0].legend(loc=legend_position)

    axs[0].bar_label(bar1, padding=3, fmt=fmt)
    axs[0].bar_label(bar2, padding=3, fmt=fmt)
    axs[0].invert_xaxis()

    bar1 = axs[1].barh(x - width / 2, y1, width, label=y[0])
    bar2 = axs[1].barh(x + width / 2, y2, width, label=y[1])

    # Add some text for labels, title and custom x-axis tick labels, etc.
    axs[1].set_title(title)
    # axs[0].set_xticks(x, labels)
    axs[1].set_yticks(x, labels)
    axs[1].legend(loc=legend_position)

    axs[1].bar_label(bar1, padding=3, fmt=fmt)
    axs[1].bar_label(bar2, padding=3, fmt=fmt)
    # axs[1].invert_xaxis()

    fig.subplots_adjust(wspace=0)
    fig.tight_layout()

    plt.show()


if __name__ == '__main__':
    data = {
        'year': ['营收', '总成本', '净利润', '经营现金流', '归母净利润'],
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
