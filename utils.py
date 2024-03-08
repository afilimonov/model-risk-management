import os
import logging

def getLogLevel() -> int:
    # get the log level from an environment variable
    log_level_str = os.environ.get('LOG_LEVEL', 'INFO')

    # convert the log level string to a log level constant
    return getattr(logging, log_level_str.upper(), logging.INFO)

def getLogger(name) -> logging.Logger:
    log_level_str = os.environ.get('LOG_LEVEL', 'INFO')
    log_level_str =  getattr(logging, log_level_str.upper(), logging.INFO)
    logger = logging.getLogger(name)
    logger.setLevel(log_level_str)

    return logger

def read_file(file) -> str:
    with open(file) as f:
        return f.read().strip()
    
def read_files(files) -> str:
    result = ""
    for file in files:
        with open(file, "r") as f:
            result += f.read()
    return result

def read_files_dir(directory) -> dict:
    result = {}
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), "r") as f:
            content = f.read()
            result[filename] = content
    return result

def save_file(file, content):
    with open(file, 'w') as f:
        f.write(content)
