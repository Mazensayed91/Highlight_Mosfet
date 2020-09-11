#!/usr/bin/env python
# coding: utf-8

# In[27]:


import schemdraw
import schemdraw.elements as elm
from schemdraw.segments import *
from helper_customized_elements import *

file = open("mosfet_tobe_highlighted.txt","r")

mosfet_number = int(file.read()[-1]) - 1

colors = ['blue' for i in range(0,6)]
colors[mosfet_number] = 'red'


# In[28]:


d = schemdraw.Drawing()
left_mosfet = d.here

mosfets_label_color = 'blue'

# Drawing The Supply
d.add(elm.Line)
d.add(elm.Line).add_label('VDD',color = 'blue',fontsize=10)
d.add(elm.Line())

# Drawing the right mosfet
right_mosfet = d.here
d.add(elm.Line('right',l=d.unit/8,at=left_mosfet))
x=d.here
mosfetm5a = PMOS(anchor='source',at=x)
d.add(mosfetm5a).add_label("M5a",color=colors[4],loc ='lft',fontsize=10)
d.push()
mosfet4a = PMOS(anchor='source',at = (mosfetm5a,'drain'))
d.add(mosfet4a).add_label("M4a",color=colors[3],loc ='lft',fontsize=10)
d.add(Bias(bias = True,at = (mosfet4a,'gate'))).add_label("Vcascp",color=mosfets_label_color,loc ='rgt',fontsize=10)
d.add(elm.Line('down',at = (mosfet4a,'drain'),l=d.unit/8))
d.add(elm.Dot)
x = d.here
d.add(elm.Line('left',l=d.unit/8)).add_label('Vout-',color = 'blue',loc = "lft",fontsize=10)
d.add(elm.Line('down',at = x,l=d.unit/4)).add_label('Ibias',color = 'blue',fontsize=8)

mosfet3a = NMOS(anchor='drain',d = 'right')
d.add(mosfet3a).add_label("M3a",color=colors[2],loc ='lft',fontsize=10)
d.add(elm.Line('down',at = (mosfet3a,'source'),l=d.unit/12))
d.add(elm.Dot)
m1a_drain = d.here
# bias m3a
d.add(Bias(bias = True,at = (mosfet3a,'gate'))).add_label('Vcasn',color = 'blue',fontsize=10,loc= 'rgt',ofst = [0.6])

d.add(elm.Line('down',at = d.here,l=d.unit/12))
mosfet2a = NMOS(anchor = 'drain', at=d.here,d='right')
d.add(mosfet2a).add_label("M2a",color=colors[1],loc ='lft',fontsize=10)
d.add(elm.Line(at=(mosfet2a,'source'),l=d.unit/8))
d.add(elm.Ground())

#Drawing the left mosfets
d.add(elm.Line('right',l=d.unit/8,at=right_mosfet))
x = d.here
mosfetm5b = PMOS(anchor='source',at=x)
d.add(mosfetm5b).add_label("M5b",color=colors[4],loc ='rgt',fontsize=10)
d.push()
mosfet4b = PMOS(anchor='source',at = (mosfetm5b,'drain'))
d.add(mosfet4b).add_label("M4b",color=colors[3],loc ='lft',fontsize=10)
d.add(Bias(bias = True,at = (mosfet4b,'gate'))).add_label("Vcascp",color=mosfets_label_color,loc ='rgt',fontsize=10)

d.add(elm.Line('down',at = (mosfet4b,'drain'),l=d.unit/8))
d.add(elm.Dot)
x = d.here
d.add(elm.Line('right',l=d.unit/8)).add_label('Vout+',color = 'blue',loc = "rgt",fontsize=10)
d.add(elm.Line('down',at = x,l=d.unit/4)).add_label('Ibias',color = 'blue',fontsize=8)

mosfet3b = NMOS(anchor='drain',d = 'right')
d.add(mosfet3b).add_label("M3b",color=colors[2],loc ='lft',fontsize=10)
d.add(elm.Line('down',at = (mosfet3b,'source'),l=d.unit/12))
d.add(elm.Dot)
m1b_drain = d.here
# bias m3b
d.add(Bias(bias = True,at = (mosfet3b,'gate'))).add_label('Vcasn',color = 'blue',fontsize=10,loc= 'rgt',ofst = [0.6])

d.add(elm.Line('down',at = d.here,l=d.unit/12))
mosfet2b = NMOS(anchor = 'drain', at=d.here,d='right')
d.add(mosfet2b).add_label("M2b",color=colors[1],loc ='rgt',fontsize=10)
d.add(elm.Line(at=(mosfet2b,'source'),l=d.unit/8))
d.add(elm.Ground())

# biasing M2a and M2b
d.add(elm.Line('right',at = (mosfet2a,'gate')))
left_line = d.here
d.add(elm.Line('left',at = (mosfet2b,'gate')))
d.add(elm.Line('left',at = d.here))
d.add(elm.Dot(at = d.here))
d.add(elm.Line('down',at = d.here,l = d.unit/6))
d.add(Bias(bias = True)).add_label("Vbiasn",color = 'blue',fontsize=10)

# biasing M5a and M5b
d.add(elm.Line('right',at = (mosfetm5a,'gate')))
start_m6 = d.here # useful when drawing m6
d.add(elm.Line('left',at = (mosfetm5b,'gate')))
d.add(elm.Dot(at = d.here))
left_line = d.here

d.add(elm.Line('left',at = d.here))
d.add(elm.Line('down',at = left_line,l = d.unit/6))
d.add(Bias(bias = True)).add_label("Vbiasp",color = 'blue',fontsize=10)


# Drawing M6 branch
d.add(elm.Line('down',at=start_m6, l = d.unit/4)).add_label("2Ibias",color = 'blue',fontsize=8)
mosfet6 = PMOS('right',anchor = 'source',at = d.here)
d.add(mosfet6).add_label("M6",color = colors[5],fontsize=10)
d.add(Bias(bias = True,at = (mosfet6,'gate'))).add_label(loc = 'rgt',label = "Vcmfb",color = 'blue',fontsize=10,ofst=[0.2,0.8])
d.add(elm.Dot(at=(mosfet6,'drain')))
d.add(elm.Line('right',at=(mosfet6,'drain'), l = d.unit/3))
m1b_start = d.here
d.add(elm.Line('left',at=(mosfet6,'drain'), l = d.unit/3))
m1a_start = d.here

#Drawing m1 mosfets
mosfet1b = PMOS('right',anchor = 'source',at=m1b_start)
d.add(mosfet1b).add_label(loc= 'bot',label = "M1b",color = colors[0],fontsize=10)
d.add(Bias(at = (mosfet1b,'gate'))).add_label(loc = 'rgt',label = "Vin-",color = 'blue',fontsize=10)
d.add(elm.Line('down',at=(mosfet1b,'drain'),l = d.unit/2.5))
d.add(elm.Line('left',at=m1b_drain,l = d.unit*1.37)).add_label(label = "Ibias",color = 'blue',fontsize=8)
d.add(Arrow([-2,0],[-2.1,0]))


mosfet1a = PMOS('right',anchor = 'source',at=m1a_start,reverse=True)
d.add(mosfet1a).add_label("M1a",color = colors[0],fontsize=10)
d.add(Bias(at = (mosfet1a,'gate'))).add_label(loc = 'lft',label = "Vin+",color = 'blue',fontsize=10)
d.add(elm.Line('down',at=(mosfet1a,'drain'),l = d.unit/2.5))
d.add(elm.Line('right',at=m1a_drain,l = d.unit*0.97)).add_label(label = "Ibias",color = 'blue',fontsize=8)
d.add(Arrow([-0.7,0],[-0.8,0]))
d.draw()
d.save('schematic.jpg')


# In[ ]:




