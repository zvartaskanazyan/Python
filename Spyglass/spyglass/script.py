import os
import sys

lib_name = sys.argv[1]
output = sys.argv[2]
result = open(output,'w+')
list_dir = os.listdir(os.chdir(lib_name))


for name in list_dir:
    path = os.getcwd()
    if os.path.exists(path + '/' + name + '/spyglass/spyglass.html'):
        with open(path + '/' + name + '/spyglass/spyglass.html') as source:
            text = source.read()
            text = text.replace('Change this by directory name', name)
            result.write(text)
    else:
        print('There is not html file in ' + name + ' directory')
