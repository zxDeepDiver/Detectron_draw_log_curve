import re
name ='log'
from matplotlib import pylab as plt
import numpy as np

losses = np.zeros((0),dtype=np.float32)
with open(name, 'r') as fid:
    for line in fid:
        if len(line)<500:
            continue
        line = list(line)
        line=line[12:]
        line = ''.join(line)
        #line=re.sub('"','',line)
        line=re.sub('eta\:[ ]*\d{1,2}\:\d{1,2}:\d{1,2},','',line)
        try:
            a=eval(line)
        except:
            print line
        losses=np.append(losses,np.array([a['loss']]),axis=0)


plt.plot(losses)
plt.show()
