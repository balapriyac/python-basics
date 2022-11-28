import time
sleep_times = [3,4,1.5,2,0.75]
string = "How long will this take?"
for sleep_time,word in zip(sleep_times,string.split()):
    print(word)
    time.sleep(sleep_time)
