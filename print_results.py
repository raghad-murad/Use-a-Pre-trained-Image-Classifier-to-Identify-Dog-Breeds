#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Abeer Bassam Saleh
# DATE CREATED: 3/11/2024 

def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
      
    # Print summary statistics over the run
    print("\n\n*** Results Summary for CNN Model Architecture", model.upper(), "***")
    print("{:20}: {:3d}".format('N Images', results_stats_dic['n_images']))
    print("{:20}: {:3d}".format('N Dog Images', results_stats_dic['n_dogs_img']))

    # TODO: 6a. Print the number of NOT-dog images
    print("{:20}: {:3d}".format('N Not-Dog Images', results_stats_dic['n_notdogs_img']))

    # Print summary statistics (percentages) on Model Run
    print(" ")
    for key in results_stats_dic:
        # TODO: 6b. Print all the percentages in the results_stats_dic
        if key.startswith('pct'):
            print("{:20}: {:.2f}".format(key, results_stats_dic[key]))

    # IF print_incorrect_dogs == True AND there were images incorrectly classified as dogs or vice versa - print out these cases
    if (print_incorrect_dogs and 
        ((results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs']) != results_stats_dic['n_images'])):
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        
        # Process through results dict, printing incorrectly classified dogs
        for key in results_dic:
            # TODO: 6c. Print the pet label and the classifier label from results_dic ONLY when the classifier function misclassified dogs
            if (results_dic[key][3] == 1 and results_dic[key][4] == 0) or (results_dic[key][3] == 0 and results_dic[key][4] == 1):
                print("Real: {:>26}   Classifier: {:>30}".format(results_dic[key][0], results_dic[key][1]))

    # IF print_incorrect_breed == True AND there were dogs whose breeds were incorrectly classified - print out these cases                    
    if (print_incorrect_breed and 
        (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed'])):
        print("\nINCORRECT Dog Breed Assignment:")
        
        # Process through results dict, printing incorrectly classified breeds
        for key in results_dic:
            # Pet Image Label is-a-Dog, classified as-a-dog but is WRONG breed
            if (sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0):
                print("Real: {:>26}   Classifier: {:>30}".format(results_dic[key][0], results_dic[key][1]))