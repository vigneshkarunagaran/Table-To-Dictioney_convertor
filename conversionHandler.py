
class DataHandler:

    @staticmethod
    def sample():
        print('test')

    @staticmethod
    def modify_leaf(root:list, old_leaf:list): 
        '''
        Method to strip child header in accordance with parent header
        '''
        old_leaf = ('|').join(old_leaf) 
        new_leaf =[]
        current_position = 0
        for i in root:
            new_leaf.append(old_leaf[current_position:current_position+len(i)])
            current_position = current_position+len(i)+1
        return new_leaf

    @staticmethod
    def validate_header_list(column_heading:list):
        '''
        Method to modify all header to have same number of elements
        '''
        for i in range(len(column_heading) - 1):
            if len(column_heading[i]) != len(column_heading[i+1]):
                column_heading[i+1] = DataHandler.modify_leaf(column_heading[i],column_heading[i+1])

    @staticmethod
    def cleanup_header_list(column_heading:list):
        '''
        Method to remove all "|" char and strip into seperate list of elements
        '''
        for i, _ in enumerate(column_heading):
            column_heading[i] = [x.split('|') for x in column_heading[i]]

    @staticmethod
    def generate_keys(root:list, leaf:list):
        '''
        Method used to reduce multiple header lines into one single header 
        '''
        header_key = []
        for root_element, leaf_element in zip(root,leaf):
            header_key.append([root_element[0].strip() + ' '+ element.strip() for element in leaf_element])
        return(header_key)

    @staticmethod
    def extend_keys(nested_keys:list):
        '''
        Method to convert Nested list elements into one single list
        '''
        extended_keys = []
        for nested_element in nested_keys:
            extended_keys.extend(nested_element)
        return extended_keys