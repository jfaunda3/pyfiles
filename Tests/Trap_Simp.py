import math
def feval(f,a):
	arr = []
	for x in a:
		arr.append(eval(f))
	return sum(arr)

def trap(f,a,b,n):
	'''
	INPUT: function in strings in terms of x, lower bound, upper bound, itereation
	OUTPUT: Integral
	'''
	h = (float(b)-float(a))/float(n)
	S = feval(f,[a])
	x = []
	for c,i in enumerate(range(1,n+1)):
		x.append(float(a)+float(h)*float(i))
		S = S+2*feval(f,[x[c]])
	S = S+feval(f,[b])
	I = h * S/2
	return I

def simp(f,a,b,n):
	'''
	INPUT: function in strings in terms of x, lower bound, upper bound, itereation
	OUTPUT: Integral
	'''
	h=(float(b)-float(a))/float(n);
	S=feval(f,[a])
	x = []
	for c,i in enumerate(range(1,n,2)):
		x.append(float(a)+float(h)*float(i))
		S=S+4*feval(f,[x[c]])
	x = []
	for c,i in enumerate(range(2,n+1,2)):
		x.append(float(a)+float(h)*float(i))
		S=S+2*feval(f,[x[c]])
	S=S+feval(f,[b])
	I=h*S/3
	return I


# test
#I = trap('2.0*math.pi*x*(1.0-x**2.0)',0,1,5)
#Is = simp('2.0*math.pi*x*(1.0-x**2.0)',0,1,50)
#print I
#print Is
