from Band_diagram import metal, semiconductor, plot

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
