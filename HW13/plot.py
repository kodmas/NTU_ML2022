import matplotlib.pyplot as plt

x = [0.05*i for i in range(20)]
y = [0.85,0.85,0.843,0.842,0.831,0.822,0.802,0.763,0.687,0.5,0.29,0.24,0.15,0.14,0.13,0.11,0.1,0.098,0.095,0.093]

plt.plot(x,y)
plt.axis([0,0.95,0,1])
plt.title('model accuracy & pruning ratio',fontsize=24)
plt.xlabel('pruning ratio',fontsize=12)
plt.ylabel('model accuracy',fontsize=12)

plt.show()
