def read_ascii1(fname):
	f = open(fname, 'r')
	da = [];da1=[]
	for line in f:
	    x = line.split()
	    x[0] = float(x[0])
	    da.append(x)
	f.close()
	for sublist in da:
	    for item in sublist:
	        da1.append(item)
	return (da1,len(da1))
#####
def read_ascii2(fname):
	f = open(fname, 'r')
	da = [];da1=[]
	h1=f.readline() #read first line to skip contents
	for line in f:
		line=line.strip()
		cols = line.split()
		da.append(float(cols[1])) # second column: convert to float and keep
	f.close()
	#for sublist in da:
	#    for item in sublist:
	#        da1.append(item)
	return (da,len(da))
#####
def taper(nt,t1,t2,alpha,cos,zeros,concat):
	wndo=[]; nts=t2-t1;r=alpha*float(nts);
	for i in range(0,int(r/2)):
		ri=0.5*( 1+cos( 2*3.1416*(1/r)*(float(i)-r/2) ) )
		wndo.append(ri)
	for i in range(int(r/2)+1,nts-int(r/2)+1):
		wndo.append(1)
	for i in range(nts-int(r/2)+1,nts+1):
		ri=0.5*( 1+cos( 2*3.1416*(1/r)*(float(i)-nts+r/2) ) )
		wndo.append(ri)
	#wndo=tukey(t2-t1,alpha)
	padleft=zeros(t1);padright=zeros(nt-t2)
	wndo_a=concat((padleft,wndo,padright))
	return(wndo_a)
