import math
import operator

c = {'t' : 0.5,'f' : 0.5}
s = {'t|t' : 0.1,'t|f' : 0.5}
r = {'t|t' : 0.8,'t|f' : 0.2}
w = {'t|tt' : 0.99,'t|tf' : 0.9,'t|ft' : 0.9,'t|ff' : 0.00} 
r['t'] = r['t|t']*c['t'] + r['t|f']*c['f']
s['t'] = s['t|t']*c['t'] + s['t|f']*c['f']
r['f'] = 1 - r['t']
s['f'] = 1 - s['t']
w['t'] = w['t|tt']*s['t']*r['t'] + w['t|tf']*s['t']*r['f'] + w['t|ft']*s['f']*r['t'] + w['t|ff']*s['f']*r['f']
w['t|t_'] =  w['t|tt']*s['t']*r['t'] + w['t|tf']*s['t']*r['f'] / w['t']


a = c['t']
b = c['t']*r['t|t']/r['t']
c = s['t']*w['t|t_']/w['t']
d = s['t']

samp = [0.82,	0.56,	0.08,	0.81,	0.34,	0.22,	0.37,	0.99,	0.55,	0.61,	0.31,	0.66,	0.28,	1.0,	0.95,	
0.71,	0.14,	0.1,	1.0,	0.71,	0.1,	0.6,	0.64,	0.73,	0.39,	0.03,	0.99,	1.0,	0.97,	0.54,	0.8,	0.97,	
0.07,	0.69,	0.43,	0.29,	0.61,	0.03,	0.13,	0.14,	0.13,	0.4,	0.94,	0.19, 0.6,	0.68,	0.36,	0.67,	
0.12,	0.38,	0.42,	0.81,	0.0,	0.2,	0.85,	0.01,	0.55,	0.3,	0.3,	0.11,	0.83,	0.96,	0.41,	0.65,	
0.29,	0.4,	0.54,	0.23,	0.74,	0.65,	0.38,	0.41,	0.82,	0.08,	0.39,	0.97,	0.95,	0.01,	0.62,	0.32,	
0.56,	0.68,	0.32,	0.27,	0.77,	0.74,	0.79,	0.11,	0.29,	0.69,	0.99,	0.79,	0.21,	0.2,	0.43,	0.81,	
0.9,	0.0,	0.91,	0.01]


#1a
pc = 0.0 
cvar = float(len(samp)/4)
temp = 0.0
for i in range (0,100,4):
	ct = samp[i]
	if 0 <= ct < 0.5:
		temp = temp + 1	
pc = temp/cvar
print '1.a) prior prob(c=t) =', pc	

#1b
pr = 0.0
pcr = 0.0
num =0.0
denom = 0.0
count = 0.0
for i in range (2,102,4):
	if 0 <= samp[i-2] < 0.5 and 0 <= samp[i] < 0.8:
		count = count + 1
	if 0.5 <= samp[i-2] < 1 and 0.8 <= samp[i] < 1:
		count = count + 1
pr = count/cvar
for i in range (2,102,4):
    if 0 <= samp[i] < r['t']:
        denom = denom + 1
    if  0 <= samp[i] < r['t'] and 0 <= samp[i-2] < 0.5:
        num = num + 1	
pcr = num/denom
print '1.b) prior prob(c=t | r=t) =', pcr	

#1c
pw = 0.0
psw = 0.0
num =0.0
denom = 0.0
count = 0.0
for i in range (3,103,4):
	if 0 <= samp[i-2] < 0.1 and 0 <= samp[i-1] < 0.8 and 0 <= samp[i] < .99:
		count = count + 1
	elif 0 <= samp[i-2] < 0.1 and 0.8 <= samp[i-1] < 1 and 0 <= samp[i] < .9:	
		count = count + 1
	elif 0.1 <= samp[i-2] < 1 and 0 <= samp[i-1] < 0.8 and 0 <= samp[i] < .9:	
		count = count + 1
	elif 0.1 <= samp[i-2] < 1 and 0.8 <= samp[i-1] < 1 and 0 <= samp[i] < 0.0:
		count = count + 1
pw = count / cvar		
for i in range (3,103,4):
	if  0 <= samp[i] < pw:
		denom = denom + 1
		if 0 <= samp[i-2] < .1:
			num = num + 1	
psw = num/denom
print '1.c) prior prob(s=t | w=t) =', psw	

#1d
pscw = 0.0
num =0.0
denom = 0.0
for i in range (1,101,4):
	if 0 <= samp[i-1] < 0.5 and 0 <= samp[i+2] < pw:
		denom = denom + 1
		if 0 <= samp[i] < 0.1:
			num = num + 1	
pscw = num/denom
print '1.d) prior prob(s=t | c=t,w=t) =', pscw	

#2
print '2.a) exact prob(c=t) = ', a
print '2.b) exact prob(c=t | r=t) = ', b
print '2.c) exact prob(s=t | w=t) = ', c
print '2.d) exact prob(s=t | c=t,w=t) = ', d	

#3a
rpc = 0.0 
rcvar = float(len(samp))
temp = 0.0
for i in range (0,100):
	ct = samp[i]
	if 0 <= ct < 0.5:
		temp = temp + 1	
rpc = temp/rcvar
print '3.a) rejected prob(c=t) =', rpc	


#3b
rpr = 0.0
rpcr = 0.0
rnum =0.0
rdenom = 0.0
rcount = 0.0
rcvar = float(len(samp)/2)
'''for i in range (0,100,2):
	if 0 <= samp[i] < 0.5 and 0 <= samp[i+1] < 0.8:
		rcount = rcount + 1
	if 0 <= samp[i] < 1 and 0.8 <= samp[i+1] < 1:
		rcount = rcount + 1
rpr = rcount/rcvar'''
for i in range (0,100,2):
    if 0 <= samp[i+1] < r['t']:
        denom = denom + 1
    if  0 <= samp[i+1] < r['t'] and 0 <= samp[i] < 0.5:
        num = num + 1
rpcr = num/denom
print '3.b) rejection prob(c=t | r=t) =', rpcr	

#3c
pw = 0.0
psw = 0.0
num =0.0
denom = 0.0
count = 0.0
for i in range (3,103,4):
	if 0 <= samp[i-2] < 0.1 and 0 <= samp[i-1] < 0.8 and 0 <= samp[i] < .99:
		count = count + 1
	elif 0 <= samp[i-2] < 0.1 and 0.8 <= samp[i-1] < 1 and 0 <= samp[i] < .9:	
		count = count + 1
	elif 0.1 <= samp[i-2] < 1 and 0 <= samp[i-1] < 0.8 and 0 <= samp[i] < .9:	
		count = count + 1
	elif 0.1 <= samp[i-2] < 1 and 0.8 <= samp[i-1] < 1 and 0 <= samp[i] < 0.0:
		count = count + 1
pw = count / cvar		
for i in range (0,100,2):
    if  0 <= samp[i+1] < w['t']:
        denom = denom + 1
    if 0 <= samp[i+1] < w['t'] and 0 <= samp[i] < .1:
        num = num + 1	
psw = num/denom
print '3.c) rejected prob(s=t | w=t) =', psw	

#3d
rpscw = 0.0
rnum =0.0
rdenom = 0.0
for i in range (0,100,4):
    if 0 <= samp[i] < 0.5 and 0 <= samp[i+3] < w['t']:
        rdenom = rdenom + 1
    if 0 <= samp[i] < 0.5 and 0 <= samp[i+3] < w['t'] and 0 <= samp[i+1] < 0.1:
        rnum = rnum + 1	
rpscw = rnum/rdenom
print '3.d) rejected prob(s=t | c=t,w=t) =', rpscw	










