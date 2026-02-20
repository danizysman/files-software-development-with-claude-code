def validate_config(config):
    """Validate that a configuration dictionary has all required fields."""
    # Bug reproduction:
    # print(validate_config({'host': 'localhost', 'port': 8080}))   # True  (correct)
    # print(validate_config({'host': 'localhost'}))                 # True  (WRONG — should be False!)
    # print(validate_config({'port': 8080}))                        # True  (WRONG — should be False!)
    # print(validate_config({}))                                    # False (correct)
    return 'host' in config or 'port' in config


