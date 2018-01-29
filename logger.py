import os
import platform
import logging

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

logging.debug('Start of the program')
logging.info('Doing something')
logging.warning('Dying now')
