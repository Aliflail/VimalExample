import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

#reference 10cm x 10cm square
xsquare = [-1, -4.937, -4.937, -1, -1]
ysquare = [-1, -1, -4.937, -4.937, -1]

def curvevia(arr):
	xt = arr[:,0]
	yt = arr[:,1]
	tck,u = interpolate.splprep( [xt,yt] ,s = 0 )
	xt, yt = interpolate.splev( np.linspace(0,1,100), tck,der = 0)
	return xt,yt
	
#changelog 26/05/17
#made the shirt length longer - previously, 2 inches added; now 3.25
#made the armhole curves symmetric
#extended the shoulder offset from 0.25 to 1 (overall 2 inches added now)
#collar slightly extended
#chest offset increased slightly from 10 to 12
#removed offset for armscye round (was -2)	
	
#refer to this link:	
#https://sewing.wonderhowto.com/how-to/draft-sleeve-pattern-0159101/

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

#shoulder_to_wrist = 23 # = x+2, for full sleeves, might be hard to get from kinect
ptA = (0,sleeve_length)
ptB = (armscye_round+2, sleeve_length - 3.5) #3.5 taken arbitrary
ptC = (sleeve_circum,2)
ptD = (ptB[0],0)
ptE = (0,0)
#reflected points
ptBm = (-ptB[0],ptB[1])
ptCm = (-ptC[0],ptC[1])
ptDm = (-ptD[0],ptD[1])

#join B C D E Dm Cm Bm
arr = np.array([ptB,ptC,ptD,ptE,ptDm,ptCm,ptBm])
xvals = arr[:,0]
yvals = arr[:,1]

#points 1 inch either side of A
ptAl = (ptA[0]-1,ptA[1])
ptAr = (ptA[0]+1,ptA[1])

#finding line from Bm to Al
z = np.polyfit([ptBm[0],ptAl[0]], [ptBm[1],ptAl[1]], 1)
p = np.poly1d(z)
xt = np.linspace(ptBm[0],ptAl[0],7)
yt = p(xt)


#curve Bm to Al
z1 = (xt[2], yt[2] - 0.75)
z2 = (xt[4], yt[4]) 
z3 = (xt[5], yt[5] + 0.25) 

#line plot from Ar to B
z = np.polyfit([ptAr[0],ptB[0]], [ptAr[1],ptB[1]], 1)
p = np.poly1d(z)
xt1 = np.linspace(ptAr[0],ptB[0],5)
yt1 = p(xt1)

#curve Bm to B
p1 = (xt1[1], yt1[1] + 0.7)
p2 = (xt1[2], yt1[2] + 1) 
p3 = (xt1[3], yt1[3] + 0.7) 
arr = np.array([ptBm,z1,z2,z3,ptA,p1,p2,p3,ptB])
x,y = curvevia(arr)
xvals = np.append(xvals,x)
yvals = np.append(yvals,y) 

xpoint = ptC[0]
ypoint = ptC[1]

plt.figure(1,(25,25))
plt.plot(xvals,yvals,'-r',xsquare,ysquare,'-b',xpoint,ypoint,'o')
plt.axis('equal')
plt.savefig('sleeve.png')
plt.show()