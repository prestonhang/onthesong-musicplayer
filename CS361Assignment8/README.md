# CS361Assignment8

song_suggester.py usage:  
python song_suggester.py song_list_path pipe_file_path  
song_list_path should be a string that is a path to a text file that contains the names of the songs. Each song should be on its own line.  
pipe_file_path is the path to the file being used as the commuication pipe.  

<br>

## REQUESTING DATA:
Change the contents of the pipe communication file to "run".   
Example in python (assuming pipe communication file named file_path):  
```
with open(file_path, 'w') as file:
  file.write("run")
```
  
<br>
  
 ## RECEIVING DATA:
 Read the contents of the pipe communication file after a request.  
 Example in python (assuming pipe communication file named file_path):  
 ```
 with open(file_path, 'r') as file:
  data = file.readline()
  ```
  
The variable data now contains the data from the microservice  

## UML
![UML Diagram](/image.png "UML DIAGRAM")
