import pandas as pd
import os.path

class Compare_Csv_File(object):
#     src_file_obj = None
#     dest_file_obj = None
#     delimiter_obj = None
    
#     def __init__(self):
#         pass
#       
#     def __init__(self,src_file,dest_file,delimiter):
#         global src_file_obj,dest_file_obj,delimiter_obj 
#         src_file_obj = src_file
#         dest_file_obj = dest_file
#         delimiter_obj = delimiter
       
#     def __init__(self,dest_file,delimiter):
#         global dest_file_obj,delimiter_obj 
#         dest_file_obj = dest_file
#         delimiter_obj = delimiter
          
               
    def comparecsv(self,src_file,dest_file,ignore_col_list,delimiter):
        try:
            source_DataFrame=pd.read_csv(src_file, sep=delimiter, low_memory=False)
#             print source_DataFrame
            target_DataFrame=pd.read_csv(dest_file, sep=delimiter, low_memory=False)
            total_rows_compare = len(source_DataFrame.index)
            print total_rows_compare
            if (ignore_col_list != "None"):
                source_DataFrame.drop(ignore_col_list, inplace=True, axis=1)
                target_DataFrame.drop(ignore_col_list, inplace=True, axis=1)
            diff_DataFrame = pd.concat([source_DataFrame,target_DataFrame]).drop_duplicates(keep=False)
            total_rows = len(diff_DataFrame.index)
            if total_rows > 0:
                print "Not_Matched"
                print total_rows
#                 print diff_DataFrame
#                 print diff_DataFrame.iloc[:,3]
            else:
                print "Matched"            
        except IOError:
            print  "File Not Found"
        except Exception:
            print  "Unknown error, please check the input"
           
        
    def fileexist(self):
        print os.path.exists(targ_file)

    def getStatusFromCSV(self,status_field,**input_fields):
        try:
            target_DataFrame=pd.read_csv(dest_file_obj, sep=delimiter_obj)
#             print target_DataFrame
            if input_fields is not None:
                for key in input_fields:
    #                 print "another keyword arg: %s: %s" % (key, kwargs[key])
    #                 print target_DataFrame[key]
    #                 print kwargs[key]
                    target_DataFrame = target_DataFrame[(target_DataFrame[key] == input_fields[key])]
                    print target_DataFrame
            else:
                print "Please pass the keyword arguments"
            return  target_DataFrame.get_value(0, status_field, False)
        except IOError:
            print "File Not Found: %s" %dest_file_obj
            return  "Error"
        except TypeError:
            print "Search field type is incorrect: %s" %input_fields
            return  "Error"
        except Exception:
            print "Unknown Error, please check the input"
            return  "Error"


# c1 = Compare_Csv_File('D:\\Automation\\CSVPanda\\File1.csv','D:\\Automation\\CSVPanda\\File2.csv',',')
c1 = Compare_Csv_File()
ignore_col_list = "None"
c1.comparecsv("D:\Automation\CSVPanda\XLUpdate_Big.csv","D:\Automation\CSVPanda\XLUpdate_Big1.csv",ignore_col_list,',')
# c1 = Compare_Csv_File("D:\\Automation\\CSVPanda\\File1.csv",',')
# c1.getStatusFromCSV('id',name='dhanya', mark=90 , id=122)

# target_DataFrame=pd.read_csv("D:\\Automation\\CSVPanda\\File1.csv", sep=',')
# key='name'
# value='dhanya'
# final = target_DataFrame[(target_DataFrame[key] == value)]
# final = target_DataFrame[(target_DataFrame['name'] == 'dhanya')]
# print final.id


