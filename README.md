# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

I completed the starter Python project using a network device and managed switch example. The code demonstrated inheritance, class and instance namespaces, and how copying objects affected nested data. I kept the original TODO labels visible in the Python file.

## Implementation

I created `ParentClass` to represent a network device with a hostname and IP address. It included a shared `device_category` class variable, a constructor, a `display_info()` method, and a `__str__()` special method for readable output.

I created `ChildClass` to represent a managed switch. It inherited the device information, added a shared `vendor` class variable, and stored its location and a list of ports. Its overridden `display_info()` included the additional switch information. The `add_port()` method stored dictionaries containing port numbers and nested VLAN settings. I initialized port lists separately so different switches would not accidentally share the same list.

## Namespaces and copying

I created two switches and accessed the shared `vendor` value through both the class and an object. I then attached a maintenance ticket to just one switch and printed both objects' `__dict__` values. This showed that an attribute added to one instance did not automatically appear on another. I also printed the child class namespace keys.

I demonstrated shallow and deep copying with a switch containing a nested port configuration. After changing the original port's VLAN, the shallow copy reflected the new value because the nested list and dictionaries were shared. The deep copy retained its original VLAN because its nested objects were independent.

## Testing and edge cases

I tested a switch with no ports and verified that its list started empty. I also attempted to add a zero-numbered port, an out-of-range VLAN, and a duplicate port. The program caught those cases with `ValueError`, printed an explanation, and continued running. Assertions checked that the copy behavior was correct and that invalid operations did not add any extra ports.

The port list required more memory as ports were added. Adding a port was generally inexpensive, but checking whether a port number already existed required scanning the list, so the duplicate check became slower as the list grew. A dictionary keyed by port number would have been more efficient for a large switch inventory.

## Real-world application

I chose a switch configuration example because it related to maintaining network infrastructure. Reusing a common network device class reduced repeated code, and keeping each switch's settings separate made the program easier to expand and troubleshoot. The validation checks also illustrated how rejecting an invalid configuration early could prevent a larger operational problem.

## Running the project

I ran the project with Python 3 using:

```bash
python unit1_discussion.py
```

The program printed the parent and child objects, namespace information, shallow versus deep copy results, and validation messages, then finished with `All demonstration checks passed.`

## Discussion reflection

I learned more about how inheritance, namespaces, and copying objects actually work in Python. The biggest thing that stood out was the difference between shallow and deep copying. At first, making a copy sounds like it should give you a completely separate object, but that is not necessarily true when lists and dictionaries are nested inside it. I tested this by changing a VLAN on the original switch and watching the shallow copy change too, while the deep copy stayed the same.

I also worked through input validation so a bad port or VLAN would raise an error instead of silently being accepted. Compared with procedural programming, I found that OOP made more sense for this kind of example because each switch kept its own configuration while sharing common behavior with other network devices. That should reduce maintenance overhead as a project grows. In a larger application, I could reuse the parent class for routers, firewalls, or other equipment without rewriting the basics every time.
