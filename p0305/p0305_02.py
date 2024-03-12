b = []
b_i = []
for i in range(0,25):
    if(i+1)%5==0:
        b_i.append(i+1) #[1,2,3,4,5]
        b.append(b_i)
        b_i = []
        
    else:
        b_i.append(i+1) # [1,2,3,4]
        
print(b)
print("-"*45)