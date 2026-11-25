from datetime import datetime
import time

for n in range(10):
    print("hola mon", n)
    f = open("log-prova-job.txt", "a")
    f.write (datetime.today().strftime('%Y-%m-%d %H:%M:%S')+":"+str(n) +'\n')
    f.close()
    time.sleep(2) # Seconds
print("finalitzat", n)