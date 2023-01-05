import glob
import os
import time
import pandas as pd

filelist = []

for path, subdirs, files in os.walk(r'D:/'):
        #filelist.append(os.path.join(path, name))
    for file in files:
        fcreated = time.strftime('%m/%d/%Y %H:%M:%S', time.gmtime(os.path.getctime(os.path.join(path, file)))) 
        fmodified = time.strftime('%m/%d/%Y %H:%M:%S', time.gmtime(os.path.getmtime(os.path.join(path, file)))) 
        fsize = str(round(os.path.getsize(os.path.join(path, file))/1024,0))
        filelist.append(fcreated + ' - ' + fmodified + ' - ' + fsize + ' - ' + os.path.join(path, file))




test = [sub.replace(' - ', ' #-# ', 3) for sub in filelist]
test_df = pd.DataFrame(test, columns=['col1'])
test_df[['created','modified','size','name']] = test_df['col1'].str.split(' #-# ',expand=True)


test_df.to_csv('D:/filelist.csv', index=False)

my_df = pd.DataFrame(filelist, columns=['col1'])
my_df.to_csv('D:/filelist.csv', index=False)

test_df['size'] = test_df['size'].astype(float)
