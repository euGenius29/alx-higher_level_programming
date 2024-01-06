#!/usr/bin/python3
"""
A class called LockedClass
"""
class LockedClass:
    """
    A class that prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called 'first_name'.
    """
    def __setattr__(self, name, value):
        """
        Override the default attribute setting behavior.

        Parameters:
        - name (str): The name of the attribute being set.
        - value: The value to be assigned to the attribute.

        Raises:
        - AttributeError: If an attempt is made to set an attribute other than 'first_name'.
        """
        if name == 'first_name':
            super().__setattr__(name, value)
        else:
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
