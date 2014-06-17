import sys

sys.path.append(r'./') 
from store import GFS
gfs = GFS()
gfs.store_2_db("test","test@email.com","12321451234","/root/Downloads/Test_CVs/HenryChai.doc","filetext")
gfs.search_cv("file","text1")
