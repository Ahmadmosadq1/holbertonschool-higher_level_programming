class VerboseList(list):
    """
    A subclass of the built-in list class that prints messages
    when items are added or removed using append, extend, remove, or pop.
    """

    def append(self, item):
        """
        Add an item to the end of the list and print a message.

        Args:
            item: The item to be added.
        """
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """
        Extend the list by appending elements from the iterable
        and print a message with the number of items added.

        Args:
            iterable (iterable): The iterable whose items are to be added.
        """
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with {count} items.")

    def remove(self, item):
        """
        Remove the first occurrence of an item from the list and
        print a message. Raises ValueError if item is not found.

        Args:
            item: The item to be removed.
        """
        if item in self:
            print(f"Removed {item} from the list.")
        else:
            print(f"Item {item} not found in the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return item at index (default last). Print a message
        with the popped item. Raises IndexError if list is empty or index
        is out of range.

        Args:
            index (int, optional): Index of the item to pop. Defaults to -1.

        Returns:
            The item that was removed.
        """
        try:
            item = self[index]
            print(f"Popped {item} from the list.")
            return super().pop(index)
        except IndexError:
            print("Pop operation failed: list index out of range.")
            raise
