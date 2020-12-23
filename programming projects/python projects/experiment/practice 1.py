import time
def counting():
    counting = True
    for i in range(100):
        print(i+1)
        time.sleep(1)
        if i == 5-1:
            return
counting()



