class Fish:
    """
    Represents a fish with swimming behavior and aquatic habitat.
    """

    def swim(self):
        """
        Print a message indicating the fish is swimming.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Print a message indicating the fish's natural habitat.
        """
        print("The fish lives in water")


class Bird:
    """
    Represents a bird with flying behavior and sky-based habitat.
    """

    def fly(self):
        """
        Print a message indicating the bird is flying.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Print a message indicating the bird's natural habitat.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A class that represents a flying fish, inheriting from both Fish and Bird.
    Demonstrates multiple inheritance and method overriding.
    """

    def swim(self):
        """
        Override Fish's swim method with a flying fish variant.
        """
        print("The flying fish is swimming!")

    def fly(self):
        """
        Override Bird's fly method with a flying fish variant.
        """
        print("The flying fish is soaring!")

    def habitat(self):
        """
        Override both parents' habitat methods with a flying fish variant.
        """
        print("The flying fish lives both in water and the sky!")
