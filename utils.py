def read_file(file):
    with open(file) as f:
        return f.read().strip()
    
def read_files(files):
    result = ""
    for file in files:
        with open(file, "r") as f:
            result += f.read()
    return result

def read_files_dir(directory):
    result = ""
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), "r") as f:
            result += f.read()
    return result
