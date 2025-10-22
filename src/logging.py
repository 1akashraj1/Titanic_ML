import os
from datetime import datetime
import time



start_time = datetime.now().strftime('%H_%M_%S')
date = datetime.today().strftime('%Y_%m_%d')

def logger(logging_message):

    file_path = os.path.join(os.getcwd(),'my_logs',f'{date}')
    os.makedirs(file_path,exist_ok=True)
    
    with open(f'my_logs\{date}\{start_time}.txt', 'a') as file:
        file.writelines(f'[{datetime.now()}] {logging_message}{'\n'}')



