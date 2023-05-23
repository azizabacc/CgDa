''' general example for fitting with kafe
      - read datafile fitexample.dat
      - perform fit (2nd orfer polynomial)
      - show and save output
'''

import kafe
from kafe.function_tools import FitFunction, LaTeX, ASCII
from kafe.function_library import quadratic_3par


# ---- fit function definition in kafe style
#         (decorators for nice output not mandatory)
@ASCII(expression='a * x^2 + b * x + c')
@LaTeX(name='f', parameter_names=('a', 'b', 'c'), expression=r'a\,x^2+b\,x+c')
@FitFunction
def poly2(x, a=1.0, b=0.0, c=0.0):
    return a * x**2 + b * x + c

# ---- begin of fit ---
# set the function
fitf = poly2             # own definition
# fitf = quadratic_3par  # or from kafe function library
# --------- begin of workflow ----------------------
# set data
xm = [0.05, 0.36, 0.68, 0.80, 1.09, 1.46, 1.71, 1.83, 2.44, 2.09, 3.72, 4.36, 4.60]
ym = [0.35, 0.26, 0.52, 0.44, 0.48, 0.55, 0.66, 0.48, 0.75, 0.70, 0.75, 0.80, 0.90]
ye = [0.06, 0.07, 0.05, 0.05, 0.07, 0.07, 0.09, 0.1, 0.11, 0.1, 0.11, 0.12, 0.1]
#
kdata = kafe.Dataset(data=(xm, ym), basename='kData',
                     title='example data')
kdata.add_error_source('y', 'simple', ye)
kfit = kafe.Fit(kdata, fitf)  # create the fit
kfit.do_fit()               # perform fit
kplot = kafe.Plot(kfit)     # create plot object
kplot.axis_labels = [r'$St\"utzstellen \, x $', r'$data\,\&\,f(x)$']
kplot.plot_all()            # make plots
kfit.plot_correlations()    # eventually, produce contour plots
kplot.show()                # Show the plots

