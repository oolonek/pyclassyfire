## pyclassyfire
[![Build Status](https://travis-ci.org/JamesJeffryes/pyclassyfire.svg?branch=master)](https://travis-ci.org/JamesJeffryes/pyclassyfire)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/011626d1fdc54bc089adf1c0ae1208ca)](https://www.codacy.com/app/JamesJeffryes/pyclassyfire?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=JamesJeffryes/pyclassyfire&amp;utm_campaign=Badge_Grade)

This package provides a set of helper functions in python for 
annotating chemical structures with the chemical ontology developed by 
Djoumbou et. al using the [ClassyFire API](http://classyfire.wishartlab.com/)

## New function dev

The objective is to fetch classyfire results for large table of smiles or inchi encoded structures.

### Two problems :


The ClassyFire API now only returns paginated JSON files (10 compounds/page) see <http://classyfire.wishartlab.com/access>
It is thus required to adapt the get_results function.

This first problem is apparently resolved by the proposed get_results_multipage function.

However, when calling the get_results_multipage function from the tabular_query function only the output from chunk 1 are returned.
The tabular_query_multipage was written to call get_results_multipage. Did not sucess for now.
Looks like a faulty incrementation of the i counter indicating the change of query_id.




