def label_txt_to_list(file_name):
    label_list = []

    with open(file_name) as file:
        while line := file.readline().rstrip():
            temp = []
            for word in line.split():
                temp.append(word)
            temp.pop()
            label_list.append(temp)

    label_list = replace_class_type_with_name(label_list)

    print("Label parameters read from .txt to label_list")
    return label_list


def replace_class_type_with_name(l_list):
    for index, l_item in enumerate(l_list):
        match l_item[0]:
            case '0':
                l_list[index][0] = 'text'
            case '2':
                l_list[index][0] = 'button'
            case '3':
                l_list[index][0] = 'checkbox'
            case '4':
                l_list[index][0] = 'password'
            case '5':
                l_list[index][0] = 'radio'
            case '6':
                l_list[index][0] = 'dropdown'

    return list
