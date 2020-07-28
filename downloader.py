
import wget
import csv
import os
 

# Columns:
# df.columns = [  'Assessment_reference',   -> row[0]
#                 'Assessment_createdAt',   -> row[1] 
#                 'App_build_digest',       -> row[2] Hash256 needed to download mobile app
#                 'App_build_version',      -> row[3]
#                 'build',                  -> row[4] empty 
#                 'Application_createdAt',  -> row[5]
#                 'Application_reference',  -> row[6]
#                 'package_key',            -> row[7]
#                 'Platform',               -> row[8]
#                 'AnalysisConfigLevel']    -> row[9]

dir = "downloads"
if not os.path.exists(dir):
    os.mkdir(dir)

with open('result.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print(f'\tAssessment ref: {row[0]} assessment created at: {row[2]} ')
            # print(f'\thttps://content-api.nowsecure.com/sha256/{row[2]}')

            print(f'\tBeginning file download of {row[7]}')
            
            url = 'https://content-api.nowsecure.com/sha256/'+str(row[2])
            print(url)
            
            file_extension = ".ipa" if row[8] == "ios" else ".apk"
            wget.download(url, "downloads/"+str(row[7])+"_"+row[8]+"_"+row[9]+"_"+row[1]+file_extension)

            line_count += 1
    print(f'Processed {line_count} lines.')
