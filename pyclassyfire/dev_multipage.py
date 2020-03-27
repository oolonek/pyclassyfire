from pyclassyfire import client



url = "http://classyfire.wishartlab.com"
chunk_size = 50
sleep_interval = 100




tabular_query_multipage('./test_data/sample_table.tsv', 'sanitized_smiles', 'excel-tab')

