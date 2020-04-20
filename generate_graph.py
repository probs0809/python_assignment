import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def generate_male_female_statewise_graph(df,path):
    fig,ax= plt.subplots(figsize=(8,22),ncols=3,nrows=10)
    fig.tight_layout(pad = 4.0)
    stateList = df['detectedstate'].unique()
    gen_count = lambda g,sc : len(df[df['detectedstate']==sc][df['gender']==g])
    for i, a in enumerate(ax.flatten()):
        sc = stateList[i]
        a.pie([gen_count('M',sc),gen_count('F',sc)],radius = (gen_count('M',sc)+ gen_count('F',sc) + gen_count('UK',sc))**0.08,labels = ['Male','Female'], autopct='%1.2f%%')
        a.set_title(sc)   
    plt.title('Statewise gender report of covid 19') 
    plt.savefig(path)
    plt.clf()

def generate_statewise_death_recovery_graph(df,path):
    fig,ax = plt.subplots(figsize=(10,8))
    statecodes = df['statecode'].unique()
    gen_len = lambda g : [len(df[df['statecode']==sc][df['currentstatus']==g]) for sc in statecodes]
    ypos = np.arange(len(statecodes))
    plt.bar(ypos-0.20,np.array(gen_len('Recovered')),color = 'g',width=0.40)
    plt.bar(ypos+0.20,np.array(gen_len('Deceased')), color = 'r',width=0.40)
    plt.legend(['Recovered','Decased'])
    plt.title('Statewise Recovered and deceased report of covid 19')
    plt.xticks(ypos,statecodes)
    plt.xlabel("States")
    plt.ylabel("count")
    plt.savefig(path)
    plt.clf()

def generate_death_recovery_total_plot(df,path):
    fig,ax = plt.subplots(figsize=(20,10))
    statecodes = df['statecode'].unique()
    gen_len = lambda g : [len(df[df['statecode']==sc][df['currentstatus']==g]) for sc in statecodes]
    ypos = np.arange(len(statecodes))
    totalCount = np.array(gen_len('Recovered'))+np.array(gen_len('Deceased'))+np.array(gen_len('Hospitalized')) 
    recovered = np.array(gen_len('Recovered'))
    deceased = np.array(gen_len('Deceased'))
    stateList = df['detectedstate'].unique()
    x = (recovered/totalCount)*100
    y = (deceased/totalCount)*100
    size = (totalCount/totalCount.sum())*100
    plt.scatter(x,y,s=size*1000,c = size,alpha=0.2,cmap='viridis')
   
    for i,a,b in zip(stateList,x,y):
        plt.annotate(i, 
                 (a,b), 
                 textcoords="offset points", 
                 xytext=(0,0), 
                 ha='center') 

    plt.title('Statewise Recovery rate and deceased rate report of covid-19 based on total cases',fontsize=30)
    plt.xlabel("Recovery Rate",fontsize=20)
    plt.ylabel("Deceased Rate",fontsize = 20)
    plt.savefig(path)
    plt.clf()