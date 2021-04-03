# shutil and os are for moving and reading files created by samridhi
import os
import fleep  #to detect magic no and file segragation
import shutil
sub_dir=["image","audio","video","document","archive","executables","font","system","database"]#fleep support these formats
name_of_dir=""
def make_directories(name_of_dir):   #to create new directory
    print(name_of_dir)
    path="./"+name_of_dir
    print(path)
    isExist = os.path.exists(path)
    if isExist:
        print("Directory Exists")
    else:
        os.mkdir(name_of_dir)
    return 1
    # fleep fordetecting file
def identify_file_type(name_of_file):
    global name_of_dir
    fname,fext = os.path.splitext(name_of_file)
    with open(name_of_file, "rb") as file:
        info = fleep.get(file.read(128))
        if(info.extension_matches(fext[1:])):
            for i in sub_dir:
                flag=0
                for j in info.mime:
                    if j.find(i)!=-1:
                        flag=1
                        name_of_dir=i
                        print("directory name is",name_of_dir)
                        break
                if flag==1:
                    break
        else:
            name_of_dir=fext[1:]
            #preprocessing of files to remove spaces to make it readable
def remove_spaces_from_filenames():
    try:
        filenames = os.listdir("./")
        for filename in filenames:
            os.rename(os.path.join("./", filename), os.path.join("./", filename.replace(' ', '-')))
    except Exception:
        pass
     # ct/paste that is moves files to above folders
def move_to_dir(name_of_file,name_of_dir):
    try:
        source=os.path.join("./",name_of_file)
        dest =os.path.join("./",name_of_dir+"/")
        shutil.move(source,dest)
        print("Moved successfully")
    except Exception:
        pass
remove_spaces_from_filenames()  #first fun to calll
with os.scandir('./') as entries:
    counter=0
    for name_of_file in entries:
        path=os.path.join("./",name_of_file)
        fname,fext = os.path.splitext(name_of_file)
        n=fname[2:].strip()+".py"
        #print("path:",path)
        if n=="source.py" or n=="run_automatically.py":
            continue
        if os.path.isdir(path):
            continue
        else:
            print(name_of_file)
            identify_file_type(name_of_file)
            make_directories(name_of_dir)
            move_to_dir(name_of_file,name_of_dir)
            counter+=1
            print("done",counter)
            
     # tool for additional features i.e sequence naming
def multi_rename():
    with os.scandir('./') as entries:
        count=0
        for name_of_file in entries:
            path=os.path.join("./",name_of_file)
            fname,fext = os.path.splitext(name_of_file)
            n=fname[2:].strip()+".py"
            if n=="source.py":
                continue
            dst ="Pattern"+str(count)+fext
            dst =os.path.join("./",dst)
            #src =os.path.join("./",filename)
            os.rename(name_of_file, dst)
            count+=1
#multi_rename()
