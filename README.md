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

## Example
![Example image](https://private-user-images.githubusercontent.com/82970354/313541073-5630dd42-636e-402b-bc4b-f00fca3d0f65.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTA3MzI4OTgsIm5iZiI6MTcxMDczMjU5OCwicGF0aCI6Ii84Mjk3MDM1NC8zMTM1NDEwNzMtNTYzMGRkNDItNjM2ZS00MDJiLWJjNGItZjAwZmNhM2QwZjY1LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAzMTglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMzE4VDAzMjk1OFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWI2OGJhMTI3M2VhMjg2MjcwMzhhMWRiOWVjY2NmYzM3ZDJiZWI1NGFmN2ExODkwZDcyNjQ5ODExNmRhMzA3MTImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.bu-CXh29H7yPv2YtpTOYaA6vO6yaWtBRVM8-Wvv_izs)
