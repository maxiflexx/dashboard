import os


def get_root():
    current = os.path.realpath(__file__) # ~/src/core/services
    root = f"{os.path.dirname(current)}/../../.."
    return root

