#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: Abeer Bassam Saleh
# DATE CREATED: 3/11/2024 

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels

def calculates_results_stats(results_dic):

    # Creates empty dictionary for results_stats_dic
    results_stats_dic = dict()
    
    # Sets all counters to initial values of zero so that they can 
    # be incremented while processing through the images in results_dic 
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0       
    
    # process through the results dictionary
    for key in results_dic:

        # Labels Match Exactly
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1

        # Pet Image Label is a Dog AND Labels match - counts Correct Breed
        if results_dic[key][3] == 1 and results_dic[key][2] == 1:
            results_stats_dic['n_correct_breed'] += 1
        
        # Pet Image Label is a Dog - counts number of dog images
        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1
            
            # Classifier classifies image as Dog (& pet image is a dog)
            # counts number of correct dog classifications
            if results_dic[key][4] == 1:
                results_stats_dic['n_correct_dogs'] += 1

        # Pet Image Label is NOT a Dog
        else:
            # Classifier classifies image as NOT a Dog (& pet image isn't a dog)
            # counts number of correct NOT dog classifications
            if results_dic[key][4] == 0:
                results_stats_dic['n_correct_notdogs'] += 1


    # Calculates run statistics (counts & percentages) below that are calculated
    # using the counters from above.
    
    # calculates number of total images
    results_stats_dic['n_images'] = len(results_dic)

    # calculates number of not-a-dog images using - images & dog images counts
    results_stats_dic['n_notdogs_img'] = (results_stats_dic['n_images'] - 
                                      results_stats_dic['n_dogs_img']) 

    # Calculates % correct for matches
    results_stats_dic['pct_match'] = (results_stats_dic['n_match'] / results_stats_dic['n_images']) * 100.0

    # Calculates % correct dogs
    results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] / results_stats_dic['n_dogs_img']) * 100.0

    # Calculates % correct breed of dog
    results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] / results_stats_dic['n_dogs_img']) * 100.0

    # Calculates % correct not-a-dog images
    # Uses conditional statement for when no 'not a dog' images were submitted 
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] /
                                                results_stats_dic['n_notdogs_img'])*100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0

    # Return the results_stats_dic dictionary
    return results_stats_dic