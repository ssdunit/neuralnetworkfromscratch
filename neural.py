import torch
import random as rand
import numpy as np
input_neurons = [2,1,3,4]
weights = torch.rand(5,4)
bias = rand.sample(range(1,100),4)
counter = 0
neutron_out = []
for neuron_weight_tensor_list,bias_n in zip(weights,bias):
    neutron_output = 0
    neutron_output+=(np.dot(input_neurons,neuron_weight_tensor_list)+bias[counter])
    counter+=1
    neutron_out.append(neutron_output)
print(neutron_out)
