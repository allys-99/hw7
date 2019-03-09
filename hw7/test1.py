#!/usr/bin/env python

import plotly
import plotly.plotly as py
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np

plotly.tools.set_credentials_file(username='allys_99', api_key='lmcalra_Aug99')

N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers'
)


data = [trace]

# Plot and embed in ipython notebook!
py.iplot(data, filename='basic-scatter')

# or plot with: plot_url = py.plot(data, filename='basic-line')
