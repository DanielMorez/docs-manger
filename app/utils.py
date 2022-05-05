def str_to_bool(string):
    if string in ["False", "false"]:
        return False
    if string in ["True", "true"]:
        return True

    return None
