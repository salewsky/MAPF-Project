import multiprocessing

def solving():
    while(True):
        print("Hi")

if __name__ == "__main__":
    p = multiprocessing.Process(target=solving, name="Solving", args=())
    p.start()
    p.join(1)
    if p.is_alive():
        p.terminate()
        p.join
        print("Timeout")
