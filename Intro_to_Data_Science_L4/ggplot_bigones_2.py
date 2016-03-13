'''
In this .py program, we select a subset of time and its correspondent number of entries to plot a graph.
One out of every 50 time is selected
'''
from pandas import *
from ggplot import *

def plot_weather_data(turnstile_weather):
    
    #select the columns from Time and number of entries per hour
    grouped_time_entry = turnstile_weather.groupby('TIMEn')['ENTRIESn_hourly'].sum()
    grouped_time_exit = turnstile_weather.groupby('TIMEn')['EXITSn_hourly'].sum()
    #make it a data frame
    df_time_entry = pandas.DataFrame(grouped_time_entry)
    
    #decide how many time I want to choose as a subset
    Step = 50
    NTime = (int)(len(grouped_time_entry)/Step)
    
    #initiate two empty lists
    groupedby5_value = []
    groupedby5_index = []
    i=1
    #fill the list with one out of every Step time data
    while i in range(NTime):
        #temp = pandas.Series(grouped_time_entry[i*5], index = [grouped_time_entry.index[i*5]])
        groupedby5_value.extend([grouped_time_entry[i*Step]])
        groupedby5_index.extend([grouped_time_entry.index[i*Step]])
        i += 1
    
    #combine the subset as a dataframe
    Grouped_df = pandas.DataFrame([groupedby5_index,groupedby5_value])
    Grouped_df = Grouped_df.transpose()
    Grouped_df.columns = ['Time','Entries']
    
    #plot
    x_time = range(1,NTime)
    plot = ggplot(aes(x=x_time, y='Entries'),data = Grouped_df) \
    +geom_line(color='blue')+ geom_point() + xlab('Time') + ylab('Entries')\
    +scale_x_discrete(breaks=range(1,NTime),labels=Grouped_df['Time'])\
    +theme(axis_text_x=element_text(angle=45,hjust=-20000000, vjust=0.5, size=5)) +ylim(0,2500)
    return plot
