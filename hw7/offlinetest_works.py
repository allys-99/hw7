#!/usr/bin/env python

import os
from plotly.offline import iplot, init_notebook_mode
import plotly as py
import plotly.graph_objs as go
import plotly.io as pio

init_notebook_mode(connected=True)

#trace1 =plot([go.Scatter(x=[1, 2, 3], y=[3, 1, 6])])


#layout = go.Layout(
#        title='Simple example',
#        yaxis=dict(
#            title='volts'
#        ),
#        xaxis=dict(
#            title='nanoseconds'
#        )
#)



trace1 = go.Scatter(x=[1, 2, 3], y=[3, 1, 6])



fig = go.Figure(data=[trace1])
iplot(fig)


if not os.path.exists('images1160'):
    os.mkdir('images1160')
pio.write_image(fig, 'images1160/fig1.png')
#fig = go.Figure(data=[trace1], layout=layout)
#py.offline.iplot(fig)

