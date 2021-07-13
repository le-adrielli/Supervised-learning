import functions as f
import numpy as np
import matplotlib.pyplot as plt
import random
from sklearn.preprocessing import MinMaxScaler

def grad_func(data, theta, alpha, fx, var):
    sd =[0,0,0]
    nt = [0,0,0]
    j=[]
    for i in range(len(data)//4):
            j.append(random.randrange(0, len(data)))
    for i in j:
        a = data[i][var]
        h = theta[0]+theta[1]*a+theta[2]*(a**2)
        sd[0] += (h-data[i][fx])
        sd[1] += (h-data[i][fx])*a
        sd[2] += (h-data[i][fx])*(a*a)
    sd[0]= sd[0]/len(data)
    sd[1]= sd[1]/len(data)
    sd[2]= sd[2]/len(data)
    nt[0] = theta[0]- alpha*sd[0]
    nt[1] = theta[1]- alpha*sd[1]
    nt[2] = theta[2]- alpha*sd[2]
    return nt

        
def regrassion(data, alpha):
    thetax = np.array([random.random(),random.random(),random.random()])
    thetaz = np.array([random.random(),random.random(),random.random()])
    ep_x = 0
    ep_z = 0
     
    #thetas de x
    while(ep_x < 100000):
        ep_x += 1
        new_thetax = grad_func(data, thetax, alpha, 0, 1)
        if((abs(new_thetax[0]-thetax[0])<=0.00001) and (abs(new_thetax[1]-thetax[1])<=0.00001) and (abs(new_thetax[2]-thetax[2])<=0.00001)):
            thetax = new_thetax
            break
        else:
            thetax = new_thetax
    rae_x = RAE(data, thetax, 0)
    plot_eq(data,thetax,0,1,rae_x,ep_x)

    #thetas de z
    while(ep_z < 100000):
        ep_z += 1
        new_thetaz = grad_func(data, thetaz, alpha, 2, 1)
        if((abs(new_thetaz[0]-thetaz[0])<=0.00001) and (abs(new_thetaz[1]-thetaz[1])<=0.00001) and (abs(new_thetaz[2]-thetaz[2])<=0.00001)):
            thetaz = new_thetaz
            break
        else:
            thetaz = new_thetaz
    
    rae_z = RAE(data, thetaz, 2)
    plot_eq(data,thetaz,2,1,rae_z,ep_z)
    
    return(thetax , thetaz)

def RAE(data, theta, v):
	d = np.take(data,v,1)
	y = np.take(data,1,1)
	m = np.mean(d)

	sum1 = 0
	sum2 = 0

	for i in range(d.shape[0]):
		sum1 = sum1 + abs(theta[0]+(theta[1]*y[i])+theta[2]*(y[i]**2) - data[i][v])
		sum2 = sum2 + abs(data[i][v] - m)

	return sum1 / sum2    
    
def plot_eq(data,theta,fx, v,rae, ep):
    x = np.take(data,fx,1)
    y = np.take(data,v,1)
    new_x = []
    for i in y:
        val = theta[0]+(theta[1]*i)+theta[2]*(i**2)
        new_x.append(val)
    plt.plot(y,x,"r.")
    plt.plot(y,new_x)
    plt.xlabel('Y')
    if (fx == 0):
        plt.ylabel('X')
        title='x = '
    else:
        plt.ylabel('Z')
        title='z = '
    title += "{:.2f}".format(theta[0])+"+"
    title += "{:.2f}".format(theta[1])+"y+"
    title += "{:.2f}".format(theta[2])+"y^2"
    title += "\nRAE = "+str(rae)
    title += "\nEpochs = "+str(ep)
    plt.title(title)
    plt.show()
    


def main():
    data = f.read_data("kick2.dat")
    #f.plot_data(data)
    #pre_processing
    tx_1, tz_1 =regrassion(data,0.001)
    print("Com alpha = 0,001 - A posição da bola quando ela for atingir o gol (y=0) será x = "+"{:.2f}".format(tx_1[0])+" e z = " "{:.2f}".format(tz_1[0]))
    tx_2, tz_2 =regrassion(data,0.01)
    print("Com alpha = 0,01 - A posição da bola quando ela for atingir o gol (y=0) será x = "+"{:.2f}".format(tx_2[0])+" e z = " "{:.2f}".format(tz_2[0]))
    tx_3, tz_3 =regrassion(data,0.1)
    print("Com alpha = 0,1 - A posição da bola quando ela for atingir o gol (y=0) será x = "+"{:.2f}".format(tx_3[0])+" e z = " "{:.2f}".format(tz_3[0]))
    tx_4, tz_4 =regrassion(data,0.7)
    print("Com alpha = 0,7 - A posição da bola quando ela for atingir o gol (y=0) será x = "+"{:.2f}".format(tx_4[0])+" e z = " "{:.2f}".format(tz_4[0]))

    #Dados normalizados
    scaler = MinMaxScaler()
    min_x = min(data[:,0])
    max_x = max(data[:,0])
    min_z = min(data[:,2])
    max_z = max(data[:,2])
    dataNorm = scaler.fit_transform(data)
    #f.plot_data(dataNorm)
    tx_1, tz_1 =regrassion(dataNorm,0.001)
    print("Com alpha = 0,001 - A posição da bola quando ela for atingir o gol (y=0) será x = "+"{:.2f}".format(tx_1[0])+" e z = " "{:.2f}".format(tz_1[0]))
    tx_2, tz_2 =regrassion(dataNorm,0.01)
    print("Com alpha = 0,01 - A posição da bola quando ela for atingir o gol (y=0) será x = "+"{:.2f}".format(tx_2[0])+" e z = " "{:.2f}".format(tz_2[0]))
    tx_3, tz_3 =regrassion(dataNorm,0.1)
    print("Com alpha = 0,1 - A posição da bola quando ela for atingir o gol (y=0) será x = "+"{:.2f}".format(tx_3[0])+" e z = " "{:.2f}".format(tz_3[0]))
    tx_4, tz_4 =regrassion(dataNorm,0.7)
    print("Com alpha = 0,7 - A posição da bola quando ela for atingir o gol (y=0) será x = "+"{:.2f}".format(tx_4[0])+" e z = " "{:.2f}".format(tz_4[0]))
main()
