from __future__ import division, print_function
import os
import sys
import shutil
import libtbx.load_env
from libtbx import easy_run

def run():
  '''
  Loop through scripts in cctbx_website/examples and check if they run
  correctly
  '''
  regression_dir = os.path.dirname(os.path.abspath(__file__))
  root_dir = os.path.dirname(regression_dir)
  examples_dir = os.path.join(root_dir, 'examples')
  tmp_dir = os.path.join(regression_dir, 'tmp_files')

  # make temporary directy "tmp_dir"
  if (not os.path.isdir(tmp_dir)):
    os.makedirs(tmp_dir)
  os.chdir(tmp_dir)

  results = list()
  skipped = list()
  r1 = easy_run.fully_buffered('phenix.setup_tutorial tutorial_name=model-building-scripting')
  # loop through all .py files in "examples"
  for script in os.listdir(examples_dir):
    cmd = 'libtbx.python ' + os.path.join(examples_dir, script)
    #if script in ['doc_map_manager.py', 'doc_model_map_manager.py'] \
    if script in [] \
      and not libtbx.env.has_module('phenix'):
      skipped.append(script)
      continue
    if script in ['doc_model_building_read_files.py', 'doc_fit_ligand.py',
      'doc_model_building_1.py', 'doc_model_building_2.py'] :
      os.chdir('model-building-scripting')
    r = easy_run.fully_buffered(cmd)
    results.append([script, r.return_code, r.stdout_lines, r.stderr_lines])

    # remove files once done
    # (the scripts sometimes operate on the same input files, so need to delete each time)
    for f in os.listdir(tmp_dir):
      if f == 'model-building-scripting':
        pass
      #if os.path.isdir(os.path.join(tmp_dir, f)):
      #  shutil.rmtree(os.path.join(tmp_dir, f))
      else:
        os.remove(os.path.join(tmp_dir, f))
    os.chdir(tmp_dir)
  #
  # go back up to "regression" and delete tmp directory
  os.chdir(root_dir)
  shutil.rmtree(os.path.join(tmp_dir, 'model-building-scripting'))
  os.rmdir(tmp_dir)

  # print info if fail or success; print stderr if failed
  return_code = 0
  for l in results:
    if (l[1] == 0): re = 'ran successfully'
    else: re = 'failed'
    print('%s %s  ' % (l[0], re))
    if l[1] != 0:
      return_code = 1
      for line in l[3]:
        print('\t', line, file=sys.stderr)
  for l in skipped:
    print('%s skipped' % l)

  return return_code

if __name__ == '__main__':
  sys.exit(run())
