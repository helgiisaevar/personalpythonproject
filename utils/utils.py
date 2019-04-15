class Utils(object):
    def res(command, input):
        '''
        Returns responses
        '''

        if command == 'invalid-route':
            return ' Route: "' + input + '" is invalid or values are missing. Send a GET request to "/" to see instructions '

        if command == 'invalid-req':
            return 'This method is not supported on this endpoint. Try using: ' + input

        return input

