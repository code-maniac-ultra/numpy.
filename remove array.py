data = some numpy array
label = some numpy array
A = np.argwhere(label==0) 
B = np.argwhere(data>1.5) 
out = np.argwhere(label==0 and data>1.5) 
