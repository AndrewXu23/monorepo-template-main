# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

In many standard libraries (like the C++ Standard Template Library or Python's built-in list method), the pop operation not only removes an element but also returns it. This has become a common convention. Therefore, in this context, using pop is not necessarily a "bad" example. Still, for someone unfamiliar with that convention, there might be a mismatch in expectations.

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

They are both collection data types, but they serve different purposes and are based on different underlying data structures. While both dictionaries and lists store collections of data, dictionaries are centered around unique keys mapping to values, and lists are about maintaining an ordered collection of items. The choice between them should be based on the specific requirements of the task at hand.

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

A list allows for random access, meaning you can access any element directly by its index in constant time O(1). In the context of a list implemented as a dynamic array (like Python's list or C++'s std::vector), you can access any element using its index without having to traverse through other elements.

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

While generic container data structures offer significant advantages in terms of flexibility, reusability, and type safety, they also come with challenges related to complexity, potential performance overheads, and usability. Deciding to use them often depends on the specific needs of the project and the familiarity of the development team with generic programming.

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

I will go with CRUD:
**get(url, params=None, kwargs): Used to make a GET request. The name "get" accurately represents the HTTP GET method.

**post(url, data=None, json=None, kwargs): Used for a POST request. The name "post" matches the HTTP POST method.

**put(url, data=None, kwargs): Matches the HTTP PUT method.

**delete(url, kwargs): Matches the HTTP DELETE method.

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

Functions with many arguments can become confusing and potentially error-prone, especially if many of those arguments are of similar types or their order is hard to remember.

Regarding the requests library, from my last training data up to January 2022, the primary functions provided by the API generally accept a handful of commonly-used arguments directly and then rely on **kwargs to capture any additional parameters. Using **kwargs provides flexibility without overloading the function signature with numerous parameters.

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

`**kwargs` is a syntax in Python that allows pass a variable number of keyword arguments to a function. 
 While **kwargs provides flexibility, it should be used judiciously. As with many programming constructs, striking a balance is key. In situations where the benefits outweigh the potential clarity or safety trade-offs, **kwargs can be an excellent tool. Otherwise, it might be better to be more explicit in your function signatures.

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?

    -Why use None as a default:
        Indicates optional features.
        Safeguard against issues with mutable default values.
    -Can default values be other than None?
        Yes, any valid Python value can be a default.
    -Benefits of predetermined default values:
        Simplifies calls for common cases.
        Ensures backward compatibility.
        Provides hints about expected values.
        Reduces caller complexity.
        Offers safer default behavior.
