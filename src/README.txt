To run Neural Networks Simulation: python neuralnetworks.py

This is a implemenation of Multi Layer Perceptron.
Following Steps:

1.The Multi-Layer Feed Forward is run.
2.Backpropagation
3.Multi Layer Feed Forward is run again. 
4.Check for a solution

Functions and definitions:

sigmoid function: Used as activation function

print_header function:: prints the node numbers for the network

print_network function: Prints the adjacency matrix of the network with the 
nodes's corresponding input and weight values

multi-layer_feed_forward function: Runs the Feed Forward algorithm over the network

backpropagate: Learning function or rule. Run over the network

is_solution: Sees if the output layer equals the target values. 


Test sets are adjacency matrices in the code

3 adjacency matrices

Each matrix include 1 for the graph to and 1 for the network of inputs and weights

Each matrix is a list of list
There are 1 to n lists
Inside of those list are values from 1 to n
From 1 to n, the value is a list of 2 values or a tuple of 2 values
If the 1st value is a 0 for the value that means there is no edge to that
node or index in the list. If the 1st value is a 1, then there is an edge to that
index. Also, if there is a 1 there will be an associated input and weight in the
network.


4 printouts of the network happen at these times:

Network before Feed Forward
Network after Feedforward and before Backpropagation
Network after Backpropagation and before Feedforward
Network and second Feed Forward


IF there are any other questions email Tola at aadewodu@gmu.edu