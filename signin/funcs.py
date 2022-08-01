import io, base64
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

def LinearFunction():
    x = np.linspace(-5,5,100)
    y = 2*x+1
    # Generate plot, setting the axes at the centre
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.spines['left'].set_position('center')
    axis.spines['bottom'].set_position('zero')
    axis.spines['right'].set_color('none')
    axis.spines['top'].set_color('none')
    axis.xaxis.set_ticks_position('bottom')
    axis.yaxis.set_ticks_position('left')
    axis.legend(loc='upper left')
    axis.grid()
    axis.plot(x, y,'b', label='y=2x+5')

    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)

    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

    return pngImageB64String

def QuadraticEquation():
    x = np.linspace(-5,5,100)
    y = x**2
    # Generate plot
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.spines['left'].set_position('center')
    axis.spines['bottom'].set_position('zero')
    axis.spines['right'].set_color('none')
    axis.spines['top'].set_color('none')
    axis.xaxis.set_ticks_position('bottom')
    axis.yaxis.set_ticks_position('left')
    axis.grid()
    axis.plot(x, y,'b', label='X^2')
    axis.legend(loc='upper left')

    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)

    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

    return pngImageB64String


def CubicEquation():
    # 100 linearly spaced numbers
    x = np.linspace(-5,5,100)
    # the function, which is y = x^3 here
    y = x**3
    # Generate plot
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.spines['left'].set_position('center')
    axis.spines['bottom'].set_position('zero')
    axis.spines['right'].set_color('none')
    axis.spines['top'].set_color('none')
    axis.xaxis.set_ticks_position('bottom')
    axis.yaxis.set_ticks_position('left')
    axis.grid()
    axis.plot(x, y,'b', label='X^3')
    axis.legend(loc='upper left')

    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)

    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

    return pngImageB64String

def SinEquation():
    # 100 linearly spaced numbers
    x = np.linspace(-np.pi,np.pi,100)
    # the function, which is y = sin(x) here
    y = np.sin(x)
    # Generate plot
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.spines['left'].set_position('center')
    axis.spines['bottom'].set_position('zero')
    axis.spines['right'].set_color('none')
    axis.spines['top'].set_color('none')
    axis.xaxis.set_ticks_position('bottom')
    axis.yaxis.set_ticks_position('left')
    axis.grid()
    axis.plot(x, y,'b', label='sin(x)')
    axis.legend(loc='upper left')

    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)

    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

    return pngImageB64String

def CosEquation():
    # 100 linearly spaced numbers
    x = np.linspace(-np.pi,np.pi,100)
    # the function, which is y = sin(x) here
    y = np.cos(x)
    # Generate plot
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.spines['left'].set_position('center')
    axis.spines['bottom'].set_position('zero')
    axis.spines['right'].set_color('none')
    axis.spines['top'].set_color('none')
    axis.xaxis.set_ticks_position('bottom')
    axis.yaxis.set_ticks_position('left')
    axis.grid()
    axis.plot(x, y,'b', label='cos(x)')
    axis.legend(loc='upper left')

    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)

    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

    return pngImageB64String

def ExpEquation():
    # 100 linearly spaced numbers
    x = np.linspace(-2,2,100)
    # the function, which is y = sin(x) here
    y = np.exp(x)
    # Generate plot
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.spines['left'].set_position('center')
    axis.spines['bottom'].set_position('zero')
    axis.spines['right'].set_color('none')
    axis.spines['top'].set_color('none')
    axis.xaxis.set_ticks_position('bottom')
    axis.yaxis.set_ticks_position('left')
    axis.grid()
    axis.plot(x, y,'b', label='cos(x)')
    axis.legend(loc='upper left')

    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)

    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

    return pngImageB64String