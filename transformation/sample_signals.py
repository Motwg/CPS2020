def signal_switcher(signal_code):
    switcher = {
        's1': 's101',
        's2': 's102',
        's3': 's103'
    }
    return switcher.get(signal_code.lower(), 's101')
