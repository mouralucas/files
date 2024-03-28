from open_files import list_files, listdir, list_files_recursive
from rename_files import create_hash
import os
from tqdm import tqdm

# os.chdir(r'D:\System\Documents\mega\Imagens\Eu, Família e Amigos')
# os.chdir(r'D:\System\Documents\mega\Imagens\Eu, Família e Amigos\2019')
os.chdir(r'E:\System\Documents\mega\Imagens\Eu, Família e Amigos')
# os.chdir(r'D:\System\Documents\mega\Imagens\Tatuagens')
# os.chdir(r'C:\Users\lucas\Desktop\img_test')
file_list_1, directories = list_files_recursive(os.getcwd())

os.chdir(r'E:\System\Documents\mega\Camera Uploads')
file_list_2, directories_2 = list_files_recursive(os.getcwd())

os.chdir(r'C:\Users\lucas\iCloudPhotos\Photos')
file_list_3, directories_3 = list_files_recursive(os.getcwd())

file_list = file_list_1 + file_list_2 + file_list_3

duplicate = {}
total_items = len(file_list)
total = 0
with tqdm(total=total_items, desc="Calculating Total") as pbar:
    for idx, i in enumerate(file_list):
        filehash = create_hash(i)
        print('Item {item_idx} from {total_items}. Hash: {item_hash}'.format(item_idx=idx, total_items=total_items, item_hash=filehash))
        if filehash not in duplicate:
            duplicate[filehash] = [i]
        else:
            print('           Duplicated found: {file}'.format(file=i))
            duplicate[filehash].append(i)

file = open('Itens duplicados.txt', 'w')
# print('\n')
for d in duplicate:
    if len(duplicate[d]) > 1:
        file.write('\n')
        for i in duplicate[d]:
            file.write(i + '\n')
            print(i)
        print('\n')
file.close()

# for file_indexes in duplicate:
#     try:
#
#         plt.subplot(121), plt.imshow(imread(file_list[file_indexes[1]]))
#         plt.title(file_indexes[1]), plt.xticks([]), plt.yticks([])
#
#         plt.subplot(122), plt.imshow(imread(file_list[file_indexes[0]]))
#         plt.title(str(file_indexes[0]) + ' duplicate'), plt.xticks([]), plt.yticks([])
#         plt.show()
#
#     except OSError as e:
#         continue
