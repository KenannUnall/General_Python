#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[2]:


plt.plot([1,2,3,4], [1,4,9,16])


# In[4]:


x = [1,2,3,4]
y = [1,4,9,16]


plt.plot(x,y)
plt.show()


# In[5]:


plt.title("İlk grafiğimiz!")
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.plot(x,y)
plt.show()


# In[6]:



plt.xticks([1,2,3,4])   #küsüratları da gösterebilir!
plt.yticks([1,4,9,16])
plt.title("İlk grafiğimiz!")
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.plot(x,y)
plt.show()


# In[8]:


plt.plot(x,y, label='x^2', color='green')
plt.xticks([1,2,3,4,5])   
plt.yticks([1,4,9,16,25])
plt.title("İlk grafiğimiz!")
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.show()


# In[9]:


# linewidth ekleme
plt.plot(x,y, label='x^2', color='blue', linewidth = 2, linestyle = '--', marker='.')
plt.xticks([1,2,3,4,5])   
plt.yticks([1,4,9,16,25])
plt.title("İlk grafiğimiz!")
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.show()


# In[10]:


plt.plot(x,y, label='x^2', color='green', linewidth = 2, linestyle = '--', marker='.')
plt.xticks([0,1,2,3,4,5])   
plt.yticks([0,1,4,9,16,25])
plt.title("İlk grafiğimiz!")
plt.xlabel('x axis')
plt.ylabel('y axis')


x2 = np.arange(0,5,0.5)
plt.plot(x2,x2*2,color='red', linewidth = 2, marker='.', label='2*x')

plt.legend()
plt.show()


# In[11]:


plt.plot(x,y, label='x^2', color='green', linewidth = 2, linestyle = '--', marker='.')
plt.xticks([0,1,2,3,4,5])   
plt.yticks([0,1,4,9,16,25])
plt.title("İlk grafiğimiz!")
plt.xlabel('x axis')
plt.ylabel('y axis')


x2 = np.arange(0,5,0.5)
plt.plot(x2,x2*2,color='red', linewidth = 2, marker='.', label='2*x')

plt.legend()

plt.savefig('ilkgrafigim.png', dpi=300)

plt.show()


# <H3>Barchart</H3>

# In[12]:


x = ['Ankara', 'İstanbul', 'İzmir']
y = [120, 178, 87]

plt.bar(x,y)
plt.show()


# In[12]:



x = ['Ankara', 'İstanbul', 'İzmir']
y = [120, 178, 87]

cubuklar = plt.bar(x,y)
cubuklar[1].set_hatch('/')
cubuklar[0].set_hatch('.')
cubbuklar[2]
plt.show()


# <H1> Detaylı Örnekler </H1>
# 

# In[23]:


gas = pd.read_csv('petrolfiyatlari.csv')

gas


# In[26]:


plt.title('Petrol Fiyatları')
plt.plot(gas['Year'], gas['USA'], 'b-', label='USA')

plt.xlabel('Yıl')
plt.ylabel('Dolar')

plt.legend()
plt.show()


# In[28]:



plt.title('Petrol Fiyatları')

plt.plot(gas.Year, gas.USA, 'b-', label='USA')
plt.plot(gas.Year, gas.Canada, 'r-', label="Kanada")
plt.plot(gas.Year, gas['South Korea'], 'g.-', label='Güney Kore')
plt.plot(gas.Year, gas['France'], 'y.-', label='Fransa')
plt.plot(gas['Year'], gas.Germany, color='brown', label='Germany')

plt.xlabel('Yıl')
plt.ylabel('Dolar')

plt.legend()

plt.show()


# In[35]:


plt.figure(figsize=(14,5))
plt.title('Petrol Fiyatları')

plt.plot(gas.Year, gas.USA, 'b-', label='USA')
plt.plot(gas.Year, gas['Canada'], 'r-', label="Kanada")
plt.plot(gas.Year, gas['South Korea'], 'g.-', label='Güney Kore')
plt.plot(gas.Year, gas['France'], 'y.-', label='Fransa')


plt.xlabel('Yıl')
plt.ylabel('Dolar')

plt.legend()
plt.savefig('ikincigrafigim.png', dpi=300)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




