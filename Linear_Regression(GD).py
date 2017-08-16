from numpy import *

#Gradient Descent Function
def gradient_descent(b,m,n,x,y,learning_rate,i):
    for j in xrange(i):
        b,m = step(b,m,n,array(x),array(y),learning_rate);
    return [b, m];

def step(bi,mi,n,x,y,learning_rate):
    b_grad = 0;
    m_grad = 0;
    for j in xrange(len(x)):
        b_grad += -(2/n)*(y[j] - (bi + (mi*x[j])));
        m_grad += -(2/n)*x[j]*(y[j] - (bi + (mi*x[j])));
    b_new = bi - (learning_rate*b_grad);
    m_new = mi - (learning_rate*m_grad);
    return [b_new, m_new];

data = []
x= []
y=[]
while(True):
    try:
        data = raw_input().split();
        x.append(float(data[0]));
        y.append(float(data[1]));
    except EOFError:
        break        

learning_rate = 0.0001;
initial_b = 0;
initial_m = 0;
iterations = 10000;
n = float(len(x));

[b, m] = gradient_descent(initial_b,initial_m,n,x,y,learning_rate,iterations);
print n
print b, m

