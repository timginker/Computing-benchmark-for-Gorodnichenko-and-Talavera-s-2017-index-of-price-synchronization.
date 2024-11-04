# Computing benchmark for Gorodnichenko and Talavera's (2017) index of price synchronization.

In the following code snippet, we demonstrate our method of computing the benchmark for Gorodnichenko and Talavera's (2017) index of price synchronization under the null hypothesis of no coordination (i.e. independence) between the stores. We calculate the benchmark as follows. We use the fact that the index represents a scaled sum of binary variables indicating the price change of good $i$ at time $t$ in a store $s$. Thus, under the null hypothesis of no coordination, the expectation of the index is completely characterized by the probability of a price change for each good in each store, which can be proxied by the associated frequencies. 

When the number of stores is small, calculating the benchmark is straightforward and can be done analytically. For example, consider a scenario with only three stores. Let’s assume (w.l.o.g.) that the probabilities of price change for some product in a store $j$ ($j=1,2,3$) are given by $p_{1}=0.1, p_{2}=0.2, p_{3}=0.3$. In this case, the benchmark can be computed as follows:


```python
%config Completer.use_jedi = False
import numpy as np
```


```python
p1=0.1 # probability of a price change in store 1
p2=0.2 # probability of a price change in store 2
p3=0.3 # probability of a price change in store 3

ps0=(p1*(1-p2)*(1-p3)+p2*(1-p1)*(1-p3)+p3*(1-p1)*(1-p2))/(1-(1-p1)*(1-p2)*(1-p3)) # conditional probability of a single price change conditional on at least one price change  (the index takes the value of 0)
ps12=(p1*p2*(1-p3)+p1*p3*(1-p2)+p3*p2*(1-p1))/(1-(1-p1)*(1-p2)*(1-p3)) # conditional probability of a price change in two stores at the same time conditional on at least one price change (the index takes the value of 0.5)
ps1=(p1*p2*p3)/(1-(1-p1)*(1-p2)*(1-p3)) # conditional probability of a price change in all stores at the same time conditional on at least one price change (the index takes the value of 1)

# Conditional expectation of the index at time t
E_st=0.5*(p1*p2*(1-p3)+p1*p3*(1-p2)+p3*p2*(1-p1))/(1-(1-p1)*(1-p2)*(1-p3))+(p1*p2*p3)/(1-(1-p1)*(1-p2)*(1-p3)) 

print("Benchmark value of Gorodnichenko and Talavera's (2017) index={}".format(np.round(E_st,3)))
```

    Benchmark value of Gorodnichenko and Talavera's (2017) index=0.105
    

We can also compute the benchmark numerically using the following function:


```python
def benchmark(p,rep,n,seed=123456):
    """
    This function computes  the benchmark for Gorodnichenko and Talavera's (2017) index of price 
    synchronization under the null hypothesis of no coordination (i.e. independence) between the stores.
    
    Arguments:
    
    p - list of probabilities of price change in store j
    rep - number of replications
    n - length of the simulated sample
    seed - random seed, set to 123456 by default
    
    Value:
    
    The benchmark value
    
    """
    
    import numpy as np
    
    np.random.seed(seed=seed)
    
    S=[]

    for r in range(rep):
    
        # sampling binary indicators of a price change
    
        D=[]
    
        for i in range(len(p)):
            D.append(np.random.binomial(n=1,p=p[i],size=n))
    
        # computing the price synchronization index
    
        S_t=(np.concatenate([D],axis=1).T.sum(axis=1)-1)/(len(p)-1) #  Gorodnichenko and Talavera's (2017) index over time
    
        S.append(np.mean(S_t[S_t>=0])) # computing conditional mean
        
    return np.mean(S)
    
```


```python
print("Benchmark value of Gorodnichenko and Talavera's (2017) index={}".format(np.round(benchmark(p=[0.1,0.2,0.3],
                                                                                                  n=1000,rep=1000),3)))
```

    Benchmark value of Gorodnichenko and Talavera's (2017) index=0.105
    

As we can observe, the numerical estimate is reasonably accurate. Moreover, when dealing with a large number of stores, analytical computation of the benchmark becomes challenging, making numerical methods particularly useful.

The function’s arguments can be easily adjusted to provide numerical estimates for any number of stores and looped over different products, as demonstrated in the code snippet below:


```python
p=np.full((10, ), 0.1) # ten stores with equal probability of price change
print("Benchmark value of Gorodnichenko and Talavera's (2017) index={}".format(np.round(benchmark(p=p,
                                                                                                  n=1000,rep=1000),3)))
```

    Benchmark value of Gorodnichenko and Talavera's (2017) index=0.059


# References

GInker, T., Ilek, A., and Snir, A. (2024), “Rigidity and Synchronization: Analyzing Online and Offline Price Dynamics”. [paper link](http://dx.doi.org/10.13140/RG.2.2.35045.20962)

Gorodnichenko, Y. and O. Talavera (2017), “Price Setting in Online Markets,” American Economic Review 107(1), 249–282.


# Disclamer 

The views expressed here are solely of the author and do not necessarily represent the views of the Bank of Israel.


