<h3> <p align="center">
AirBnB clone - The console </p</h3>

  
## About the project:
The Airbnb project involves developing a command-line console that serves as a managment system for our project.
the console we have allows users to create, update, and delete instances of classes. The console also provides functionalites for retriving and maniulating data. The Airbnb project mainly focuses on object orented programing.

## storage: 
In this project we were suposed to store 
our data on a Json file
  <p> __file_path: string - path to the JSON file (ex: file.json)</p>
  __objects: dictionary - empty but will store all objects by <class name>.id
  
## console:
  The script defines a class called HBNBCommand that inherits from the cmd.Cmd class. This class defines several methods for interacting with the storage system, including methods for creating, showing, destroying, and listing instances of various classes. The do_quit and do_EOF methods allow the user to exit the program.

## testing:
The test files have to start by test_ inside the tests/test_models/ folders
  and should be executed using this command python3 -m unittest discover tests or you also test file by file using this command python3 -m unittest tests/test_models/test_base_model.py :shipit:
  
  ```diff 
   $ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
  ```
  
 ```diff
   $ python3 -m unittest tests/test_base_model.py

...................................................................................
...................................................................................
.......................
Ran 189 tests in 13.135s

OK
```
  
## our files:

| No. | File               | File Hierarchy                          | Description                                    |
|-----|--------------------|-----------------------------------------|------------------------------------------------|
| 1   | console.py         |                                         | The main console, command interpreter (EOF, all, create, destroy, help, quit, show, update.) |
| 2   | Authors            |                                         | File with the name of Authors                  |                          
| 3   | README.md          |                                         | Readme file proyect                            |
| 4   | '__init__.py'        | models/__init__.py                      | File to mark a directory as a package          |
| 5   | amenity.py         | models/amenity.py                       | The amenity subclass                           |
| 6   | base_model.py      | models/base_model.py                    | Defines all common attributes/methods for other classes |
| 7   | city.py            | models/city.py                           | The city subclass                              |
| 8   | place.py           | models/place.py                          | The place subclass                             |
| 9   | review.py          | models/review.py                         | The review subclass                            |
| 10  | state.py           | models/state.py                          | The state subclass                             |
| 11  | user.py            | models/user.py                           | The user subclass                              |
| 12  | __init__.py        | models/engine/__init__.py                | File to mark a directory as a package          |
| 13  | file_storage.py    | models/engine/file_storage.py            | The file storage class                         |
| 14  | test_amenity.py    | tests/test_models/test_amenity.py        | The unittest module for amenity                |
| 15  | test_base_model.py | tests/test_models/base_model.py          | The unittest module for base model             |
| 16  | test_city.py       | tests/test_models/city.py                | The unittest module for city                   |
| 17  | test_place.py      | tests/test_models/place.py               | The unittest module for place                  |
| 18  | test_review.py     | tests/test_models/review.py              | The unittest module for review                 |
| 19  | test_state.py      | tests/test_models/state.py               | The unittest module for state                  |
| 20  | test_user.py       | tests/test_models/user.py                | The unittest module for user                   |
| 21  | '__init__.py'        | tests/test_models/test_engine/__init__.py | File to mark a directory as a package         |
| 22  | test_file_storage.py| tests/test_models/test_engine/test_file_storage.py | The unittest module for file storage   |


## Commands in terminal

| Command | Description |
| ------ | ------ |
| Quit | Quit the Prompt |
| Help | Display help the console |
| Create | Create New object |
| Show | Show the info object |
| All | Display All objects |
| Update | Update objects |
| Destroy | Destroy Objects |
