# Capstone-2-Lists-Functions-and-String-Handling
Lists, Functions, and String Handling Task 21 HyperionDev Bootcamp


########################## PSEUDOCODE START #################################
# STARTED THIS TASK WITHOUT PSEUDOCODE, MADE A LOT OF PROGRESS BUT GOT STUCK
# IT IS VERY UNCLEAR TO ME HOW TO PROCEED WITH THE TASK BECAUSE IT IS SO LARGE
# BY TRIAL AND ERROR I GOT TO A CERTAIN POINT WHERE I COULD MODIFY THE TASK BUT...
#   ...DID NOT KNOW HOW TO SAVE THE MODIFIED TASK
# A CHAT WITH A CODE REVIEWER HIGHLIGHTED COMPLEXITY IN USING A <for loop> TO INDEX...
#   ...BY BOTH ROW & COLUMN, BUT I WAS UNABLE TO INCORPORATE THAT ALTERATION SUCCESSFULLY...
#   ...CODE JUST DID NOT WORK AFTER THE CHANGE
# THE KEY CHALLENGE IS IN NOT KNOWING HOW TO SUCCESSFULLY MODIFY/MANIPULATE THE LIST

# I HAVE NOW, MADE MOST OF THE BASIC FUNCTIONALITY WORK ON THIS TASK. WHAT REMAINS ARE THE STATS REPORTS
# I HAVE LEARNED HOW TO MODIFY A txt FILE
# I LEARNED THAT IT IS BEST PRACTICE TO MODIFY A FILE & THEN OVERWRITE THE FILE BACK, NOT MODIFY IN THE txt FILE
# THE STATS PART OF THE TASK IS UNCLEAR, ALTHOUGH I HAVE HAD SOME INPUT FROM A MENTOR, I NEED TO REREAD THE MENTOR INPUT
# I BELIEVE THAT MY STATS SHOULD TAKE IN INPUT FROM THE USER AND SAVE THIS TO AN EXTERNAL FILE...
#   ...(txt NOT NECESSARILY BEST CHOICE), CHECK IF THE FORMAT IS SPECIFIED --> .txt IS SPECIFIED
# DO I ATTEMPT TO EDIT THE STATS FILE - IN PLACE (NOT BEST PRACTICE) - OR READ INTO MEMORY, AMEND & WRITE BACK???
# I NEED SOME SORT OF COUNTER TO WRITE TO A FILE, EACH & EVERY TIME A USER LOGS IN, THIS WAS A REQUIREMENT...
#   ...IT STATES, "The total number of tasks that have been generated and tracked using task_manager.py", THIS IS VAGUE...
#   ...DOES IT MEAN THE TOTAL EVER ASSIGNED, OR THE TOTAL CURRENTLY ASSIGNED??? PRESUMABLY THE LATTER OPTION
# THE MATHS TO MANIPULATE THE FIGURES INTO STATS DOES NOT SOUND DIFFICULT, THE MAIN DIFFICULTY APPEARS TO BE I/O OPS
# AN OBVIOUS DIFFICULTY IS IN READING THE DATES, BECAUSE THE tasks.txt PROVIDES DATES IN A FORMAT COMPLETELY DIFFERENT...
#   ...TO THE datetime MODULE
# I HAVE FOUND THAT THE datetime() => strptime().date MODULE CONVERTS A STR TO AN OBJECT #=> https://medium.com/analytics-vidhya/dealing-with-date-time-of-different-formats-in-python-f1f973d8cdb

# THESE ARE THE REQUIREMENTS:-
'''
task_overview.txt should contain:

▪The total number of tasks that have been generated and tracked using the task_manager.py.  [I THINK THIS JUST MEANS, HOW MANY TASKS, BOTH COMPLETED & UNCOMPLETED]

▪The total number of completed tasks. [LOOPING THROUGH THE FILES, WITH A COUNTER TO ADD UP EACH TASK, IF: INDEX[-1] == YES]

▪The total number of uncompleted tasks. [LOOP, COUNT IF INDEX[-1] == NO]

▪The total number of tasks that havent been completed and that are overdue. [REQUIRES datetime() MODULE TO IDENTIFY & CALCULATE THE CURRENT DATE & TO INTERPRET DIFFERENT DATE FORMATS, TO BASE A CALCULATION ON, IF THE TASK IS OVERDUE]

▪The percentage of tasks that are incomplete. [IDENTIFY IF OVERDUE AND WORK-OUT % BASED ON TOTAL NUMBER OF TASKS]

▪The percentage of tasks that are overdue [IDENTIFY IF OVERDUE AND WORK-OUT % BASED ON TOTAL NUMBER OF TASKS]


TASK INSTRUCTIONS :-
user_overview.txt should contain:

The total number of users registered with task_manager.py. [I THINK THIS JUST MEANS HOW MANY USERS]

The total number of tasks that have been generated and tracked using task_manager.py.  [I THINK THIS JUST MEANS, HOW MANY TASKS, BOTH COMPLETED & UNCOMPLETED => this the same as above for -> task_overview.txt, a repitition]

For each user also describe:
▪The total number of tasks assigned to that user. [LOOP THROUGH FILE, A COUNTER COUNTS HOW MANY TASKS FOR EACH USER]

▪The percentage of the total number of tasks that have been assigned to that user [THIS DOES NOT MAKE SENSE, A % OF WHAT? I THINK THIS MEANS THE % OUT OF ALL TASKS IN THE FILE, PRESUMABLY BOTH COMPLETE AND UNCOMPLETE TASKS]

▪The percentage of the tasks assigned to that user that have been completed [CALCULATION BASED ON SEPERATING/IDENTIFYING EACH TASK BY USER AT INDEX[0] AND IDENTIFYING THE Yes/No AT INDEX [-1]]

▪The percentage of the tasks assigned to that user that must still be completed [AS ABOVE BUT THE INVERSE TO COMPLETED TASKS]

▪The percentage of the tasks assigned to that user that have not yet been completed and are overdue [LOOP THROUGH BUT IDENTIFY A SUB-SET OF UNCOMPLETED TASKS. THIS REQUIRES USING A MODULE TO KNOW WHAT THE CURRENT DATE IS, I DO NOT THINK THAT THE CURRENT TIME IS RELEVANT]

Modify the menu option that allows the admin to display statistics so that the reports generated 
are read from task_overview.txt and user_overview.txt and displayed on the screen 
in a user-friendly manner. If these textfiles dont exist (because the user hasnt selected
 to generate them yet), first call the code to generate the text files

'''
# task_overview.txt and user_overview.txt FUNCTIONS() ARE BOTH SIMILAR, I CAN ONLY IDENTIFY THAT THE task_overview.txt FUNCTION() WILL NOT NEED ANY ARGUMENT SENT TO IT, BUT user_overview.txt MIGHT NEED THE USER INFO AS AN ARGUMENT FOR THIS FUNCTION()

# WE ARE REQUIRED TO CREATE 2-SEPARATE FUNCTIONS FOR THE 'MENU'; GENERATE_REPORTS() & REVIEW_STATISTICS(), I DO NOT UNDERSTAND THIS BECAUSE THE INSTRUCTIONS SAY,
'''
When the user chooses to generate reports, two text files, called task_overview.txt and user_overview.txt, should be generated.Both these text files should output data in a user-friendly, easy to read manner
'''
#...THE ABOVE IMPLIES THAT ONLY THE generate_reports() -> FUNCTION OUTPUTS ALL THE DATA. OR, DOES IT MEAN THAT IT DOES THE CALCULATION & THE display_statistics() FUNCTION OUTPUTS THE INFORMATION. BUT THEN WHY HAVE 2-SEPARATE OPTIONS ON THE MENU???

# WHAT I THINK IS MEANT, IS THAT generate_reports() GIVES BARE FIGURES & display_statistics() GIVES PERCENTAGE FIGURES

# NOTA BENE : I COULD NOT GET THE LOGIC TO WORK FOR user_overview.txt, MY APPROACH WAS BAD, I SPENT WEEKS ON THIS WITHOUT SUCCES

# I UNDERSTAND MY FUNCTIONS ARE TOO LONG, BUT I COULD NOT WASTE MORE TIME ON THIS TASK AS I AM WELL BEHIND NOW ON TASKS
########################## PSEUDOCODE END ###################################
