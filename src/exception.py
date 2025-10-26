import sys
from src.logging import logger
import time



def raise_error_message(error_message,error_detail:sys):
    _, _, exec_tb = error_detail.exc_info()

    file_name = exec_tb.tb_frame.f_code.co_filename
    message = "The error occured in the script {0}, line no. {1} with message {2}".format(file_name, exec_tb.tb_lineno, str(error_message))

    return message

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        logger('calling the error message')
        self.error_message = raise_error_message(error_message,error_details)


    def __str__(self):
        return self.error_message
    
