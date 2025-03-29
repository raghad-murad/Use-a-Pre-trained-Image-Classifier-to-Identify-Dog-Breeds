#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Abeer Bassam Saleh
# DATE CREATED: 3/11/2024 

import argparse
 
def get_input_args():
    
    # Creates Argument Parser object named parser 
    parser = argparse.ArgumentParser()

    # Argument 1: Image Folder 
    parser.add_argument('--dir', type=str, default='pet_images/', help='path to the folder of pet images')  

    # Argument 2: CNN Model Architecture 
    parser.add_argument('--arch', type=str, default='vgg', help='CNN model architecture to use') 
    
    # Argument 3: Text File with Dog Names 
    parser.add_argument('--dogfile', type=str, default='dognames.txt', help='text file with dog names') 
    
    # Replace None with parser.parse_args() parsed argument collection 
    return parser.parse_args()