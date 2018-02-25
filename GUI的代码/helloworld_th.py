import theano
import theano.tensor as T
import numpy

mytype = T.TensorType('float32', (False,)*5)
data = mytype('x')
print(data.type())
data = numpy.array([[1,2,3],[4,5,6]])
shared_data = theano.shared(data)
print(type(shared_data))


x = theano.tensor.ivector('x')
y = x**2
print(y)


N = 10000
M =784
X = numpy.random.randn(N,M)
Y = numpy.random.randint(low =0, high=2, size = N)

w_value = numpy.random.randn(M)
w = theano.shared(value = w_value, name = 'w')
b = theano.shared(value = 0.0, name = 'b')

