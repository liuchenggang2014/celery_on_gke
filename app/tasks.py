from celery import Celery
import time
import os

redis_server = os.environ['REDIS_SERVER']

app = Celery('tasks', broker=f'redis://{redis_server}:6379', backend=f'redis://{redis_server}:6379')

@app.task
def reverse(x):
    time.sleep(10)
    return x[::-1]
  

@app.task
def add(x,y):
    time.sleep(2)
    return x+y