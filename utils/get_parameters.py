def label_txt_to_list(file_name):
    labels_list = []

    with open(file_name) as file:
        while line := file.readline().rstrip():
            label = []
            for item in line.split():
                label.append(item)
            label.pop()  # pops confidence-score from label list
            labels_list.append(label)

    labels_list = replace_class_type_with_name(labels_list)

    print("Label parameters read from .txt to label_list")
    return labels_list


def replace_class_type_with_name(l_list):
    for index, label in enumerate(l_list):
        match label[0]:
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
