import sys

def is32bit():
    import platform
    
    return '32' in platform.architecture()[0]

def iswinplatform():
    """
    Returns:
    --------

    True if you are running on windows platform
    False otherwise
    """
    return sys.platform.startswith('win')

def fixpath(path):

    if iswinplatform():
        return path.replace('/','\\')
    return path


