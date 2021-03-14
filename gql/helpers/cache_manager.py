'''Defines the base class for managing a cached object.

'''

import logging

class CacheManager:
    '''Defines the base class for managing a cached object.

    '''

    def __init__(self, builder):
        '''Initializes a new instance of the CacheManager object.

        Args:
            builder: The cache object builder.
        '''
        self.input = []
        self.builder = builder
        self.cache = None

    def get(self, *args):
        '''Gets a cached object or transforms one from the given input.

        The input args are first validated against a set a of cached input/s.
        If the input has changed, the input is transformed into output then returned.
        If the input has not changed, the cached object is returned.
        '''
        if self.cache is None or self.__invalidate(args):
            logging.info('Cache not found or invalidated.')
            self.input = args
            self.cache = self.builder.build(*args)
        return self.cache

    def __invalidate(self, args):
        if len(self.input) != len(args):
            return True

        def is_equal(x, y):
            if type(x) is not type(y):
                return False
            elif isinstance(x, str):
                return x == y
            else:
                return x is y

        for i in range(len(self.input)):
            if not is_equal(self.input[i], args[i]):
                return True

        return False
