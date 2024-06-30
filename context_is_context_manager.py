def is_context_manager(obj):
    if all([hasattr(obj, '__enter__'), hasattr(obj, '__exit__')]):
        return True
    return False
