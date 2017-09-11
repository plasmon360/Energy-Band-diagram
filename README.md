# Energy-Band-digram
The code helps in plotting the energy band diagram of stacks of semiconductors and metals that are commonly used in Solar cell and LED research. 


Example:

    from Band_diagram import metal, semiconductor, plot
    # # stack 1
    ITO = metal(wf = -5.2, name= 'ITO')
    p_nio = semiconductor(cb = -1.85, vb = -5.49, name = 'P-NIO')
    p3HT = semiconductor(cb = -3, vb = -5.0, name = 'P3HT')
    PCBM = semiconductor(cb = -4, vb = -6.5, name = 'PCBM')
    ZnO = semiconductor(cb = -4.2, vb = -7.5, name = 'ZnO')
    LiF_Al = metal(wf=-3.7, name = 'LiF/Al')

    stack = [ITO,p_nio,p3HT,PCBM,ZnO,LiF_Al]
    plot(stack, filepath = 'Images/Stack1.png')

will result in

![alt text](https://user-images.githubusercontent.com/10491839/29846348-647611be-8ccb-11e7-942d-8420256716dc.png)

