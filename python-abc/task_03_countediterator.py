class CountedIterator:
    """
    A custom iterator that wraps a standard Python iterator and
    counts the number of items that have been retrieved using __next__.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable.

        Args:
            iterable (iterable): Any Python iterable (e.g., list, tuple, generator).
        """
        self._iterator = iter(iterable)
        self._count = 0

    def __iter__(self):
        """
        Return the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Return the next item from the iterator and increment the counter.

        Returns:
            The next item in the iterable.

        Raises:
            StopIteration: If there are no more items to return.
        """
        item = next(self._iterator)  # May raise StopIteration
        self._count += 1
        return item

    def get_count(self):
        """
        Get the number of items that have been iterated over.

        Returns:
            int: The current count.
        """
        return self._count
