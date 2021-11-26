import numpy as np

def bimodal(mu1,sigma1,mu2,sigma2,N):
    x = np.random.normal(mu1,sigma1,N//2)
    x = np.concatenate([x,np.random.normal(mu2,sigma2,N//2)])
    return x
