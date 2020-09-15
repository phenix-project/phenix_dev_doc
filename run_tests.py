from __future__ import absolute_import, division, print_function
from libtbx import test_utils
import libtbx.load_env

tst_list = [
  "$D/regression/tst_doc_model_building_read_files.py",
  "$D/regression/tst_doc_fit_ligand.py",
  "$D/regression/tst_doc_model_building_1.py",
  "$D/regression/tst_doc_model_building_2.py",
  "$D/regression/tst_doc_model_building_3.py",
  "$D/regression/tst_doc_model_building_morphing.py",
  "$D/regression/tst_doc_model_building_sequence.py",
  "$D/regression/tst_doc_quick_reference.py",
  ]

def run():

  build_dir = libtbx.env.under_build("phenix_dev_doc")
  dist_dir = libtbx.env.dist_path("phenix_dev_doc")

  test_utils.run_tests(build_dir, dist_dir, tst_list)

if (__name__ == "__main__"):
  run()
