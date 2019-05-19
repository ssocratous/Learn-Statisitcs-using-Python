import numpy as np

a = np.random.normal(1400, 200, 1000)  #mu =1400,sugma=200, sample=1000
school_one = [x for x in a if x <= 1600]

b = np.random.normal(1000, 300, 1000)  #mu =1000,sugma=300, sample=1000
school_two = [x for x in b if x <= 1600]

c = np.random.normal(800, 500, 1000) #mu =800,sugma=500, sample=1000
school_three = [x for x in c if x <= 1600 and x >=200]


d = np.random.normal(600, 300, 1000) #mu =2000,sugma=300, sample=1000
school_four = [x for x in c if x <= 1600 and x >=200]