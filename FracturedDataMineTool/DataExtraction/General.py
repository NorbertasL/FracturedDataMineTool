import os

def find_match_in_file(file_path: str, pattern: str) -> bool|list[tuple[int, str]]: 
    '''
    Checks if the file contails the pattern
        return list[int] -> line_indexes that it occured on
        or
        return False
    '''
    
    with open(file_path) as file:
        on_lines: list[tuple[int, str]] = [];
        try:
            lines = file.readlines()
        
            for line in lines:
                if pattern in line:
                    on_lines.append((lines.index(line), line))
            print(f'{file} Done!')
        except Exception as e:
            print(f'{file} failed to open becouse: {e}')
        return on_lines if on_lines else False
    
def get_all_files_in_dir(start_directory: str) -> list[str]:
    '''
        Walk through all the files and folders in the given directory
        stores their path in a list and retunrs the list
    '''
    file_list: list[str] = []
    for root, _, files in os.walk(start_directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list
    