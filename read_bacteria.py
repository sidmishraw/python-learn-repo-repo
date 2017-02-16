# read_bacteria.py
# -*- coding: utf-8 -*-
# @Author: Sidharth Mishra
# @Date:   2017-02-13 00:48:54
# @Last Modified by:   Sidharth Mishra
# @Last Modified time: 2017-02-13 00:53:14


from json import loads
from pprint import pprint


if __name__ == '__main__':

  with open('bacteria.json', 'r', encoding='utf-8') as json_file:
    string = json_file.read()
    json_string = loads(string)
    pprint(json_string)
    reqd_data = json_string['ubiome_bacteriacounts']
    dict_bac = { bac['taxon']:bac for bac in reqd_data }
    print(len(reqd_data))
    print(len(dict_bac))