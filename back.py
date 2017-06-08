import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

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

def curvevia(arr):
	xt = arr[:,0]
	yt = arr[:,1]
	tck,u = interpolate.splprep( [xt,yt] ,s = 0 )
	xt, yt = interpolate.splev( np.linspace(0,1,100), tck,der = 0)
	return xt,yt
	

#needed values
chest_circ = 41+12 #if x is measured value, take x+12
full_length = 29+3.25 #x+3.25 
shoulder_length = 11 #x/2+1
neck_round = 17 #this is taken elliptical, so offset might be needed from 3d model
neck_l = neck_round/6
neck_w = neck_round/6
shoulder_shape = 2.5 #lower value needed (~1) for kids
armscye_round = 19.5/2 #=(x/2); needs calibration from actual models

back_length = full_length - 3.5
sleeve_length = 12.5 #x+2
sleeve_circum = 13/2+0.75 +3#(=x/2 + 0.75) requires checking from models # +3 new update for kinect values 

ptA = (0,back_length)
ptD = (shoulder_length,back_length)
ptB = (chest_circ/4, back_length)
ptG = (ptD[0],back_length-6)
ptC = (chest_circ/4,ptG[1])
ptF = (0,0)
ptE = (chest_circ/4,0)

t = (ptD[0],ptG[1]+5)
p = (ptG[0]+0.625,ptC[1]+0.625)


xvals = np.array([ptA[0],ptD[0]])
yvals = np.array([ptA[1],ptD[1]])

arr = np.array([ptD,t,p,ptC])
xt, yt = curvevia(arr)
xvals = np.append(xvals,xt)
yvals = np.append(yvals,yt)

#xvals = np.append(xvals,xc)
#yvals = np.append(yvals,yc)

xvals = np.append(xvals,[ptE[0],ptF[0],ptA[0]])
yvals = np.append(yvals,[ptE[1],ptF[1],ptA[1]])

plt.figure(1,(40,40))
plt.plot(xvals,yvals,'-r',xsquare,ysquare,'-b')
plt.axis('equal')
plt.savefig('back.png')
plt.show()