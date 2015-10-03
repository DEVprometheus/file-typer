#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  a very simple file binary viewer and format/type detection utility...
  actually this code is prepared for first GitHub file upload test...
"""

__author__ = 'developer.prometheus@gmail.com (bulent sahin)'
__version__ = '0.0.1'

import sys
import os

from functools import partial

"""
  MAIN
  ----
"""

if len(sys.argv) > 1:
    filename = sys.argv[1]
    if len(sys.argv) > 2:
        opt2 = sys.argv[2].upper()
    else:
        opt2 = "NULL"
else:
    print "[typer] knows: JPEG, PNG, GIF, TIFF, PDF, GZIP file formats now..."
    print "usage:"
    print "     typer.py <filename>"
    sys.exit(1)

if not os.path.exists(filename):
        print "!*! file [ "+filename+" ] not found..."
        sys.exit(1)

total = os.path.getsize(filename)

with open(filename, 'rb') as file:
     allb = 0; co = 0; topi = ''; jpg = ''; gif = ''; png = ''; tiff = ''
     pdf = ''; gzip = ''

     for byte in iter(partial(file.read, 1), b''):
         co = co + 1; allb = allb + 1

         deci = ord(byte); hexi = hex(deci)
         last = hexi[2:]
         if len(last) < 2:
             last = '0'+last

         if allb == 1 or allb == 2 or (allb == (total)) or (allb == (total-1)):
             jpg = jpg+last

         if allb >= 1 and allb <= 6:
             gif = gif+last

         if allb >= 1 and allb <= 8:
             png = png+last

         if allb >= 1 and allb <= 4:
             tiff = tiff+last
             pdf = pdf+last

         if allb >= 1 and allb <= 2:
             gzip = gzip+last

         topi = topi+last+' '
         if co == 8:
             topi = topi+' '

         if co >= 16:
             if opt2 != "-NOP":
                 print '%08d' % allb,'<>',topi
             co = 0
             topi = ''

if opt2 != "-NOP":
    print '%08d' % allb,'<>',topi
    print "------------------------------------------------------------"

if jpg == "ffd8ffd9":
    print "* this is a JPEG file..."

if gif == "474946383961":
    print "* this is a GIF89a file..."

if gif == "474946383761":
    print "* this is a GIF87a file..."

if png == "89504e470d0a1a0a":
    print "* this is a PNG file..."

if tiff == "49492a00":
    print "* this is a TIFF (Intel) file..."

if tiff == "4d4d002a":
    print "* this is a TIFF (Motorola) file..."

if pdf == "25504446":
    print "* this is a PDF file..."

if gzip == "1f8b":
    print "* this is a GZIP file..."

"""
  end of the code.
"""
