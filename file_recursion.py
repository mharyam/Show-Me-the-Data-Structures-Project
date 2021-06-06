import os


#valid path = 'C:/Users/pc/Downloads/Documents/testdir'


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    files_with_suffix = []
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)

        if os.path.isdir(full_path):
            files_with_suffix.extend(find_files('c', full_path))
        elif os.path.isfile(full_path):
            if full_path.endswith(f".{suffix}"):
                files_with_suffix.append(full_path)

    return files_with_suffix


# print(find_files('c', 'C:/Users/pc/Downloads/Documents/testdir'))

def test_function(path):
    result = find_files('c', path)
    test_result = 'FAIL'
    for _ in result:
        if _.endswith('.c'):
            test_result = "PASS"
    print(test_result)


test_function('C:/Users/pc/Downloads/Documents/testdir')  # this should pass
test_function('C:/Users/pc/Documents/PROJECTS/api_project')  # this should fail
