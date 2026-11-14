import numpy as np
from numpy.typing import NDArray


class Solution:
    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:


       z_max = np.max(z)
       z_shifted = z-z_max
       exp_value = np.exp(z_shifted)
       probabilities = exp_value/np.sum(exp_value)
       return np.round(probabilities,4)
