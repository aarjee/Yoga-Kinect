#this script created scatterplots for asan-asan and asan-pebl combinations
# takes input from OUTPUT file

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf
import csv
import sys

threshold = 30
metric_values = {}
names_of_asan_metrics = []
names_of_pebl_metrics = []
subjIDs = []
metric_values_dur = {}
names_of_asan_metrics_dur = []
names_of_pebl_metrics_dur = []
subjIDs_dur = []
unilateral = ['Ardhachakrasana','Gorakshasana','Tadasana','Still']
bilateral = ['Garudasana','Katichakrasana','Pranamasana','Natavarasana','TriyakTadasana','Virabhadrasana','Vrikshasana']


myfile_stab = 'OUTPUT_STAB_'+str(threshold)+'.csv'
#myfile_stab = 'OUTPUT_STAB_PIX_'+str(threshold)+'.csv'
myfile_dur = 'OUTPUT_DUR_'+str(threshold)+'.csv'
#myfile_dur = 'OUTPUT_DUR_PIX_'+str(threshold)+'.csv'      

def create_metric_dict(code):
    global metric_values
    global names_of_asan_metrics
    global names_of_pebl_metrics
    global subjIDs
    global metric_values_dur
    global names_of_asan_metrics_dur
    global names_of_pebl_metrics_dur
    global subjIDs_dur
    metric_values = {}
    names_of_asan_metrics = []
    names_of_pebl_metrics = []
    subjIDs = []
    metric_values_dur = {}
    names_of_asan_metrics_dur = []
    names_of_pebl_metrics_dur = []
    subjIDs_dur = []
    
    # preparing data structures for instabilities
    with open (myfile_stab,'r') as input:
        csv_reader = csv.reader(input)

        # inititalize metric name
        metric_name = ''
        # initialize the key name
        subjID = ''
        # read the csv and classify
        for row in csv_reader:
            if(not row):
                continue

            # skipping undesired rows corresponding to aasanas            
            #components = row[2].split('_')
            if(row[1].find('overall')!=-1):
                continue
                
            if(row[1] in bilateral or row[1] in unilateral):
                #print(row[2])
                if(row[2].find('JointType')!=-1 or row[2].find('F30')!=-1 or row[2].find('L30')!=-1 or row[2].find('overall')!=-1 or row[2].find('upper')!=-1 or row[2].find('lower')!=-1):
                    continue
            
            # add subjID to the list of keys of inner dict
            subjID = row[0]
            if(code==0):
                if(subjID not in subjIDs):
                    subjIDs.append(subjID)
            if(code==1):
                if(row[1].startswith("IITD") and (row[0] not in subjIDs)):
                    subjIDs.append(row[0])
            if(code==2):
                if(row[1].startswith("Non-IIT") and (row[0] not in subjIDs)):
                    subjIDs.append(row[0])
            if(code==3):
                if(row[1].startswith("IITD_PG") and (row[0] not in subjIDs)):
                    subjIDs.append(row[0])
            if(code==4):
                if(row[1].startswith("IITD_UG") and (row[0] not in subjIDs)):
                    subjIDs.append(row[0])
                        
                
            # skipping undesired rows corresponding to pebl
            if(row[1]=='simon' and row[2]!='total_correct_responses' and row[2]!='total_time'):
                continue
                    
            if(row[1]=='dspan' and row[2]!='largest_no_of_digits' and row[2]!='total_time'):
                continue    
                    
            if(row[1]=='toh' and row[2]!='overall_avg_time_per_step'):
                continue
                    
            if(row[1]=='iowa' and row[2]!='net_gain'):
                continue
                    
            if(row[1]=='tol' and row[2]!='total_goal_achieved_num' and row[2]!='total_time'):
                continue       
               
            if(row[1]=='rotation' and row[2]!='overall_corr_count' and row[2]!='total_abs_time'):
                continue   
                
            if(row[1]=='bcst' and row[2]!='total_corr_count' and row[2]!='avg_resp_time'):
                continue   
                
            if(row[1]=='stroop' and row[2]!='total_corr_count_overall' and row[2]!='avg_resp_time_overall'):
                continue   
                    
            if(row[1]=='corsi' and row[2]!='memory_span' and row[2]!='avg_time'):
                continue 
                
                 
            # extract metric value
            try:
                value = np.float64(row[3])
            except:
                continue
            
            if(row[2]=='CGPA'):
                metric_name = row[2]
            else:
                if(row[1].startswith("IITD")):
                    metric_name = "IITD_"+row[2]
                else:
                    metric_name = row[1]+'_'+row[2]           
                           
            if row[1] in unilateral:
                metric_name = row[1]
               
            if row[1] in bilateral:
                if('-l' in row[2]):
                    metric_name = row[1]+'-l'
                else:
                    metric_name = row[1]+'-r'
                 
            if row[1]=='simon' and row[2]=='total_correct_responses':
                metric_name = 'simon_correct' 
                
            if row[1]=='toh':
                metric_name = 'toh_avg_time'     
                
            if row[1]=='tol' and metric_name == 'tol_total_goal_achieved_num':
                metric_name = 'tol_goals_achieved'                        
                  
            if row[1]=='rotation':
                if metric_name == 'rotation_overall_corr_count':
                    metric_name = 'rot_correct'   
                if metric_name == 'rotation_total_abs_time':
                    metric_name = 'rot_total_time'
                        
            if row[1]=='bcst':
                if metric_name == 'bcst_total_corr_count':
                    metric_name = 'bcst_correct'   
                if metric_name == 'bcst_avg_resp_time':
                    metric_name = 'bcst_avg_time'    
                
            if row[1]=='stroop':
                if metric_name == 'stroop_total_corr_count_overall':
                    metric_name = 'stroop_correct'   
                if metric_name == 'stroop_avg_resp_time_overall':
                    metric_name = 'stroop_avg_time'
                                          
              
            if(row[1] in unilateral or row[1] in bilateral):
                if (metric_name not in names_of_asan_metrics):
                    names_of_asan_metrics.append(metric_name)
                    metric_values[metric_name] = {}
            else:
                if (metric_name not in names_of_pebl_metrics):
                    names_of_pebl_metrics.append(metric_name)
                    metric_values[metric_name] = {}
            inner_dict = metric_values[metric_name]
            inner_dict[subjID] = value
            
                
   # print(names_of_asan_metrics)
   # print(names_of_pebl_metrics)
     
    # preparing data structures for durations                         
    with open (myfile_dur,'r') as input:
        csv_reader = csv.reader(input)

        # inititalize metric name
        metric_name = ''
        # initialize the key name
        subjID = ''
        # read the csv and classify
        for row in csv_reader:
            if(not row):
                continue

            # skipping undesired rows corresponding to aasanas            
            if(row[2].find('Normalized')!=-1 or row[2].find('tough')!=-1):
                continue
                
            if(row[1].find('overall')!=-1):
                continue
            
                
            # add subjID to the list of keys of inner dict
            subjID = row[0]
            if(code==0):
                if(subjID not in subjIDs_dur):
                    subjIDs_dur.append(subjID)
            if(code==1):
                if(row[1].startswith("IITD") and (row[0] not in subjIDs_dur)):
                    subjIDs_dur.append(row[0])
            if(code==2):
                if(row[1].startswith("Non-IIT") and (row[0] not in subjIDs_dur)):
                    subjIDs_dur.append(row[0])
            if(code==3):
                if(row[1].startswith("IITD_PG") and (row[0] not in subjIDs_dur)):
                    subjIDs_dur.append(row[0])
            if(code==4):
                if(row[1].startswith("IITD_UG") and (row[0] not in subjIDs_dur)):
                    subjIDs_dur.append(row[0])
                
            # skipping undesired rows corresponding to pebl
            if(row[1]=='simon' and row[2]!='total_correct_responses' and row[2]!='total_time'):
                continue
                    
            if(row[1]=='dspan' and row[2]!='largest_no_of_digits' and row[2]!='total_time'):
                continue    
                    
            if(row[1]=='toh' and row[2]!='overall_avg_time_per_step'):
                continue
                    
            if(row[1]=='iowa' and row[2]!='net_gain'):
                continue
                    
            if(row[1]=='tol' and row[2]!='total_goal_achieved_num' and row[2]!='total_time'):
                continue       
                 
            if(row[1]=='rotation' and row[2]!='overall_corr_count' and row[2]!='total_abs_time'):
                continue   
                
            if(row[1]=='bcst' and row[2]!='total_corr_count' and row[2]!='avg_resp_time'):
                continue   
                
            if(row[1]=='stroop' and row[2]!='total_corr_count_overall' and row[2]!='avg_resp_time_overall'):
                continue   
                    
            if(row[1]=='corsi' and row[2]!='memory_span' and row[2]!='avg_time'):
                continue 
                
                 
            # extract metric value
            try:
                value = np.float64(row[3])
            except:
                continue

            if(row[2]=='CGPA'):
                metric_name = row[2]
            else:
                if(row[1].startswith("IITD")):
                    metric_name = "IITD_"+row[2]
                else:
                    metric_name = row[1]+'_'+row[2]           
                            
            if row[1] in unilateral:
                metric_name = row[1]
                
            if row[1] in bilateral:
                if('-l' in row[2]):
                    metric_name = row[1]+'-l'
                else:
                    metric_name = row[1]+'-r'
                 
            if row[1]=='simon' and row[2]=='total_correct_responses':
                metric_name = 'simon_correct' 
               
            if row[1]=='toh':
                metric_name = 'toh_avg_time'     
                
            if row[1]=='tol' and metric_name == 'tol_total_goal_achieved_num':
                metric_name = 'tol_goals_achieved'                        
                    
            if row[1]=='rotation':
                if metric_name == 'rotation_overall_corr_count':
                    metric_name = 'rot_correct'   
                if metric_name == 'rotation_total_abs_time':
                    metric_name = 'rot_total_time'
                       
            if row[1]=='bcst':
                if metric_name == 'bcst_total_corr_count':
                    metric_name = 'bcst_correct'   
                if metric_name == 'bcst_avg_resp_time':
                    metric_name = 'bcst_avg_time'    
                
            if row[1]=='stroop':
                if metric_name == 'stroop_total_corr_count_overall':
                    metric_name = 'stroop_correct'   
                if metric_name == 'stroop_avg_resp_time_overall':
                    metric_name = 'stroop_avg_time'
                                          
                              
            if(row[1] in unilateral or row[1] in bilateral):
                if (metric_name not in names_of_asan_metrics_dur):
                    names_of_asan_metrics_dur.append(metric_name)
                    metric_values_dur[metric_name] = {}
            else:
                if (metric_name not in names_of_pebl_metrics_dur):
                    names_of_pebl_metrics_dur.append(metric_name)
                    metric_values_dur[metric_name] = {}
            inner_dict = metric_values_dur[metric_name]
            inner_dict[subjID] = value

            
def generate_arrays(metric1,metric2,flag):
    if(flag==0):
        first_data = metric_values[metric1]
        second_data = metric_values[metric2]
        arr1 = []
        arr2 = []
        #print("stab subjects")
        for subj in subjIDs:
            a1 = 0
            a2 = 0
            try:
                a1 = first_data[subj]
                a2 = second_data[subj]
                #print(subj)
            except:
                continue
            arr1.append(a1)
            arr2.append(a2)
    else:
        first_data2 = metric_values_dur[metric1]
        second_data2 = metric_values_dur[metric2]
        arr1 = []
        arr2 = []
        #print("dur subjects")
        for subj in subjIDs_dur:
            a1 = 0
            a2 = 0
            try:
                a1 = first_data2[subj]
                a2 = second_data2[subj]
                #print(subj)
            except:
                continue
            arr1.append(a1)
            arr2.append(a2)      
    return arr1, arr2
       
def plot(code):
    if(code==0):
        pdf1 = matplotlib.backends.backend_pdf.PdfPages("stability_plots_all.pdf")
    elif code==1:
        pdf1 = matplotlib.backends.backend_pdf.PdfPages("stability_plots_IIT.pdf")
    elif code==2:
        pdf1 = matplotlib.backends.backend_pdf.PdfPages("stability_plots_non-IIT.pdf")
    elif code==3:
        pdf1 = matplotlib.backends.backend_pdf.PdfPages("stability_plots_IIT-PG.pdf")
    elif code==4:
        pdf1 = matplotlib.backends.backend_pdf.PdfPages("stability_plots_IIT-UG.pdf")   
        
    plot_count = 0
    fig_count = 0
    fig = []

    # plotting asan-asan instabilities
    for first_metric in names_of_asan_metrics:
        for second_metric in names_of_asan_metrics:
            if(first_metric==second_metric):
                continue
                      
            if(second_metric<first_metric):
                continue
                        
            print(first_metric+"-"+second_metric)
            #try:
            array1,array2 = generate_arrays(first_metric,second_metric,0)
    
            X = np.array(array1,dtype = np.float64)
            Y = np.array(array2,dtype = np.float64)
                      
            if(plot_count%4==0):
                fig.append(plt.figure())

            ax = fig[fig_count].add_subplot(221+plot_count)
            ax.plot(X, Y, 'bo')
            ax.set(xlabel=first_metric, ylabel=second_metric)
            plot_count = plot_count+1
                            
            if(plot_count==4):
                pdf1.savefig(fig[fig_count])
                fig_count = fig_count+1
                plot_count = 0
        
    # plotting asan-pebl instabilities
    for first_metric in names_of_asan_metrics:
        for second_metric in names_of_pebl_metrics:
                                   
            print(first_metric+"-"+second_metric)
            #try:
            array1,array2 = generate_arrays(first_metric,second_metric,0)
    
            X = np.array(array1,dtype = np.float64)
            Y = np.array(array2,dtype = np.float64)
                      
            if(plot_count%4==0):
                fig.append(plt.figure())

            ax = fig[fig_count].add_subplot(221+plot_count)
            ax.plot(X, Y, 'bo')
            ax.set(xlabel=first_metric, ylabel=second_metric)
            plot_count = plot_count+1
                            
            if(plot_count==4):
                pdf1.savefig(fig[fig_count])
                fig_count = fig_count+1
                plot_count = 0          
                    
    pdf1.close()
       
    ## plotting asan-asan durations
    if(code==0):
        pdf2 = matplotlib.backends.backend_pdf.PdfPages("duration_plots_all.pdf")
    if(code==1):
        pdf2 = matplotlib.backends.backend_pdf.PdfPages("duration_plots_IIT.pdf")
    if(code==2):
        pdf2 = matplotlib.backends.backend_pdf.PdfPages("duration_plots_non-IIT.pdf")
    if(code==3):
        pdf2 = matplotlib.backends.backend_pdf.PdfPages("duration_plots_IIT-PG.pdf")
    if(code==4):
        pdf2 = matplotlib.backends.backend_pdf.PdfPages("duration_plots_IIT-UG.pdf")

    plot_count = 0
    fig_count = 0
    fig = []

    for first_metric in names_of_asan_metrics_dur:
        for second_metric in names_of_asan_metrics_dur:
            if(first_metric==second_metric):
                continue
                      
            if(second_metric<first_metric):
                continue
                        
            print(first_metric+"-"+second_metric)
            #try:
            array1,array2 = generate_arrays(first_metric,second_metric,0)
    
            X = np.array(array1,dtype = np.float64)
            Y = np.array(array2,dtype = np.float64)
                      
            if(plot_count%4==0):
                fig.append(plt.figure())

            ax = fig[fig_count].add_subplot(221+plot_count)
            ax.plot(X, Y, 'bo')
            ax.set(xlabel=first_metric, ylabel=second_metric)
            plot_count = plot_count+1
                            
            if(plot_count==4):
                pdf2.savefig(fig[fig_count])
                fig_count = fig_count+1
                plot_count = 0
    
    # plotting asan-pebl durations   
    for first_metric in names_of_asan_metrics_dur:
        for second_metric in names_of_pebl_metrics_dur:
                                   
            print(first_metric+"-"+second_metric)
            #try:
            array1,array2 = generate_arrays(first_metric,second_metric,0)
    
            X = np.array(array1,dtype = np.float64)
            Y = np.array(array2,dtype = np.float64)
                      
            if(plot_count%4==0):
                fig.append(plt.figure())

            ax = fig[fig_count].add_subplot(221+plot_count)
            ax.plot(X, Y, 'bo')
            ax.set(xlabel=first_metric, ylabel=second_metric)
            plot_count = plot_count+1
                            
            if(plot_count==4):
                pdf2.savefig(fig[fig_count])
                fig_count = fig_count+1
                plot_count = 0          
    
                  
    pdf2.close()
    

        
def main():
    if(1):
        create_metric_dict(0)
        plot(0)
        
    if(1):
        create_metric_dict(1)
        plot(1)
       
    if(1):
        create_metric_dict(2)
        plot(2)
        
    if(1):
        create_metric_dict(3)
        plot(3)
        
    if(1):
        create_metric_dict(4)
        plot(4)


main()

