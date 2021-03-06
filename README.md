Make [D3 Calendar Views](http://bl.ocks.org/mbostock/4063318) in python.

![Python Execution](https://raw.github.com/oneschirm/python-calview/master/redeye_data_nodates.png)

Data must be supplied in this format:
<pre>data = [{'year':2013,'month':11,'day':05, 'value':412}
{'year':2013,'month':11,'day':06, 'value':221}]
</pre>

Data must not contain duplicate dates, as they will be overwritten. 

Usage can be as simple as this: 

<pre>import pycalview 
calendar = pycalview.CalView(data, True, False, True)
calendar.render()
calendar.save('default settings')</pre>

or as complex as this:

<pre>import pycalview
calendar = pycalview.CalView(data, False, False, True)
calendar.min_color = 'blue'
calendar.max_color = 'red'
calendar.cell_color = '#F5F5F5'
calendar.text_color = 'black'
calendar.background_color = 'white'
calendar.render()
calendar.save('temperatures')</pre>

In the line `calendar = pycalview.CalView(data, True, False, True)`, you're passing the following arguments:
- Data (in the format specified above)
- A boolean that tells the class whether or not to draw individual days in the calendar cells. (True == display days)
- A boolean that tells the class whether to use the median (good for values) or the max(good for frequency) to determine the cells' alphas. (True == Use median)
- A boolean that tells the class whether to calculate the alpha for each year in isolation or all together. (True == Same scale for all)

Other easily-customizable fields are:
- min_color
- max_color
- text_color 
- cell_color
- background_color
- dpi = 300

Check out demo.py for a working example of this tool. The output looks like this:
![Python Execution](https://raw.github.com/oneschirm/python-calview/master/SNSTKHLM_temp.png)

###Dependencies
[matplotlib](http://matplotlib.org/)

[numpy](http://www.numpy.org/)

### Sample Data Source
[Redeye Chicago](http://homicides.redeyechicago.com/)

[Sverige](http://academic.udayton.edu/kissock/http/Weather/gsod95-current/SNSTKHLM.txt)