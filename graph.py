import matplotlib.pyplot as plt 
import math

# x-axis values 
x = [] 
# y-axis values 
y = [] 
  
def kvadriraj(i, j):
    x = i*i + j*j*(-1)
    y = i*j + i*j
    
    return [x, y]

def pristej(i, j, x, y):
    r = i + x
    t = j + y

    return [r, t]
    

                         
for i in range (-2000, 2000):
    for j in range (-2000, 2000): 
        cx = i / 1000.0
        cy = j / 1000.0
        print(cx)
        print(cy)
        
        kompl = [cx, cy]
        for h in range (0, 100): 
            kompl = kvadriraj(kompl[0], kompl[1])
            kompl = pristej(kompl[0], kompl[1], cx, cy)
            
            if math.sqrt(kompl[0]**2 + kompl[1]**2) > 2:
                break
            
        if math.sqrt(kompl[0]**2 + kompl[1]**2) < 2:
            print("success")
            print(cx)
            print(cy)
            x.append(cx)
            y.append(cy)
  
  
# plotting points as a scatter plot 
plt.scatter(x, y, color= "green",  
            marker= ".", s=1) 
  
# x-axis label 
plt.xlabel('x - axis') 
# frequency label 
plt.ylabel('y - axis') 
# plot title 
plt.title('My scatter plot!') 
# showing legend 
plt.legend() 

  
# function 
plt.show()