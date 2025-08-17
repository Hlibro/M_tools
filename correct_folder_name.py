import re

def is_valid_folder_name(folder_name):
    """
    Checks if folder name is valid and returns True or False
    """
    # Check for Windows reserved names
    reserved_names = {"CON", "PRN", "AUX", "NUL", "COM1", "COM2", "COM3", "COM4", "COM5", 
                      "COM6", "COM7", "COM8", "COM9", "LPT1", "LPT2", "LPT3", "LPT4", 
                      "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"}
    
    # Check for empty name
    if not folder_name or folder_name.strip() == "":
        return False
    
    # Check for reserved names
    if folder_name.upper() in reserved_names:
        return False
    
    # Check for invalid characters
    invalid_chars = r'[<>:"/\\|?*\x00-\x1F]'
    if re.search(invalid_chars, folder_name):
        return False
    
    # Check for trailing periods and spaces
    if folder_name.endswith('.') or folder_name.endswith(' '):
        return False
    
    # Check name length (max 255 characters)
    if len(folder_name) > 255:
        return False
    
    return True

def correct_folder_name(folder_name):
    """
    Corrects invalid folder names and returns a valid folder name
    """
    # Handle empty names
    if not folder_name or folder_name.strip() == "":
        return "new_folder"
    
    # Replace invalid characters with underscores
    invalid_chars = r'[<>:"/\\|?*\x00-\x1F]'
    corrected_name = re.sub(invalid_chars, "_", folder_name)
    
    # Remove trailing periods and spaces
    corrected_name = corrected_name.rstrip('. ')
    
    # Handle reserved names
    reserved_names = {"CON", "PRN", "AUX", "NUL", "COM1", "COM2", "COM3", "COM4", "COM5", 
                      "COM6", "COM7", "COM8", "COM9", "LPT1", "LPT2", "LPT3", "LPT4", 
                      "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"}
    
    if corrected_name.upper() in reserved_names:
        corrected_name = f"folder_{corrected_name}"
    
    # Handle length limits (max 255 characters)
    if len(corrected_name) > 255:
        corrected_name = corrected_name[:251] + "..."
    
    # Final check - if name becomes empty after correction, provide default
    if corrected_name.strip() == "":
        corrected_name = "new_folder"
    
    return corrected_name

# Test examples
if __name__ == "__main__":
    test_names = [
        "valid_folder",           # Valid
        "Valid Folder",          # Valid
        "CON",                   # Invalid - reserved name
        "test<file",             # Invalid - invalid character
        "",                      # Invalid - empty name
        "   ",                   # Invalid - spaces only
        "folder.",               # Invalid - ends with period
        "folder ",               # Invalid - ends with space
        "normalfolder123",       # Valid
        "a" * 300               # Invalid - too long
    ]
    
    print("Validation and Correction Results:")
    print("=" * 50)
    
    for name in test_names:
        is_valid = is_valid_folder_name(name)
        corrected = correct_folder_name(name)
        
        display_name = f"'{name[:30]}{'...' if len(name) > 30 else ''}'"
        status = "✓ Valid" if is_valid else "✗ Invalid"
        
        print(f"{display_name:<35} -> {status}")
        if not is_valid:
            print(f"{'':35}    Corrected: '{corrected}'")
        print()