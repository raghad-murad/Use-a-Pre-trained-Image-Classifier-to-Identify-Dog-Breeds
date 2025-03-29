#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Abeer Bassam Saleh
# DATE CREATED: 3/11/2024 

def adjust_results4_isadog(results_dic, dogfile):
          
    # Creates dognames dictionary for quick matching to results_dic labels from 
    # real answer & classifier's answer 
    dognames_dic = dict() 
    
    # Reads in dognames from file, 1 name per line & automatically closes file 
    with open(dogfile, "r") as infile: 
        # Reads in dognames from first line in file 
        line = infile.readline() 
        
        # Processes each line in file until reaching EOF (end-of-file) by 
        # processing line and adding dognames to dognames_dic with while loop 
        while line != "": 
            # Process line by stripping newline from line 
            line = line.strip() 
            # Adds dogname(line) to dognames_dic if it doesn't already exist 
            if line not in dognames_dic: 
                dognames_dic[line] = 1 
                
            # Reads in next line in file to be processed with while loop 
            line = infile.readline() 
            
    # Add to whether pet labels & classifier labels are dogs by appending 
    # two items to end of value(List) in results_dic. 
    # List Index 3 = whether(1) or not(0) Pet Image Label is a dog AND 
    # List Index 4 = whether(1) or not(0) Classifier Label is a dog 
    # How - iterate through results_dic if labels are found in dognames_dic 
    # then label "is a dog" index 3/4 = 1 otherwise index 3/4 = 0 "not a dog" 
    for value in results_dic.values(): 
        # Pet Image Label IS of Dog (e.g. found in dognames_dic) 
        if value[0] in dognames_dic: 
            # Classifier Label IS image of Dog (e.g. found in dognames_dic) 
            # appends (1, 1) because both labels are dogs 
            if value[1] in dognames_dic: 
                value.extend((1, 1)) 
            
            # Classifier Label IS NOT image of dog (e.g. NOT in dognames_dic) 
            # appends (1, 0) because only pet label is a dog 
            else: 
                value.extend((1, 0)) 
            
        # Pet Image Label IS NOT a Dog image (e.g. NOT found in dognames_dic)
        else: 
            # Classifier Label IS image of Dog (e.g. found in dognames_dic) 
            # appends (0, 1) because only classifier label is a dog 
            if value[1] in dognames_dic: 
                value.extend((0, 1)) 
            
            # Classifier Label IS NOT image of Dog (e.g. NOT in dognames_dic) 
            # appends (0, 0) because both labels aren't dogs 
            else: 
                value.extend((0, 0))