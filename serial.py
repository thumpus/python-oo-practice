"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start = 0):
        """creates the serial number generator, starting at the start number"""
        self.start = self.next = start
    
    def __repr__(self):
        """representation"""
        return f"<SerialGenerator start = {self.start} next = {self.next}>"

    def generate(self):
        """generate next serial"""
        self.next = self.next + 1
        return self.next
    
    def reset(self):
        """reset serial number generator"""
        self.next = self.start




