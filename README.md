# Phenix developers documentation.

This readme describes how content submission and testing works.

## Important

Don't rename the html files without changing the urls and javascript in the django repository phenix-lbl/cctbx_phenix_doc.

## Content:

To create content for the website, you can either:
1. submit content to me (dcliebschner), f.ex. on a google doc --> I will then transfer to html
2. write the html yourself by using the template: html_files/template.html


## Testing:

If the new html page has executable code in it, the code will be incorporated in the t96 regression tests. This way, we know if code on the website becomes obsolete.

* The html files in this repository are also part of the repository `phenix-lbl/cctbx_phenix_doc` which contains the django code. 
For example `doc_mb_model_building.html` (rendered like this on the phenix dev doc website - the code in blue shaded areas is the code that is tested)

* If you run bootstrap or libtbx.refresh, these html files are automatically converted to executable python scripts, located in `phenix_dev_doc/examples`. 
For example doc_mb_model_building.py (it has the same basename as the .html file!). 
Note that this examples folder is NOT part of the repository. It could have been done "on the fly" for the tests, but it has been requested that the examples should be available.

* If you run t96, the test phenix_dev_doc/run_tests.py will be executed. This test tries to run the scripts in the `phenix_dev_doc/examples` folder. 
In other words, it tries to execute the code that is described on the website

* The tests are run in parallel: run_test.py calls a list of individual tests that that each test one script, 
for example `phenix_dev_doc/regression/tst_doc_mb_model_building.py` will try to run `phenix_dev_doc/examples/doc_mb_model_building.py` 

* If a test fails, someone has to fix the corresponding html file in `phenix_dev_doc/html_files`

## Bottom line:
* If you submit content to the cctbx documentation or to the phenix developers documentation, please make sure that this code can be 
  1. executed in isolation (or provide means to have example model etc; for example Tom set up an easy command to access his test files)
  1. does not exceed desired testing length (~100 s)  

## In practice:
The large majority of the steps described above are automatic or set up by me. So you don't have to worry about anything.
The only time you'll have to do something is when a test fails. 
If unsure how to proceed, let me know. I can then send a minimal script to show where the code is failing. 
You can do so by yourself as well by running the accompanying .py file in the phenix_dev_doc/examples folder. 
Be aware though that changing the .py file won't fix the test. To do that, you'll have to edit the .html file. Again, I can help if needed.

## Other:
* The cctbx_website tests work exactly in the same way.
* Not every  page is tested, for example if it does not contain code, it is not tested.
