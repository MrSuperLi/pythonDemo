from time import sleep
from functools import wraps
import logging
import os
import platform

if platform.platform().startswith('Windows'):
    logging_dir = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'))
    logging_file = os.path.join(logging_dir, 'test.log')
else:
    logging_dir = os.getenv('HOME')
    logging_file = os.path.join(logging_dir, 'test.log')

if not os.path.exists(logging_dir):
    os.mkdir(logging_dir)

print('Logging to', logging_file)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    filename=logging_file,
                    filemode='a')

log = logging.getLogger('retry')


def retry(f):
    @wraps(f)
    def wrapped_f(*args, **kwargs):
        MAX_ATTEMPT = 5
        for attempt in range(1, MAX_ATTEMPT + 1):
            try:
                return f(*args, **kwargs)
            except:
                log.exception('Attempt %s/%s failed : %s', attempt, MAX_ATTEMPT, (args, kwargs))
            sleep(2 * attempt)
        log.critical("All %s attempts failed : %s", MAX_ATTEMPT, (args, kwargs))
    return wrapped_f


counter = 0


@retry
def save_to_database(arg):
    print("Write to a database or make a network call or etc. ")
    print("This will be automatically retried if exception is thrown. ")
    global counter
    counter += 1
    print(counter)
    # 这将在第 一次调用 时抛出 异常
    # 在第 二次运行时将正常工作（ 也就是重试）
    if counter >= 2:
        raise ValueError(arg)
    print('run success')


if __name__ == '__main__':
    save_to_database('Some bad value')
    save_to_database('Some bad value')
