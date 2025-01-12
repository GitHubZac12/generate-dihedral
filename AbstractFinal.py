import matplotlib.pyplot as plt

def Dihedral(n):
    order = 2*n
    order_lst = list(range(order))
    vertices = []
    #create a list of all vertices of the group
    for v in order_lst:
        if v == 0:
            vertices += ["e"]
        elif v == 1:
            vertices += ["r"]
        elif v>1 and v<n:
            vertices += ["r$^{"+str(v)+"}$"]
        elif v == n:
            vertices += ["s"]
        elif v == n+1:
            vertices += ["rs"]
        else:
            vertices += ["r$^{"+str(v-n)+"}$s"]
    #create a blank image to begin plotting vertices and arrows
    plt.figure()
    plt.axis('off')
    plt.xlim(-2, 3)
    plt.ylim(n*-1, 2)
    #dihedral group for all even n
    if n%2 == 0:
        for v in order_lst:
            if v == 0:
                plt.text(0, 0, vertices[v], fontsize=20)
                plt.annotate("", xytext=(0.2, n*0.02), xy=(1, n*0.02), arrowprops=dict(color='black', arrowstyle='->', lw=2))
            elif v>=1 and v<(n/2):
                plt.text(1, (v*-2)+2, vertices[v], fontsize=20)
                plt.annotate("", xytext=(1.05, (v*-2)+1.9), xy=(1.05, (v*-2)+0.6), arrowprops=dict(color='black', arrowstyle='->', lw=2))
            elif v == (n/2):
                plt.text(1, (v*-2)+2, vertices[v], fontsize=20)
                plt.annotate("", xytext=(1, ((v*-2)+2)+(n*0.02)), xy=(0.2, ((v*-2)+2)+(n*0.02)), arrowprops=dict(color='black', arrowstyle='->', lw=2))
            elif v>(n/2) and v<n:
                plt.text(0, (n*-2)+(v*2), vertices[v], fontsize=20)
                plt.annotate("", xytext=(0.05, (n*-2)+(v*2)+0.6), xy=(0.05, (n*-2)+(v*2)+1.9), arrowprops=dict(color='black', arrowstyle='->', lw=2))
            #outer rectangle begins
            elif v == n:
                plt.text(-1, 1, vertices[v], fontsize=20)
                if n == 2:
                    plt.annotate("", xytext=(2, 1.2), xy=(-0.8, 1.2), arrowprops=dict(color='black', arrowstyle='<->', lw=2))
                else:
                    plt.annotate("", xytext=(2, 1.2), xy=(-0.8, 1.2), arrowprops=dict(color='black', arrowstyle='->', lw=2))
                if n > 4:
                    plt.annotate("", xytext=(-0.9, 0.8), xy=(-0.9, -1.25), arrowprops=dict(color='black', arrowstyle='->', lw=2))
                elif n == 4:
                    plt.annotate("", xytext=(-0.9, 0.8), xy=(-0.9, -2.5), arrowprops=dict(color='black', arrowstyle='->', lw=2))
                plt.annotate("", xytext=(-0.8, 0.8), xy=(-0.05, 0.25), arrowprops=dict(color='black', arrowstyle='<->', lw=2))
            elif v == n+1:
                plt.text(2, 1, vertices[v], fontsize=20)
                if n > 4:
                    plt.annotate("", xytext=(2.1, -1.25), xy=(2.1, 0.8), arrowprops=dict(color='black', arrowstyle='->', lw=2))
                elif n == 4:
                    plt.annotate("", xytext=(2.1, -2.5), xy=(2.1, 0.8), arrowprops=dict(color='black', arrowstyle='->', lw=2))
                plt.annotate("", xytext=(1.95, 0.8), xy=(1.2, 0.25), arrowprops=dict(color='black', arrowstyle='<->', lw=2))
            elif v>=(n+2) and v<((3*n)/2):
                plt.text(2, ((v-n)*-2)+2, vertices[v], fontsize=20)
                plt.annotate("", xytext=(1.25, ((v-n)*-2)+2.2), xy=(1.95, ((v-n)*-2)+2.2), arrowprops=dict(color='black', arrowstyle='<->', lw=2))
                if v>=(n+3) and v<((3*n)/2):
                    plt.annotate("", xytext=(2.1, ((v-n)*-2)+2.7), xy=(2.1, ((v-n)*-2)+3.8), arrowprops=dict(color='black', arrowstyle='->', lw=2))
            elif v == (3*n)/2:
                plt.text(2, (n-1)*-1, vertices[v], fontsize=20)
                if n > 4:
                    plt.annotate("", xytext=(2.1, ((n-1)*-1)+0.75), xy=(2.1, ((n-1)*-1)+2.8), arrowprops=dict(color='black', arrowstyle='->', lw=2))
                plt.annotate("", xytext=(1.95, ((n-1)*-1)+0.8), xy=(1.2, ((n-1)*-1)+1.25), arrowprops=dict(color='black', arrowstyle='<->', lw=2))
            elif v == ((3*n)/2)+1:
                plt.text(-1, (n-1)*-1, vertices[v], fontsize=20)
                plt.annotate("", xytext=(-0.6, (n-1.2)*-1), xy=(2, (n-1.2)*-1), arrowprops=dict(color='black', arrowstyle='->', lw=2))
                if n > 4:
                    plt.annotate("", xytext=(-0.9, ((n-1)*-1)+2.8), xy=(-0.9, ((n-1)*-1)+0.75), arrowprops=dict(color='black', arrowstyle='->', lw=2))
                plt.annotate("", xytext=(-0.6, ((n-1)*-1)+0.8), xy=(-0.05, ((n-1)*-1)+1.25), arrowprops=dict(color='black', arrowstyle='<->', lw=2))
            else:
                plt.text(-1, (n*-2)+((v-n)*2), vertices[v], fontsize=20)
                plt.annotate("", xytext=(-0.5, (n*-2)+((v-n)*2)+0.2), xy=(-0.05, (n*-2)+((v-n)*2)+0.2), arrowprops=dict(color='black', arrowstyle='<->', lw=2))
                if v>(((3*n)/2)+2):
                    plt.annotate("", xytext=(-0.9, (n*-2)+((v-n)*2)-0.3), xy=(-0.9, (n*-2)+((v-n)*2)-1.4), arrowprops=dict(color='black', arrowstyle='->', lw=2))
    #dihedral group for all odd n except for 1
    elif (n%2)!=0 and n!=1:
        for v in order_lst:
            if v == 0:
                plt.text(0.5, 0, vertices[v], fontsize=20)
                plt.annotate("", xytext=(0.75, 0), xy=(1, -0.5), arrowprops=dict(color='black', arrowstyle='->', lw=2))
                plt.annotate("", xytext=(0.25, -0.3), xy=(0.5, 0), arrowprops=dict(color='black', arrowstyle='->', lw=2))
                plt.annotate("", xytext=(0.59, 0.4), xy=(0.59, 1.4), arrowprops=dict(color='black', arrowstyle='<->', lw=2))
            elif v>=1 and v<(n/2):
                plt.text(1, (v*-2)+1, vertices[v], fontsize=20)
                if v < ((n/2)-0.5):
                    plt.annotate("", xytext=(1.03, (v*-2)+0.9), xy=(1.03, (v*-2)-0.5), arrowprops=dict(color='black', arrowstyle='->', lw=2))
                    plt.annotate("", xytext=(1.175, (v*-2)+1.1), xy=(1.925, (v*-2)+1.1), arrowprops=dict(color='black', arrowstyle='<->', lw=2))
                if v == ((n/2)-0.5):
                    plt.annotate("", xytext=(0.95, (v*-2)+1.2), xy=(0.275, (v*-2)+1.2), arrowprops=dict(color='black', arrowstyle='->', lw=2))
            elif v>(n/2) and v<n:
                plt.text(0, (n*-2)+(v*2)+1, vertices[v], fontsize=20)
                if v > ((n/2)+0.5):
                    plt.annotate("", xytext=(0.03, (n*-2)+(v*2)-0.5), xy=(0.03, (n*-2)+(v*2)+0.9), arrowprops=dict(color='black', arrowstyle='->', lw=2))
                    plt.annotate("", xytext=(-0.55, (n*-2)+(v*2)+1.1), xy=(-0.05, (n*-2)+(v*2)+1.1), arrowprops=dict(color='black', arrowstyle='<->', lw=2))
            #outer shape begins
            elif v == n:
                plt.text(0.5, 1.5, vertices[v], fontsize=20)
                if n == 3:
                    plt.annotate("", xytext=(2, -1.5), xy=(0.75, 1.5), arrowprops=dict(color='black', arrowstyle='->', lw=2))
                    plt.annotate("", xytext=(0.4, 1.5), xy=(-0.75, -1.5), arrowprops=dict(color='black', arrowstyle='->', lw=2))
                else:
                    plt.annotate("", xytext=(1.95, -0.5), xy=(0.75, 1.5), arrowprops=dict(color='black', arrowstyle='->', lw=2))
                    plt.annotate("", xytext=(0.4, 1.5), xy=(-0.75, -0.2), arrowprops=dict(color='black', arrowstyle='->', lw=2))
            elif v>n and v<(((3*n)/2)-0.5):
                plt.text(2, ((v-n)*-2)+1, vertices[v], fontsize=20)
                if v < (((3*n)/2)-1.5):
                    plt.annotate("", xytext=(2.125, ((v-n)*-2.25)), xy=(2.125, ((v-n)*-2)+0.85), arrowprops=dict(color='black', arrowstyle='->', lw=2))
            elif v == (((3*n)/2)-0.5):
                plt.text(2, ((v-n)*-2), vertices[v], fontsize=20)
                plt.annotate("", xytext=(-0.5, ((v-n)*-2)+0.2), xy=(2, ((v-n)*-2)+0.2), arrowprops=dict(color='black', arrowstyle='->', lw=2))
                plt.annotate("", xytext=(2, ((v-n)*-2)+0.5), xy=(1.15, ((v-n)*-2)+1), arrowprops=dict(color='black', arrowstyle='<->', lw=2))
            elif v == (((3*n)/2)+0.5):
                plt.text(-1, (n*-2)+((v-n)*2), vertices[v], fontsize=20)
                plt.annotate("", xytext=(-0.6, (n*-2)+((v-n)*2)+0.5), xy=(-0.05, (n*-2)+((v-n)*2)+1), arrowprops=dict(color='black', arrowstyle='<->', lw=2))
                if n > 3:
                    plt.annotate("", xytext=(2.125, (n*-2)+((v-n)*2)+0.8), xy=(2.125, (n*-2)+((v-n)*2)+2.8), arrowprops=dict(color='black', arrowstyle='->', lw=2))
                    plt.annotate("", xytext=(-0.95, (n*-2)+((v-n)*2)+2.8), xy=(-0.95, (n*-2)+((v-n)*2)+0.75), arrowprops=dict(color='black', arrowstyle='->', lw=2))
            else:
                plt.text(-1, (n*-2)+((v-n)*2)+1, vertices[v], fontsize=20)
                if v > (((3*n)/2)+1.5):
                    plt.annotate("", xytext=(-0.95, (n*-2)+((v-n)*2)+0.8), xy=(-0.95, (n*-2)+((v-n)*2)-0.3), arrowprops=dict(color='black', arrowstyle='->', lw=2))
    #fixes the special case when n=1
    else:
        vertices[1] = "s"
        for v in order_lst:
            plt.text(v, 0, vertices[v], fontsize=20)
            plt.annotate("", xytext=(0.25, 0.05), xy=(0.95, 0.05), arrowprops=dict(color='black', arrowstyle='<->', lw=2))
    #generate final figure
    plt.show()

Dihedral(10)