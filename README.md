# Welcome To My Python Repository 
![Python Logo](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

**Here you can find a collection of Python examples, tutorials, practicing exercises and more, from basic data types and operators to advanced topics:<br/>**
Strings Numbers and Operators, Variables, Indexing, Slicing, Immutability, Conditions, Loops, Functions, Classes and Objects, Using and Building Modules, Files and Directories, Programming optimized code, Errors and Exceptions, Multi-Threading, Managing SQLite DB, Sockets Programming, Object Oriented Programming, Operator Overloading, Encapsulation & Data Hiding, Inheritance, OS module, Regular Expressions, Debugging in Pycharm

<br/>

# [Python Project](./Python%20Project):
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
When opening the [Server file](./Python%20Project/Server/Server.py) it will be listening for the Client <br/>
When opening the [Client file](./Python%20Project/Client/Client.py) it will ask for a file to read from: [Status1.txt](./Python%20Project/Client/Status1.txt) , [Status2.txt](./Python%20Project/Client/Status2.txt) , [Status3.txt](./Python%20Project/Client/Status3.txt) , a different file name can be entered or to Edit the Status<br/>
[Status Edit](./Python%20Project/Client/Status_Edit.py) gives options to edit any file's ID, alarm or to show the file's content.
