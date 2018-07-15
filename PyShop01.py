
# coding: utf-8

# In[1]:


data='''
NOTIFY * HTTP/1.1
HOST: 239.255.255.250:1900
CACHE-CONTROL: max-age=60
LOCATION: http://172.24.1.1:5000/rootDesc.xml
SERVER: OpenWRT/OpenWrt UPnP/1.1 MiniUPnPd/2.0
NT: urn:schemas-upnp-org:device:InternetGatewayDevice:1
USN: uuid:160a13d7-926e-4103-b6c6-3b34570c2921::urn:schemas-upnp-org:device:InternetGatewayDevice:1
NTS: ssdp:alive
OPT: "http://schemas.upnp.org/upnp/1/0/"; ns=01
01-NLS: 1530181145
BOOTID.UPNP.ORG: 1530181145
CONFIGID.UPNP.ORG: 1337
'''


# In[13]:


# FIND URL 

import re

url=list(re.findall('http://[a-z0-9\./]*',data))

for i in url:
    print(i)


# In[12]:


# FIND UUID

if 'uuid' in data:
    print(re.findall('[a-z0-9\-]{36}',data))


# In[ ]:


# FIND IP ADDRESS ?

