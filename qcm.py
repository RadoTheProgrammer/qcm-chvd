FILE="data_vd.txt"





import random
from time import sleep
from sys import stderr
letters=["a","b","c","d"]
commands=["getline","save","stop"]

class Questionnaire:
    def __init__(self,file_data,file_progression):
        self.file_data = file_data
        self.file_progression = file_progression
        
    def go(self):
        
def Random(iterable):
    if isinstance(iterable,int):
        iterable=range(iterable)
    iterable=list(iterable)
    RandomList=[]
    for _ in range(len(iterable)):
            RandomList.append(iterable.pop(random.randint(0,len(iterable)-1)))
    return RandomList
def sstr(string):
    return str([string])[1:-1]
def convert_to_scratch(file=FILE):
    f=open(file)
    lignes=f.readlines()
    f.close()
    while lignes[-1]=="\n":
        del lignes[-1]
    #id=int(data[1])
    nombre_questions=int((len(lignes)+1)/6)
    sdata=""
    idx=0
    for _ in range(nombre_questions):
        sdata+=lignes[idx].strip()+";"
        sdata+=lignes[idx+1].strip()+";"
        sdata+=lignes[idx+2].strip()+";"
        sdata+=lignes[idx+3].strip()+";"
        sdata+=lignes[idx+4].strip()+";;"
        idx+=6
    print(sdata+";"+"\n"*50)
# class Questionnaire:
#     def __init__(self,file,file_progression):
#         self.file=file
#         self.file_progression=file_progression
def continuer(data):
    data=data.split("|")
    file=data[0]
    f=open(file)
    lignes=f.readlines()
    f.close()
    while lignes[-1]=="\n":
        del lignes[-1]
    id=int(data[1])
    nombre_questions=int((len(lignes)+1)/6)-id
    rList=list(map(int,data[2].split(",")))
    setmultrandom=False
    if rList==[-1]:
        RandomList=list(range(nombre_questions))
        random.shuffle(RandomList)
    else:
        RandomList=rList
    data3=list(map(int,data[3].split(",")))
    if data3==[-1]:
        setmultrandom=True
    else:
        setmultrandom=False
        choixmult=data3
        print(choixmult)
    for _ in range(id):
        RandomList.insert(0,None)
    print("Il y a %s questions"%(nombre_questions+id))
    for _ in range(nombre_questions):
        idx=RandomList[id]*6
        print("\n\nQuestion n°"+str(id+1)+"\n"+lignes[idx])
        if setmultrandom:
            choixmult=Random(4)
        setmultrandom=False
        idxletter=0
        for choix in choixmult:
            print(letters[idxletter]+". "+lignes[idx+choix+1].strip())
            #print(choix)
            idxletter+=1
        reponse=None
        while reponse not in [*letters,*commands]:
        
            reponse=input()
            if reponse:
                if reponse not in commands:
                    reponse=reponse[0]
        if reponse==commands[0]:
            print(idx+1)
        elif reponse==commands[1]:
            data=file+"|"+str(id)+"|"+",".join(map(str,RandomList[id:]))+"|"+",".join(map(str,choixmult))
            print(data)
            #print((FILE,id,RandomList[id:],choixmult))
                                                
                                                     
            input()
                #data=""
                #for id in range(len(nombre_questions)):
        elif reponse==commands[2]:
            break
                        
        else:
            setmultrandom=True
            id+=1
            if choixmult[letters.index(reponse)]==0:
                print("Juste")
                sleep(1)
            else:
                stderr.write("Faux\nréponse:%s"%(letters[choixmult.index(0)])+"\n")
                #print("réponse:%s"%(letters[choixmult.index(0)]))
                input()
        #del choixmult
def jouer():
    continuer(FILE+"|0|-1|-1")
    #continuer((file,0,None,None))
print("Pour jouer tapez \"jouer()\"")
