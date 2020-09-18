
#INPUT inputs and weights
#RETURN 0 or 1 using activation definition
#Use Equation (2)
def activation(inputs, weights):
    sum = 0
    for i in range(0,len(weights)):
        sum += inputs[i]*weights[i]
    if sum>0:
        return 1
    else:
        return 0


#learning rate
eta = .25

#INPUT weights and function
#RETURN updated weights using update function
#Use Equation (5)
def update(weights,fp):
    g = activation(fp[0],weights)
    for i in range(0,len(weights)):
        weights[i] = weights[i] + eta*(fp[1]-g)*fp[0][i]
#TO DO: Implement this function


#INPUT weights and function
#OUTPUT a number that reflects error
#0 means no error
def test(weights,f):
    sum = 0
    for fp in f:
        input = fp[0]
        output = fp[1]
        sum += (output - activation(input,weights))**2
    print("Error: {0}".format(sum**.5))

#Function to be learned including bias
f = [[[-1,0,0], 0], [[-1,0,1],1], [[-1,1,0],1], [[-1, 1,1],1]]
#Randomly assigned small weights
weights = [-.05,-0.02,.02]


for i in range(0,10):
    print(weights)
    update(weights,f[i%4])
    test(weights,f)
