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

from datetime import datetime

import os.path

# STARTS HERE ->
# THE PROGRAM STARTS WITH user_sec_details() ON THE BOTTOM-LINE, IT CALLS THIS FUNCTION BELOW. THEN, FUNCTIONS START TO PROGRESS IN A LINEAR WAY.
temp = list()
'''opens up the user.txt file, cleans and converts the username & password pair into a dictionary'''
def user_sec_details() :
    with open ("user.txt", "r") as file :
        for lines in file :
            temp = lines.strip()          #<= intended to clean input, did not work
            temp = lines.replace(',', '')   #<= this did remove 'whitespace' from input
            all_details = temp.split()              #<= puts strings into list[]
        file.seek(0)
    usernames_and_passwords = {all_details [i]: all_details [i + 1] for i in range(0, len(all_details ), 2)}     #<== converts list[] into dictionary{}    # https://www.geeksforgeeks.org/python-convert-a-list-to-dictionary/
    login(usernames_and_passwords)
#--------FUNCTION END--------------------------------FUNCTION END------------------------------------FUNCTION END---------------


def login(x) :
    '''checks username and password against database'''
    logged_in = False
    while not logged_in :
        user_name = input("Please enter your username : ")
        pass_word = input("Please enter your password : ")
        if user_name not in x.keys() :
            print("Incorrect username, please try again")
            continue
        elif pass_word not in x.values() :
            print("incorrect password, please try again")
            continue
        else :
            print(f"Welcome {user_name} , please make a selection below ")
            logged_in = True
        while logged_in :
            now = datetime.now()
            with open("task_manager_log.txt", "a+") as fhand :
                print(f'''{user_name} : {now}''', file=fhand)
            return menu_options(x, user_name)
#--------FUNCTION END--------------------------------FUNCTION END------------------------------------FUNCTION END---------------


def menu_options(x, user_name) :
    '''the main menu, for the user to navigate through, the user should be brought back here after each step is completed'''
    print('''
    r  -->   register new user
    a  -->   add new task
    va -->   view all tasks
    vm -->   view my tasks
    gr -->   generate reports
    ds -->   display statistics
    e  -->   exit program
    ''')
    user_choice = input(" : ").lower()
    if user_choice == "r" :
        return reg_user(x, user_name)
    elif user_choice == "a" :
        return add_task(x, user_name)
    elif user_choice == 'va' :
        return view_all(x, user_name)     #<= CAN I MAKE THIS AN OPTIONAL ARGUMENT, BECAUSE IT IS NOT NEEDED, EXCEPT TO CALL-BACK TO MENU
    elif user_choice == 'vm' :
        return view_mine(x, user_name)
    elif user_choice == 'gr' :
        return gen_report(x, user_name)         #<= WORK IN PROGRESS
    elif user_choice == 'ds' :
        return disp_stats(x, user_name)         #<= WORK IN PROGRESS
    elif user_choice == "e" :
        quit()
#--------FUNCTION END--------------------------------FUNCTION END------------------------------------FUNCTION END---------------


def reg_user(x, user_name) :
    '''register a new user and write user details to the database'''
    new_user_name = input("Please enter the new username : ")
    new_pass_word = input("Please enter the new password : ")       #<= make sense? I know the password for another user. make admin only function? 
    if new_user_name in x.keys() or new_pass_word in x.values() :
        print("Username or Password in use, please try again")     #<== figure out how to make this loop with an incorrect username
        reg_user(x)                                                #<= creates a loop back to the start, if wrong info input
    else :
        with open("user.txt", "a") as file :
            file.write(f" {new_user_name}, {new_pass_word},")     #<= PROGRAM ONLY WORKS, IF ALL user.txt INFO IS ON 1-LINE. THEREFORE, NO 'NEWLINE' TAB USED HERE
            print("\nUser details added")
            file.seek(0)
    return menu_options(x, user_name)   #<= THIS NEEDs TO GO BACK TO LOGIN() PAGE, SINCE A USER IS ADDED: NOT, SWITCHING USERS.
#--------FUNCTION END--------------------------------FUNCTION END------------------------------------FUNCTION END---------------


def add_task(x, y) :
    '''adds task/s for a user'''
    assigned_user = input("Enter the assigned user : ")
    task_header = input("Enter the task heading : ")
    task_desc = input("Enter task description : ")
    start_date = input("Enter the date of assignment as; Day Month Year : ")
    due_date = input("Enter the due date as; Day Month Year : ")
    completed = "No"
    if assigned_user not in x.keys() :
        print("This user does not exist")
    else :
        with open("tasks.txt", "a") as file :
            file.seek(0)
            file.write(f"\n{assigned_user}, {task_header}, {task_desc}, {start_date}, {due_date}, {completed}") #<= NEWLINE CHAR, TURNED OUT THAT THIS NEEDS TO BE ADDED AT FRONT OF SENTENCE, ?_COS_? THE LAST TASK IN tasks.txt, AS PROVIDED DOES NOT HAVE A NEWLINE CHAR AT THE END
    return menu_options(x, y)
#--------FUNCTION END--------------------------------FUNCTION END------------------------------------FUNCTION END---------------


def view_all(x, y) :
    '''this function displays tasks to the user'''
    with open("tasks.txt", "r") as fhand :
        show_list = fhand.read().splitlines()
        task_list = [i.split(',') for i in show_list]     #<== https://bobbyhadz.com/blog/python-split-elements-in-list#:~:text=To%20split%20the%20elements%20of%20a%20list%20in,part%20of%20each%20string%20you%20want%20to%20keep.
        for i in task_list :
            print(f"\n")
            print("#"*99)
            print("\t\t # This is an assigned task # ")
            print("-"*99)
            print(f"| ASSIGNED TO :        {(i[0])}")
            print(f"| TASK :              {(i[1])}")
            print(f"| TASK DESCRIPTION :  {(i[2])}")
            print(f"| DATE ASSIGNED :     {(i[3])}")
            print(f"| DUE DATE :          {(i[4])}")
            print(f"| TASK COMPLETE ? :   {(i[5])}")
            print("-"*99)
            print("#"*99)
            fhand.seek(0)

        # THIS BLOCK SHOULD TAKE THE USER BACK TO THE MENU
        while True :
            choose_the_menu_back = int(input("To go back to the menu, type in '-1' : "))
            if choose_the_menu_back == (-1) :
                return menu_options(x, y)
            else :
                continue
#--------FUNCTION END--------------------------------FUNCTION END------------------------------------FUNCTION END---------------


def view_mine(x, y) :
    '''this is a function which allows a user to view & edit (under certain conditions & limitations their "assigned" tasks. But all these different operations make this code block long. I have not wasted more time trying to break down this function. A function should do only one thing but this function modifies and outputs data. The instructions specified a different order to present the data back to the user. But, I have presented the data in the same index[] order provided in the list because it was too difficult to change the order just for viewing by the user & for little benefit'''
    user_name = y
    with open("tasks.txt", "r+") as fhand :
        show_list = fhand.read().splitlines()
        task_list = [i.split(',') for i in show_list]     #<== https://bobbyhadz.com/blog/python-split-elements-in-list#:~:text=To%20split%20the%20elements%20of%20a%20list%20in,part%20of%20each%20string%20you%20want%20to%20keep.
        fhand.seek(0)
        counter = 0
        task_list_to_edit = list()
        task_list_to_not_edit = list()
        for i in task_list :
            if i[0] == user_name :
                task_list_to_edit.append(i)     #<== INSTRUCTIONS STATE, "... the user selects‘vm’ to view all the tasks assigned to them" SO THIS LINE SEPERATES THE TASKS BETWEEN ONES THE USER CAN EDIT, & ONES USER CANNOT EDIT
                counter += 1                    #<== THIS 'COUNTER' IDENTIFIES TASKS TO EDIT, LATER ON

                # THIS LONG CODE BLOCK, PRINTS OUTPUT TO THE USER. TRIED MULTI-LINES BUT PROBS. KEPT THIS COS IT WORKED
                print(f"\n")
                print("#"*99)
                print("\t\t\tTHIS IS TASK # ",counter)
                print("-"*99)
                print(f"| ASSIGNED TO :        {(i[0])}")   #<== AN EXTRA 'SPACE' IN THIS LINE, COS THE 1st ITEM IN tasks.txt HAS NO SPACE. POSSIBLE TO USE strip() ON OTHER LINES? DIFFICULTY MAKING strip() WORK IN THIS TASK
                print(f"| TASK :              {(i[1])}")
                print(f"| TASK DESCRIPTION :  {(i[2])}")
                print(f"| DATE ASSIGNED :     {(i[3])}")
                print(f"| DUE DATE :          {(i[4])}")
                print(f"| TASK COMPLETE ? :   {(i[5])}")
                print("-"*99)
                print("#"*99)
                #print("this is the edit task list : ",task_list_to_edit)
            elif i[0] != user_name :
                task_list_to_not_edit.append(i)     #<== INSTRUCTIONS STATE, "... the user selects‘vm’ to view all the tasks assigned to them" SO THIS LINE SEPERATES THE TASKS BETWEEN ONES THE USER CAN EDIT, & ONES USER CANNOT EDIT

        # AFTER SEEING THE PRINT-OUT, THIS CODE BLOCK GIVES THE USER AN OPTION TO EDIT HIS/HER TASKS
        print("""--------------------To edit a task, type the task number , 
                                ~~~ you can only edit an uncompleted task ~~~
                                   (or type '-1' to return to the main menu)""")
        task_choice = int(input('''________________________________________________________Please enter a number : '''))
        if task_choice == (-1) :
            menu_options(x, y)
        elif task_choice != (-1) :
            if (task_list_to_edit[((task_choice)-1)][-1]) == str('No') or str('no') or str('NO') :
                new_completed_id = input("Is this task complete, type YES or NO : ").lower()       #<== this line is to meet a task requirement
                while True :
                    indx = int((task_choice)-1)         #<== translates the 'task number' to a list() 'index number'
                    if new_completed_id == 'no' :       #<== the input() for this variable was set to lower(), just above

                    #THIS CODE BLOCK TAKES INPUT & UPDATES TASK LIST USING SLICING
                        new_assigned_user = input(" Enter the assigned user : ")
                        if new_assigned_user not in x.keys() :
                            print("The user is not recognised")
                            continue
                        task_list_to_edit[indx][0] = new_assigned_user           #<== list() slice, update value
                        new_due_date = input(' ' + "Enter the due date as; Day Month Year : ")
                        task_list_to_edit[indx][4] = new_due_date                #<== list() slice, update value
                        new_completed = input(' ' + "Has the task been completed, YES or NO : ").capitalize()
                        task_list_to_edit[indx][-1] = new_completed               #<== list() slice, update value
                    else :
                        print('This task is complete, good job. You will get a Christmas bonus and not the "sack"')
                    updated_task_list_to_write2file = task_list_to_edit + task_list_to_not_edit
                    #print("this is update task list to write to file",updated_task_list_to_write2file)
                    updated_task_list_to_write2file_lines = [','.join(line) for line in updated_task_list_to_write2file] #<== https://stackoverflow.com/questions/69762892/how-to-write-2d-list-to-a-txt-file
                    #print("this is update task list to write to file", updated_task_list_to_write2file_lines)
                    updated_task_list_to_write2file_text = '\n'.join(updated_task_list_to_write2file_lines)
                    #print("updated_task_list_to_write2file_text", updated_task_list_to_write2file_text)
                    break

    with open('tasks.txt', 'w') as fhand:
        fhand.write(updated_task_list_to_write2file_text + '\n')
        fhand.seek(0)

    while True :
        choose_the_menu_back = int(input("To go back to the menu, type in '-1' : "))
        if choose_the_menu_back != (-1) :
            continue
        else :
            return menu_options(x, y)
#--------FUNCTION END--------------------------------FUNCTION END------------------------------------FUNCTION END---------------

def disp_stats(x, y) :
    '''Confusing, task instructions say, "If these text files dont exist (because the user hasnt selected
    to generate them yet), first call the code to generate the text files",... thus checking if task_overview.txt exists, otherwise going to the next function to create them. But, logically the file should NOT exist already, else the file is likely out of date and not relevant as a report for managing tasks?'''
    filename_task = ("task_overview.txt")
    filename_user = ("user_overview.txt")
    if not os.path.isfile(filename_task) or not os.path.isfile(filename_user) :
        return gen_report(x, y)
    else :
        with open("task_overview.txt") as fhand :
            tasks_to_display = fhand.read()
            print(tasks_to_display)

        with open("user_overview.txt") as fhand :
            users_to_display = fhand.read()
            print(users_to_display)

    # THIS BLOCK SHOULD TAKE THE USER BACK TO THE MENU
    while True :
        choose_the_menu_back = int(input("To go back to the menu, type in '-1' : "))
        if choose_the_menu_back == (-1) :
            return menu_options(x, y)
        else :
            continue
#--------FUNCTION END--------------------------------FUNCTION END------------------------------------FUNCTION END---------------


# NOTA BENE : THE LOGIC DOES NOT WORK AT ALL FOR THE user_overview.txt PART, I DO NOT KNOW HOW TO FIX IT AT THIS TIME
def gen_report(x, y) :
    ''' x=usernames_and_passwords=dict() & y=user_name=user-logged-in
    this function generates 2 reports (task_overview + user_overview) and then sends them back to the display statistics function'''
    # TAKES TASKS FILE & MANIPULATES IT TO GET RELEVANT INFO INTO A NEW LIST FOR task_overview.txt
    with open("tasks.txt", "r") as fhand :
        show_list = fhand.read().replace(' ', '').splitlines()  #<== strip() DID NOT WORK. WHY NOT?...replace() <-- strip()
        task_list = [i.split(',') for i in show_list]
        report_list = list()
        for i in task_list :
            report_list.append(i[0])
            report_list.append(i[3])
            report_list.append(i[4])
            report_list.append(i[5])
        
        # THIS CODE BLOCK TAKES THE ABOVE LIST, SPLITS IT INTO A 2-d LIST() OF INDIVIDUAL TASKS: n = DIVISION POINT
        n = 4
        report_2d_list = [report_list[i:i+n] for i in range(0, len(report_list), n)]
        format_date = ("%d%b%Y")

        # THIS BLOCK STARTS A PROCESS OF SORTING TASKS AND WRITING A REPORT TO task_overview.txt
        # MISC. COUNTERS ARE SET TO ZERO BEFORE COLLATING INFO FOR REPORT 
        counter = 0
        counter_not_done = 0
        counter_done = 0
        counter_overdue = 0

        # THIS WRITES THE BELOW TASKS TO : task_overview.txt
        with open("task_overview.txt", "w") as fhand :
            for i in report_2d_list :
                counter += 1
                print(f"""
                --------------------------------------------------------------
                Task # : ---------------- {counter} 
                Task assigned to : ------ {i[0]}
                Task assignment date : -- {datetime.strptime(i[1], format_date).date()}
                Task due date : --------- {datetime.strptime(i[2], format_date).date()}
                Task completion : ------- {i[3]}
                --------------------------------------------------------------""", file=fhand)
                if datetime.today() > datetime.strptime(i[2], format_date) :
                    counter_overdue += 1
                if i[3] == ('No') :
                    counter_not_done += 1
                else :
                    counter_done += 1

        # THIS WRITES THE COLLATED 'OVERALL'-TASK REPORT TO task_overview.txt               
        with open("task_overview.txt", "a+") as fhand :
            if counter_done != 0 and counter_not_done != 0 :    #<== HERE, I WANT TO AVOID ATTEMPTING TO DIVIDE BY ZERO
                tasks_not_done_percent = (counter_not_done / counter) * 100
            else :
                tasks_not_done_percent = 100
            if counter_overdue != 0 :
                tasks_overdue_percent = ( counter_overdue / counter) * 100
            todays_date = datetime.today()
            print(f"""
            -------------------      TASK REPORT      -----------------------
            Report time : ====================== {todays_date}
            Total number of tasks : ============ {counter}
            Number of tasks complete : ========= {counter_done}
            Number of tasks NOT complete : ===== {counter_not_done}
            Number of tasks overdue now : ====== {counter_overdue}
            Percentage of tasks not complete : = {tasks_not_done_percent}%
            Percentage of tasks now overdue : == {round(tasks_overdue_percent)}%
            -----------------------------------------------------------------""", file=fhand)
        print("task_overview.txt written")

    # THIS CODE BLOCK STARTS THE PROCESS OF TRYING TO PUT USER INFO INTO A DICT() FOR user_overview.txt
    user_dictstore = dict()
    new_2d_list = report_2d_list[:]
    count_num_of_users = 0
    secret = x      #<== user & password info
    for user in secret.keys() :
        count_num_of_users += 1
    for i in new_2d_list :
        for user in secret.keys() :
            total_this_user_tasks = (sum(i[0]==user for i in new_2d_list))  #<== https://www.stackvidhya.com/count-number-of-elements-in-list/#:~:text=Count%20Number%20of%20Elements%20In%20List%20Matching%20Criteria,sum%20the%20results%20where%20the%20condition%20is%20True.
            # user_dictstore[f'Total number of {user}\'s tasks are'] = total_this_user_tasks

            #  THIS  SECTION IS A PROB. WHEREVER I TRIED PLACING THESE COUNTERS, THE TALLY WAS STILL WRONG. COUNTERS GET RESET TO ZERO. I CANNOT GET THE COUNTERS TO FOCUS ON EACH USER CORRECTLY
            count_user_tasks_no = 0
            count_user_tasks_yes = 0
            cnt_usr_tsks_no_and_overdue = 0

            # THIS SECTION TRIES TO SORT INFO, BUT THE OUTPUT IS INCORRECT. MY LOGIC IS BAD. I DO NOT KNOW YET HOW TO FIX
            if i[0] != user :
                continue
            elif datetime.today() > datetime.strptime(i[2], format_date) and i[3] == ("No") :
                cnt_usr_tsks_no_and_overdue += 1
            elif i[3] == ("No") :
                count_user_tasks_no += 1
            elif i[3] == ("Yes") :
                count_user_tasks_yes += 1
            user_dictstore[f'Total number of users are'] = count_num_of_users
            user_dictstore[f'Total number of tasks generated & tracked are'] = counter
            user_dictstore[f'Total number of {user}\'s tasks are'] = total_this_user_tasks
            user_dictstore[f'Total number of {user}\'s tasks completed are'] = count_user_tasks_yes
            user_dictstore[f'Percentage of total tasks given to {user} is'] = ((total_this_user_tasks / counter) * 100)
            user_dictstore[f'Percentage of {user}\'s tasks completed are'] = (count_user_tasks_yes / total_this_user_tasks * 100)
            user_dictstore[f'Percentage of {user}\'s tasks not completed are'] = (count_user_tasks_no / total_this_user_tasks * 100)
            user_dictstore[f'Percentage of {user}\'s tasks not completed and overdue are'] = (cnt_usr_tsks_no_and_overdue/ total_this_user_tasks * 100)
    
    # THIS CODE BLOCK TAKES INFO FROM MY LOGIN FILE task_manager_log TO ADD TO INFOR FOR user_overview. THIS SEEMS TO WORK
    count_log_in = 0
    with open("task_manager_log.txt") as fhand :
        log_list = fhand.read().splitlines()
        for key in secret.keys() :
            for i in log_list :
                if key in i :
                    count_log_in += 1
                    user_dictstore[f'The number of times {key} logged in is'] = (count_log_in)
    
    # THIS CODE WRITES user_overview.txt TO FILE USING print()
    with open("user_overview.txt", "w") as fhand :
        for k, v in user_dictstore.items() :
            print(f"{k} : {v}", file=fhand)
        print("user_overview.txt written")
    return disp_stats(x, y)
#--------FUNCTION END--------------------------------FUNCTION END------------------------------------FUNCTION END---------------

# **** ALL STARTS HERE **** :->
user_sec_details()
'''this starts off the program by calling for the user login information'''
#--------FUNCTION END--------------------------------FUNCTION END------------------------------------FUNCTION END---------------

# MENTOR NOTES BELOW : #################################################################################################
""" 1. GENERATE REPORTS
1.A. For tasks
  show how many tasks are complete or not complete
  show it by % if peter has 2 tasks and one is done then 50% complete
  2. A. For users
  Then show for example that Peter has logged in one time."""

""" EXAMPLES OF HOW TO READ AND PRINT FORM TEXT FILES; PYTHON
3. Very simple example of how to read files for 'va' tasks menu option;
 3.a.   This function displays all the tasks created in the tasks.txt folder when user chooses,
		'va' from the menu
    with open("tasks.txt", "r") as ftasks:
        for contents in ftasks:
            print(contents, "\n")
    return contents

4.a. Links for working with txt files in Python:
https://pythonexamples.org/python-count-number-of-words-in-text-file/
https://www.programiz.com/python-programming/file-operation#:~:text=Python%20has%20a%20built%2Din,or%20modify%20the%20file%20accordingly.&text=We%20can%20specify%20the%20mode,append%20a%20to%20the%20file.
https://www.pythonpool.com/python-read-file-line-by-line/
https://www.freecodecamp.org/news/python-write-to-file-open-read-append-and-other-file-handling-functions-explained/
https://www.geeksforgeeks.org/python-how-to-search-for-a-string-in-text-files/#:~:text=Method%201%3A%20Finding%20the%20index,if%20found%20it%20returns%200.
CODE EXAMPLES:
A. Reading your file and stripping the 'newline character - \n' 
with open(fname) as f:
    content = f.read().splitlines()

### Use this to help with generating your reports how to mark taks done ect ###
https://stackoverflow.com/questions/60971143/changing-the-correct-object-in-the-text-file


You must decide if the tasks.txt file will be a list or a dictionary and then choose an operation to read/write to the file
Here is a link to write to file as a list
https://pynative.com/python-write-list-to-file/

### CODE EXAMPLE ###
def view_mine():
    This function shows all the tasks for the specific user that is logged in. From the tasks.txt folder
		when 'vm' is chosen from menu
    with open("tasks.txt", "rt") as ftasks:
        lines = ftasks.readlines()
        word = input("Enter name ")  # enter the name of the person's task you are looking for
    for line in lines:
        if line.find(word) == 1:  # if that persons name is in tasks the person's tasks will print
            print(line)
        return line
    choice = "Do you want to edit tasks: yes/no  "
    if choice.lower() == 'yes':  # if user wants to edit a task then he must add name of person's task to edit
        lines = ftasks.read()
        ftasks.seek(0)
        choice = input('Enter user_name of task:  ')
        for line in ftasks:
            if choice in line:
                print(line)
                replace_string = input("Enter data to be replaced in file for entered user_name\n")
                with open("tasks.txt", "a+") as ftasks:  # edit data in text file through user input
                    ftasks.writelines(str(replace_string))
                return replace_string, "data edited"
"""