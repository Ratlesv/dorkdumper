# dorkdumper
A tool to process large amounts of google dorks into a text file of urls.
<h2> Installation and running</h2>

To install, run the following command: `$ git clone https://github.com/mistertoenails/dorkdumper`
To run, use the `python` command like so: `python dork_dumper.py`

<h2> Parameters </h2>
  Takes in parameters for the file to use and the delay time between searches.

  Dork file: a path to the file with the search queries.  `file.txt` or `dir/file.txt`
  Sleep time: seconds to sleep in between search queries, so as to avoid triggering CAPTCHA mechanisms.
  The default dork filename is bulk.txt, and the default sleep value is 3 seconds. An example command might look like this: 
  `python dork_dumper.py bulk.txt 3`

Note: The parameter syntax is still rudimentary, and will be updated. As of now, these are the only two arguments, and cannot be placed out of order, and therefore time cannot be specified without specifying the filepath, even if you are intending to use the defaults. 
<h2> Dependencies </h2> 
This script uses the googlesearch-python and duckduckgo-search python modules.
<h2> File formatting

<h3>Input files: </h3> 
 The bulk file of dorks should be a text file organized with one query per line, for an inurl operator, and <b> SHOULD NOT CONTAIN AN OPERATOR ITSELF. </b>
 
 Example: 
```
example_query
example_query2
example_query_3
```
<b> DO NOT FORMAT IT LIKE THIS: </b>
```
inurl:example_query
inurl:example_query2
inurl:example_query3
```
Note: more options for search operators will be added in the future, this version is pretty unfinished.

<h3> Output files </h3>
The output files are organized with one URL per line, and can be directly fed into SQLmap as a bulk target file. 

Results look like this: 
```
https://url1
https://url2
https://url3
https://url4
```
<h2> A note on CAPTCHAs </h2>
Sometimes, a captcha will still be triggered, and the duckduckgo module is imported as well to prevent this, but even that isn't foolproof, so be sure to take your time.


 
