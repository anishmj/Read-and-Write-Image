#!/usr/bin/env python
# coding: utf-8

# In[8]:


import cv2
color = cv2.imread('ex1.jpg',1)
cv2.imshow("Colour",color)
cv2.waitKey(0)


# In[9]:


import cv2
gray=cv2.imread('ex1.jpg',0)
cv2.imshow('BLACK_WHITE',gray)
cv2.waitKey()


# In[14]:


## SHAPE OF AN IMAGE
import cv2
img=cv2.imread('ex1.jpg',1)
print(img.shape)


# In[12]:


#WRITING AN IMAGE
import cv2
img=cv2.imread('ex1.jpg',1)
cv2.imwrite('ship.jpg',img)


# In[10]:


import cv2
img=cv2.imread('ex1.jpg',-1)
for i in range(100,250):
    for j in range(100,500):
        img[i][j]=[255,255,255] 
cv2.imshow('access rows & columns',img);
cv2.waitKey(0)
cv2.destroyAllWindows()
    


# In[13]:



import cv2
img1=cv2.imread('ex1.jpg',-1)
cut=img1[150:250,250:450]
img1[100:200,200:400]=cut
cv2.imshow('copy & paste',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




