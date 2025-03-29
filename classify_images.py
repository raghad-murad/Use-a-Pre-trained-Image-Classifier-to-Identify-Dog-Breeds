#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Abeer Bassam Saleh
# DATE CREATED: 3/11/2024 

import os.path
from classifier import classifier 

def classify_images(images_dir, results_dic, model):
    
    # Iterate over the dictionary items 
    for filename, value in results_dic.items(): 
        # Get the full path of the image using os.path.join to handle paths intelligently
        image_path = os.path.join(images_dir, filename) 
        # Classify the image using the classifier function and the provided model
        classifier_label = classifier(image_path, model).lower().strip() 
        # Get the pet label from the dictionary value 
        pet_label = value[0] 
        # Check if the pet label is in the classifier label (for match) 
        match = 1 if pet_label in classifier_label else 0 
        # Update the results dictionary with classifier label and match value 
        value.extend([classifier_label, match])