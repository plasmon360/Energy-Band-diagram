# Define a semiconductor material model, needs the Conduction band (CB) and Valence band (VB) energy levels
# p_nio = semiconductor(cb=-1.85, vb=-5.49, name='P-NIO')
# PTB7 = semiconductor(cb=-3.5, vb=-5.25, name='PTB7')

class semiconductor():
    def __init__(self,cb,vb, name = None):
        self.vb = vb
        self.cb = cb
        self.type = 'semiconductor'
        self.name = name

# Define a metal material model, needs the work function (wf)
# ITO = metal(wf=-5.2, name='ITO')
class metal():
    def __init__(self,wf, name = None):
        self.wf = wf
        self.type = 'metal'
        self.name = name

# plot the band diagram of stack. Stack is a list of materials, filepath for the file which will store the banddiagram.

def plot(stack, filepath = "Images/test.png"):
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches

    band_width_in_x = 1
    space_between_bands = band_width_in_x+0.15
    text_offset = 0.15

    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')

    limits = [] # For some reason annotations are getting cropped and autoscale is not solving this. I use limits to
                # capture the anotation y positions and use them to determine final y axis limits.

    for i, m in enumerate(stack):
        if m.type == 'semiconductor':
            band_width_in_y = m.cb - m.vb
            y = m.vb
        elif m.type == 'metal':
            band_width_in_y = 0.01 # make it small to look like a line instead of rectangle.
            y = m.wf
        p = patches.Rectangle(
            (0.05 + (i * space_between_bands), y),
            band_width_in_x,
            band_width_in_y,
            fill=False
        )
        rx, ry = p.get_xy()
        cx = rx + p.get_width() / 2.0
        cy = ry + p.get_height() / 2.0
        ax.add_patch(p)


        if m.type == 'semiconductor':
            ax.annotate(m.name, (cx, cy), color='b', weight='bold',fontsize=10, ha='center', va='center')
            ax.annotate(m.cb, (cx, cy + p.get_height() / 2.0 + text_offset), weight='bold', ha='center', va='center', fontsize=10)
            limits.extend([cy + p.get_height() / 2.0 + text_offset])
            ax.annotate(m.vb, (cx, cy - p.get_height() / 2.0 - text_offset), weight='bold', ha='center', va='center', fontsize=10)
            limits.extend([cy - p.get_height() / 2.0 - text_offset])

        elif m.type == 'metal':
            ax.annotate(m.name, (cx, cy + p.get_height() / 2.0 + text_offset), color='b',  weight='bold', ha='center', va='center', fontsize=10)
            ax.annotate('{}'.format(m.wf), (cx, cy - p.get_height() / 2.0 - text_offset),  weight='bold', ha='center', va='center', fontsize=10)
            limits.extend([y - p.get_height() / 2.0 - text_offset])



    ax.autoscale()
    ax.set_ylim([min(limits)*1.2, max(limits)*0.98])
    ax.yaxis.set_ticks_position('left')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(True)
    ax.get_xaxis().set_visible(False)
    plt.tight_layout()
    plt.savefig(filepath, dpi= 80)
    plt.show()

if __name__ == "__main__":

    # # stack 1
    ITO = metal(wf = -5.2, name= 'ITO')
    p_nio = semiconductor(cb = -1.85, vb = -5.49, name = 'P-NIO')
    p3HT = semiconductor(cb = -3, vb = -5.0, name = 'P3HT')
    PCBM = semiconductor(cb = -4, vb = -6.5, name = 'PCBM')
    ZnO = semiconductor(cb = -4.2, vb = -7.5, name = 'ZnO')
    LiF_Al = metal(wf=-3.7, name = 'LiF/Al')

    stack = [ITO,p_nio,p3HT,PCBM,ZnO,LiF_Al]
    plot(stack, filepath = 'Images/Stack1.png')


    # # Stack 2
    Graphene= metal(wf = -4.5, name = 'Graphene')
    PEDOT = semiconductor(cb = -2.2, vb = -5.2, name = 'PEDOT')
    CuPC = semiconductor(cb = -3.3, vb = -5.2, name = 'CUPc')
    C60 = semiconductor(cb = -4, vb = -6.2, name = 'C60')
    BCP = semiconductor(cb = -3, vb = -6.4, name = 'BCP')
    Al = metal(wf = -4.3, name = 'Al')

    stack =[Graphene, PEDOT, CuPC,C60, BCP, Al ]
    plot(stack, filepath = 'Images/Stack2.png')



    # Stack 3
    ITO = metal(wf=-4.7, name='ITO')
    Zno = semiconductor(cb=-4.25, vb=-7.4, name='ZnO')
    AgBiS2 = semiconductor(cb=-3.8, vb=-5.1, name='AgBiS2')
    PTB7 = semiconductor(cb=-3.5, vb=-5.25, name='PTB7')
    niox = semiconductor(cb=-1.85, vb=-5.49, name='NioX')
    moo3 = metal(wf=-5.4, name='MoO3')
    Ag = metal(wf=-4.6, name='Ag')

    stack = [ITO, Zno, AgBiS2, PTB7, niox, moo3, Ag]
    plot(stack, filepath='Images/Stack3.png')












