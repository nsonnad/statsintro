'''Calculate the sample size for experiments, for normally distributed groups, for:
- Experiments with one single group
- Comparing two groups

'''

'''
Author : Thomas Haslwanter
Date : May 2013
Ver : 1.1
'''

from scipy.stats import norm
from numpy import round
import numpy as np

def sampleSize_oneGroup(d, alpha=0.05, beta=0.2, sigma=1):
    '''Sample size for a single group.'''
    
    n = round((norm.ppf(1-alpha/2.) + norm.ppf(1-beta))**2 * sigma**2 / d**2)
    
    print(('In order to detect a change of {0} in a group with an SD of {1},'.format(d, sigma)))
    print(('with significance {0} and test-power {1}, you need at least {2:d} subjects.'.format(alpha, 100*(1-beta), int(n))))
    
    return n

def sampleSize_twoGroups(d, alpha=0.05, beta=0.2, sigma1=1, sigma2=1):
    '''Sample size for two groups.'''
    
    n = round((norm.ppf(1-alpha/2.) + norm.ppf(1-beta))**2 * (sigma1**2 + sigma2**2) / d**2)
    
    print(('In order to detect a change of {0} between groups with an SD of {1} and {2},'.format(d, sigma1, sigma2)))
    print(('with significance {0} and test-power {1}, you need in each group at least {2:d} subjects.'.format(alpha, 100*(1-beta), int(n))))
    
    return n

if __name__ == '__main__':
    sampleSize_oneGroup(0.5)
    print('\n')
    sampleSize_twoGroups(0.4, sigma1=0.6, sigma2=0.6)
    