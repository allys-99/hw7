#!/usr/bin/env python

import os
from plotly.offline import iplot, init_notebook_mode
import plotly as py
import plotly.graph_objs as go
import plotly.io as pio
import pandas as pd

init_notebook_mode(connected=True)



characteristics = ['cultivator','Alcohol', 'Malic Acid', 'Ash', 'Alcalinity of Ash',
        'Magnesium', 'Total Phenols', 'Flavanoids', 'Nonflavanoid Phenols',
        'Proanthocyanins', 'Colour Intensity', 'Hue',
        'OD280_OD315 of diluted wines', 'Proline']

def LoadDataSet():
    df = pd.read_table("wine.data.txt", delimiter=",",header=None)
    df.columns =['C','Alcohol','Malic Acid','Ash','Alcalinity of Ash',
            'Magnesium','Total Phenols','Flavanoids','Nonflavanoid Phenols',
            'Proanthocyanins','Colour Intensity','Hue','OD280_OD315 of diluted wines','Proline']
    return df

def PlotFeatures(df):
    c1 = df.loc[df['C'] == 1]
    c2 = df.loc[df['C'] == 2]
    c3 = df.loc[df['C'] == 3]
    if not os.path.exists('images1160'):
        os.mkdir('images1160')
    for idx in range(1,len(characteristics)):
        feat1 = characteristics[idx]
        c1feat1 = c1.loc[:,feat1]
        c2feat1 = c2.loc[:,feat1]
        c3feat1 = c3.loc[:,feat1]
        for jdx in range(idx+1, len(characteristics)):
            feat2 = characteristics[jdx]
            c1feat2 = c1.loc[:,feat2]
            c2feat2 = c2.loc[:,feat2]
            c3feat2 = c3.loc[:,feat2]
            trace1 = go.Scatter(x=c1feat1,y=c1feat2,mode = 'markers')
            trace2 = go.Scatter(x=c2feat1,y=c2feat2,mode = 'markers')
            trace3 = go.Scatter(x=c3feat1,y=c3feat2,mode = 'markers')

        #trace1 = go.Scatter(x=[1, 2, 3], y=[3, 1, 6])
        fig = go.Figure(data=[trace1,trace2,trace3])
        iplot(fig)
        filename = "images1160/"+feat1+"_"+feat2+".png"
        pio.write_image(fig, filename)
        exit()
        #fig = go.Figure(data=[trace1], layout=layout)
        #py.offline.iplot(fig)




def WineMain():
    myTable = LoadDataSet()
    PlotFeatures(myTable)



WineMain()

