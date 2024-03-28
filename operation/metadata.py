from operation.rename_files import read_metadata

file_path = 'C:\\Users\\lucas\\Desktop\\GH011628.MP4'

metadata = read_metadata(file_path)
print(metadata)
