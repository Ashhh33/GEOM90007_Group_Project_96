import os, zipfile

dir_name = '/Users/tangxuanjin/Desktop/2022-s2/GEOM90007-IV/Assignment/Group/Bicycle_Volume_Speed_2022'
extension = ".zip"

os.chdir(dir_name) # change directory from working dir to dir with files

for item in os.listdir(dir_name): # loop through items in dir
    if item.endswith(extension): # check for ".zip" extension
        target_dir = './' + item.split('.')[0]
        target_dir = target_dir.split('_')[0]
        os.makedirs(target_dir)

        file_name = os.path.abspath(item) # get full path of files
        zip_ref = zipfile.ZipFile(file_name) # create zipfile object
        zip_ref.extractall(target_dir) # extract file to dir
        zip_ref.close() # close file
        # os.remove(file_name) # delete zipped file