# COGS18_SP24_FinalProject_UCSD
### Vaidehi Bhavaraju, 06/11/2024
Hello, welcome to my project! I wanted to create a project that could be useful for at-home monitoring of vitals. This project contains a Chatbot known as Healthbot, which will allow a user to test their blood pressure, heartrate, and blood glucose against expected ranges given the user's age and gender. Additionally, the user can plot their blood pressure to visualize where their numbers lie against average expected values. Run the second cell below with the code 'from scripts import my_script' to launch the chatbot and try it out!

Notes:

Blood pressure data sourced from: https://www.medicinenet.com/blood_pressure_chart_reading_by_age/article.htm and https://www.baptisthealth.com/blog/heart-care/healthy-blood-pressure-by-age-and-gender-chart

Heartrate data sourced from: https://www.verywellfit.com/resting-heart-rate-3432632

Glucose data sourced from: https://www.forbes.com/health/wellness/normal-blood-sugar-levels/

ChatGPT was used for understanding how to create a general seaborn/matplotlib violin plot. ChatGPT's code for a general plot with a random database was edited and restructured to make it applicable to my data, to add user values to the plot, and to combine 2 plots together (to see both systolic and diastolic bp on the plot).

The information about vitals should be not be used as health advice, as there are multiple factors other than sex and age which relate to healthy vitals, and the expected ranges may not be completely accurate.

### This project has the following files:
ProjectNotebook - where the chatbot can be run
my_module - contains files test_functions.py and functions.py
scripts - contains my_script.py, which writes the code to run the chatbot

### KNOWN ISSUES:
Occasionally, Jupyter Notebooks fails to plot on some browsers. This can be fixed by restarting the browser and the kernel.
