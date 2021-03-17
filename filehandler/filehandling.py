File="world.txt"




    
#append()
Fileobj=open(File,'a')
Fileobj.write('where')
Fileobj.close()


#deleting
#import os
#os.remove('hello.txt')

import os
if os.path.exists("here.txt"):
    os.remove('here.txt')
    print("removed")
else:
    print("no file")
