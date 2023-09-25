# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
	- Since MObject lacks the ABC metaclass and doesn’t have any @abstractmethod decorated methods, and can be instantiated, it is not an abstract class based on Python’s definition, despite it not having any implemented methods or attributes.
1. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	- The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	The commented-out __del__ method in the Image class is a method in Python known as a destructor. When un-commented and implemented, it would be invoked when the object is about to be destroyed (when there are no more references to the object), allowing for any necessary cleanup operations, like releasing resources.
1. What class does Texture inherit from?
	- inherits from the Image class. 
1. What methods and attributes does the Texture class inherit from 'Image'? 
	-  inherits all the methods and attributes defined in the Image class.
1. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	- Is-A (Inheritance) Relationship: If a Texture can be considered as a specialized form of an Image, sharing the same essential properties and behaviors but possibly having additional properties, behaviors, or modifications, then an "is-a" relationship would be appropriate.

	- Has-A (Composition) Relationship: If a Texture is fundamentally different in properties or behaviors but utilizes an Image as one of its components, then a "has-a" relationship would be more suitable.

1. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	- Yes, the default constructor takes no arguments except for self, which is the reference to the object being created.

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

ok

1. Are singleton's in Python thread safe? Why or why not?
	Singletons in Python are not inherently thread-safe. When multiple threads are involved, there is a possibility that two or more threads try to create the singleton object at the same time, leading to the creation of multiple instances, which violates the singleton pattern.