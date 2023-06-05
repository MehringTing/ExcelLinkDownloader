import pandas as pd
from pyquery import PyQuery as pq

file='../report.xlsx'

df = pd.read_excel(file, sheet_name='总体经营指标完成情况', skiprows=2,)
html = df.to_html(index=False)
# print(df)
# print(df.loc[0])
# print(html)

pq_doc = pq(html)
th_row1 = pq(pq_doc('thead').html())
pq_doc('th:contains("Unnamed")').remove()
pq_doc('tbody tr:first').append_to(pq_doc('thead'))
pq_doc('thead tr:first th').attr('colspan', '5')
pq_doc('thead tr:first').prepend(pq_doc('thead tr:last td:first'))
pq_doc('thead tr:first td:first').attr('rowspan', '2')
print(pq_doc)
th_row1.find('th').attr('colspan', '5')
pq_tr_row1 = pq_doc('tbody > tr:first')
cell1 = pq_tr_row1('td:first').attr('rowspan', '2')
# print(cell1)

# th_row1.prepend(cell1)
# print(th_row1+pq_tr_row1)
# print(pq_doc('thead').html(th_row1 + pq_tr_row1))
# pq_doc('tbody > tr:first').remove()
# print(pq_doc)

# th_row1.append(pq_tr_row1.find('td:first'))
# print(pq_tr_row1)
# print(doc('tbody > tr:first'))
# doc('thead').html(doc('tbody > tr:first'))
# print(doc)


def a():
    x = 10

    def b(y):
        return y + 10

    print(b(10))


a()