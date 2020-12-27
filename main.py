import statistics
import random
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff

df=pd.read_csv('data.csv')
data = df["reading_time"].tolist()
population_mean=statistics.mean(data)
print(population_mean)

def random_set_of_data(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def plot_graph(mean_list):
    df=mean_list
    fig=ff.create_distplot([df],['reading_time'],show_hist=False)
    fig.show()
    
    
def setup():
    mean_list=[] 
    for i in range(0,100):
        set_of_data=random_set_of_data(30)
        mean_list.append(set_of_data)
    plot_graph(mean_list)   
    print("sampling mean:- ", statistics.mean(mean_list))
setup() 


        
        