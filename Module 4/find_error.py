import sys
import os
import re

def error_search(log_file):
        error = input("What is the error? ")
        returned_errors = []
        with open(log_file, mode = 'r', encoding='UTF-8') as file:

                for log in file.readlines():
                        error_patterns = ['error']
                        for i in range(len(error.split())):
                                error_patterns.append(r'{}'.format(error.split(' ')[i].lower()))
                        if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                                returned_errors.append(log)
                file.close()
        return returned_errors

def file_output(return_errors):
        #with open(os.path.expanduser('~') + './Module 4/errors_found.log', 'w') as file:
        with open('./Module 4/errors_found.log', 'w') as file:
                for error in returned_errors:
                        file.write(error)
        file.close()

if __name__ == '__main__':
        #log_file = sys.argv[1]
        log_file = './Module 4/fishy.log'
        returned_errors = error_search(log_file)
        file_output(returned_errors)
        sys.exit(0)


### Error will be: CRON ERROR Failed to start