import os
import sys
import json


def recursiveWalk(root):
    for dir, subdir, files in os.walk(root):
        if len(subdir)==0 and len(files)!=0 :
             path=os.path.join(dir)
             countFiles(path,files)

    calcProb()

def countFiles(path,files):
    for file in files:
        if 'txt' in file:
            if file.endswith('.txt'):
                new_path=os.path.join(path+"/"+file)
                lines= open(new_path,'r',encoding="latin1")
                for line in lines:
                    words=line.split()
                    for word in words:
                        word = word.strip()
                        word = word.lower()
                        commonWords.append(word)
                        if "ham" in file:
                            ham.append(word)
                            if word in hamWordCount:
                                hamWordCount[word] += 1
                            else:
                                hamWordCount[word] = 1
                                spamWordCount[word]=0

                        elif "spam" in file:
                            spam.append(word)
                            if word in spamWordCount:
                                spamWordCount[word] += 1
                            else:
                                spamWordCount[word] = 1
                                hamWordCount[word]=0

                lines.close()


def calcProb():

    for word in spamWordCount:
        spamWordCount[word]+=1
    for word in hamWordCount:
        hamWordCount[word]+=1
    hamDenom=sum(hamWordCount.values())
    for key in hamWordCount:
        hamProb[key]=hamWordCount[key]/hamDenom

    spamDenom = sum(spamWordCount.values())
    for key in spamWordCount:
        spamProb[key]=spamWordCount[key]/spamDenom

    json.dump(hamProb, open("nbmodel.txt",'w+'))
    with open("nbmodel.txt","a") as model:
        model.write("\n")
    model.close()

    json.dump(spamProb, open("nbmodel.txt",'a'))




if __name__=="__main__":
    spamProb={}
    hamProb={}
    commonWords=[]
    spamWordCount={}
    hamWordCount={}
    ham=[]
    spam=[]
    #root = "/Users/vchandan/Downloads/Varsha/Spam or Ham/train/"
    root = str(sys.argv[1])
    recursiveWalk(root);


