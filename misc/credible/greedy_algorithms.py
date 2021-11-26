import numpy as np

def greedy_credible_1D(x,bins=50,level=0.68):
    """
    Compute a 1D credible interval using a greedy binning algorithm.

    Parameters:
    - x: 1D array of parameter samples
    - bins: array of bin edges, or number of equally spaced bins
    - level: the desired credible level`

    Returns:
    - c_edges: the edges of the credible interval (an even number)
    """
    # create histogram f x
    h,edges = np.histogram(x,bins=bins)

    # create sorting index
    s = np.argsort(h)
    # create cumulative sum (normalized)
    csum = np.zeros_like(h)
    csum[s]=np.cumsum(h[s])
    csum=csum/csum.max()

    # compute credible range edges
    return edges,csum>=(1.-level)
