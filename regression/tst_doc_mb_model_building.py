from __future__ import division, print_function
import sys
import libtbx.load_env
from phenix_dev_doc.regression.exercise import exercise

def run():
  return_code = exercise(script   = 'doc_mb_model_building.py',
                         tmp_path = 'tmp_files_3')
  return return_code

if __name__ == '__main__':
  sys.exit(run())
