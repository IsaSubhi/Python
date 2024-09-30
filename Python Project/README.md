# Python Project:
### Description:
The Client reads data from a Status file, connects and sends the data to the Server once every 60 seconds<br/>
The Server will insert the data to a database file
The status file will contain the data of a single station using the following 3 lines<br/>
The first line represents the station ID<br/>
The second line represent the state of Alarm1 (0 for OFF; 1 for ON)<br/>
The third line represent the state of Alarm2 (0 for OFF; 1 for ON)<br/>
The status can be changed while the client is running manually or by using the Status Edit file<br/>
<br/>
### Usage:
When opening the [Server file](./Server/Server.py) it will be listening for the Client <br/>
When opening the [Client file](./Client/Client.py) it will ask for a file to read from: [Status1.txt](./Client/Status1.txt) , [Status2.txt](./Client/Status2.txt) , [Status3.txt](./Client/Status3.txt) , a different file name can be entered or to Edit the Status<br/>
[Status Edit](./Client/Status_Edit.py) gives options to edit any file's ID, alarm or to show the file's content.
