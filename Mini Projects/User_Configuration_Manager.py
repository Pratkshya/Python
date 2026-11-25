test_settings = {
    'theme': 'light',
    'notification': 'disabled',
    'volume': 'high'
}
def add_setting(test_settings, setting):
    key,value = (item.lower() for item in setting)
    if key in test_settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        test_settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(test_settings, setting):
    key,value = (item.lower() for item in setting)
    if key in test_settings:
        test_settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(test_settings, key):
    key = key.lower()
    if key in test_settings:
        del test_settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(test_settings):
    if not test_settings:
        return "No settings available."
    else:
        result = 'Current User Settings:\n'
        for key, value in test_settings.items():
            result += f"{key.capitalize()}: {value}\n"
    return result
            
        


# print(add_setting({'theme': 'light'}, ('volume', 'high')))
# print(update_setting({'theme': 'light', 'language': 'English'}, ('theme', 'dark')))
# print(delete_setting({'theme': 'light', 'language': 'English'}, 'theme'))
print(view_settings(test_settings))