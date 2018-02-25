import numpy as np
import theano
import theano.tensor as T

# activation function example
x = T.dmatrix('x')
s = 1 / (1 + T.exp(-x))    # logistic or soft step
logistic = theano.function([x], s)
print(logistic([[0, 1],[-1, -2]]))

a, b = T.dmatrices('a', 'b')
diff = a - b
abs_diff = abs(diff)
diff_squared = diff ** 2
f = theano.function([a, b], [diff, abs_diff, diff_squared])
print( f(np.ones((2, 2)), np.arange(4).reshape((2, 2))) )

# default value and name for a function
x, y, w = T.dscalars('x', 'y', 'w')
z = (x+y)*w
f = theano.function([x,
                     theano.In(y, value=1),
                     theano.In(w, value=2, name='weights')],
                   z)
print(f(23, 2, weights=4))

import numpy as np
import theano
import theano.tensor as T

state = theano.shared(np.array(0,dtype=np.float64), 'state') # inital state = 0
inc = T.scalar('inc', dtype=state.dtype)
accumulator = theano.function([inc], state, updates=[(state, state+inc)])

# to get variable value
print(state.get_value())
accumulator(1)   # return previous value, 0 in here
print(state.get_value())
accumulator(10)  # return previous value, 1 in here
print(state.get_value())

# to set variable value
state.set_value(-1)
accumulator(3)
print(state.get_value())

# temporarily replace shared variable with another value in another function
tmp_func = state * 2 + inc
a = T.scalar(dtype=state.dtype)
skip_shared = theano.function([inc, a], tmp_func, givens=[(state, a)]) # temporarily use a's value for the state
print(skip_shared(2, 3))
print(state.get_value()) # old state value
