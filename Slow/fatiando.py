
# coding: utf-8

# In[ ]:


def seismic_wiggle(section, dt=0.004, ranges=None, scale=1.,
                   color='k', normalize=False):
    """
    Plot a seismic section (numpy 2D array matrix) as wiggles.

    Parameters:

    * section :  2D array
        matrix of traces (first dimension time, second dimension traces)
    * dt : float
        sample rate in seconds (default 4 ms)
    * ranges : (x1, x2)
        min and max horizontal values (default trace number)
    * scale : float
        scale factor multiplied by the section values before plotting
    * color : tuple of strings
        Color for filling the wiggle, positive  and negative lobes.
    * normalize :
        True to normalizes each trace in the section using individual trace max/min
        data will be in the range (-0.5, 0.5) zero centered

    .. warning::
        Slow for more than 200 traces, in this case decimate your
        data or use ``seismic_image``.

    """
    import numpy as numpy
    import matplotlib.pyplot as pyplot
    npts, ntraces = section.shape  # time/traces
    if ntraces < 1:
        raise IndexError("Nothing to plot")
    if npts < 1:
        raise IndexError("Nothing to plot")
    t = numpy.linspace(0, dt*npts, npts)
    amp = 1.  # normalization factor
    gmin = 0.  # global minimum
    toffset = 0.  # offset in time to make 0 centered
#     if normalize:
#         gmax = section.max()
#         gmin = section.min()
#         amp = (gmax-gmin)
#         toffset = 0.5
    pyplot.ylim(max(t), 0)
    if ranges is None:
        ranges = (0, ntraces)
    x0, x1 = ranges
    # horizontal increment
    dx = float((x1-x0)/ntraces)
    pyplot.xlim(x0, x1)
    for i, trace in enumerate(section.transpose()):
        if normalize:
            gmax = max(trace.min(), trace.max(), key=abs)
            gmin = trace.min()
            amp=abs(gmax-gmin)
            if (amp==0): 
                if (gmax == 0): amp=1
                else: amp=abs(gmax)
            toffset = 0.05
        # tr = (((trace-gmin)/amp)-toffset)*scale*dx
        tr = ((trace/amp)-toffset)*scale*dx
        x = x0+float(i)*dx  # x positon for this trace
        pyplot.plot(x+tr, t, 'k')
        #pyplot.fill_betweenx(t, x+tr, x, tr > 0, color=color)
        pyplot.fill_betweenx(t, x+tr, x, tr>0 , color=color)

