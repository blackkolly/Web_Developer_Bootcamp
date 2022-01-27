def f(u,y=[]) :
    for i in range(u) :
        y.append(i*i) 
    print(y)
print (f(6) ) 
print (f(6,[4,1,5] )) 
print (f(6) )   