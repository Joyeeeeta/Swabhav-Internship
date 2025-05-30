import numpy as np

arr = np.arange(20).reshape(4,5)
print(arr)

even=np.arange(20,71,2)
print(even)

odd=np.arange(21,72,2)
print(odd)

random=np.random.randint(0,100,15)
print(random)
print(np.sort(random))

zero=np.array([0]*10)
zero[4]=1
print(zero)

array=[1,2,2,3,4,4,5]
print(array)
print(np.unique(array))

arr=np.arange(11)
reverse=np.flip(arr)
print(reverse)

birds=['spoonbills','plovers','plovers','plovers','plovers','Cranes','plovers','plovers','Cranes','spoonbills']
age=[5.5,6.0,3.5,1.5,3.0,4.0,3.5,2.0,5.5,6.0]

crane_age=np.array(age)[np.array(birds)=='Cranes']
print(crane_age)
print(round(np.mean(crane_age),2))

oldest_bird=np.array(birds)[np.array(age)==np.max(age)]
print(oldest_bird)

original=np.arange(30).reshape(5,6)
print(original)

rows=original[1:4]
cols=rows[:,-3:]
sub=cols[::-1]
print(sub)
