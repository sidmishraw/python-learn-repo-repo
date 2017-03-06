# process_pdf_rough.py
# -*- coding: utf-8 -*-
# @Author: Sidharth Mishra
# @Date:   2017-03-01 14:45:50
# @Last Modified by:   Sidharth Mishra
# @Last Modified time: 2017-03-05 16:29:36



# Creating a new PDF parsing utility for customized use.
# Here I'm going to try and parse the PDF document to view the contents of the 
# PDF objects decoded from their zlib encoding.
#
# Self Notes - 
# Bytes in Python are represented in `bytes` class. They are just like string but
# are bytes. String like splits, random access are possible like 
# bytes_sequence[1:10].
#
# using that to extract out the start byte number for XREF table of the PDF.




# Python standard library imports
from zlib import decompress
from argparse import ArgumentParser
from json import dumps




# python debugging related
from pdb import set_trace




# constants for detecting flags in PDF bytes sequence
__LF_STREAM__ = b'\nstream\n'
__LF_ENDSTREAM__ = b'\nendstream\n'
__LF_STARTXREF__ = b'\nstartxref\n'
__LF_EOF__ = b'\n%%EOF\n'
__CR_STREAM__ = b'\rstream\nx'
__CR_ENDSTREAM__ = b'\rendstream\nx'
__CR_STARTXREF__ = b'\rstartxref\nx'
__CR_EOF__ = b'\r%%EOF\nx'



# the global dictionary that is used to store the decoded(zlib decompressed)
# objects from the PDF.
decoded_obj_dict = {}



def check_line_ending(bytes_sequence):
  '''
  Since the PDF's flags can use `\n` or `\r` or a combination of both for lineendings,
  this utility will determine the line-ending used in the PDF from the first flag it reads in.
  This way, we can choose one line-ending style for the PDF.
  Although, this is not a great solution, this can provide a cleaner approach for decoding the
  contents of the stream objects.

  :param: bytes_sequence `bytes`

  :return: `None`
  '''

  start_pos_stream_flag = 







def find_xref_pos(bytes_sequence, codec='utf-8'):
  '''
  Finds the XREF start position or the number of bytes to skip if doing this manually
  using the `dd` tool on UNIX.

  :param: bytes_sequence `bytes` - The sequence of bytes of the PDF.

  :param: codec `str` - The codec is the coding standard used to code the bytes.
  For eg - `utf-8`, `latin-1`, `utf-16` etc...
  default value - `utf-8`

  :return: `int`
  '''

  # since bytes_sequence is a sequence of immutable single bytes of form b'......'
  # xref_begin_pos is the start position of the bytes sequence for the xref table positon
  # xref_end_pos is the end position of the bytes sequence for the xref table positon
  # xref_pos is the position (an int) of the xref table begining
  # just like using the dd tool from terminal, xref_pos can be used to skip to that position.
  # Adding a check since the lines can be delimited with a CR or \r if the PDF was made on
  # a windows machine or using a Ghostscript application.
  xref_begin_pos = bytes_sequence.find(__LF_STARTXREF__) + 11 \
  if bytes_sequence.find(__LF_STARTXREF__) != -1 else bytes_sequence.find(__CR_STARTXREF__) + 12

  xref_end_pos = bytes_sequence.find(__LF_EOF__) if bytes_sequence.find(__LF_EOF__) != -1 \
  else bytes_sequence.find(__CR_EOF__)

  xref_pos = int(str(bytes_sequence[xref_begin_pos : xref_end_pos], encoding = codec))

  print('xref table begins from position {}'.format(xref_pos))

  return xref_pos




def build_decoded_obj_dict(bytes_sequence):
  '''
  Builds the decoded_obj_dict from the bytes sequence of the PDF.

  :param: bytes_sequence `bytes` - The bytes sequence of the parsed PDF document.

  :return: `None`
  '''

  # decode and store the decoded objects into a dict holding the
  # decoded bytes in it mapped to the object number.
  global decoded_obj_dict

  # start_stream_pos is the starting position of the __LF_STREAM__ and __CR_STREAM__
  # flag in the PDF's byte sequence
  start_stream_pos = bytes_sequence.find(__LF_STREAM__) \
  if bytes_sequence.find(__LF_STREAM__) != -1 else bytes_sequence.find(__CR_STREAM__)

  # end_stream_pos is the starting position of the __ENDSTREAM__ flag in the PDF's
  # byte sequence
  end_stream_pos = bytes_sequence.find(__LF_ENDSTREAM__) \
  if bytes_sequence.find(__LF_ENDSTREAM__) else bytes_sequence.find(__CR_ENDSTREAM__)

  # The counter to maintain the count of objects
  object_counter = 0

  # offset for the next stream if any.
  offset = 0

  while start_stream_pos != -1 or end_stream_pos != -1:
    # Using zlib decompression to extract data out of the POSTScript object streams
    # need to add 8 to the start_stream_pos because we need to skip the bytes for
    # b`\nstream\n` and 9 for b`\rstream\nx` and or the __LF_STREAM__ and __CR_STREAM__
    # flag in the bytes sequence.
    # same goes for the offset updation, need to add 11 in order to skip
    # b`\nendstream\n` or the __LF_ENDSTREAM__ and __CR__ENDSTREAM__ flag in the bytes sequence.
    decoded_obj_dict[object_counter] = decompress(bytes_sequence[offset + \
      start_stream_pos + 8 : offset + end_stream_pos])

    object_counter += 1
    offset += end_stream_pos + 11

    start_stream_pos = bytes_sequence[offset : ].find(__LF_STREAM__) \
    if bytes_sequence[offset : ].find(__LF_STREAM__) != -1 else \
    bytes_sequence[offset : ].find(__CR_STREAM__)

    end_stream_pos = bytes_sequence[offset : ].find(__LF_ENDSTREAM__) \
    if bytes_sequence[offset : ].find(__LF_ENDSTREAM__) != -1 else \
    bytes_sequence[offset : ].find(__CR_ENDSTREAM__)

  return




def obtain_bytes_sequence(input_file):
  '''
  Parses the input PDF file and obtains its bytes sequence.

  :param: input_file `str` - Path to the input PDF file.

  :return: bytes_sequence `bytes`
  '''

  # the bytes sequence of the PDF
  bytes_sequence = None

  with open(input_file, 'rb') as f_input:
    bytes_sequence = f_input.read()

  return bytes_sequence




def __build_json__(input_dict):
  '''
  Generates the JSON for the input_dict since it contains bytes as it's values.

  :param: input_dict `dict`{`int`:`bytes`} - The input dict needs to be a dict of int to bytes

  :return: json_string `str`
  '''

  contents = []

  for item in input_dict.items():
    contents.append('"{}":{}'.format(item[0], dumps(str(item[1]))))

  json_string = '{{{}}}'.format(','.join(contents))

  return json_string




def create_intermediary_file(output_file_name):
  '''
  Creates the intermediary file from the decoded_obj_dict.
  The intermediary file has the name intrm_<output_file_name>.txt

  :param: output_file_name `str` - The name of the final output txt file

  :return: `None`
  '''

  global decoded_obj_dict

  json_string = __build_json__(decoded_obj_dict)

  output_file_name = 'intrm_' + output_file_name

  with open(output_file_name, 'w') as f_output:
    f_output.write(json_string)

  return




def process_pdf(input_file, output_file_name):
  '''
  Begin Parsing the pdf.
  This phase includes the following steps:
  > Obtain the bytes sequence from the PDF.
  > Obtain the byte position for start of XREF section of the PDF document.
  > Obtain the Postscript objects and decode their streams, store the decoded streams into a dict.

  :param: input_file `str` - Path to the input PDF file.

  :param: output_file_name `str` - Name of the output txt file.

  :return: `None`
  '''

  bytes_sequence = obtain_bytes_sequence(input_file)

  # build the decoded object dict from the bytes_sequence
  build_decoded_obj_dict(bytes_sequence)

  # create the intermediary txt file from the decoded_obj_dict
  create_intermediary_file(output_file_name)

  return

  


def parse_input_args():
  '''
  Parse the command line arguments to the utility.

  :param: `None`

  :return: (input_file_name, output_file_name) `tuple`(`str`, `str`)
  '''

  argparser = ArgumentParser(description='''
    A PDF parser utility.
    The tool will parse the input PDF file and generate a txt file containing text from the PDF.
    It will also generate an intermediary file that contains all the PDF objects.''',\
    usage='''
    python process_pdf_rough.py -i [input-file] -o [output-file-name]
    Inputs -
    -i or --input-file    The path of the pdf file you want decoded.
    -o or --output-file-name   The name of the output txt file you want.
    ''')

  # add in -i and --input-file argument
  argparser.add_argument('-i', '--input-file', nargs=1, action='store', \
    required = True, dest = 'INPUT_FILE')

  # add in -o --output-file argument
  argparser.add_argument('-o', '--output-file-name', nargs=1, action='store', \
    required = True, dest = 'OUTPUT_FILE')

  parsed_args = argparser.parse_args()

  return (parsed_args.INPUT_FILE[0], parsed_args.OUTPUT_FILE[0])




if __name__ == '__main__':
  '''
  Trying out the pdfminer APIs to decode a PDF document.

  Here I'm going to try and parse the PDF document to view the contents of the 
  PDF objects decoded from their zlib encoding.

  Self Notes - 
  Bytes in Python are represented in `bytes` class. They are just like string but
  are bytes. String like splits, random access are possible like 
  bytes_sequence[1:10].

  using that to extract out the start byte number for XREF table of the PDF.
  '''

  input_file, output_file_name = parse_input_args()

  print('generating output file named {} \
    from the input pdf named {}'.format(output_file_name, input_file))
  process_pdf(input_file, output_file_name)
