import textdistance
import os
import numpy
import csv
from datetime import datetime

print('TXT_SIMILARITY')
result_array = []
result_array.append( ['file_A','file_B','hamming_normalized','levenshtein_normalized','jaro_winkler','ratcliff_obershelp','jaccard'])
for filename_a in os.listdir('/app/input_txt_a'):

    if filename_a.endswith(".txt"):
        path_a = '/app/input_txt_a'+'/'+filename_a
        with open(path_a, 'r') as file:
            data_a = file.read()
            for filename_b in os.listdir('/app/input_txt_b'):
                if filename_b.endswith(".txt"):
                    path_b = '/app/input_txt_b'+'/'+filename_b
                    with open(path_b, 'r') as file:
                        data_b = file.read()
                        print('(A: '+filename_a+') VS (B: '+filename_b+')')
                        hamming_normalized = round( (textdistance.hamming.normalized_similarity(data_b, data_a)),2)
                        print('     Hamming percent normalized similarity: '+str(hamming_normalized))
                        levenshtein_normalized = round( (textdistance.levenshtein.normalized_similarity(data_b, data_a)),2)
                        print('     Levenshtein percent normalized similarity: '+str(levenshtein_normalized))
                        jaro_winkler = round( (textdistance.jaro_winkler(data_b, data_a)),2)
                        print('     Jaro/Winkler percent similarity: '+str(jaro_winkler))
                        ratcliff_obershelp = round( (textdistance.ratcliff_obershelp(data_b, data_a)),2)
                        print('     Ratcliff/Obershelp percent similarity: '+str(ratcliff_obershelp))
                        jaccard = round( (textdistance.jaccard(data_b, data_a)),2)
                        print('     Jaccard percent similarity: '+str(ratcliff_obershelp))
                        result_array.append([filename_a,filename_b,hamming_normalized,levenshtein_normalized,jaro_winkler,ratcliff_obershelp,jaccard])

now = datetime.now()
timestamp = datetime.timestamp(now)

with open("/app/output_csv/confrontation"+str(timestamp)+".csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(result_array)