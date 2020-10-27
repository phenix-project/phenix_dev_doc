from __future__ import division, print_function
import sys
import libtbx.load_env
from phenix_dev_doc.regression.exercise import exercise

def run():
  return_code = exercise(script   = 'doc_quick_reference.py',
                         tmp_path = 'tmp_files_8')
  return return_code

if __name__ == '__main__':
  sys.exit(run())
