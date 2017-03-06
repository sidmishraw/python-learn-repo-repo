# process_pdf_rough2.py
# -*- coding: utf-8 -*-
# @Author: Sidharth Mishra
# @Date:   2017-03-05 17:48:50
# @Last Modified by:   Sidharth Mishra
# @Last Modified time: 2017-03-05 19:01:46



# python standard library imports
from json import dumps
from json import loads
from pprint import pprint
from re import compile
from re import findall



# PDFMiner library imports
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdftypes import PDFStream



# Fetches the stream objects from the PDFDocument.
def get_stream_objs(doc):
  '''
  Gets the PDFStream objects for the PDFDocument.

  :param: doc `PDFDocument`

  :return: obj_list `list(PDFStream)`
  '''

  obj_list = []
  i = 1
  obj = doc.getobj(i)
  while obj != None:
    if type(obj) == PDFStream:
      print('objid = {}'.format(i))
      obj_list.append(obj)
    i += 1
    try:
      obj = doc.getobj(i)
    except:
      break
  return obj_list




# Decode the stream and get the decoded stream data
def get_stream_data(stream_obj_list):
  '''
  Creates a JSON string after decoding the stream objects.

  :param: stream_obj_list `list(PDFStream)` - The list of PDFStream objects
  that need to be decoded.

  :return: json_string `JSON`
  '''

  # need to filter the steam objects
  stream_obj_list = list(filter(lambda x: len(x.attr) == 2, stream_obj_list))

  json_string = {}

  for stream_obj in stream_obj_list:
    # decode the stream obj
    stream_obj.decode()
    json_string[stream_obj.objid] = stream_obj.data

  return dumps(json_string)




if __name__ == '__main__':
  '''
  Using PDFMiner lib's PDFParser get all the stream objects.
  The stream objects that have only 2 attributes are of interest since they contain
  the text needed by us.

  Hence, the procedure should include a way of filtering them out from the list of
  stream objects. Also we need to decode the rawdata(zlib format compressed data) and then fetch the
  decoded data.

  '''

  doc_name1 = 'Sidharth Mishra.pdf'
  doc_name2 = 'obscalculi_testing_pdf_conv.pdf'

  f1 = open(doc_name1, 'rb')
  f2 = open(doc_name2, 'rb')

  p1 = PDFParser(f1)
  p2 = PDFParser(f2)

  doc1 = PDFDocument(p1)
  doc2 = PDFDocument(p2)

