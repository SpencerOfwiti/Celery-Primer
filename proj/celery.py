from celery import Celery

app = Celery('proj',
             broker='redis://localhost:6379',
             backend='redis://localhost:6379',
             include=['proj.tasks'])

if __name__ == '__main__':
    app.start()
