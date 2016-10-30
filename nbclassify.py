import json
import os
import math
import sys

def NaiveBayes():

    with open('nbmodel.txt', 'r') as handle:
        json_data = [json.loads(line) for line in handle]
    hamProb=json_data[0]
    spamProb=json_data[1]
    recursiveWalk(root,hamProb, spamProb)

def recursiveWalk(root,hamProb, spamProb):
    for dir, subdir, files in os.walk(root):
        if len(subdir) == 0 and len(files) != 0:
            path = os.path.join(dir)
            countFiles(files, path,hamProb, spamProb)

def countFiles(files,path, hamProb, spamProb):
    for file in files:
        if 'txt' in file:
            if file.endswith('.txt'):
                hamValue=0
                spamValue=0
                label=""
                new_path = os.path.join(path + "/" + file)
                lines = open(new_path, 'r', encoding="latin1")
                for line in lines:
                    words = line.split()
                    for word in words:
                        word=word.lower()
                        if word in hamProb:
                            hamValue+=math.log(hamProb[word],10)

                        if word in spamProb:
                            spamValue+=math.log(spamProb[word],10)

                lines.close()
                if(spamValue>=hamValue):
                    label="SPAM"
                elif(spamValue<hamValue):
                    label="HAM"

                docClass[new_path]=label



if __name__=="__main__":
    root = str(sys.argv[1])
    #root="/Users/vchandan/Downloads/Varsha/Spam or Ham/train/"
    hamProb={}
    spamProb={}
    ham=[]
    spam=[]
    docClass={}
    truePos = []
    trueNeg = []
    falsePos = []
    falseNeg = []
    NaiveBayes()


    with open("nboutput.txt","w+") as output:
        for key in docClass:
            output.write(docClass[key]+" "+key+"\n")
    output.close()

