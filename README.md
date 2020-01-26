# TXT Similarity

Just a Docker/Python script that checks the similarities between two groups of txt files using the Python library **text_distance**.

The input are the **txt files** in the directories:
* /app/input_txt_a/
* /app/input_txt_b/

The output are the **csv files** in the directory:
* /app/output_csv/

The script uses 5 different algorithms to measure the similarities:
* Hamming distance
* Levenshtein distance
* Jaro-Winkler
* Jaccard index
* Ratcliff-Obershelp
