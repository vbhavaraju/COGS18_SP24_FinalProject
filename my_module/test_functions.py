"""Test for my functions.

"""

from my_module.functions import vitals_result, greet_user, plot_bp, color_text
##
##

def test_vitals_result():

    #test blood pressure outputs
    assert callable(vitals_result)
    assert type(vitals_result(age=20, gender='Female', systolic=100, diastolic=80)) == str
    assert vitals_result(age=20, gender='Female', systolic=100, diastolic=80) == "BLOOD PRESSURE IS HIGH"
    assert vitals_result(age=20, gender='Male', systolic=130, diastolic=70) == "BLOOD PRESSURE IS HIGH"
    assert vitals_result(age=41, gender='Male', systolic=150, diastolic=70) == "BLOOD PRESSURE IS HIGH"
    assert vitals_result(age=50, gender='Female', systolic=120, diastolic=85) == "BLOOD PRESSURE IS HIGH"
    assert vitals_result(age=20, gender='female', systolic=115, diastolic=70) == "BLOOD PRESSURE IS NORMAL"
    assert vitals_result(age=15, gender='Female', systolic=100, diastolic=70) == "Age was not within any range. Please try again, ensuring that age is between 18 and 65."
    assert vitals_result(age=90, gender='Male', systolic=100, diastolic=70) == "Age was not within any range. Please try again, ensuring that age is between 18 and 65."
    assert vitals_result(age=20, gender='emale', systolic=100, diastolic=70) == 'Please enter gender as biological sex: "Male" or "Female"'
    
    #test heartrate outputs
    assert type(vitals_result(age=20, gender='Female', heartrate=60)) == str
    assert vitals_result(age=20, gender='Female', heartrate=60) == "Heartrate within normal range"
    assert vitals_result(age=36, gender='Male', heartrate=85) == "Heartrate is high"
    assert vitals_result(age=10, gender='female', heartrate=78) == "Age was not within any range. Please try again, ensuring that age is between 18 and 120."
    assert vitals_result(age=30, gender='blah', heartrate=80) == 'Please enter gender as biological sex: "Male" or "Female"'
    assert vitals_result(age=60, gender='Male', heartrate=40) == "Heartrate is low"
    
    #test glucose outputs
    assert type(vitals_result(age=40, glucose=80)) == str
    assert vitals_result(age=40, glucose=80) == "Blood sugar is within range"
    assert vitals_result(age=80, glucose=120) == "Blood sugar is high"
    assert vitals_result(age=40, glucose=10) == "Blood sugar is low"
    assert vitals_result(age=15, glucose=100) == "Age was not within any range. Please try again, ensuring that age is between 18 and 120."

def test_greeting():
    
    assert callable(greet_user)
    assert type(greet_user('ralkdjflsdk')) == str
    assert type(greet_user(1239184)) == str
    assert greet_user('Vaidehi') == "Hello Vaidehi. What lab result would you like to test today?"    
    assert greet_user('sdfkjs') == "Hello sdfkjs. What lab result would you like to test today?"
                 
def test_plot_bp():
        
    assert plot_bp(20, 'Female', 120, 80) is not None
    assert plot_bp(20, 'Male', 140, 70) is not None
    assert plot_bp(45, 'Female', 140, 70) is not None
    assert plot_bp(45, 'Male', 120, 80) is not None
    assert plot_bp(-6, 'Male', 120, 80) == "Please enter gender as 'Male' or 'Female' and age between 18 and 65."
    assert plot_bp(80, 'Male', 120, 80) == "Please enter gender as 'Male' or 'Female' and age between 18 and 65."
    
    assert callable(plot_bp)

def test_color_text():
    
    assert callable(color_text)
    assert type(color_text('input text')) == str
    assert color_text('input text') == "\x1b[1m \033[34m input text \x1b[0m"
    assert color_text('Blood sugar is within range') == "\x1b[1m \033[32m Blood sugar is within range \x1b[0m"
    assert color_text("Heartrate is low") == "\x1b[1m \033[31m Heartrate is low \x1b[0m"