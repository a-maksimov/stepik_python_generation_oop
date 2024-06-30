def non_closed_files(files):
    return [file for file in files if not file.closed]