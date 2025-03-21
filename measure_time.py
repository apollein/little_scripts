import argparse
import subprocess
import time
import numpy as np

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('command')
    parser.add_argument("-n", "--times", help="Number of runs.", type=int, required=False)
    args = parser.parse_args()
    if args.times!=None:
        number_of_runs = args.times
    else:
        number_of_runs = 100
    values = []
    for i in range(number_of_runs):
        try:
            start = time.time()
            subprocess.run(args.command, shell=True, check=True, capture_output=True)
            end = time.time()
            values.append((end - start))
        except Exception as e:
            print("Failed on run #{} ({})".format(i, str(e)))
            exit(1)
    print("Mean time: {}".format(np.mean(values)))
    print("Stdev time: {}".format(np.std(values)))