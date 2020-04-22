import time, os
from os import listdir
from os.path import isfile, join
import json
import shutil


start_time = time.time()
total_time=0

def extractor(fname):

    """ Run for each file and create dictionary of unique domain addresses """
    addr_count={}

    with open(fname, 'rb') as f, open('../outputFiles/junkmail.txt', 'a+') as jfile:
        jfile.write("\n==========" + i + "================\n")

        # remove newline characters
        file_addr = f.read().splitlines()
        for index, line in enumerate(file_addr, start=1):
            try:
                #split by '@'
                t = (line.decode()).split('@')
                if len(t) > 2:
                    jfile.write(str(index) + '\t' + str(line) + '\n')
                else:
                    domain = (t[1]).rstrip()
                    tmp = len(domain.split('.'))

                    if tmp > 1:
                        domain = str((domain.split('.')[0]).lower())
                        if domain in addr_count:
                            addr_count[domain] = addr_count[domain] +1
                        else:
                            addr_count[domain] = 1
                    else:
                        jfile.write(str(index)+'\t'+ str(line) +'\n')
            except:
                jfile.write(str(index)+'\t'+ str(line) +'\n')

    return addr_count


if __name__ == "__main__":

    """ create outputFiles dir """
    if os.path.exists('outputFiles'):
        shutil.rmtree('outputFiles')
        os.mkdir('outputFiles')
    else:
        os.mkdir('outputFiles')

    """ Check addressFiles path and print unique dictionary domains """
    if os.path.exists('addressFiles'):
        onlyfiles = [f for f in listdir('addressFiles') if isfile(join('addressFiles', f))]
        os.chdir('addressFiles')
        f_result={}
        for i in onlyfiles:
            result = extractor(i)
            print("Unique domain addresses count in file {} is {}".format(i, len(result)))
            print("The unique domain addresses count in file {} is {}".format(i, result))
            f_result[i] = result
            result = json.dumps(f_result, sort_keys=True, indent=3)

            with open('../outputFiles/output.json', 'a+') as f:
                f.write(result)
    else:
        print("Folder is empty.")
    file_time = time.time() - start_time
    print("Total time taken by extractor is {} seconds".format(file_time))
    

