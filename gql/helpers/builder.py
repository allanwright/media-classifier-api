'''Defines a base class for building objects.

'''

from abc import abstractmethod

class Builder:
    '''Defines a base class for building objects.

    '''

    @abstractmethod
    def build(self, *args):
        '''Builds the object.

        Args:
            args: The args required to build the object.
        '''
