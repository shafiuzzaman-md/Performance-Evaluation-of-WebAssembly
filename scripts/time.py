import time
import subprocess
import sys


def main():
    bashCommand = sys.argv[1]
    cmd = bashCommand.split()
    start_time = time.time()
    #main()
    process = subprocess.Popen(cmd,
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
    end_time = time.time()
    time_taken = end_time-start_time
    stdout, stderr = process.communicate()
    print("Time taken to execute:", (time_taken))
    print("Output: ", stdout)
    print("Error: ", stderr)
    

main()
