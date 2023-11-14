def reading_text_file_readlines(file: str) -> list:
    with open(file, 'r') as f:
        data = f.readlines()  # read all lines
    return data


def writelines_text_file(file: str, data: list):
    with open(file, 'w') as my_file:  # w - write
        my_file.writelines(data)  # write all lines
        