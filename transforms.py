def forward_ft(ut,dt,arange,fft):
	nti=len(ut);k = arange(nti);T=nti*dt;
	frq=k/T
	# Careful with scaling! with fft python, we need 2*dt to get correct spectral amplitude:
	Y = (2*dt) * fft(ut) # fft computing and normalization
	return (Y,frq)
def backward_ft(ut,dt,arange,ifft):
	nti=len(ut);k = arange(nti);
	# Careful with scaling! with fft python, we need 2*dt to get correct spectral amplitude:
	Y =  1/(2*dt) * ifft(ut) # fft computing and normalization
	return Y
