import os
from datetime import datetime


def write_list_to_file(file_path, my_list) -> bool:
    '''
        Create a file based on "file_path"
        append each line of "my_list" as a line in the file
        returns bool base on the success of the write
    '''
    try:
        # Extract directory path and filename
        directory, filename = os.path.split(file_path)
        
        # Create directory if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        # Add timestamp to filename
        timestamp = datetime.now().strftime("%Y-%m-%d__%H-%M-%S")
        timestamped_filename = f"{timestamp}_{filename}"
        
        # Construct full file path
        timestamped_file_path = os.path.join(directory, timestamped_filename)
        
        # Write to the file
        with open(timestamped_file_path, 'w') as file:
            for item in my_list:
                file.write(str(item) + '\n')
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
        return False
    return True