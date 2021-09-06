import os

files_folder = os.path.join(os.getcwd(), 'sorted')


def files_to_dict(files_path):
    files = os.listdir(files_path)
    tmp_list = {}

    for file_name in files:
        file_path = os.path.join(files_path, file_name)
        file_content = []
        with open(file_path) as file:
            # file_content = file.readlines()
            for line in file.readlines():
                file_content.append(line.strip())
            count_lines = len(file_content)
            content = '\n'.join(file_content)
            tmp_list[file_name] = {count_lines: content}

    return tmp_list


res = files_to_dict(files_folder)
print(res)


def dict_to_file(dictionary):
    tmp_list = []

    for file in dictionary:
        dict_keys = dictionary[file].keys()
        for key in dict_keys:
            tmp_list.append(key)

    sorted_keys_list = sorted(tmp_list)

    for number in sorted_keys_list:
        for key, file in dictionary.items():
            if dictionary[key].get(number):
                file_content = dictionary[key][number]
                number = str(number)
                a = str(key)
                with open('result.txt', 'a') as file:
                    file.write(a)
                    file.write(f"\n{number}\n")
                    file.write(f"{file_content}\n")


dict_to_file(res)