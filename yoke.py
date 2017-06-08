import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

def curvevia(arr):
	xt = arr[:,0]
	yt = arr[:,1]
	tck,u = interpolate.splprep( [xt,yt] ,s = 0 )
	xt, yt = interpolate.splev( np.linspace(0,1,100), tck,der = 0)
	return xt,yt
	
#changelog 26/05/17
#made the shirt length longer - previously, 2 inches added; now 3.25
#made the armhole curves more symmetric
#extended the shoulder offset from 0.25 to 1 (overall 2 inches added now)
#collar slightly reshaped
#chest offset increased slightly from 10 to 12
#removed offset for armscye round (was -2)	
	
	
#reference 10cm x 10cm square
xsquare = [-1, -4.937, -4.937, -1, -1]
ysquare = [1, 1, 4.937, 4.937, 1]
	
	
#needed values
chest_circ = 41.0+12.0 #if x is measured value, take x+12
full_length = 29.0+3.25 #x+3.25 
shoulder_length = 11.0 #x/2+1
neck_round = 17.0 #this is taken elliptical, so offset might be needed from 3d model
neck_l = neck_round/6.0
neck_w = neck_round/6.0
shoulder_shape = 2.5 #lower value needed (~1) for kids
armscye_round = 19.5/2.0 #=(x/2); needs calibration from actual models

back_length = full_length - 3.5
sleeve_length = 12.5 #x+2
sleeve_circum = 13/2+0.75 #(=x/2 + 0.75) requires checking from models

ptE = (0,0)
ptA = (0,5-neck_round/12) #5 inches yoke length taken arbitraty
ptB = (neck_round/6,5)
ptC = (shoulder_length,5-shoulder_shape)
ptD = (shoulder_length,0)

p1 = (ptA[0]+neck_round/21.0,ptA[1])
#p2 = (ptB[0],ptB[1]-.3)
p2 = p2 = (ptA[0]+neck_round*0.14,5.0 - neck_round/24.0)

xp = [p1[0],p2[0]]
yp = [p1[1],p2[1]]

xvals = np.array([ptB[0],ptC[0],ptD[0],ptE[0],ptA[0]])
yvals = np.array([ptB[1],ptC[1],ptD[1],ptE[1],ptA[1]])



arr = np.array([ptA,p1,p2,ptB])
xt,yt = curvevia(arr)
xvals = np.append(xvals,xt)
yvals = np.append(yvals,yt)

plt.figure(1,(20,20))
plt.plot(xvals,yvals,'-r',xsquare,ysquare,'-b')
plt.axis('equal')
plt.savefig('yoke.png')
plt.show()