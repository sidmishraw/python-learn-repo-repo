# process_pdf.py
# -*- coding: utf-8 -*-
# @Author: Sidharth Mishra
# @Date:   2017-02-15 13:42:12
# @Last Modified by:   Sidharth Mishra
# @Last Modified time: 2017-02-26 19:31:59


__author__ = 'sidmishraw'

'''
An utility for extracting the text from the pdf files using PDFMiner2 module.
PDFMiner Utility creator - Yusuke Shinyama
documentation from Python PDF Parser https://euske.github.io/pdfminer/

:author: sidmishraw
:email: sidharth.mishra@sjsu.edu
'''


# generic imports for stuff
from os import getcwd
from os.path import isdir
from os.path import sep as SEPARATOR
from os.path import split
from os.path import basename
from os import listdir
from pprint import pprint
from sys import argv
from sys import exit
from re import match
from re import compile
from traceback import print_exc
from sys import stdout


# command line UI builder for this utility
from argparse import ArgumentParser



# PDFMiner2 related imports
from pdfminer.psparser import PSBaseParser
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.converter import HTMLConverter
from pdfminer.image import ImageWriter
from pdfminer.pdfinterp import PDFResourceManager




# read the input parameters to the utility
def read_inputs():
  '''
  Reads the inputs from the CLI. 
  Basically constructs the CLI UI for this utility.

  :return: (input_files=list(string), output_dir=list(string))
  '''

  argparser = ArgumentParser(description='''
      PDF to Text convertion utility using PDFMiner2.
      ''')
  argparser.add_argument('-i', '--input-files', action='store', \
      nargs='+', required=True, dest='input_files')
  argparser.add_argument('-o', '--output-dir', action='store', \
      nargs=1, required=True, dest='output_dir')
  parsed_args = argparser.parse_args()
  input_files = parsed_args.input_files
  output_dir = parsed_args.output_dir
  return (input_files, output_dir)




# generate the output filepath
def __generate_op_file_name__(ip_file, output_dir):
  '''
  Generates the OP filepath from the input file name.

  :param: ip_file str
  :param: output_dir str

  :return: op_file str
  '''

  # fetch the input file name and extension
  file_name, extension = tuple(basename(ip_file).split('.'))
  # if the extension is not pdf, move on and do nothing
  if extension != 'pdf':
    return None
  op_file = output_dir + SEPARATOR + file_name + '.txt'
  # op_file = output_dir + SEPARATOR + file_name + '.html'
  return op_file



def __process_pdf__(f, o, output_path):
  '''
  Processes the PDF files. Extracts the text from the PDF.
  Uses PDFMiner's Imagewriter, PDFInterpreter etc to work extract out the text
  from the pdf.

  :param: f _io.BufferedReader
  :param: o _io.BufferedReader
  :param: output_path str

  :return: None
  '''

  import pdb

  # setting codec to utf-8
  codec = 'utf-8'
  # link the open file to the parser
  parser = PDFParser(f)
  # link the pdfdocument to the parser
  pdf = PDFDocument(parser)
  # initialize the imagewriter, resource manager, device and interpreter
  # imagewriter is the last renderer
  imagewriter = ImageWriter(output_path)
  resource_manager = PDFResourceManager()
  device = TextConverter(resource_manager, o, codec, imagewriter=imagewriter)
  # device = HTMLConverter(resource_manager, o, codec, imagewriter=imagewriter)
  interpreter = PDFPageInterpreter(resource_manager, device)

  pdb.set_trace()

  for page in PDFPage.create_pages(pdf):
    interpreter.process_page(page)
  device.close()



# process the pdf
def process_pdf(input_file, output_dir):
  '''
  Processes the pdf, extracts the text from the pdf.

  :param: input_file str - The input filepath, can be a file or dir
  :param: output_dir str - The output filepath, needs to be a dir

  :return: None
  '''

  list_files = []
  if isdir(input_file):
    parse_dir(input_file, list_files)
  else:
    list_files.append(input_file)
  for ip_file in list_files:
    op_file = __generate_op_file_name__(ip_file, output_dir)
    if not op_file:
      continue
    with open(ip_file, 'rb') as f,\
    open(op_file, 'wt') as o:
      __process_pdf__(f, o, op_file)





if __name__ == '__main__':
  '''
  Takes as input the input PDF files and the output directory and outputs
  the extracted text for each PDF file.
  '''

  try:
    input_files, output_dir = read_inputs()
    print(input_files, output_dir)
    if not isdir(output_dir[0]):
      print('The OUTPUT_DIR has to be a directory not a file.')
      exit(0)
    for input_file in input_files:
      process_pdf(input_file, output_dir[0])
  except Exception as e:
    print_exc(file=stdout)
    exit(0)

