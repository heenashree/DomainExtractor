from itertools import zip_longest
filename = 'sales_record.csv'
with open('sales_record.csv', 'r') as f:
    header = f.readline()
    header_list = [i for i in header.split(',')]


    def called(filename):
            temp1 = f.readline()
            line_list = [i for i in temp1.split(',')]
            zipper(header_list, line_list)
            called(filename)
    called(filename)

    def zipper(header, line):
        k = zip_longest(header, line, fillvalue=None)
        dict_Data = {kv[0]: kv[1] for kv in k}
        print(dict_Data)



