import matplotlib.pyplot as plt
fig = plt.figure()

x = [1,2,3,4,5,6,7]
y = [1,3,4,2,5,8,6]

left,bottom,width,height = 0.1,0.1,0.8,0.8

ax1 = fig.add_axes([left,bottom,width,height])
ax1.plot(x,y,'r')

left,bottom,width,height = 0.2,0.6,0.25,0.25
ax2 = fig.add_axes([left,bottom,width,height])
ax2.plot(y,x,'b')



plt.show()
