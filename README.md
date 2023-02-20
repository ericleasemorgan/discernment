
# Discernment

Given a set of documents, the contents of this repository creates a corpus and makes an attempt to measure how the concept of discernment evolves over time. To that end, there is the briefest of documentation:

   * originals2txt.sh - extract plain text from a set of configured files
   * list-names.sh - output a list of names associated with each file
   * anonymize.sh - do our best to remove names of people content
   * rename.sh - rename files to finish the anonymization process
   * filenames2metadata.py - create a metadata (CSV) file suitable to the Reader

After all of the above steps have been completed, one can then create a Distant Reader study carrel (data set) from the result using the `rdr build` command.

---
<p style='text-align:right'>Eric Lease Morgan &lt;emorgan@nd.edu&gt;<br />
Feburary 20, 2023
</p>