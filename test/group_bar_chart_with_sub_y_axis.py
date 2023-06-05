import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.size'] = 10
plt.rcParams['axes.unicode_minus'] = False


def group_bar_chart(df=None, x=[], y=[]):
    # plt.rcdefaults()

    labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    men_means = [20, 34, 30, 35, 27]
    women_means = [25, 32, 34, 20, 25]

    x = np.arange(len(labels))  # the label locations
    print(x)
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, men_means, width, label='Men', color='green', alpha=0.7)
    rects2 = ax.bar(x + width / 2, women_means, width, label='Women', alpha=0.7)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Scores', color="r")
    ax.set_title('Scores by group and gender')
    ax.set_xticks(x, labels)
    ax.legend(loc='upper left')

    # ax.grid(color='#efefef', linestyle='--', linewidth=0.5)

    ax2 = ax.twinx()
    ax2.set_ylim(ymin=0, ymax=100)
    y2 = np.random.rand(len(labels)) * 80
    # ax2.plot(labels, np.random.rand(len(men_means)) * 100, 'r-')
    ax2.scatter(labels, y2, marker='o', c='r', alpha=.5)
    ax2.set_ylabel('目标完成率')
    for i in range(len(labels)):
        ax2.annotate('%.2f%%' % y2[i], xy=(labels[i], y2[i]), xytext=(labels[i], y2[i] + 1.5))
    ax2.legend(['目标完成率'])
    ax2.spines['right'].set_color('red')
    for label in ax2.yaxis.get_ticklabels():
        label.set_color('red')
        # label.set_rotation(45)
        # label.set_fontsize(16)
    # for line in ax2.yaxis.get_ticklines():
    #     line.set_color('red')
    #     line.set_markersize(3)

    ax2.tick_params(axis='y', colors="red", direction='inout')

    ax.bar_label(rects1, padding=3, fmt='%d万')
    # ax.bar_label(rects2, padding=3)
    for i in range(len(labels)):
        ax.text(i, women_means[i], s='%d\n(10.23%%)' % women_means[i], ha="left")

    fig.tight_layout()

    plt.show()


if __name__ == '__main__':
    group_bar_chart()
