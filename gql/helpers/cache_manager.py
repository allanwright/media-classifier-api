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
        self.guid = ''
        self.builder = builder
        self.cache = None

    def get(self, guid: str, *args):
        '''Gets a cached object or transforms one from the given input.

        The guid is validated against a cached guid.
        If the guid has changed, the cache is assummed to be invalid and a new cache built.
        If the guid has not changed, the existing cache returned.
        '''
        if self.cache is None or self.__invalidate(guid):
            logging.info('Cache not found or invalidated.')
            self.guid = guid
            self.cache = self.builder.build(*args)
        return self.cache

    def __invalidate(self, guid):
        return self.guid != guid
