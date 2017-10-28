import operator
from Compressor.binaryTree import BinaryTree
from Compressor.stack import Stack


class CompressTree:
    def __init__(self, text):
        self.text = text
        self.text_bin = ''.join(format(ord(x), 'b') for x in text)
        self.text_len = len(self.text_bin)
        self.root = generate_tree_letter(text)
        self.dictionary = generate_dictionary(self.root)
        self.comp_bin = binary(text, self.dictionary)
        self.comp_len = len(self.comp_bin)
        self.comp_rate = round(100-((100*self.comp_len)/self.text_len), 2)


    def compare(self):
        print()
        print('\t*\t** Comparation **')
        print('\t*')

        print('\t*\tText:')
        print('\t*\t\t',self.text)
        print('\t*')

        print('\t*\tBinary without compress:')
        print('\t*\t\t',self.text_bin)
        print('\t*\tLength:',self.text_len)
        print('\t*')

        print('\t*\tBinary compressed:')
        print('\t*\t\t',self.text_bin)
        print('\t*\tLength:',self.text_len)
        print('\t*')

        print('\t*\tCompression rate: ', self.comp_rate, '%')
        print()


def binary(text, dictionary):
    binary = ''
    for letter in text:
        binary += dictionary[letter]

    return binary


# def compress_letter(self, text):
def generate_tree_letter(text):
    dic_qtd = histogram(text)
    list_aux = sort(dic_qtd.items())  # se der problema use a linha de baixo
    # list_aux = sorted(dic_qtd.items(), key=operator.itemgetter(1))
    while len(list_aux) > 1:
        a_val, a_qtd = list_aux.pop()
        b_val, b_qtd = list_aux.pop()

        aux_node = BinaryTree(a_qtd + b_qtd)
        aux_node.insert_right(a_val)
        aux_node.insert_left(b_val)

        tuple_node = (aux_node, aux_node.get_val())
        list_aux.append(tuple_node)
        list_aux = sort(list_aux)
    node, qtd = list_aux.pop()
    return node


def generate_dictionary(root):
    dict_comp = dict()
    code = Stack()
    read_tree(root, dict_comp, code)
    print(dict_comp)
    return dict_comp


def read_tree(no, dc, st):
    if no.get_left():
        st.push(0)
        read_tree(no.get_left(), dc, st)
    if no.get_right():
        st.push(1)
        read_tree(no.get_right(), dc, st)

    if no.is_leaf():
        print(no.get_val(), '=', str(st))
        dc[no.get_val()] = str(st)

    if not st.is_empty():
        st.pop()


def histogram(txt):
    my_dict = dict()
    for letter in txt:
        if letter not in my_dict:
            my_dict[letter] = 1
        else:
            my_dict[letter] += 1
    return my_dict


def histogram_words(txt):
    txt = txt.split()
    my_dict = dict()
    for word in txt:
        if word not in my_dict:
            my_dict[word] = 1
        else:
            my_dict[word] += 1
    return my_dict


def sort(lst):
    return sorted(lst, key=operator.itemgetter(1), reverse=True)
