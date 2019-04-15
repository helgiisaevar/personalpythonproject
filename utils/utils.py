class Utils(object):
    def res(command, input):
        '''
        Returns responses
        '''

        if command == 'invalid-route':
            return 'Route: "' + input + '" is invalid. \n Send a GET request to "/" to see instructions'

        return ''
