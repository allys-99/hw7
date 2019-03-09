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
            for kdx in range(jdx+1, len(characteristics)):
                feat3 = characteristics[kdx]
                c1feat3 = c1.loc[:,feat3]
                c2feat3 = c2.loc[:,feat3]
                c3feat3 = c3.loc[:,feat3]
                for ldx in range(kdx+1, len(characteristics)):
                    feat4 = characteristics[ldx]
                    c1feat4 = c1.loc[:,feat4]
                    c2feat4 = c2.loc[:,feat4]
                    c3feat4 = c3.loc[:,feat4]
                    for mdx in range(ldx+1, len(characteristics)):
                        feat5 = characteristics[mdx]
                        c1feat5 = c1.loc[:,feat5]
                        c2feat5 = c2.loc[:,feat5]
                        c3feat5 = c3.loc[:,feat5]
                        layout = go.Layout(
                            width=1600,
                            height=1200,
                            #margin=go.layout.Margin(
                            #    l=10,r=10,b=40,t=40,pad=40
                            #    ),
                            title = feat1 + " - " + feat2 + " - " + feat3 + " - " + feat4 + " - " + feat5,
                            xaxis=dict(
                                showgrid=True,
                                gridwidth=1,
                                title=feat1+","+feat2+","+feat3+","+feat4
                                #tick0=0,
                                #dtick=20
                                #tickvals=[0,2,4,6,8,10,12,14,16,18,20,22,24,26]
                                ),
                            yaxis=dict(
                                showgrid=True,
                                rangemode='tozero',
                                gridwidth=1,
                                title=feat2+","+feat3+","+feat4+","+feat5
                                #tick0=0,
                                #dtick=10
                                #tickvals=[0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]
                                )
                        )
                        trace1 = go.Scatter(x=c1feat1,y=c1feat2,mode = 'markers',name='c1, '+feat1+', '+feat2, marker={'symbol': 104, 'size': 8,'color':'#0000ff'})
                        trace2 = go.Scatter(x=c2feat1,y=c2feat2,mode = 'markers',name='c2, '+feat1+', '+feat2, marker={'symbol': 1, 'size': 8,'color':'#0000ff'})
                        trace3 = go.Scatter(x=c3feat1,y=c3feat2,mode = 'markers',name='c3, '+feat1+', '+feat2, marker={'symbol': 'star', 'size': 8,'color':'#0000ff'})

                        trace4 = go.Scatter(x=c1feat1,y=c1feat3,mode = 'markers',name='c1, '+feat1+', '+feat3, marker={'symbol': 104, 'size': 8,'color':'#ff2800'})
                        trace5 = go.Scatter(x=c2feat1,y=c2feat3,mode = 'markers',name='c2, '+feat1+', '+feat3, marker={'symbol': 1, 'size': 8,'color':'#ff2800'})
                        trace6 = go.Scatter(x=c3feat1,y=c3feat3,mode = 'markers',name='c3, '+feat1+', '+feat3, marker={'symbol': 'star', 'size': 8,'color':'#ff2800'})

                        trace7 = go.Scatter(x=c1feat1,y=c1feat4,mode = 'markers',name='c1, '+feat1+', '+feat4, marker={'symbol': 104, 'size': 8,'color':'#71bc78'})
                        trace8 = go.Scatter(x=c2feat1,y=c2feat4,mode = 'markers',name='c2, '+feat1+', '+feat4, marker={'symbol': 1, 'size': 8,'color':'#71bc78'})
                        trace9 = go.Scatter(x=c3feat1,y=c3feat4,mode = 'markers',name='c3, '+feat1+', '+feat4, marker={'symbol': 'star', 'size': 8,'color':'#71bc78'})

                        trace10 = go.Scatter(x=c1feat1,y=c1feat5,mode = 'markers',name='c1, '+feat1+', '+feat5, marker={'symbol': 104, 'size': 8,'color':'#ffbf00'})
                        trace11 = go.Scatter(x=c2feat1,y=c2feat5,mode = 'markers',name='c2, '+feat1+', '+feat5, marker={'symbol': 1, 'size': 8,'color':'#ffbf00'})
                        trace12 = go.Scatter(x=c3feat1,y=c3feat5,mode = 'markers',name='c3, '+feat1+', '+feat5, marker={'symbol': 'star', 'size': 8,'color':'#ffbf00'})


                        trace13 = go.Scatter(x=c1feat2,y=c1feat3,mode = 'markers',name='c1, '+feat2+', '+feat3, marker={'symbol': 104, 'size': 8,'color':'#ff1493'})
                        trace14 = go.Scatter(x=c2feat2,y=c2feat3,mode = 'markers',name='c2, '+feat2+', '+feat3, marker={'symbol': 1, 'size': 8,'color':'#ff1493'})
                        trace15 = go.Scatter(x=c3feat2,y=c3feat3,mode = 'markers',name='c3, '+feat2+', '+feat3, marker={'symbol': 'star', 'size': 8,'color':'#ff1493'})

                        trace16 = go.Scatter(x=c1feat2,y=c1feat4,mode = 'markers',name='c1, '+feat2+', '+feat4, marker={'symbol': 104, 'size': 8,'color':'#ccff00'})
                        trace17 = go.Scatter(x=c2feat2,y=c2feat4,mode = 'markers',name='c2, '+feat2+', '+feat4, marker={'symbol': 1, 'size': 8,'color':'#ccff00'})
                        trace18 = go.Scatter(x=c3feat2,y=c3feat4,mode = 'markers',name='c3, '+feat2+', '+feat4, marker={'symbol': 'star', 'size': 8,'color':'#ccff00'})

                        trace19 = go.Scatter(x=c1feat2,y=c1feat5,mode = 'markers',name='c1, '+feat2+', '+feat5, marker={'symbol': 104, 'size': 8,'color':'#ff00ff'})
                        trace20 = go.Scatter(x=c2feat2,y=c2feat5,mode = 'markers',name='c2, '+feat2+', '+feat5, marker={'symbol': 1, 'size': 8,'color':'#ff00ff'})
                        trace21 = go.Scatter(x=c3feat2,y=c3feat5,mode = 'markers',name='c3, '+feat2+', '+feat5, marker={'symbol': 'star', 'size': 8,'color':'#ff00ff'})


                        trace22 = go.Scatter(x=c1feat3,y=c1feat4,mode = 'markers',name='c1, '+feat3+', '+feat4, marker={'symbol': 104, 'size': 8,'color':'#a52a2a'})
                        trace23 = go.Scatter(x=c2feat3,y=c2feat4,mode = 'markers',name='c2, '+feat3+', '+feat4, marker={'symbol': 1, 'size': 8,'color':'#a52a2a'})
                        trace24 = go.Scatter(x=c3feat3,y=c3feat4,mode = 'markers',name='c3, '+feat3+', '+feat4, marker={'symbol': 'star', 'size': 8,'color':'#a52a2a'})

                        trace25 = go.Scatter(x=c1feat3,y=c1feat5,mode = 'markers',name='c1, '+feat3+', '+feat5, marker={'symbol': 104, 'size': 8,'color':'#738678'})
                        trace26 = go.Scatter(x=c2feat3,y=c2feat5,mode = 'markers',name='c2, '+feat3+', '+feat5, marker={'symbol': 1, 'size': 8,'color':'#738678'})
                        trace27 = go.Scatter(x=c3feat3,y=c3feat5,mode = 'markers',name='c3, '+feat3+', '+feat5, marker={'symbol': 'star', 'size': 8,'color':'#738678'})

                        trace28 = go.Scatter(x=c1feat4,y=c1feat5,mode = 'markers',name='c1, '+feat4+', '+feat5, marker={'symbol': 104, 'size': 8,'color':'#a020f0'})
                        trace29 = go.Scatter(x=c2feat4,y=c2feat5,mode = 'markers',name='c2, '+feat4+', '+feat5, marker={'symbol': 1, 'size': 8,'color':'#a020f0'})
                        trace30 = go.Scatter(x=c3feat4,y=c3feat5,mode = 'markers',name='c3, '+feat4+', '+feat5, marker={'symbol': 'star', 'size': 8,'color':'#a020f0'})

                        data = [trace1,trace2,trace3,trace4,trace5,trace6,trace7,trace8,trace9,trace10,trace11,trace12,trace13,trace14,trace15,
                                trace16,trace17,trace18,trace19,trace20,trace21,trace22,trace23,trace24,trace25,trace26,trace27,trace28,trace29,trace30]

                        fig = go.Figure(data=data,layout=layout)
                        iplot(fig)
                        filename = "images1160/"+feat1+"_"+feat2+"_"+feat3+"_"+feat4+"_"+feat5+".png"
                        pio.write_image(fig, filename)


def WineMain():
    myTable = LoadDataSet()
    PlotFeatures(myTable)



WineMain()

