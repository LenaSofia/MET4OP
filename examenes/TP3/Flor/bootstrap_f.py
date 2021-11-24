# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
np.random.seed(123)
pop = np.random.randint(0,500 , size=1000)
sample = np.random.choice(pop, size=300) #so n=300

sample_mean = []
for _ in range(10000):  #so B=10000
    sample_n = np.random.choice(sample, size=300)
    sample_mean.append(sample_n.mean())

plt.hist(sample_mean)

# %%
np.mean(sample_mean)
# %%
pop.mean()
# %%
sample.mean()
# %%