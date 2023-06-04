import speedtest
import matplotlib.pyplot as plt
import time
lds=[]
lus=[]
for i in range(5):
    s=speedtest.Speedtest()
    ds=round(s.download()/1000000,2)
    us=round(s.download()/1000000,2)
    lds.append(ds)
    lus.append(us)
    time.sleep(60)
    print(lds)
    print(lus)
x=["1","2","3","4","5"]
plt.plot(x,lds,label="Download Speed")
plt.plot(x,lus,label="Upload Speed")
plt.title("Internet Speed")
plt.legend()
plt.show()
    
    