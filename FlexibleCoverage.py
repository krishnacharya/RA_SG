
# coding: utf-8

# In[22]:


import numpy as np


# In[59]:


np.version.version


# In[45]:


def linearithmic_alg(utility_vec, num_res):
    sorted_utility_vec = np.sort(utility_vec)[::-1]#sorted in descending order
    n = len(utility_vec)
    sorted_utility_vec = np.append(sorted_utility_vec, 0)
    cuml_inverse_sum = 0
    q = 0#the utility for all the covered targets
    for i in range(0, n):
        cuml_inverse_sum = cuml_inverse_sum + 1.0 / sorted_utility_vec[i]
        q = ((i+1) - num_res) / cuml_inverse_sum
        if sorted_utility_vec[i] >= q >= sorted_utility_vec[i+1]:
            break
    return q


# In[19]:


utils = np.random.randint(low = 5, high = 20, size=5)


# In[20]:


utils


# In[77]:


u = [10,2,2,2,1]


# In[78]:


a = linearithmic_alg(u, 1)


# In[79]:


a

