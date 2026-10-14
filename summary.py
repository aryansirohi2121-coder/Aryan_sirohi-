import sys

log_file = sys.argv[1]

with open(log_file, 'r') as src, \
     open('error.log', 'a') as err, \
     open('info.log', 'a') as info:
    for line in src:
        if "error" in line:
            err.write(line)
        elif "info" in line:
            info.write(line)