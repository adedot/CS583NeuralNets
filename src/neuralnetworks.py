import math, random

#Constant
learning_rate = 0.5

#Sigmoid function
def sigmoid(val):
    return 1.0/(1.0 + math.exp(-val))

def print_header(num):
    header="\n\tj\t"
    for n in range(num):
        header +="%d\t\t" % (n+1)
    print header

def print_network(network):
    print "\nPrinting Network"
    print_header(len(network))
    print "i "
     
    for i in range(len(network)):
        row = "%d\t" % (i+1)
        for j in range(len(network[i])):
            row +='%3.4f:%3.4f   ' % (network[j][i][0], network[j][i][1])
        print row
        
        
def mulit_layer_feed_forward(graph, network, input_layer, output_nodes, inputs):
    # Multi-Layer Feed-Forward Algorithm
    for i in range(len(network)):
    #    print "input",i+1
        #
        w = bias[i][0]*bias[i][1]
    #    print "initial W=",w
        for j in range(len(network[i])):
             
            #if i+1 not in input_layer:
                # Output only connections from input to hidden and output layers
            if graph[i][j][0] <> 0:
    #            print "bias",bias[i]
    #            print "input",j+1,i+1,network[i][j][0]
    #            print "weight",j+1,i+1,network[i][j][1]
                
                w += network[i][j][0]*network[i][j][1]
    #            print "computed weight",w
            
        #print "final weight", sigmoid(w)
        inputs[i] = sigmoid(w)    
        #update the inputs
    #    if i+1 in output_nodes:
    #        output_nodes.remove(i+1)
        #print output_nodes
        
        #Recalcuate weights for ajacency matrix
        for k in range(len(output_nodes)):
            out = output_nodes[k]
            
            #print out
            if i+1 not in input_layer and graph[out-1][i][0] <> 0:
                network[out-1][i][0] = sigmoid(w)
                #print "new input is", network[out-1][i][0]
                
    return network,inputs
                
#Backpropagation 
def backpropagate(graph, network, input_layer, output_layer, inputs,
                  error_rates,bias, output_nodes, target):
    #Get the hidden layer
    hidden_layer = set(output_nodes).symmetric_difference(output_layer)
    hidden_layer = list(hidden_layer)
    
    #input nodes 
    input_nodes = set(input_layer).union(hidden_layer)
    input_nodes = list(input_nodes)
    
    #print "Error Rates",error_rates
    #Calculate the error rates for output nodes
    #print "Output Layer Error Rates"

    for i in range(len(output_layer)):
        last = output_layer[i]
       # print "Output Nodes",last
        error_rates[last-1] = ((target[i] -inputs[last-1])* \
                               inputs[last-1]*(1-inputs[last-1]))
    
    #print "Hidden Layer Error Rates"
    for i in range(len(hidden_layer)):
        h = hidden_layer[i]
        #print "hidden node", h
        #print "weight",network[last][h-1][1]
        #print inputs[h-1]
        #print error_rates[h-1]
        for i in range(len(output_layer)):
            last = output_layer[i]-1
            #print error_rates[last]
            if graph[last][h-1][0] <> 0:
                error_rates[h-1] += (error_rates[last] *network[last][h-1][1])* \
                inputs[h-1]*(1-inputs[h-1])
            #error_rates[h-1] = sigmoidDerivative(error_rates[h-1])
    #print error_rates
    
    #Reweight the graph
    for i in range(len(hidden_layer)):
        h = hidden_layer[i]
        #print "hidden node", h
        #print "weight",network[last][h-1][1]
        #print inputs[h-1]
        #print error_rates[h-1]
        for i in range(len(output_layer)):
            last = output_layer[i]-1
            #print error_rates[last]
            if graph[last][h-1][0] <> 0:
                network[last][h-1][1] = network[last][h-1][1] + \
                learning_rate*error_rates[last]*inputs[h-1]
                #print "weight", h, last+1, network[last][h-1][1]
    
    ## Reweight output cell bias
    #for b in range(len(output_layer)):
    #    w_o = output_layer[b]
    #    print w_o
    #    network[w_o][h-1][1] = network[last][h-1][1] + learning_rate*error_rates[w_o]*bias[w_o][1]
    
    # Reweight the weights from input nodes to 
    # Hidden nodes
    for i in range(len(hidden_layer)):
        h_i = hidden_layer[i]
        #print "hidden node", h_i
        for j in range(len(input_nodes)):
            i_j =  input_nodes[j]
            #print "input",i_j
            if graph[h_i-1][i_j-1][0] <> 0:
                network[h_i-1][i_j-1][1] =  network[h_i-1][i_j-1][1] + \
                learning_rate*error_rates[h_i-1]*inputs[i_j-1]
                #print "New for weight", i_j, h_i, "is ", network[h_i-1][i_j-1][1]
    return network

def is_solution(graph, network, output_layer, target):
    
    
    for i in range(len(output_layer)):
        output = output_layer[i]
        for j in range(len(network)):
            if graph[output-1][j][1] <> 0 and network[output-1][j][1] == target[i]:
                print "There is a solution"
            elif graph[output-1][j][1] <> 0:
                print "No solution"
#graph
graph = [[(0,0), (0,0), (0,0),(0,0),(0,0),(0,0),(0,0)],
           [(0,0), (0,0), (0,0),(0,0) ,(0,0),(0,0),(0,0)],
           [[1,1.0], [1,0.5], (0,0), (0,0),(0,0), (0,0),(0,0)],
           [[1,-1.0], [1,2.0], (0,0), (0,0),(0,0), (0,0),(0,0)],
           [(0,0), (0,0), [1,1.5], [1,-1.0],(0,0), (0,0),(0,0)],
           [(0,0), (0,0), (0,0),(0,0),[1,1.5],(0,0),(0,0)],
           [(0,0), (0,0), (0,0),(0,0) ,[1,-1.0],(0,0),(0,0)]
           ]

#network
network = [[(0,0), (0,0), (0,0),(0,0),(0,0),(0,0),(0,0)],
           [(0,0), (0,0), (0,0),(0,0) ,(0,0),(0,0),(0,0)],
           [[0,1.0], [1,0.5], (0,0), (0,0),(0,0), (0,0),(0,0)],
           [[0,-1.0], [1,2.0], (0,0), (0,0),(0,0), (0,0),(0,0)],
           [(0,0), (0,0), [1,1.5], [1,-1.0],(0,0), (0,0),(0,0)],
           [(0,0), (0,0), (0,0),(0,0),[1,1.5],(0,0),(0,0)],
           [(0,0), (0,0), (0,0),(0,0) ,[1,-1.0],(0,0),(0,0)]
           ]
input_layer = [1,2]
output_nodes = [3,4,5,6,7]
#input weights
inputs = [0,0,0,0,0,0,0]

target = [1,0]
output_layer = [6,7]

##Get the hidden layer
#hidden_layer = set(output_nodes).symmetric_difference(output_layer)
#hidden_layer = list(hidden_layer)
#
##input nodes 
#input_nodes = set(input_layer).union(hidden_layer)
#input_nodes = list(input_nodes)

error_rates = [0,0,0,0,0,0,0]
# introduces a threshold to the neuron
bias = [(0,0), (0,0), (1,1),(1,1),(1,1),(1,1),(1,1)]

print "\nBefore Feed Forward\n"

print_network(network)

network, inputs = mulit_layer_feed_forward(graph, network, input_layer, output_nodes, inputs)

print "After 1st Feed Forward and before Backpropagation\n"
print_network(network)

network = backpropagate(graph, network, input_layer, output_layer, inputs, \
                        error_rates, bias, output_nodes, target)

print "\nAfter backpropagation and before 2nd Feed Forward\n" 
print_network(network)

network, inputs = mulit_layer_feed_forward(graph, network, input_layer, output_nodes, inputs)

print "\nAfter the 2nd Feed Forward\n"
print_network(network)

print "See if the network has a optimal solution"
is_solution(graph, network, output_layer, target)

#graph
graph = [[(0,0), (0,0), (0,0),(0,0),(0,0)],
           [(0,0), (0,0), (0,0),(0,0) ,(0,0)],
           [(1,1.0), (1,0.5), (0,0), (0,0),(0,0)],
           [(1,-1.0), (1,2.0), (0,0), (0,0),(0,0)],
           [(0,0), (0,0), (1,1.5), (1,-1.0),(0,0)]
           ]

#network
network = [[(0,0), (0,0), (0,0),(0,0),(0,0)],
           [(0,0), (0,0), (0,0),(0,0) ,(0,0)],
           [[0,1.0], [1,0.5], (0,0), (0,0),(0,0)],
           [[0,-1.0], [1,2.0], (0,0), (0,0),(0,0)],
           [(0,0), (0,0), [1,1.5], [1,-1.0],(0,0)]
           ]



input_layer = [1,2]
output_nodes = [3,4,5]
#input weights
inputs = [0,0,0,0,0]

target = [1]
output_layer = [5]

##Get the hidden layer
#hidden_layer = set(output_nodes).symmetric_difference(output_layer)
#hidden_layer = list(hidden_layer)

error_rates = [0,0,0,0,0]
# introduces a threshold to the neuron
bias = [(0,0), (0,0), (1,1),(1,1),(1,1)]

print "\nBefore Feed Forward\n"

print_network(network)

network, inputs = mulit_layer_feed_forward(graph, network, input_layer, output_nodes, inputs)

print "After 1st Feed Forward and before Backpropagation\n"
print_network(network)

network = backpropagate(graph, network, input_layer, output_layer, inputs, \
                        error_rates, bias, output_nodes, target)

print "\nAfter backpropagation and before 2nd Feed Forward\n" 
print_network(network)

network, inputs = mulit_layer_feed_forward(graph, network, input_layer, output_nodes, inputs)

print "\nAfter the 2nd Feed Forward\n"
print_network(network)

print "See if the network has a optimal solution"
is_solution(graph, network, output_layer, target)

#XOR Problem

#graph
graph = [[(0,0), (0,0), (0,0)],
           [(0,0), (0,0), (0,0)],
           [(1,1.0), (1,1.0), (0,0)]
           ]

#network
network = [[(0,0), (0,0), (0,0)],
           [(0,0), (0,0), (0,0)],
           [[0,1.0], [0,1.0], (0,0)]
           ]



input_layer = [1,2]
output_nodes = [3]
#input weights
inputs = [0,0,0]

#target outputs
target = [0]

output_layer = [3]

error_rates = [0,0,0]
# introduces a threshold to the neuron
bias = [(0,0),(0,0),(1,1)]

print "\nBefore Feed Forward\n"

print_network(network)

network, inputs = mulit_layer_feed_forward(graph, network, input_layer, output_nodes, inputs)

print "After 1st Feed Forward and before Backpropagation\n"
print_network(network)

network = backpropagate(graph, network, input_layer, output_layer, inputs, \
                        error_rates, bias, output_nodes, target)

print "\nAfter backpropagation and before 2nd Feed Forward\n" 
print_network(network)

network, inputs = mulit_layer_feed_forward(graph, network, input_layer, output_nodes, inputs)

print "\nAfter the 2nd Feed Forward\n"
print_network(network)

print "See if the network has a optimal solution"
is_solution(graph, network, output_layer, target)