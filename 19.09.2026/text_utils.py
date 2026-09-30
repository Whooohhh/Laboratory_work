
def load_data():
    return [3, 17, 8, 25, 6, 12, 25, 9, 14]

def filter_above(values, threshold=10):
    filtered_list = []
    for i in values:
        if i > threshold:
            filtered_list.append(i)
    return filtered_list

def mean(values):
    if not values:
        return 0
    return sum(values) / len(values)



import text_utils

otvet1 = text_utils.load_data()
otvet2 = text_utils.filter_above(otvet1, threshold=10)
otvet3 = text_utils.mean(otvet2)

print('Ответ:',otvet3)
