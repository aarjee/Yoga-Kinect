import numpy as np
import os
import sys
import csv

if(len(sys.argv)!=4):
    sys.exit('Usage: <base_dir> <PEBL_test_name> <subj_id>')

base_dir = sys.argv[1]
test_name = sys.argv[2]
subj_id = sys.argv[3]
'''
base_dir = 'C:/Users/a299792458tm/Anaconda3/CSProject/version2/simon'
test_name = 'simon'
subj_id = '53'
'''
csv_name = test_name + '-' + subj_id + r'.csv'
csv_address = base_dir + '/' + test_name + '/data/'+subj_id+ '/' + csv_name

def simon():
    # print('simon')
    dataset = [] # figment of old script, kept here for reference
    all_response_times = [] # for calculation of overall mean
    # list of strings maintaining different types of simon tests
    subtypes_simon = []
    supertypes_simon = []
    # dataset classified based on type
    classified_dataset = {} # example key: 1_-50
    super_types = {} # example key: 1 
    # read the csv file and classify each row
    with open(csv_address,'r+') as sim:
        csv_reader = csv.reader(sim)
        for row in csv_reader:
            type_of_simon = str(row[2])+'_'+str(row[3])
            supertype_of_simon = str(row[2])
            if(row[0]!='subnum'): # first row is not useful for analysis
                dataset.append(row)
                # store all response times for mean computation
                all_response_times.append(np.float64(row[7]))
                # classification based on type 1, 2
                # created a classified dict called super_types
                # keys stored in supertypes_simon
                if(supertype_of_simon not in supertypes_simon):
                    supertypes_simon.append(supertype_of_simon)
                    super_types[supertype_of_simon] = []
                super_types[supertype_of_simon].append(row)
                # classification based on type 1_-200, 1_-50 ...
                # created a classified dict called classified_dataset
                # keys stored in subtypes_simon
                if(type_of_simon not in subtypes_simon):
                    # create a subtype in the list of subtypes and 
                    # add that category for storage of data
                    subtypes_simon.append(type_of_simon)
                    classified_dataset[type_of_simon] = []
                classified_dataset[type_of_simon].append(row)
                # if new classificaton type needed, add below
                # create a classified dict with a fancy name eg DICT_1
                # store keys in a list eg LIST_1
        pass
    # now we have a dict, with each key mapped to a copy of the rows of
    # the csv file, which belong to the same category
    means = {}
    names = []
    # for adding more classification types
    # copy paste the following code block
    # replace the list of title subtypes_simon by LIST_1
    # replace the dict of classified dataset with DICT_1
    for test_type in subtypes_simon:
        # create a list of response times
        # initialize the mean of this category
        list_of_response_times = []
        mean_of_response_times = np.float64(0)
        final_name = ''
        # fill the elements of the list_of_respose_times
        for row in classified_dataset[test_type]:
            list_of_response_times.append(np.float64(row[7]))
            continue
        # compute mean and store it the dict created above
        mean_of_response_times = np.mean(list_of_response_times)
        final_name = 'mean_'+ test_type
        means[final_name] = mean_of_response_times
        names.append(final_name)
        continue
    # print(names,len(means))
    # compute mean of 1 and 2 tasks
    for test_type in supertypes_simon:
        # create a list of response times
        # initialize the mean of this category
        list_of_response_times = []
        mean_of_response_times = np.float64(0)
        final_name = ''
        # fill the elements of the list_of_respose_times
        for row in super_types[test_type]:
            list_of_response_times.append(np.float64(row[7]))
            continue
        # compute mean and store it the dict created above
        mean_of_response_times = np.mean(list_of_response_times)
        final_name = 'mean_'+ test_type + '_mean'
        means[final_name] = mean_of_response_times
        names.append(final_name)
        continue
    # print(names,len(means))
    # add the overall mean in the beginning
    _name = 'mean_mean_mean'
    names.append(_name)
    means[_name] = np.mean(all_response_times)
    # write the metrics into the csv
    for name in names:
        row = [subj_id,'simon',name,means[name]]
        with open('OUTPUT.csv',"a") as outp:
            csv_writer = csv.writer(outp)
            csv_writer.writerow(row)
    
def dspan():
    print('dspan')
    pass

def toh():
    print('toh')
    pass


# Create a dict of functions, call the function corresponding to the required test

func_dict = {'simon':simon, 'dspan':dspan, 'toh':toh}


# In[139]:


func_dict[test_name]()

