import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

def curvevia(arr):
	xt = arr[:,0]
	yt = arr[:,1]
	tck,u = interpolate.splprep( [xt,yt] ,s = 0 )
	xt, yt = interpolate.splev( np.linspace(0,1,100), tck,der = 0)
	return xt,yt
	
#reference 10cm x 10cm square
xsquare = [-1, -4.937, -4.937, -1, -1]
ysquare = [1, 1, 4.937, 4.937, 1]

#changelog 26/05/17
#made the shirt length longer - previously, 2 inches added; now 3.25
#made the armhole curves more symmetric
#extended the shoulder offset from 0.25 to 1 (overall 2 inches added now)
#collar slightly reshaped
#chest offset increased slightly from 10 to 12
#removed offset for armscye round (was -2)	
	
		
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

ptA = (0,full_length)
ptB = (2,full_length - neck_l)
ptC = (2+neck_w,full_length)
ptE = (2+shoulder_length,ptC[1]-shoulder_shape)
ptF = (2+chest_circ/4, full_length - armscye_round - shoulder_shape)
ptG = (ptF[0],0)
ptH = (0,0)
ptI = (0,full_length - (neck_l/3))

#from B to C
z1 = (2+neck_l*0.75,full_length-neck_l*0.75)
z2 = (ptC[0],ptC[1]-0.0001)

#from E to F
p1 = (ptE[0]-0.2,full_length - shoulder_shape - armscye_round/2)
p2 = (ptE[0]+0.025,p1[1]-((p1[1]-ptF[1])/2))
#x = np.array([ptA[0],ptB[0],ptC[0],ptE[0],ptF[0],ptG[0],ptH[0],ptI[0]])
#y = np.array([ptA[1],ptB[1],ptC[1],ptE[1],ptF[1],ptG[1],ptH[1],ptI[1]])

xvals = np.array([ptI[0],ptB[0]])
yvals = np.array([ptI[1],ptB[1]])

arr = np.array([ptB,z1,z2,ptC])
xt,yt = curvevia(arr)
xvals = np.append(xvals,xt)
yvals = np.append(yvals,yt)

xvals = np.append(xvals,ptE[0])
yvals = np.append(yvals,ptE[1])

arr = np.array([ptE,p1,p2,ptF])
xt,yt = curvevia(arr)
xvals = np.append(xvals,xt)
yvals = np.append(yvals,yt)

xvals = np.append(xvals,[ptG[0],ptH[0],ptI[0]])
yvals = np.append(yvals,[ptG[1],ptH[1],ptI[1]])


plt.figure(1,(40,40))
plt.plot(xvals,yvals,'-r',xsquare,ysquare,'-b')
plt.axis('equal')
plt.savefig('front.png')
plt.show()