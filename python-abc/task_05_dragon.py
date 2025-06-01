class SwimMixin:
    """
    Mixin that provides swimming behavior.
    """

    def swim(self):
        """
        Print a message indicating the creature can swim.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin that provides flying behavior.
    """

    def fly(self):
        """
        Print a message indicating the creature can fly.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon that can swim and fly by inheriting from SwimMixin and FlyMixin.
    """

    def roar(self):
        """
        Print a message indicating the dragon is roaring.
        """
        print("The dragon roars!")


# Testing
if __name__ == "__main__":
    draco = Dragon()
    draco.swim()    # The creature swims!
    draco.fly()     # The creature flies!
    draco.roar()    # The dragon roars!
