import pycalview
import time

data = []
file = open('SNSTKHLM.txt', 'rb')
for row in file:
    row = row.replace('\n', '').replace('\r', ' ')
    line_item = []
    last = ''
    for char in row:
        if char is not ' ':
            last = '%s%s' % (last, char)
        else:
            if last is not '':
                line_item.append(last)
            last = ''
    data.append({'year': int(line_item[2]), 'month': int(line_item[0]), 'day':int(line_item[1]), 'value':float(line_item[3])})

calendar = pycalview.CalView(data, True, True, True)
calendar.max_color = '#FFFF66'
calendar.min_color = '#3399FF'
calendar.cell_color = '#F5F5F5'
calendar.text_color = 'white'
calendar.background_color = 'black'
calendar.render()
calendar.save('SNSTKHLM_temp')