#!/usr/bin/env python
# coding: utf-8

# In[1]:


t = (4,5,6,7,"sudh","kumar")


# In[2]:


t


# In[3]:


l  = [3,4,5,6,7,"sudh"]


# In[4]:


l


# In[5]:


type(t)


# In[6]:


type(l)


# In[7]:


l[0]


# In[8]:


t[0]


# In[9]:


t


# In[10]:


t[-1]


# In[13]:


t[0:3:-1]


# In[14]:


t[4:0:-1]


# In[12]:


l[0:3]


# In[15]:


l


# In[16]:


t


# In[18]:


l[0] = 34


# In[19]:


l


# In[21]:


t[0] = 234


# In[22]:


t = [5,6,7,8]


# In[23]:


t


# In[26]:


t = (4,5,6,7,[2,3,4,5,6] , "sudh",True,4+7j, 45.56, (3,4,5,6,7))


# In[27]:


t


# In[28]:


l = [(3,4,5,6,7) , (4,5,6,7)]


# In[29]:


l


# In[30]:


s= {}


# In[31]:


type(s)


# In[32]:


s1 = {4,5,6}


# In[33]:


type(s1)


# In[36]:


s2 = {2,3,4,5,6,7,89,4,5,5,5,5,5,5,5,"sudh" , "sudh" ,"sudh"}


# In[37]:


s2


# In[38]:


s3 = {"Sudh" , "sudh"}


# In[39]:


s3


# In[40]:


s = {334,454,5454,545,454,545,2342,42,22,3,3424234,448,788767,565}


# In[41]:


s


# In[45]:


s = {"a"  ,"sudh" , "kumar" , 4,5,6,7,34255345,3445455,34535,5345,54}


# In[46]:


s


# In[44]:


s1 = set()


# In[47]:


s


# In[48]:


s[0]


# In[49]:


l1 = list(s)


# In[50]:


l1


# In[56]:


s2 = l1[4:50]
s2


# In[57]:


s = set(s2)


# In[58]:


s


# In[59]:


t


# In[60]:


l = list(t)


# In[61]:


l


# In[62]:


l[0] = 40


# In[63]:


l


# In[64]:


tuple(l)


# In[65]:


d = {}


# In[66]:


type(d)


# In[68]:


d = {"a" :"sudh" , "name":"sudh","number" :23434453 , "mailid" :"sudfff@2sffa.com"}


# In[69]:


d


# In[70]:


d1 = {"name" :"sudh" ,"name" :"kumar"}


# In[72]:


d1


# In[73]:


d1 = {345345 :"sudh" ,"name" :"kumar"}


# In[74]:


d1


# In[75]:


d1 = {4.56 :"sudh" ,"name" :"kumar"}


# In[76]:


d1


# In[77]:


d1 = {_4.56:"sudh" ,"name" :"kumar"}


# In[78]:


d1 = {"_4.56":"sudh" ,"name" :"kumar"}


# In[79]:


d1


# In[80]:


d1 = {#2345:"sudh" ,"name" :"kumar"}


# In[81]:


d1 = {"#fsff":"sudh" ,"name" :"kumar"}


# In[82]:


d1


# In[91]:


d1 = {"#fsff":"sudh" ,"name" :"kumar","n" :[4,5,5,6,7,"sudh",(3,4,5,66)],'t':(3,4,5,6) , "s" :{4,5,6,7,8} , "d" :{"y" : "fsdsf"}}


# In[92]:


d1


# In[93]:


d1 = {"#fsff":"sudh" ,[3,4,5] :"kumar"}


# In[94]:


d1 = {"#fsff":"sudh" ,"U":"kumar" , "N":"kumar"}


# In[95]:


d1


# In[97]:


d1['#fsff']


# In[98]:


d1[0]


# In[99]:


d = {(2,3,4,5) :"sdfasfasf"}


# In[100]:


d


# In[101]:


d = {{4,5,6,7} :"fsdfsf"}


# In[103]:


d = {{'y':"ffsfsf"}:"fsdfsfsfdfd"}


# In[104]:


d = {"dfdf" :"fsdfsf"}


# In[105]:


s = "sudh"


# In[106]:


s[0]


# In[107]:


s[0] = 'v'


# In[108]:


d1 = {"#fsff":"sudh" ,"name" :"kumar","n" :[4,5,5,6,7,"sudh",(3,4,5,66)],'t':(3,4,5,6) , "s" :{4,5,6,7,8} , "d" :{"y" : "fsdsf"}}


# In[109]:


d1


# In[111]:


d1['n'][0]


# In[113]:


d1['t'][2]


# In[115]:


d1["s"][4]


# In[121]:


tuple(d1['s'])[4]


# In[122]:


list(d1['s'])[4]


# In[124]:


d1


# In[126]:


d1['d']['y']


# In[128]:


d1['n'][-1]


# In[129]:


d


# In[130]:


d["name"] = "sudh"


# In[131]:


d


# In[132]:


d["name"] = "sudhfsdfsfsaf"


# In[133]:


d


# In[134]:


d[["fd"]] = "fsdfs"


# In[138]:


d[(4,5,6)] =  "fdsfdsf"


# In[139]:


d


# In[140]:


d[(4,5,6)]


# In[141]:


l = [5,6,7,7,7,8,8,9,0]


# In[142]:


l[0:5]


# In[143]:


for i in l :
    print(i)


# In[160]:


l = [5,6,7,7,"sudh" , (4,5,6,7) ,(45,67,67,6,7), {"name" : "sudh"} , {5,6,7,8} , [1,2,54,5]]


# In[161]:


for i in l :
    if type(i) == tuple:
        print(i)
        for j in i :
            if j == 6 :
                print(j)


# In[ ]:





# In[156]:


for i in l :
    if type(i) == list:
        for j in i :
            if j == 3 :
                print("yes i am able to get three ")
            else :
                print("no there is no 3 available")


# In[ ]:





# In[145]:


for v  in l :
    print(v)


# In[ ]:





# In[150]:


for v  in l :
    if type(v) == int:
        print(v)


# In[152]:


l[-1][2]


# In[162]:


t = (3,4,5,6)


# In[163]:


for i in t :
    print(i)


# In[164]:


s = {5,6,7,8}


# In[165]:


for i in s :
    print(i)


# In[166]:


s1 = "sudhanshu"


# In[168]:


for i in s1:
    print(i)


# In[189]:


s = {4,5,6,7}


# In[190]:


s[0]


# In[191]:


t = (5,6,7,8,899,9,9,9,9,9)


# In[192]:


t[::-1]


# In[ ]:





# In[171]:


d = {"name" :"sudh" , "mail" :"Fsdf s" , "no":[454,54,454,54,5]}
d[]


# In[186]:


for i in d.items():
    if type(i[1])== list:
        print(i[1])
        for j in i[1]:
            if j > 60 :
                print("element" , j )
            else :
                print("fsffs")


# In[187]:


for i in d.items():
    if type(i[1]) == list:
        for j in i[1]:
            if j >60:
                print("elemetn" , j)
            else :
                print("no element lesser then 60 ")
    


# In[172]:


for i in d :
    print(i)


# In[180]:


for i in d.keys():
    if type(d[i])== list:
        print(d[i])
    else :
        print("fsfs ")


# In[176]:


for i in d.values():
    print(i)


# In[ ]:




