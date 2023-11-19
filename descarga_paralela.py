
import requests
import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process

def descarga(url) -> bool:
    response = requests.get(url)

    if response.status_code != 200:
        return False
    
    with open(f'./descargas/{url.split("/")[-1]}', 'wb') as f:
        f.write(response.content)
    
    return True

def descarga_serial(l):

    for url in l:
        descarga(url)

def descarga_threads(l):
    threads=[]
    for url in l:
        t=Thread(target=descarga, args=(url,))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    

def descarga_threadPool(l):
    workers=10
    with ThreadPoolExecutor (max_workers=workers) as executor:
        for url in l:
            executor.submit(descarga_serial,url)

def descarga_multiprocessing(l):
    processes=[]
    for url in l:
        p=Process(target=descarga, args=(url,))
        p.start()
        processes.append(p)
    for process in processes:
        process.join()

if __name__ == '__main__':

    def arreglo_urls(a,b):
        l=[]
        for i in range(a, b+1):
            l.append(f'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/{i:02d}.png')
        return l

    l=arreglo_urls(1,10)

    inicio=time.perf_counter()
    descarga_serial(l)
    fin=time.perf_counter()
    print(f"Tiempo de ejecucion serial {fin-inicio}")

    inicio1=time.perf_counter()
    descarga_threads(l)
    fin1=time.perf_counter()
    print(f"Tiempo de ejecucion con threads {fin1-inicio1}")

    inicio2=time.perf_counter()
    descarga_threadPool(l)
    fin2=time.perf_counter()
    print(f"Tiempo de ejecucion con threadpool {fin2-inicio2}")

    inicio3=time.perf_counter()
    descarga_multiprocessing(l)
    fin3=time.perf_counter()
    print(f"Tiempo de ejecucion multiprocessing {fin3-inicio3}")



