# DumayCloud
Application to backup your files in a secure server encrypted with AES128 with a <a href="#GUI Usage">GUI</a> and an API.

## API Usage
Firstly, import the DumayCloud module and create a client object like this:
```py
import DumayCloud
c = DumayCloud.Client()
```

If an error wan't raised, great! you're good to go!
now you could use either:
```py
c.login(yourusername, yourpassword)
```
or:
```py
c.signup(yourusername, yourpassword, youremail)
```
If signed up for a new acount, **you will not be signed in automaticly**, you will need to login.

#### After logging to your acount you could use the follwing methods: 
----
**Upload from your pc to the cloud:**

you could upload a single file like this:
```py
c.upload(pathtofile)
```
or upload multiple files at a time using:

```py
c.upload([pathtofile, pathtofile2, pathtofile3, etc])
```

----
**Download a file from your cloud file:**
```py
c.download(name_of_file, destination_folder_on_your_pc)
```
beaware that if the file dosen't exist you will be prompted with an exception.

----

**Print your files in the cloud:**
```py
c.getFiles()
```
this will print your files sorted in the ABC order.

----
**Delete a file from your cloud**
```py
c.delteFile(name_of_file)
```

----
**Run a python file in the cloud without using any local resources**
```py
c.runPython(file_name_on_cloud.py, output.txt=None)
```
The run python method recieves the .py file that is **in the server**, runs it without using any resources on your pc
and than either prints the output to your console or saves the output to file(if you provided a path).

----

**Run a linux command to organise your files to folders(ADVANCED)**

*you could use some linux commands like: ```mkdir```, ```mv```, ```rmdir``` and much more using the following commands:*

mkdir statnds for make directory, here is an example:
```py
c.linuxCmd("mkdir catPhotos")
```
you could use mv for moving files to directories:
```py
c.linuxCmd("mv cat.png catPhotos/")
```
or even use advanced mv options, like moving all the files with a certain extention to a folder:
```py
c.linuxCmd("mv *.png catPhotos/")
```
----

## GUI Usage
To open the GUI version, run the controller.py module.
## After opening it, you should see this image:

![loginpage](https://i.imgur.com/L1V0AXk.png)

## After logging in you should be able to see the control panel:

![ControlPanel](https://i.imgur.com/SwKiF0u.png)

