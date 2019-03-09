
#!/usr/bin/env python

import plotly as py
import plotly.graph_objs as go
import ipywidgets as widgets
import numpy as np
from scipy import special

py.offline.init_notebook_mode(connected=True)

x = np.linspace(0,np.pi,1000)

layout = go.Layout(
        title='Simple example',
        yaxis=dict(
            title='volts'
        ),
        xaxis=dict(
            title='nanoseconds'
        )
)

trace1 = go.Scatter(
        x=x,
        y=np.sin(x),
        mode='lines',
        name='sin(x)',
        line=dict(
            shape='spline'
        )
)

fig = go.Figure(data=[trace1], layout=layout)
py.offline.iplot(fig)


