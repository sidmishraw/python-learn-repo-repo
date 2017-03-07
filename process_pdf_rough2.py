# process_pdf_rough2.py
# -*- coding: utf-8 -*-
# @Author: Sidharth Mishra
# @Date:   2017-03-05 17:48:50
# @Last Modified by:   Sidharth Mishra
# @Last Modified time: 2017-03-06 15:40:09




'''
Going back to using `PDFMiner` library by `Yusuke Shinayama`.
However, this time, I'm planning to use only the core PDFDocument and Parser from the module.
Since I'll be customizing the output to fit our requirements, I've decided on this approach.
'''




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




# Constants that are going to be used through out this script
# These are keys defined in pdfminer module for building the dicts used in the module.
PAGES = 'Pages'
PAGELABELS = 'PageLabels'
METADATA = 'Metadata'
TYPE = 'Type'
CONTENTS = 'Contents'
KIDS = 'Kids'




# Globals
pdf_contents_dict = {}




# Toy method
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



# Toy method
# Decode the stream and get the decoded stream data
def get_stream_data(stream_obj_list):
  '''
  Creates a JSON string after decoding the stream objects.

  :param: stream_obj_list `list(PDFStream)` - The list of PDFStream objects
  that need to be decoded.

  :return: `None`
  '''

  # need to filter the steam objects
  stream_obj_list = list(filter(lambda x: len(x.attrs) == 2, stream_obj_list))

  json_string = {}

  for stream_obj in stream_obj_list:
    # decode the stream obj
    stream_obj.decode()
    json_string[stream_obj.objid] = str(stream_obj.data)

  with open('op_1.json', 'w') as op_f:
    op_f.write(dumps(json_string))

  return




# This function will extract the pages from the PDF document using the PDF's catalog
def extract_pages(pdf_doc):
  '''
  Extract the list of pages from PDF document catalog.
  This will give us all the pages in the PDF document.

  :param pdf_doc: The PDF document from whose catalog we are trying to extract the
  pages from. :class: `pdfminer.pdfdocument.PDFDocument`

  :return pages: The list of pages of the PDF document. :class: `list(dict)`
  '''

  # The catalog is a dict
  # we are only interested in the `Pages` key and its value.
  # `Pages` has a list of `pdfminer.pdftypes.PDFObjRef` as its value.
  catalog = pdf_doc.catalog

  # The list of pages that needs to be returned
  pages = []

  # looping through the page references in the catalog and resolving them before
  # adding to the list to be returned from this function.
  # catalog[PAGES] gives the object references to the Pages listing
  for objref in catalog[PAGES].resolve()[KIDS]:
    pages.append(objref.resolve())

  return pages




# Extract contents of the pages
def extract_contents_page(page_nbr, page):
  '''
  Extract the contents of a page. By iterating over the Contents list of a page of the PDF document,
  we will build a dict for the PDF contents.

  :param page_nbr: The page number as per the PDF catalog. :class: `int`
  :param page: The PDF page dict obtained from the catalog of the PDF document. :class: `dict`

  :return: `None`
  '''

  global pdf_contents_dict

  # contents is the list of `pdfminer.pdftypes.PDFStream` objects.
  contents = []

  # page dict is the dict constructed per page to hold the mapping from
  # page number to the decoded contents of that page.
  page_dict = {}

  # looping through the `pdfminer.pdftypes.PDFObjRef`s in the Contents list of the page
  # and adding the resolved PDFStream objects to the contents list
  for objref in page[CONTENTS]:
    contents.append(objref.resolve())

  # contruct the page_dict
  for index, stream_obj in enumerate(contents):
    stream_obj.decode()
    page_dict['Content#{}'.format(index)] = stream_obj.data

  # contruct the pdf_contents_dict
  pdf_contents_dict['Page#{}'.format(page_nbr)] = page_dict

  return




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

