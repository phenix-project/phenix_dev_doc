from __future__ import division, print_function
import sys
import libtbx.load_env
from phenix_dev_doc.regression.exercise import exercise

#def exercise(script, tmp_path):
#  regression_dir = os.path.dirname(os.path.abspath(__file__))
#  root_dir = os.path.dirname(regression_dir)
#  examples_dir = os.path.join(root_dir, 'examples')
#  tmp_dir = os.path.join(regression_dir, tmp_path)
#
#  # make temporary directy "tmp_dir"
#  if (not os.path.isdir(tmp_dir)):
#    os.makedirs(tmp_dir)
#  os.chdir(tmp_dir)
#
#  results = list()
#  skipped = False
#  # get example data
#  r1 = easy_run.fully_buffered('phenix.setup_tutorial tutorial_name=model-building-scripting')
#  os.chdir('model-building-scripting')
#
#  if script in [] and not libtbx.env.has_module('phenix'):
#    skipped = True
#  if not skipped:
#  # run script from html file
#    cmd = 'libtbx.python ' + os.path.join(examples_dir, script)
#    r = easy_run.fully_buffered(cmd)
#    results = [script, r.return_code, r.stdout_lines, r.stderr_lines]
#
#    # go back up to "regression" and delete tmp directory
#    os.chdir(root_dir)
#    shutil.rmtree(tmp_dir)
#
#  # parse results to see if it failed
#  return_code = 0
#  if (results[1] == 0): re = 'ran successfully'
#  else: re = 'failed'
#  print('%s %s  ' % (results[0], re))
#  if results[1] != 0:
#    return_code = 1
#    for line in results[3]:
#      print('\t', line, file=sys.stderr)
#  if skipped:
#    print('%s skipped' % script)
#
#  return return_code

def run():
  script_fn = "doc_model_building_read_files.py"
  exercise(script = script_fn, tmp_path = 'tmp_files_1')

if __name__ == '__main__':
  sys.exit(run())
