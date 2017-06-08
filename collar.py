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
chest_circ = 41+12 #if x is measured value, take x+12
full_length = 29+3.25 #x+3.25 
shoulder_length = 11 #x/2+1
neck_round = 17.0 #this is taken elliptical, so offset might be needed from 3d model
neck_l = neck_round/6.0
neck_w = neck_round/6.0
shoulder_shape = 2.5 #lower value needed (~1) for kids
armscye_round = 19.5/2 #=(x/2); needs calibration from actual models

back_length = full_length - 3.5
sleeve_length = 12.5 #x+2
sleeve_circum = 13/2+0.75 +3#(=x/2 + 0.75) requires checking from models # +3 new update for kinect values 

ptA = (0,0)
ptB = (neck_round/2.0,0)
ptC = (neck_round/2.0+0.5, 1.25) #total collar height = 1.5+2.5; here 1.25 = 1.5 - 0.25;
ptD = (ptC[0],1.5)
ptE = (ptD[0] - 1, ptD[1])
ptF = (ptD[0] - 0.75, 4) 
ptG = (0.0,3.5)

xvals = np.array([ptG[0],ptA[0],ptB[0]])
yvals = np.array([ptG[1],ptA[1],ptB[1]])

#B to C
z1 = (ptB[0]+0.2,ptB[1]+0.2)
z2 = (ptC[0],ptC[1]-0.2)
arr = np.array([ptB,z1,z2,ptC])
xt,yt = curvevia(arr)
xvals = np.append(xvals,xt)
yvals = np.append(yvals,yt)

xvals = np.append(xvals,[ptD[0],ptE[0],ptF[0]])
yvals = np.append(yvals,[ptD[1],ptE[1],ptF[1]])

#F to G curve
p1 = (1.0/8.0*(neck_round/2.0),ptG[1])
p2 = (3.0/4.0*(neck_round/2.0),ptG[1]+0.25)
arr = np.array([ptF,p2,p1,ptG])
xt,yt = curvevia(arr)
xvals = np.append(xvals,xt)
yvals = np.append(yvals,yt)

plt.figure(1,(15,15))
plt.plot(xvals,yvals,'-r',xsquare,ysquare,'-b')
plt.axis('equal')
plt.savefig('collar.png')
plt.show()