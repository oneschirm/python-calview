#Python CalView
#oneschirm.github.com
#inspired by D3's Calendar View - http://bl.ocks.org/mbostock/4063318
from pylab import *
from matplotlib.font_manager import FontProperties
import numpy as np
import calendar

class CalView(object):

    min_color = 'red'
    max_color = 'green'
    text_color = 'black'
    cell_color = '#F5F5F5'
    background_color = 'white'
    dpi = 300

    def __init__(self, import_data, import_label, import_type, import_abs):
        self.data= import_data
        self.all_years = self.determine_years()
        self.should_label = import_label
        self.split_at_median = import_type
        self.absolute = import_abs
        
    def determine_years(self):
        years = [item['year'] for item in self.data]
        unique_years = list(set(years))
        return unique_years

    def render(self):
        self.days = ['Sunday','Saturday','Friday','Thursday','Wednesday','Tuesday','Monday']
        self.index_starts = {'January':'','February':'','March':'','April':'','May':'','June':'','July':'' \
        ,'August':'','September':'','October':'','November':'','December':''}
        self.dates = []
        y_height = len(self.all_years)
        fig, ax = plt.subplots(y_height,1,figsize=(10,2*y_height))
        self.prep(fig, ax, y_height)
    
    def prep(self, fig, ax, y_height):
        plot_start = 0
        for ax_num, year in enumerate(self.all_years):
            print "year %s" % year
            if y_height>1:
                axis = ax[ax_num]
            else:
                axis = ax
            axis.set_aspect(1)
            for num, i in enumerate(range(1,13)):
                month= calendar.Calendar().monthdays2calendar(year, i)
                self.index_starts[self.get_month_name(num)] = plot_start
                day_count = 1
                for index, week in enumerate(month):
                    for item in week:
                        if item[0] != 0:
                            rect = plt.Rectangle([plot_start+index,self.get_real_number(item[1])],1,1, alpha = 0.5, color=self.cell_color)
                            if self.should_label == True:
                                axis.text(plot_start+index+.05,self.get_real_number(item[1])+.1, day_count, size=5, color=self.text_color)
                                day_count += 1
                            axis.add_patch(rect)
                            self.dates.append(rect)
                axis.text(plot_start+(len(month)/3.0),-1, self.get_month_name(num), size=8, color=self.text_color)
                plot_start += len(month)

            axis.set_yticks(np.arange(1,8)+0.5)
            axis.set_yticklabels(self.days, size=6, color=self.text_color)
            axis.set_xticks([])
            axis.set_frame_on(False)
            axis.autoscale_view()
            axis.tick_params(\
                axis='x',          # changes apply to the x-axis
                which='both',      # both major and minor ticks are affected
                bottom='off',      # ticks along the bottom edge are off
                top='off',         # ticks along the top edge are off
                labelbottom='on') # labels along the bottom edge are off
            axis.tick_params(\
                axis='y',          # changes apply to the x-axis
                which='both',      # both major and minor ticks are affected
                left='off',      # ticks along the bottom edge are off
                right='off',         # ticks along the top edge are off
                labelbottom='on') # labels along the bottom edge are off
            axis.text(0.47, 1.1, year,color=self.text_color, fontsize=18,transform=axis.transAxes,family='Verdana')
            self.plot_data(year)
            
    def max_value(self, year):
        if self.absolute == False:
            values = [x['value'] for x in self.data if x['year'] == year]
        else:
            values = [x['value'] for x in self.data]
        return np.max(np.array(values))
        
    def median_value(self, year):
        if self.absolute == False:
            values = [x['value'] for x in self.data if x['year'] == year]
        else:
            values = [x['value'] for x in self.data]
        return np.median(np.array(values))

    def plot_data(self, year):
        for item in self.data:
            specific_year = item['year']
            specific_month = item['month']
            specific_day = item['day']
            specific_value = item['value']
            if specific_year == year:
                month = calendar.Calendar().monthdays2calendar(specific_year, specific_month)
                for index, week in enumerate(month):
                    for item in week:
                        y = self.get_real_number(item[1])
                        if item[0] == specific_day:
                            x = self.index_starts[self.get_month_name(specific_month-1)] + index
                            for date in self.dates:
                                if x == date.get_x() and y == date.get_y():
                                    color, alpha = self.calculate_alpha(float(specific_value), year)
                                    date.set_color(color)
                                    date.set_alpha(alpha)
                                
    def calculate_alpha(self, specific_value, year):
        if self.split_at_median == False:
            alpha = float(specific_value)/float(self.max_value(year))
        elif self.split_at_median == True:
            alpha = (float(specific_value)-float(self.median_value(year)))/float(self.median_value(year))
        if alpha < 0:
            color = self.min_color
            alpha = -alpha
        elif alpha > 0:
            color = self.max_color
        if alpha > 1:
            alpha = 1
        elif alpha == 0:
            alpha = 0.01
            color = self.min_color      
        return color, alpha   
                                
    def show(self):
        show()
        
    def save(self, file_name):
        plt.savefig('%s.png' % file_name, facecolor=self.background_color,\
                    edgecolor='none', dpi=self.dpi, bbox_inches='tight')

    # this could be internationalized ie Jan. Feb. Maerz, April, Mai, Juni...
    def get_month_name(self,number):
        months = ['Jan.','Feb.','March','April','May','June','July','Aug.','Sept.','Oct.','Nov.','Dec.']
        return months[number]
    
    def get_real_number(self,number):
        if number == 0:
            return 7
        elif number == 1:
            return 6
        elif number == 2:
            return 5
        elif number == 3:
            return 4
        elif number == 4:
            return 3
        elif number == 5:
            return 2
        elif number == 6:
            return 1
        elif number == 7:
            return 0