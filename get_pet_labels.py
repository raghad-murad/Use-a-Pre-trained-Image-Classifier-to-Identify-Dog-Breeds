#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Abeer Bassam Saleh
# DATE CREATED: 3/11/2024 

from os import listdir
# Imports print functions that check the lab
from print_functions_for_lab_checks import *

def get_pet_labels(image_dir):
   
    # Creates list of files in directory
    filename_list = listdir(image_dir)
    
    # Creates empty dictionary for results (pet labels, etc.)
    results_dic = {}
    
    # Processes each file in the directory
    for filename in filename_list:
        if filename[0] != ".":  # Skips hidden files starting with .
            # Sets pet_image variable to filename 
            pet_image = filename.lower()

            # Splits lower case string by _ to break into words 
            word_list_pet_image = pet_image.split("_")

            # Create pet_name starting as empty string
            pet_name = ""

            # Loops to check if word in pet name is only alphabetic characters
            # and appends word to pet_name separated by trailing space 
            for word in word_list_pet_image:
                if word.isalpha():
                    pet_name += word + " "

            # Strip off starting/trailing whitespace characters 
            pet_name = pet_name.strip()

            # Adds filename and pet_name to results_dic
            if filename not in results_dic:
                results_dic[filename] = [pet_name]
            else:
                print("** Warning: Key=", filename, 
                      "already exists in results_dic with value =", 
                      results_dic[filename])

    # Return the results dictionary
    return results_dic