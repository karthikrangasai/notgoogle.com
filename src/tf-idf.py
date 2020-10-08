#TF - IDF Scores

#Importing necessary libraries
import math

#Function to compute Term Frequency
def computeTF(wordDict):
        tfDict = {}
        wordcount=0
        for key,val in wordDict.items():
        	wordcount+=val
        for key,val in wordDict.items():
                tfDict[key] = val/float(wordcount)
        return tfDict

#Function to compute Inverse Document Frequency
def computeIDF(docList):
    idfDict = {}
    N = len(docList)
    idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
            for word, val in doc.items():
                if val>0:
                    idfDict[word] += 1
    for word, val in idfDict.items():
        idfDict[word] = math.log10(N / float(val))
    return idfDict

#Function to compute  Tf-Idf Matrix
def computeTFIDF(tfs, idfs):
    tfidf = {}
    for word,val in tfs.items():
        tfidf[word] = val*idfs[word]
    return tfidf

# Sample Data
s1_text="A mathematician found a solution to the problem"
s2_text="The problem was solved by a young mathematician"
s1_dict={}
s2_dict={}
distinct=[] #(distinct words in corpus)

#Preprocessing

#Splitting Sentences to Words
s1=s1_text.split(" ")
s2=s2_text.split(" ")

#Build Term Frequency Vectors
for i in s1:
    if(i not in distinct):
        s1_dict[i]=0
        s2_dict[i]=0
        distinct.append(i)
    s1_dict[i]+=1
for i in s2:
    if(i not in distinct):
        s1_dict[i]=0
        s2_dict[i]=0
        distinct.append(i)
    s2_dict[i]+=1
print("Dictionary for DOC1")
print(s1_dict)
print("Dictionary for DOC2")
print(s2_dict)
print("TF for DOC1")
print(computeTF(s1_dict))
print("TF for DOC2")
print(computeTF(s2_dict))

#Build Inverse Document Frequency Vector
doc_list=[s1_dict,s2_dict]
print("IDF in General")
print(computeIDF(doc_list))

#Build Tf-Idf matrix
tf_idf_vector=[]
for i in range(len(distinct)):
    temp=[0,0]
    tf_idf_vector.append(temp)
j=0
for doc in doc_list:
    temp_dict=computeTFIDF(computeTF(doc),computeIDF(doc_list))
    for i in range(len(distinct)):
        tf_idf_vector[i][j]=temp_dict[distinct[i]]
    j+=1
for i in tf_idf_vector:
    print(i)
