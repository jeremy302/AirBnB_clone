# AirBnB clone - The console

This project is the first stage on  building a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data, and the console commands allow the user to create, update, destroy ... objects, and manage file storage. Using a system of JSON serialization/deserialization.

## How to Use

1. After cloning the repository locate the "console.py" file (at the root of the repo) and run it 
```
AirBnB_clone$ ./console.py 
```
Then a promp will appear like this
```
(hbnb)
```
Now u can Use our built in commands

### Commands

|     command      |       Description       |        Usage       |
|:-----------------|:-----------------------:|:-------------------:|
| EOF  |  the EOF exits the program   |    EOF     |
| all  |  Prints all string representation of all instances based or not on the class name| all *className*  |
| count|  counts how many instances of class created and saved| count *className* |
| create| creates a new instance of the class passed as argument| create *className* |
| destroy| Deletes an instance based on the class name and id| destroy *className* *objectId*|
| help | List available commands with "help" or detailed help with "help cmd"| help *cmd*|
| quit | The quit command exits the program | quit |
| show | prints the string representation of an instance | show *className* *objectId* |
| update| Updates an object's attributes | update *className* *id* *attName* *attVal*|

### Alternative Syntax
Also you can run the commands [count, show, destroy, update, all] in this format too: 
```
<class name>.<command>([<id> [<*args> or <**kwargs>]])
```

## Examples

### Syntax 1
##### Create Object
Usage: create <class_name>
```
(hbnb) create User
cb8562e5-82c1-4cb8-9d58-06c0fe3e0c98
(hbnb)  
```

##### Show string represenation of an object
Usage: show <class_name> <_id>
```
(hbnb) show User cb8562e5-82c1-4cb8-9d58-06c0fe3e0c98
[User] (cb8562e5-82c1-4cb8-9d58-06c0fe3e0c98) {'id': 'cb8562e5-82c1-4cb8-9d58-06c0fe3e0c98', 'created_at': datetime.datetime(2021, 11, 9, 17, 8, 45, 23018), 'updated_at': datetime.datetime(2021, 11, 9, 17, 8, 45, 23018)}
(hbnb) 
```

##### Destro object
Usage: destroy <class_name> <_id>
```
(hbnb) destroy User cb8562e5-82c1-4cb8-9d58-06c0fe3e0c98
(hbnb) show User cb8562e5-82c1-4cb8-9d58-06c0fe3e0c98
** no instance found **
(hbnb) 
```

### Syntax 2
##### Show all instances of class User
Usage: <class_name>.all()
```
(hbnb) User.all()
["[User] (d59dc247-6307-46b8-9e3e-9c241493838b) {'id': 'd59dc247-6307-46b8-9e3e-9c241493838b', 'created_at': datetime.datetime(2021, 11, 9, 14, 16, 45, 138082), 'updated_at': datetime.datetime(2021, 11, 9, 14, 45, 34, 287408), 'first_name': 'betty'}", "[User] (eceae679-ed06-4f47-90f4-1ffa157b3410) {'id': 'eceae679-ed06-4f47-90f4-1ffa157b3410', 'created_at': datetime.datetime(2021, 11, 9, 14, 17, 24, 456980), 'updated_at': datetime.datetime(2021, 11, 9, 14, 17, 24, 456980)}", "[User] (a80a69d0-4c72-4c0d-8184-a6b24042ff8b) {'id': 'a80a69d0-4c72-4c0d-8184-a6b24042ff8b', 'created_at': datetime.datetime(2021, 11, 9, 14, 17, 39, 881359), 'updated_at': datetime.datetime(2021, 11, 9, 14, 17, 39, 881359)}"]
(hbnb) 
```

##### Destroy a User Instance
Usage: <class_name>.destroy(<_id>)
```
(hbnb) User.destroy(d59dc247-6307-46b8-9e3e-9c241493838b)
(hbnb) User.show(d59dc247-6307-46b8-9e3e-9c241493838b)
** no instance found **
(hbnb) 
```

##### Update an object's attribute
Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>)
```
(hbnb) User.update(eceae679-ed06-4f47-90f4-1ffa157b3410, first-name, tutorial)
(hbnb) User.show(eceae679-ed06-4f47-90f4-1ffa157b3410)
[User] (eceae679-ed06-4f47-90f4-1ffa157b3410) {'id': 'eceae679-ed06-4f47-90f4-1ffa157b3410', 'created_at': datetime.datetime(2021, 11, 9, 14, 17, 24, 456980), 'updated_at': datetime.datetime(2021, 11, 9, 17, 16, 40, 617514), 'first-name': 'tutorial'}
(hbnb) 
```
