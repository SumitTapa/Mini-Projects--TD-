try:
    _filename=input("Enter the filename that you want to read, with proper file format (e.g. sample.txt): ")
    _rfile = open(_filename, 'r')
    _file = _rfile.readlines()
    _filelen = len(_file)
    for i in range(_filelen):
        print('Line', i + 1, ':', _file[i].strip())
        _rfile.close()
except FileNotFoundError:
    print("Error: The file", _filename,  "not found. Try again.")


