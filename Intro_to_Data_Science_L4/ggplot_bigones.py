#in this python ggplot practice, we plot two big graphs from the date set turnstile_weather.
#As the requirements suggested, first we plot Date vs entries and then unit vs entries
#The third suggestion is pending to be comepleted. It should be based on the groupby unit, then divided into different time slot
#of each day.

from pandas import *
from ggplot import *

def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.  
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.  

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station (UNIT)
     * Which stations have more exits or entries at different times of day
       (You can use UNIT as a proxy for subway station.)

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
     
    To see all the columns and data points included in the turnstile_weather 
    dataframe. 
     
    However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''
    #group the entries numbers by date.
    grouped_date = turnstile_weather.groupby('DATEn')['ENTRIESn_hourly'].sum()
    #print grouped_date
    x_date = range(1,31)
    x_unit = range(1,466)
    #30 days and 552 units
    #plot of x=date, y=entries. theme is used to adjust x labels, ylim is the range of y
    #plot_date = ggplot(turnstile_weather, aes(x=xtest, y=turnstile_weather.groupby('DATEn')['ENTRIESn_hourly'].sum())) \
    #+geom_histogram(stat='identity')+ geom_point() + xlab('Date') + ylab('Entries')\
    #+scale_x_discrete(breaks=range(1,31),labels=turnstile_weather['DATEn'].unique())\
    #+theme(axis_text_x=element_text(angle=90,hjust=1, vjust=0.5, size=25)) +ylim(-100000,2500000)\
    
    #plot, with histogram type, x,y labeled, scale_x_discrete to make x axis into pieces and labeled with .unique values 
    #from all Date. Theme is used to adjust style of x labels
    grouped_unit = turnstile_weather.groupby('UNIT')['ENTRIESn_hourly'].sum()
    plot_unit = ggplot(turnstile_weather, aes(x=x_unit, y=turnstile_weather.groupby('UNIT')['ENTRIESn_hourly'].sum())) \
    +geom_histogram(stat='identity')+ geom_point() + xlab('Station') + ylab('Entries')\
    +scale_x_discrete(breaks=range(1,466),labels=turnstile_weather['DATEn'].unique())\
    +theme(axis_text_x=element_text(angle=90,hjust=1, vjust=0.5, size=25)) +ylim(-100000,1000000)\
    
    
    plot = plot_unit
    return plot
