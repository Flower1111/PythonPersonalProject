def do_continue(response):
    if (response.lower() == 'y') or (response.lower() == 'yes'):
        return True
    else:
        return False
