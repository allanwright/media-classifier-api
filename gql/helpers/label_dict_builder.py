'''Defines a label dictionary builder.

'''

import json

from helpers.builder import Builder

class LabelDictBuilder(Builder):
    '''Defines a label dictionary builder.

    '''

    def build(self, *args):
        '''Builds the object.

        Args:
            args: The args required to build the object.
        '''
        label_dict = json.loads(args[0])
        label_list = [{ 'id': k, 'name': v } for (k, v) in label_dict.items()]
        return json.dumps(label_list)
