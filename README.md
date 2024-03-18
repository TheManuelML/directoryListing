# DirectoryListing
Execute shell commands in the server through the client-side connection to get the index of the files in the system

## Specifications
First execute the **server.py** file and select a valid port to host the server. Then execute the **client.py** file and write the same port where the server is hosted.
Right now the script only works in LANs, but the **ip_get()** function can be modified to accept other IPs.
Also theres the option to modify the **BITYSIZE** variable to change the lenght of the outputs and commands that can be sent and recieve.

This script was made with the pourpuse of practicing python scripting, socket programming and the use of good practices.

## Prepare
```
>> git clone https://github.com/TheManuelML/directoryListing
>> cd directoryListing
```

## Run
If you want to test this script try to open two terminals in your device (one would be the server-side and the other the client-side).
```
Server-side
>> python server.py

Client-side
>> python3 client.py
```
