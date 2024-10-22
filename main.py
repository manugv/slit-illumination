

import numpy as np
import matplotlib.pyplot as plt


def geometric_projection(x, x0, deltax):
    xn = x0 + deltax*0.5
    return 1/deltax * (x - xn) * (xn - x)
    

def main():
    x = np.arange(0, 50, 0.1)
    lambd = np.arange(-0.3, 0.301, 0.01)
    x0 = 20
    deltax = 3.4

    # u1
    u1 = geometric_projection(x, x0, deltax)
    
    # u2
    # sigma = 0.1/(2*np.sqrt(2*np.log(2))) # where 0.1 is in nm
    # fact = 1/np.sqrt(2*np.pi*sigma)
    # b = 0.0647  # nm/km
    # u2 = np.zeros((lambd.size, x.size))
    # for i in range(lambd.size):
    #     u2[i,:] = fact*np.exp(-(1/(2*sigma**2))*(-lambd[i] - b*(x0 -x))**2)
        
    # print(u1.size, u2.shape)
    # u = u2*u1                   # 
    # print(u.shape)
    # plt.pcolormesh(lambd,x, u.T)
    # plt.colorbar()

    plt.plot(x, u1)
    plt.show()

    print("Hello from slit-illumination!")


if __name__ == "__main__":
    main()
