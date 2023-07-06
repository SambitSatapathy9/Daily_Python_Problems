#Problem 10 (06-07-2023)
#Problem Statement: Create 3D surface plot for bowl shaped quadratic function ()
import numpy as np
import matplotlib.pyplot as plt

def quad_func_3d():
  #Create figure and plot with a 3D projection
    fig = plt.figure(figsize = (4,4))
    fig.canvas.toolbar_visible = False #The subsequent lines hide the toolbar, header, and footer of the 
    fig.canvas.header_visible = False  #canvas associated with the figure to remove unnecessary elements from the plot.
    fig.canvas.footer_visible = False
    
    
    #Plot Configuration
    ax = fig.add_subplot(111,projection = '3d')
    """The arguments 111 specify that we want a single subplot in a 1x1 grid.
 For example, if you want a 2x2 grid of subplots, you can use ax = fig.add_subplot(221, 
 projection='3d') for the first subplot, ax = fig.add_subplot(222, projection='3d') for 
 the second subplot, and so on.
"""
    ax.xaxis.set_pane_color((1,1,1,0))#set the color of the background pane to be fully transparent 
    ax.yaxis.set_pane_color((1,1,1,0))#((1.0, 1.0, 1.0, 0.0) represents white with 0% opacity).
    ax.zaxis.set_pane_color((1,1,1,0))
    ax.zaxis.set_rotate_label(False)
    ax.view_init(15,-120)#sets the initial viewing angles for the plot.
    
    #Useful linearspaces to give values to the parameter w and b
    w = np.linspace(-20,20,100)
    b = np.linspace(-20,20,100)
    
    #Get the z value for a bowl shaped cost function
    z = np.zeros((len(w),len(b)))
    j = 0
    for x in w:
        i=0
        for y in b:
            z[i,j] = x**2+ y**2
            i+=1
        j+=1
    
    #Meshgrid used for plotting 3d functions
    W,B = np.meshgrid(w,b)
    #Create 3D surface plot for bowl shaped cost function
    ax.plot_surface(W,B,z,cmap = "Spectral_r",alpha = 0.9,antialiased = False)
    ax.plot_wireframe(W,B,z,color = 'k',alpha = 0.1)
    ax.set_xlabel("$w$")
    ax.set_ylabel("$b$")
    ax.set_zlabel("Cost",rotation = 90)
    ax.set_title("Squared Error Cost used in Linear Regression")
    plt.show()

quad_func_3d()
