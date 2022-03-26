
import threading
import time
import os
import shutil
import yaml
from datetime import timedelta
import signal

K32SIZE=108000000000

def readConfig():
    with open(r'config.yaml') as file:
        dataDict = yaml.load(file, Loader=yaml.FullLoader)
    pollintTime=dataDict['pollingTime']
    dirsList=dataDict['destDirs']
    dirsDict={dirsList[i] : 0 for i in range(len(dirsList))}   
    return pollintTime,dirsDict

def printLog(text):
    print("{} - {}".format(time.ctime(),text))
    
def worker():
    files = [os.path.join(path, file) for file in os.listdir(path)]
    plots=[]
    for f in files:
        if f.endswith(".plot"):
            plots.append(f)
    printLog("Encontrados {} plots".format(len(plots)))
    
    for plot in plots:
        best_location = min(dic, key=dic.get)
                   
        if shutil.disk_usage(best_location).free > K32SIZE:
            finalPath=os.path.join(best_location,os.path.basename(plot))
            printLog("Moviendo {} de {} a {}".format(os.path.basename(plot),plot,finalPath))

            try:
                shutil.move(plot,finalPath)
                dic[best_location]+=1
            except:
                printLog("ERROR")


class Job(threading.Thread):
    def __init__(self, interval, execute, *args, **kwargs):
        threading.Thread.__init__(self)
        self.daemon = False
        self.stopped = threading.Event()
        self.interval = interval
        self.execute = execute
        self.args = args
        self.kwargs = kwargs

    def stop(self):
        self.stopped.set()
        self.join()

    def run(self):
        while not self.stopped.wait(self.interval.total_seconds()):
            self.execute(*self.args, **self.kwargs)
    
if __name__ == "__main__":
    path=os.getcwd()
    printLog("Analizando: {}".format(path))

    pollingTime,dic=readConfig()    
    pollingTime=pollingTime[0]
    worker()

    job = Job(interval=timedelta(seconds=pollingTime), execute=worker)
    job.start()
    
#    while True:
#        try:
#            pass
#        except KeyboardInterrupt:
            