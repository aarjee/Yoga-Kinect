import numpy as np
import csv
import sys
import pandas as pd


# hard asanas: Goraksh and Natavar
# medium: Virabhadra and Ardhachakra
# easy: Tada and Pranam

unilateral = ['Tadasana','Gorakshasana','Ardhachakrasana']
bilateral = ['Virabhadrasana','Pranamasana','Natavarasana']
header = ['Subject','Tadasana-Instability','Tadasana-Instability-lower','Tadasana-Dur','Gorakshasana-Instability','Gorakshasana-Instability-lower','Gorakshasana-Dur','Ardhachakrasana-Instability','Ardhachakrasana-Instability-lower','Ardhachakrasana-Dur','Virabhadrasana-Instability','Virabhadrasana-Instability-lower','Virabhadrasana-Dur','Pranamasana-Instability','Pranamasana-Instability-lower','Pranamasana-Dur','Natavarasana-Instability','Natavarasana-Instability-lower','Natavarasana-Dur','Easy-asans-Instability','Easy-asans-Instability-lower','Easy-asans-Duration','Medium-asans-Instability','Medium-asans-Instability-lower','Medium-asans-Duration','Hard-asans-Instability','Hard-asans-Instability-lower','Hard-asans-Duration','simon-correct','simon-total-time','dspan-max-dig','dspan-total-time','toh-avg-time','toh-total-excess-steps','toh-total-time','iowa-net-gain','tol-goals-achieved','tol-total-time','rot-correct','rot-total-time','bcst-correct','bcst-total-time','stroop-correct','stroop-total-count','corsi-memory-span','corsi-avg-time']

outcsv = 'Summary.csv'
with open(outcsv,'a') as csvFile:
    csv_writer = csv.writer(csvFile)
    csv_writer.writerow(header)

stab_data = pd.read_csv('/home/others/sonikat/Yoga-Kinect/scripts/OUTPUT_STAB_30.csv',names=["Subject", "Task", "Metric", "Value"])
dur_data = pd.read_csv('/home/others/sonikat/Yoga-Kinect/scripts/OUTPUT_DUR_30.csv',names=["Subject", "Task", "Metric", "Value"])

for num in range(76):
    row = []
    sub = "Subj"+str(num+1).zfill(3)
    row.append(sub)
    
    #unilateral   
    try:
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'Tadasana') & (stab_data["Metric"] == 'Instability-l_DUR')]
        row.append(subj_stab_data["Value"].item())
        e1_i = subj_stab_data["Value"].item()
    except:
        row.append("")
        e1_i = 0
        
    try:
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'Tadasana') & (stab_data["Metric"] == 'Instability-lower-l_DUR')]
        row.append(subj_stab_data["Value"].item())
        e1_il = subj_stab_data["Value"].item()
    except:
        row.append("")
        e1_il = 0
    
    try:
        subj_dur_data = dur_data.loc[(dur_data["Subject"] == sub) & (dur_data["Task"] == 'Tadasana') & (dur_data["Metric"] == 'Duration-l')]
        row.append(subj_dur_data["Value"].item())
        e1_d = subj_dur_data["Value"].item()
    except:
        row.append("")
        e1_d = 0
    
    try:
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'Gorakshasana') & (stab_data["Metric"] == 'Instability-l_DUR')]
        row.append(subj_stab_data["Value"].item())
        h1_i = subj_stab_data["Value"].item()
    except:
        row.append("")
        h1_i = 0
        
    try:
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'Gorakshasana') & (stab_data["Metric"] == 'Instability-lower-l_DUR')]
        row.append(subj_stab_data["Value"].item())
        h1_il = subj_stab_data["Value"].item()
    except:
        row.append("")
        h1_il = 0
        
    try:    
        subj_dur_data = dur_data.loc[(dur_data["Subject"] == sub) & (dur_data["Task"] == 'Gorakshasana') & (dur_data["Metric"] == 'Duration-l')]
        row.append(subj_dur_data["Value"].item())
        h1_d = subj_dur_data["Value"].item()
    except:
        row.append("")
        h1_d = 0
    
    try:
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'Ardhachakrasana') & (stab_data["Metric"] == 'Instability-l_DUR')]
        row.append(subj_stab_data["Value"].item())
        m1_i = subj_stab_data["Value"].item()
    except:
        row.append("")
        m1_i = 0
        
    try:
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'Ardhachakrasana') & (stab_data["Metric"] == 'Instability-lower-l_DUR')]
        row.append(subj_stab_data["Value"].item())
        m1_il = subj_stab_data["Value"].item()
    except:
        row.append("")
        m1_il = 0
    
    try:
        subj_dur_data = dur_data.loc[(dur_data["Subject"] == sub) & (dur_data["Task"] == 'Ardhachakrasana') & (dur_data["Metric"] == 'Duration-l')]
        row.append(subj_dur_data["Value"].item())
        m1_d = subj_dur_data["Value"].item()
    except:
        row.append("")
        m1_d = 0
    
    
    #bilateral
    try:
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'Virabhadrasana') & (stab_data["Metric"] == 'Instability-l_DUR')]
        v1 = subj_stab_data["Value"].item()
    except:
        v1=0
        
    try:
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'Virabhadrasana') & (stab_data["Metric"] == 'Instability-r_DUR')]
        v2 = subj_stab_data["Value"].item()
    except:
        v2=0
    
    if(v1==0 and v2==0):
        row.append("")
        m2_i = 0
    else:
        #row.append(float(v1+v2)/2)
        if(v1==0):
            m2_i = v2
        else:
            if(v2==0):
                m2_i = v1
            else:
                m2_i = float(v1+v2)/2
    
        row.append(m2_i)    
        
    try:
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'Virabhadrasana') & (stab_data["Metric"] == 'Instability-lower-l_DUR')]
        v1 = subj_stab_data["Value"].item()
    except:
        v1=0
        
    try:
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'Virabhadrasana') & (stab_data["Metric"] == 'Instability-lower-r_DUR')]
        v2 = subj_stab_data["Value"].item()
    except:
        v2=0
    
    if(v1==0 and v2==0):
        row.append("")
        m2_il = 0
    else:
        #row.append(float(v1+v2)/2)
        if(v1==0):
            m2_il = v2
        else:
            if(v2==0):
                m2_il = v1
            else:
                m2_il = float(v1+v2)/2
        
        row.append(m2_il)
                            
    try:
        subj_dur_data = dur_data.loc[(dur_data["Subject"] == sub) & (dur_data["Task"] == 'Virabhadrasana') & (dur_data["Metric"] == 'Duration-l')]
        d1 = subj_dur_data["Value"].item()
    except:
        d1 = 0
    
    try:
        subj_dur_data = dur_data.loc[(dur_data["Subject"] == sub) & (dur_data["Task"] == 'Virabhadrasana') & (dur_data["Metric"] == 'Duration-r')]
        d2 = subj_dur_data["Value"].item()
    except:
        d2 = 0
    
    if(d1==0 and d2==0):
        row.append("")
        m2_d = 0
    else:
        #row.append(float(d1+d2)/2)
        if(d1==0):
            m2_d = d2
        else:
            if(d2==0):
                m2_d = d1
            else:
                m2_d = float(d1+d2)/2
    
        row.append(m2_d)
        
    try:    
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'Pranamasana') & (stab_data["Metric"] == 'Instability-l_DUR')]
        v1 = subj_stab_data["Value"].item()
    except:
        v1=0
        
    try:    
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'Pranamasana') & (stab_data["Metric"] == 'Instability-r_DUR')]
        v2 = subj_stab_data["Value"].item()
    except:
        v2=0
    
    if(v1==0 and v2==0):
        row.append("")
        e2_i = 0
    else:
        #row.append(float(v1+v2)/2)
        if(v1==0 and v2==0):
            row.append("")
            e2_i = 0
        else:
            if(v1==0):
                e2_i = v2
            else:
                if(v2==0):
                    e2_i = v1
                else:
                    e2_i = float(v1+v2)/2        
       
        row.append(e2_i)
        
    try:    
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'Pranamasana') & (stab_data["Metric"] == 'Instability-lower-l_DUR')]
        v1 = subj_stab_data["Value"].item()
    except:
        v1=0
        
    try:    
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'Pranamasana') & (stab_data["Metric"] == 'Instability-lower-r_DUR')]
        v2 = subj_stab_data["Value"].item()
    except:
        v2=0
    
    if(v1==0 and v2==0):
        row.append("")
        e2_il = 0
    else:
        #row.append(float(v1+v2)/2)
        if(v1==0 and v2==0):
            row.append("")
            e2_il = 0
        else:
            if(v1==0):
                e2_il = v2
            else:
                if(v2==0):
                    e2_il = v1
                else:
                    e2_il = float(v1+v2)/2        
       
        row.append(e2_il)
            
    try:
        subj_dur_data = dur_data.loc[(dur_data["Subject"] == sub) & (dur_data["Task"] == 'Pranamasana') & (dur_data["Metric"] == 'Duration-l')]
        d1 = subj_dur_data["Value"].item()
    except:
        d1=0
    
    try:
        subj_dur_data = dur_data.loc[(dur_data["Subject"] == sub) & (dur_data["Task"] == 'Pranamasana') & (dur_data["Metric"] == 'Duration-r')]
        d2 = subj_dur_data["Value"].item()
    except:
        d2=0
        
    if(d1==0 and d2==0):
        row.append("")
        e2_d = 0
    else:
        #row.append(float(d1+d2)/2)
        if(d1==0):
            e2_d = d2
        else:
            if(d2==0):
                e2_d = d1
            else:
                e2_d = float(d1+d2)/2        
       
        row.append(e2_d)        
    
    try:
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'Natavarasana') & (stab_data["Metric"] == 'Instability-l_DUR')]
        v1 = subj_stab_data["Value"].item()
    except:
        v1=0
        
    try:
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'Natavarasana') & (stab_data["Metric"] == 'Instability-r_DUR')]
        v2 = subj_stab_data["Value"].item()
    except:
        v2=0
    
    if(v1==0 and v2==0):
        row.append("")
        h2_i = 0
    else:
        #row.append(float(v1+v2)/2)
        if(v1==0):
            h2_i = v2
        else:
            if(v2==0):
                h2_i = v1
            else:
                h2_i = float(v1+v2)/2        
       
        row.append(h2_i)   
        
    try:
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'Natavarasana') & (stab_data["Metric"] == 'Instability-lower-l_DUR')]
        v1 = subj_stab_data["Value"].item()
    except:
        v1=0
        
    try:
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'Natavarasana') & (stab_data["Metric"] == 'Instability-lower-r_DUR')]
        v2 = subj_stab_data["Value"].item()
    except:
        v2=0
    
    if(v1==0 and v2==0):
        row.append("")
        h2_il = 0
    else:
        #row.append(float(v1+v2)/2)
        if(v1==0):
            h2_il = v2
        else:
            if(v2==0):
                h2_il = v1
            else:
                h2_il = float(v1+v2)/2        
       
        row.append(h2_il)   
    
    try:
        subj_dur_data = dur_data.loc[(dur_data["Subject"] == sub) & (dur_data["Task"] == 'Natavarasana') & (dur_data["Metric"] == 'Duration-l')]
        d1 = subj_dur_data["Value"].item()
    except:
        d1=0
    
    try:
        subj_dur_data = dur_data.loc[(dur_data["Subject"] == sub) & (dur_data["Task"] == 'Natavarasana') & (dur_data["Metric"] == 'Duration-r')]
        d2 = subj_dur_data["Value"].item()
    except:
        d2=0
    
    if(d1==0 and d2==0):
        row.append("")
        h2_d = 0
    else:
        #row.append(float(d1+d2)/2)
        if(d1==0):
            h2_d = d2
        else:
            if(d2==0):
                h2_d = d1
            else:
                h2_d = float(d1+d2)/2        
       
        row.append(h2_d)   
    
    if(e1_i==0 and e2_i==0):
        row.append("")
    else:
        if(e1_i==0 or e2_i==0):
            row.append(e1_i+e2_i)
        else:
            row.append((e1_i+e2_i)/2)
    
    if(e1_il==0 and e2_il==0):
        row.append("")
    else:
        if(e1_il==0 or e2_il==0):
            row.append(e1_il+e2_il)
        else:
            row.append((e1_il+e2_il)/2)
    
    if(e1_d==0 and e2_d==0):
        row.append("")
    else:
        if(e1_d==0 or e2_d==0):
            row.append(e1_d+e2_d)
        else:
            row.append((e1_d+e2_d)/2)
            
    if(m1_i==0 and m2_i==0):
        row.append("")
    else:
        if(m1_i==0 or m2_i==0):
            row.append(m1_i+m2_i)
        else:
            row.append((m1_i+m2_i)/2)
    
    if(m1_il==0 and m2_il==0):
        row.append("")
    else:
        if(m1_il==0 or m2_il==0):
            row.append(m1_il+m2_il)
        else:
            row.append((m1_il+m2_il)/2)
    
    if(m1_d==0 and m2_d==0):
        row.append("")
    else:
        if(m1_d==0 or m2_d==0):
            row.append(m1_d+m2_d)
        else:
            row.append((m1_d+m2_d)/2)
    
  
    if(h1_i==0 and h2_i==0):
        row.append("")
    else:
        if(h1_i==0 or h2_i==0):
            row.append(h1_i+h2_i)
        else:
            row.append((h1_i+h2_i)/2)
    
    if(h1_il==0 and h2_il==0):
        row.append("")
    else:
        if(h1_il==0 or h2_il==0):
            row.append(h1_il+h2_il)
        else:
            row.append((h1_il+h2_il)/2)
    
    if(h1_d==0 and h2_d==0):
        row.append("")
    else:
        if(h1_d==0 or h2_d==0):
            row.append(h1_d+h2_d)
        else:
            row.append((h1_d+h2_d)/2)   

    
    # pebl
    try:
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'simon') & (stab_data["Metric"] == 'total_correct_responses')]
        row.append(subj_stab_data["Value"].item())
    except:
        row.append("")
    try:
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'simon') & (stab_data["Metric"] == 'total_time')]
        row.append(subj_stab_data["Value"].item())
    except:
        row.append("")
        
    try:    
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'dspan') & (stab_data["Metric"] == 'largest_no_of_digits')]
        row.append(subj_stab_data["Value"].item())
    except:
        row.append("")
    try:
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'dspan') & (stab_data["Metric"] == 'total_time')]
        row.append(subj_stab_data["Value"].item())
    except:
        row.append("")
    
    try:  
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'toh') & (stab_data["Metric"] == 'overall_avg_time_per_step')]
        row.append(subj_stab_data["Value"].item())
    except:
        row.append("")
    try:
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'toh') & (stab_data["Metric"] == 'total_excess_steps')]
        row.append(subj_stab_data["Value"].item())
    except:
        row.append("")
    try:
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'toh') & (stab_data["Metric"] == 'total_time')]
        row.append(subj_stab_data["Value"].item())
    except:
        row.append("")
        
    try:
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'iowa') & (stab_data["Metric"] == 'net_gain')]
        row.append(subj_stab_data["Value"].item())
    except:
        row.append("")
    
    try:
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'tol') & (stab_data["Metric"] == 'total_goal_achieved_num')]
        row.append(subj_stab_data["Value"].item())
    except:
        row.append("")
    try:
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'tol') & (stab_data["Metric"] == 'total_time')]
        row.append(subj_stab_data["Value"].item())
    except:
        row.append("")
    
    try:
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'rotation') & (stab_data["Metric"] == 'overall_corr_count')]
        row.append(subj_stab_data["Value"].item()) 
    except:
        row.append("")
    try:
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'rotation') & (stab_data["Metric"] == 'total_abs_time')]
        row.append(subj_stab_data["Value"].item())
    except:
        row.append("")
        
    try:
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'bcst') & (stab_data["Metric"] == 'total_corr_count')]
        row.append(subj_stab_data["Value"].item())
    except:
        row.append("")
    try:   
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'bcst') & (stab_data["Metric"] == 'avg_resp_time')]
        row.append(subj_stab_data["Value"].item())
    except:
        row.append("")
        
    try:
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'stroop') & (stab_data["Metric"] == 'total_corr_count_overall')]
        row.append(subj_stab_data["Value"].item())
    except:
        row.append("")
    try:   
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'stroop') & (stab_data["Metric"] == 'avg_resp_time_overall')]
        row.append(subj_stab_data["Value"].item())
    except:
        row.append("")
        
    try:
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'corsi') & (stab_data["Metric"] == 'memory_span')]
        row.append(subj_stab_data["Value"].item())
    except:
        row.append("")
    try:    
        subj_stab_data = stab_data.loc[(stab_data["Subject"] == sub) & (stab_data["Task"] == 'corsi') & (stab_data["Metric"] == 'avg_time')]
        row.append(subj_stab_data["Value"].item())
    except:
        row.append("")
        
    with open(outcsv,'a') as csvFile:
            csv_writer = csv.writer(csvFile)
            csv_writer.writerow(row)
