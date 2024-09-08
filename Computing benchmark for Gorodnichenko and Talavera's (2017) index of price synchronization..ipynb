{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "c3101a32",
   "metadata": {},
   "source": [
    "# Computing benchmark for Gorodnichenko and Talavera's (2017) index of price synchronization.\n",
    "\n",
    "In the following code snippet, we demonstrate our method of computing the benchmark for Gorodnichenko and Talavera's (2017) index of price synchronization under the null hypothesis of of no coordination (i.e. independence) between the stores. We calculate the benchmark as follows. We use the fact that Gorodnichenko and Talavera’s (2017) index represents a scaled sum of binary variables indicating the price change of good i at time t in store s. Thus, under the null hypothesis of no coordination, the expectation of the index is completely characterized by the probability of a price change for each good in each store, which can be proxied by the associated frequencies. \n",
    "\n",
    "When the number of stores is small, calculating the benchmark is straightforward and can be done analytically. For example, consider a scenario with only three stores. Let’s assume (w.l.o.g.) that the probabilities of price change for some product in store $j$ ($j=1,2,3$) are given by $p_{1}=0.1, p_{2}=0.2, p_{3}=0.3$. In this case, the benchmark can be computed as follows:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f51287ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "%config Completer.use_jedi = False\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e93192f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Benchmark value of Gorodnichenko and Talavera's (2017) index=0.105\n"
     ]
    }
   ],
   "source": [
    "p1=0.1 # probability of a price change in store 1\n",
    "p2=0.2 # probability of a price change in store 2\n",
    "p3=0.3 # probability of a price change in store 3\n",
    "\n",
    "ps0=(p1*(1-p2)*(1-p3)+p2*(1-p1)*(1-p3)+p3*(1-p1)*(1-p2))/(1-(1-p1)*(1-p2)*(1-p3)) # There is a single price change (the index takes the value of 0)\n",
    "ps12=(p1*p2*(1-p3)+p1*p3*(1-p2)+p3*p2*(1-p1))/(1-(1-p1)*(1-p2)*(1-p3)) # There is a price change in two stores at the same time (the index takes the value of 0.5)\n",
    "ps1=(p1*p2*p3)/(1-(1-p1)*(1-p2)*(1-p3)) # The price has changed in all stores at the same time (the index takes the value of 1)\n",
    "\n",
    "# Conditional expectation of the index at time t\n",
    "E_st=0.5*(p1*p2*(1-p3)+p1*p3*(1-p2)+p3*p2*(1-p1))/(1-(1-p1)*(1-p2)*(1-p3))+(p1*p2*p3)/(1-(1-p1)*(1-p2)*(1-p3)) \n",
    "\n",
    "print(\"Benchmark value of Gorodnichenko and Talavera's (2017) index={}\".format(np.round(E_st,3)))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0147dc91",
   "metadata": {},
   "source": [
    "We can also compute the benchmark numerically using the following function:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "aeae3d1c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def benchmark(p,rep,n,seed=123456):\n",
    "    \"\"\"\n",
    "    This functions computes  the benchmark for Gorodnichenko and Talavera's (2017) index of price \n",
    "    synchronization under the null hypothesis of of no coordination (i.e. independence) between the stores.\n",
    "    \n",
    "    Arguments:\n",
    "    \n",
    "    p - list of probabilities of price change in store j\n",
    "    rep - number of replications\n",
    "    n - length of the simulated sample\n",
    "    \n",
    "    Value:\n",
    "    \n",
    "    The benchmark value\n",
    "    \n",
    "    \"\"\"\n",
    "    \n",
    "    import numpy as np\n",
    "    \n",
    "    np.random.seed(seed=seed)\n",
    "    \n",
    "    S=[]\n",
    "\n",
    "    for r in range(rep):\n",
    "    \n",
    "        # sampling binary indicators of a price change\n",
    "    \n",
    "        D=[]\n",
    "    \n",
    "        for i in range(len(p)):\n",
    "            D.append(np.random.binomial(n=1,p=p[i],size=n))\n",
    "    \n",
    "        # computing the price synchronization index\n",
    "    \n",
    "        S_t=(np.concatenate([D],axis=1).T.sum(axis=1)-1)/(len(p)-1) #  Gorodnichenko and Talavera's (2017) index over time\n",
    "    \n",
    "        S.append(np.mean(S_t[S_t>=0])) # computing conditional mean\n",
    "        \n",
    "    return np.mean(S)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "6d738194",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Benchmark value of Gorodnichenko and Talavera's (2017) index=0.105\n"
     ]
    }
   ],
   "source": [
    "print(\"Benchmark value of Gorodnichenko and Talavera's (2017) index={}\".format(np.round(benchmark(p=[0.1,0.2,0.3],\n",
    "                                                                                                  n=1000,rep=1000),3)))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5148f746",
   "metadata": {},
   "source": [
    "As we can observe, the numerical estimate is reasonably accurate. When dealing with a large number of stores, analytical computation of the benchmark becomes challenging, making numerical methods particularly useful.\n",
    "\n",
    "The function’s arguments can be easily adjusted to provide numerical estimates for any number of stores and looped over different products, as demonstrated in the code snippet below:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "fccaf81f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Benchmark value of Gorodnichenko and Talavera's (2017) index=0.059\n"
     ]
    }
   ],
   "source": [
    "p=np.full((10, ), 0.1) # ten stores with equal probabilty of price change\n",
    "print(\"Benchmark value of Gorodnichenko and Talavera's (2017) index={}\".format(np.round(benchmark(p=p,\n",
    "                                                                                                  n=1000,rep=1000),3)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "63c0c79e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
