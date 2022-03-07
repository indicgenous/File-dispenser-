import os
from datetime import datetime , timedelta


def file_dispenser(path,thresh,base= True):
    """This Program works to delete Fils/Folders/Dir.s which are old from the given time.."""

    if os.path.isdir(path):
        for internals in os.listdir(path):
            file_dispenser(path + "/" + internals,thresh,False)
        if (not base) and len(os.listdir(path))==0:
            os.rmdir(path)
        return
    mod = os.path.getmtime(path)
    if thresh>mod:
        os.remove(path)


if __name__ == '__main__':
    threshold=(datetime.now()-timedelta(minutes=0.5)).timestamp()
    file_dispenser("Enter file path or name",threshold)
