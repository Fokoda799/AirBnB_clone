# AirBnB Clone Project 
Version: 1.0.0

## Welcome to the AirBnB clone project! 👋

This project aims to build a command-line interpreter to manage AirBnB objects, setting the foundation for a full web application. The primary focus is on developing a serialization/deserialization flow, creating classes for AirBnB objects, and implementing a file storage engine. The project also includes comprehensive unit tests to validate all classes and storage functionalities.

![AirBnB Clone](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240211%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240211T113258Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=927f614ad716881367020f9d78c6c9ce533e0aaefa015c2cc9cb9a83391ea4d2)

## Project Overview

### 1. Parent Class - BaseModel
- A parent class (BaseModel) is implemented to handle initialization, serialization, and deserialization of future instances.
- Establishes a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> File.

### 2. Classes for AirBnB Objects
- Classes for AirBnB objects such as User, State, City, Place, etc., are created, all inheriting from the BaseModel.

### 3. File Storage Engine
- The first abstracted storage engine, File storage, is implemented to store and retrieve objects.

### 4. Command Interpreter
- A command interpreter, similar to a shell but tailored for project-specific use cases.
- Supports operations such as creating new objects, retrieving objects from files or databases, performing operations on objects, updating attributes, and destroying objects.

## Getting Started

### Starting the Console
To initiate the console, use the following command:

```bash
./console.py
```

### Using the Console
After starting the console, type "help + Enter" to see the available commands:

```bash
~$ ./console
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit show all create update destroy
```

### Example Usage
```bash
~$ ./console
(hbnb) create User
a0d668a3-0c9a-4603-9451-f267346a4651
(hbnb) show User a0d668a3-0c9a-4603-9451-f267346a4651
[User] (a0d668a3-0c9a-4603-9451-f267346a4651) {'id': 'a0d668a3-0c9a-4603-9451-f267346a4651', 'created_at': datetime.datetime(2024, 2, 11, 12, 0, 26, 219046), 'updated_at': datetime.datetime(2024, 2, 11, 12, 0, 26, 220339)}
(hbnb) update User a0d668a3-0c9a-4603-9451-f267346a4651 first_name "Betty"
(hbnb) all
["[User] (a0d668a3-0c9a-4603-9451-f267346a4651) {'id': 'a0d668a3-0c9a-4603-9451-f267346a4651', 'created_at': datetime.datetime(2024, 2, 11, 12, 0, 26, 219046), 'updated_at': datetime.datetime(2024, 2, 11, 12, 0, 26, 220339), 'first_name': 'Betty'}"]
(hbnb) destroy User a0d668a3-0c9a-4603-9451-f267346a4651
(hbnb) all
[]
```

Feel free to explore and interact with the commands provided in the console.
