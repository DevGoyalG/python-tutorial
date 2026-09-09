# shutile module - buit in module, that provides a higher level interface for working with file and directories.
# the name "shutil" is short for shell utility
# it provides a convenient and efficient way to automate tasks that are commonly performed on files and directories.

# some functions :-
# where src = source, dst = destination

# shutil.copy(src, dst)      - Copies a single file to a new file or directory. 
# It copies the file's data and permission bits, but does not preserve metadata like creation and modification timestamps.

# shutil.copy2(src, dst)     - Copies a single file while preserving metadata. 
# It functions exactly like shutil.copy(), but attempts to keep the original file's full metadata intact, including modification and access timestamps.

# shutil.copytree(src, dst)  - Recursively copies an entire directory tree. 
# It duplicates the specified directory along with all of its subdirectories, files, permissions, and metadata to a new target location.

# shutil.move(src, dst)      - Recursively moves a file or directory to a new location. 
# It first attempts to efficiently rename the path on the same filesystem. 
# If the destination is on a different filesystem, it copies the data and then safely deletes the original source.

# shutil.rmtree(src, dst)    - The shutil.rmtree() function in Python is used to delete an entire directory tree recursively. 
# This means it permanently removes a specified directory along with all of its subdirectories, files, and contents.


# GO TO 87-shutil-module FOLDER