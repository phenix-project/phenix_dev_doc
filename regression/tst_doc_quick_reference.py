from __future__ import division, print_function
import sys
import libtbx.load_env
from phenix_dev_doc.regression.exercise import exercise

def run():
  script_fn = "doc_quick_reference.py"
  exercise(script = script_fn, tmp_path = 'tmp_files_8')

if __name__ == '__main__':
  sys.exit(run())
