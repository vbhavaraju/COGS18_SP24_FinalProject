"""A collection of functions for doing my project."""

def greet_user(name):
    """ Returns a greeting with the name of user.
    
    Parameters
    -----
    name : str
        the name that will be referenced in the greeting
    
    Returns
    -----
    greeting : str
        introductory sentence with the given name
    """
    
    greeting = "Hello " + str(name) + ". What lab result would you like to test today?"
 
    return greeting


def vitals_result(age, gender = None, heartrate = None, systolic = None, diastolic = None, glucose = None):
    """Determines if user's vitals are out of range or within range given expected ranges for their age and gender.
    
    Parameters:
    age : int
        user's age in years
    gender : str, default None
        user's biological sex
    heartrate : int, default None
        user's heartrate in bpm
    systolic : int, default None
        user's systolic blood pressure in mm Hg
    diastolic : int, default None
        user's diastolic blood pressure in mm Hg
    glucose : int, default None
        user's blood glucose level in mg/dL
        
    Returns:
    output : str
        Tells the user if their value (blood pressure, heartrate, blood glucose) is within or out of the expected range for their age and gender"""

    # gender is an input for bp and heartrate, but not for glucose
    
    if gender is not None:
        
        # put input in lowercase, so that it doesn't matter if user inputs 'male' or 'Male', for example
        
        gender = gender.lower()
    
        if gender not in ['female', 'male']:
                        
            return 'Please enter gender as biological sex: "Male" or "Female"'

        # evaluate blood pressure
        
        if systolic is not None and diastolic is not None:
            
            # nested dictionary that puts gender, then age group, then blood pressure type + values into one larger dictionary.
            # this dictionary will be looped through to identify if the user's values are in or out of range
            # depending on their age and gender
            
            expected_bps = {'female' : {(18, 41) : {'systolic' : [110, 125], 'diastolic' : [60, 71]}, 
                                    (41, 66) : {'systolic' : [116, 133], 'diastolic' : [60, 81]}}, 
                        'male' : {(18, 41) : {'systolic' : [114, 125], 'diastolic' : [65, 75]}, 
                                  (41, 66) : {'systolic' : [116, 144], 'diastolic' : [65, 85]}}}

            if gender == 'female' or gender == 'male':
                
                # get the bp ranges for their specific gender

                bp_ranges = expected_bps[gender]
                
                # If none of the following conditionals are met, this means that their age does not match the ranges
                # initialize the output variable so it can be returned, even if conditionals are not met
                # initialize systolic_range and diastolic_range so that there is no error if conditionals are not met

                output = "Age was not within any range. Please try again, ensuring that age is between 18 and 65."

                systolic_range = None
                diastolic_range = None
                
                # loop through each age range within the specific gender (there are two age ranges)
                # determine if the user's age is within that specific age range
                # identify the healthy bps for the user depending on their age range
                # identify their healthy systolic and diastolic range, so each value can be compared individually

                for age_range in bp_ranges:
                    if age in range(age_range[0], age_range[1]):
                        healthy_bps = bp_ranges[age_range]
                        systolic_range = healthy_bps['systolic']
                        diastolic_range = healthy_bps['diastolic']
                        break
                
                # if the systolic and diastolic range variables are created above, compare ranges to user's values
                
                if systolic_range is not None and diastolic_range is not None:

                    if systolic <= systolic_range[1]:
                         abnormal_sys = False
                    else:
                         abnormal_sys = True

                    if diastolic <= diastolic_range[1]:
                         abnormal_dias = False
                    else:
                         abnormal_dias = True

                    if abnormal_sys or abnormal_dias:
                        output = "BLOOD PRESSURE IS HIGH"
                    else:
                        output = "BLOOD PRESSURE IS NORMAL"

        # evaluate heartrate
        
        if heartrate is not None:
            
            # nested dictionary that puts gender, age group (tuple), and normal heartrate (list) ranges into one dictionary

            expected_hr = {'male' : {(18, 36) : [49, 81], (36, 56) : [50, 83], (56, 65) : [51, 82], (65, 120) : [50, 80]},
                           'female' : {(18, 25) : [54, 85], (25, 36) : [54, 83], (36, 46) : [54, 85], (46, 100) : [54, 84]}}

            if gender == 'female' or gender == 'male':
                
                # identify the specific ranges for the user's inputted gender

                heartrate_ranges = expected_hr[gender]   
                
                # like in bp evaluation, initialize output so that it returns without error
                # even if no conditionals are met
                # initialize exp_hr to prevent error if following conditionals are not met 

                output = "Age was not within any range. Please try again, ensuring that age is between 18 and 120."
                
                exp_hr = None
                
                # loop through each age range in given gender's dictionary to find the user's age range
                # determine the expected heartrate for their age range

                for age_range in heartrate_ranges:
                    if age in range(age_range[0], age_range[1]):
                        exp_hr = heartrate_ranges[age_range]
                        break
                    else:
                        output = "Age was not within any range. Please try again, ensuring that age is between 18 and 120."
                        
                # if exp_hr has been defined above, compare user's heartrate to their expected range

                if exp_hr is not None:       
                    if heartrate in range(exp_hr[0], exp_hr[1]):
                        output = "Heartrate within normal range"
                    elif heartrate < exp_hr[0]:
                        output = "Heartrate is low"
                    else:
                        output = "Heartrate is high"
                        
    else:
        # gender is not required for glucose evaluation, so gender parameter will be None
        
        # evaluate glucose
        
        if glucose is not None:
            
            # expected ranges for glucose in a dictionary, {age : glucose range}
            # initialize normal_gluc in case following conditionals are not met
            # initialize output variable so that it does not error out if conditionals are not met

            normal_gluc = None
            expected_gluc = {(18, 121) : [40, 101]}
            output = "Age was not within any range. Please try again, ensuring that age is between 18 and 120."
            
            # loop through dictionary to ensure user's age is within range

            for item in expected_gluc:
                if age in range(item[0], item[1]):
                    normal_gluc = expected_gluc[item]
                    break
                else:
                    output = "Age was not within any range. Please try again, ensuring that age is between 18 and 120."
                    
                #if normal_gluc has been defined above, compare user's value to expected range

            if normal_gluc is not None:
                if glucose in range(normal_gluc[0], normal_gluc[1]):
                    output = "Blood sugar is within range"
                elif glucose > normal_gluc[1]:
                    output = "Blood sugar is high"
                else:
                    output = "Blood sugar is low"

            # if their age is not within the range in dictionary
            
            else:
                output = "Age was not within any range. Please try again, ensuring that age is between 18 and 120."

        
    return output
        

def color_text(input_text):
    """Changes the color and format of text depending on what it says.
    
    Parameters
    -----
    text : str
        the input text
    
    Returns
    -----
    output : str
        the input text bolded and in a different color (red, blue, or green)
    
    """

    red_text = ["Blood sugar is high", "Blood sugar is low", "Heartrate is low", "Heartrate is high", "BLOOD PRESSURE IS HIGH"]
    green_text = ["Blood sugar is within range",  "Heartrate within normal range", "BLOOD PRESSURE IS NORMAL"]
    
    # first code makes test bold
    # second code makes text a color (red, blue, or green)
    # third code resets color, so that text printed out after the function is called returns to black
    
    if input_text in red_text:
        output = "\x1b[1m \033[31m " + input_text + " \x1b[0m"
    elif input_text in green_text: 
        output = "\x1b[1m \033[32m " + input_text + " \x1b[0m"
    else:
        output = "\x1b[1m \033[34m " + input_text + " \x1b[0m"
    
    return output

def plot_bp(age, gender, systolic, diastolic):
    
    """Plots the expected ranges of blood pressure (systolic and diastolic) in a violin plot, with markings for the user's specific values.
    
    Parameters
    ---
    age : int
        user's age in years
    gender : str
        user's gender
    systolic : int
        user's systolic blood pressure in mm Hg
    diastolic : int
        user's diastolic blood pressure in mm Hg
        
    Returns
    ---
    plt : matplotlib plot
        Violin plot of expected ranges, with X markings to indicate user's blood pressure values.
    """
        
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt 
            
    # identify means for each systolic and diastolic blood pressure range, given gender and age-group
    # young = range 18-40 (inclusive)
    # old = range 41-65 (inclusive)
    
    fem_young_sys_mean = np.mean([110, 125])
    fem_old_sys_mean = np.mean([116, 133])
    
    fem_young_dias_mean = np.mean([70.5, 74.5])
    fem_old_dias_mean = np.mean([73, 79])
    
    male_young_sys_mean = np.mean([114.5, 120.5])
    male_old_sys_mean = np.mean([115.5, 143.5])
    
    male_young_dias_mean = np.mean([70.5, 74.5])
    male_old_dias_mean = np.mean([73.5, 78.5])
    
    # create dictionaries for each age range and gender
    # the dataset is randomly generated using the mean and std from above to create the violin plot
    # loc = mean, scale = standard deviation, size = number of values generated

    female_young_data = {
        'Age': '18-41',
        'Systolic BP': np.random.normal(loc=fem_young_sys_mean, scale=10, size=100),
        'Diastolic BP': np.random.normal(loc=fem_young_dias_mean, scale=10, size=100)
    }
    male_young_data = {
        'Age': '18-41',
        'Systolic BP': np.random.normal(loc=male_young_sys_mean, scale=10, size=100),
        'Diastolic BP': np.random.normal(loc=male_young_dias_mean, scale=10, size=100)}
    
    female_old_data = {
        'Age': '41-66',
        'Systolic BP': np.random.normal(loc=fem_old_sys_mean, scale=10, size=100),
        'Diastolic BP': np.random.normal(loc=fem_old_dias_mean, scale=10, size=100) #loc = mean, scale = stdev
    }
    
    male_old_data = {
        'Age': '41-66',
        'Systolic BP': np.random.normal(loc=male_old_sys_mean, scale=10, size=100),
        'Diastolic BP': np.random.normal(loc=male_old_dias_mean, scale=10, size=100)}
    
    # determine which dictionary the plot should follow based on the user's age and gender

    if gender == 'Female' and age in range(18, 41):
        data = female_young_data
    elif gender == 'Female' and age in range(41, 66):
        data = female_old_data
    elif gender == 'Male' and age in range(18, 41):
        data = male_young_data
    elif gender == 'Male' and age in range(41, 66):
        data = male_old_data
    else:
        return "Please enter gender as 'Male' or 'Female' and age between 18 and 65."

    # create pandas dataset
    df = pd.DataFrame(data)

    # the user's systolic and diastolic bp will be plotted as a scatter plot on top of the violin plot
    # to give the user an idea of where their values stand in relation to the expected ranges for their age/gender
    # initialize variable for user's systolic and diastolic bp
    
    bp_systolic = systolic
    bp_diastolic = diastolic

    # determine figure's size (I chose square)   
    plt.figure(figsize=[6, 6])
    
    # create one plot for the Systolic BP, set the x-axis, y-axis, dataframe, and color.
    # set axis labels and values
    ax1 = sns.violinplot(x='Age', y='Systolic BP', data=df, color = 'skyblue')
    plt.ylim(0, 200)
    plt.ylabel('Systolic BP', color = 'skyblue', fontsize = 'x-large')
    
    # create a second plot for Diastolic BP, set x-axis, y-axis, dataframe, and color.
    # set axis labels and values
    ax_2 = ax1.twinx()
    sns.violinplot(ax = ax_2, x='Age', y='Diastolic BP', data=df, color = 'orange')
    plt.ylim(0, 200)
    plt.ylabel('Diastolic BP', color = 'orange', fontsize = 'x-large')
    
    # create a scatter plot for the user's values
    # [0,0] = it should be on the same coordinates as the systolic/diastolic plots (so that it overlaps with them)
    # plot both bp_systolic and bp_diastolic values with an X, size 200 and color black
    plt.scatter([0,0], [bp_systolic, bp_diastolic], marker='x', s = 200, color = 'black')

    # add axis labels and title to the graph
    plt.xlabel('Age Group')
    ax1.set_title('Distribution of Systolic and Diastolic BP by age group. X indicates your datapoints.')
    
    plt.show()
    
    return plt