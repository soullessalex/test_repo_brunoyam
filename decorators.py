import time


def run_with_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
    return wrapper

def common_function(*arg, **kw):
    pass


@run_with_time
def action(name):
    print(name)
    return [i for i in range(1000000)]

# run_with_time(action)('hello')

action('hello')

