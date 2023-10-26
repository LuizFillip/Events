# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 14:32:23 2023

@author: Luiz
"""

import json 

my_dict = json.load(open('stations.json'))

common_occurrences = set(my_dict['1'])

# # Iterate through the keys and find common elements
for key in my_dict:
    common_occurrences = common_occurrences.intersection(my_dict[key])

# # Convert the result back to a list if needed
# common_occurrences_list = list(common_occurrences)

# Print the common occurrences
# ommon_occurrences_list


# receivers = ['cesb', 'saga', 'ceeu', 
#              'paat', 'rnmo', 'past', 
#              'amco', 'brft', 'pisr']

# common_occurrences


# common_occurrences.intersection(my_dict['2'])

common_occurrences