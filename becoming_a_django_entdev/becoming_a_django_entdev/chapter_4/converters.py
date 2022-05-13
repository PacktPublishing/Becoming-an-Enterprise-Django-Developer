''' Chapter 4 Converters Module '''


class YearConverter:
    '''
    Year Converter - Uses Regular Expression to return an integer value
    '''
    regex = '[0-9]{4}'

    def to_python(self, value):
        '''
        Method enforces value to integer always
        '''
        return int(value)

    def to_url(self, value):
        '''
        Method returns four digit numeric value
        '''
        return '%04d' % value
