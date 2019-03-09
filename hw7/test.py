#!/usr/bin/env python

import plotly as plot
import plotly.graph_objs as go

plot([go.Scatter(x=[1, 2, 3], y=[3, 1, 6])])


#layout = go.Layout(
#        title='Simple example',
#        yaxis=dict(
#            title='volts'
#        ),
#        xaxis=dict(
#            title='nanoseconds'
#        )
#)



#trace1 = go.Scatter(x=[1, 2, 3], y=[3, 1, 6])



#fig = go.Figure(data=[trace1], layout=layout)
#py.offline.iplot(fig)

