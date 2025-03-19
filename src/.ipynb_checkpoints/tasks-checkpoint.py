from celery import Celery 

# The name of the file is recommended to be called as the first part 'task'
app = Celery("tasks", broker = "pyamqp://guest@localhost//",backend="redis://localhost:6379/0")

@app.task
def power(number, power):
    return number ** power