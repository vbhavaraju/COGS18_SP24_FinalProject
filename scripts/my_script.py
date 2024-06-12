"""Script to run the Chatbot."""

import sys
sys.path.append('../')

# Imports
from my_module.functions import greet_user, vitals_result, plot_bp, color_text
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

###
###

# PYTHON SCRIPT HERE

chat = True
while chat:

    #get the user's name and greet user
    
    user_name = input('Hello! Welcome to HealthBot. Please type your name : ')

    print(greet_user(user_name))
    
    # create another while loop, so that when the user is done with one selection, the selection list is regenerated for them
    
    while True:
        user_value = input("\n" + "1. Blood Pressure" + "\n" + "2. Resting Heartrate" + "\n" + "3. Blood Glucose" + "\n" + "Please indicate the number of the option you would like to select, or type 'Bye' to end the chat : ")
    
        if user_value == '1' or user_value == '2' or user_value == '3':
            
            # get user's age and gender so that they can be input as parameters into relevant functions

            user_age = int(input('Please enter your age in years, a value larger than 18 : '))

            user_gender = input('Please enter your biological sex as either "Male" or "Female" : ')

            if user_value == '1':
                
                # get systolic and diastolic blood pressure, and identify if their values are out of range or within range

                user_sys = int(input('Please enter only your systolic blood pressure in mm Hg : '))

                user_dias = int(input('Please enter only your diastolic blood pressure in mm Hg : '))

                output = vitals_result(age = user_age, gender = user_gender, systolic = user_sys, diastolic = user_dias)
                
                print(color_text(output))
                
                if output == "BLOOD PRESSURE IS HIGH" or output == "BLOOD PRESSURE IS NORMAL":
                    
                    # give user the option to plot their data
                    
                    user_input = input("Would you like to plot your data against expected ranges for your gender and age group? Yes/No : ")
                    if user_input.lower() == "yes":
                        figure = plot_bp(user_age, user_gender, user_sys, user_dias)
                        if type(figure) == str:
                            print(color_text('Sorry, plot could not be generated at this time. Please restart Jupyter Notebook and try again.'))
                        else:
                            figure.show()
                    else:
                        print(color_text('Thank you'))
                else:
                    continue
                
            elif user_value == '2':
                
                # get user's heartrate, and identify if their value is out of range or within range

                user_heartrate = int(input('Please enter your resting heartrate in bpm : '))

                output = vitals_result(age = user_age, gender = user_gender, heartrate = user_heartrate)
                
                print(color_text(output))

            elif user_value == '3':
                
                # get user's blood glucose, and identify if their value is out of range or within range

                user_glucose = int(input('Please enter your fasting glucose in mg/dL : '))

                output = vitals_result(age = user_age, glucose = user_glucose)
                
                print(color_text(output))

        elif user_value.lower() == 'bye':

            # if user chooses to terminate the chat, end the loop

            chat = False
            break
                              
        else:

            # if user's input is not clear, output this

            print(color_text("I'm not sure what you mean. Please input the number of your choice, or input 'Bye' : "))
    
    else:
        print(color_text("I'm not sure what you mean. Please input the number of your choice, or input 'Bye' : "))