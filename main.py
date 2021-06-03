"""
 #############################################   READ ME   ############################################
 # A simple Arrear Pension calculator app written in Python3 and for GUI I used PySimpleGUI module    #
 # This application is open source under GNU License v.3.                                             #
 # For any feedback or bug reporting, contact me at github - https://github.com/loku-sama             #
 # Author : SOURAV (Loku), A newbie coder.                                                            #
 # Dependencies to run the code : 1. Python3                                                          #
 #                                2. PySimpleGUI module                                               #
 #                                3. Dateutil module                                                  #
 #                                4. Default datetime module, Os module                               #
 #                                5. jinja2 module to generate HTML reports                           #
 ######################################################################################################
"""

import layout  # Importing Layout file to make GUI
import global_classes as gc  # Importing global_classes file to use global functions and classes

while True:
    event, values = layout.window.read()  # Reading window changes

    if event in [layout.sg.WIN_CLOSE_ATTEMPTED_EVENT, 'Exit     ']:
        confirm = layout.sg.popup_yes_no('Do you really want to Close the application?', title='Confirm Exit?',
                                         icon=r'icon.ico', text_color='red', image=r'exit.png')
        if confirm is 'Yes':
            break

    if event == "About the App":
        layout.sg.popup("Arrear Pension Calculator for employees of Govt. of West Bengal.\nVersion - 1.0.1\n"
                        "App coded by SOURAV, Language- Python3 and a little HTML."
                        "\nUse this app for calculating Due Drawn of Pension Between two dates.\n"
                        "This application is Open Source and licensed under GNU Public License V.3. You can download "
                        " the source code from Github. \n Always download the latest release from the Github page.",
                        title="About the Application", icon=r'icon.ico', )

    if event == "fsm":
        layout.sg.Popup("The free software movement is a social movement with the goal of obtaining and guaranteeing "
                        "certain "
                        "freedoms for software users, namely the freedom to run the software, to study the software, "
                        "to modify the software, to share possibly modified copies of the software. Software which "
                        "meets these requirements is termed free software. The word 'free' is ambiguous in English, "
                        "although in this context, it means 'free as in freedom', not 'free as in zero price'."
                        "\nSource: Wikipedia", title="Free Software Movement", custom_text="Close", icon=r'icon.ico', )

    if event == 'Fork Me on Github':
        layout.sg.webbrowser.open(url='https://github.com/loku-sama', new=2, )
    if event == 'Check for Updates':
        layout.sg.webbrowser.open(url='https://github.com/loku-sama/arrear_pension_calculator/releases', new=2, )
    if event == "Contact Me":
        layout.sg.popup("For any problem/bug reporting/help, please email me at - happysourav96@gmail.com \n"
                        "You can also visit my website www.lokusden.neocities.org for more information.",
                        title="Contact Me", icon=r'icon.ico', custom_text="Thank You")
    if event == 'python' or event == 'python1':
        layout.sg.webbrowser.open(url='https://www.python.org/', new=2, )

    if event == 'da_sh':  # Triggering the Comp. Schedule window
        layout.window['main'].update(visible=False)
        layout.window['da'].update(visible=True)
        layout.window['sub_dr'].update(disabled=True)
        layout.window['sub_dr_drawn'].update(disabled=True)
        layout.window['combo-due'].update(disabled=True)

    if event in ['back', 'Home']:  # Triggering the main window
        layout.window['main'].update(visible=True)
        layout.window['da'].update(visible=False)

    if event == "cal_dr":  # Triggering the Calculate event in Comp. schedule window
        def calculate_additional_components():
            """ Function for calculating component different component details """
            global total_dr
            try:
                dr1_1 = gc.MainStart((values["start_date_dr1"]), (values["end_date_dr1"]), (int(values['dr1'])))
                dr1_result = dr1_1.get_dr1((int(values['dr1'])), 'dr1.1')
            except:
                dr1_result = 0
            try:
                dr2_2 = gc.MainStart((values["start_date_dr2"]), (values["end_date_dr2"]), (int(values['dr2'])))
                dr2_result = dr2_2.get_dr1((int(values['dr2'])), 'dr2.2')
            except:
                dr2_result = 0
            try:
                dr3_3 = gc.MainStart((values["start_date_dr3"]), (values["end_date_dr3"]), (int(values['dr3'])))
                dr3_result = dr3_3.get_dr1((int(values['dr3'])), 'dr3.3')
            except:
                dr3_result = 0
            try:
                dr4_4 = gc.MainStart((values["start_date_dr4"]), (values["end_date_dr4"]), (int(values['dr4'])))
                dr4_result = dr4_4.get_dr1((int(values['dr4'])), 'dr4.4')
            except:
                dr4_result = 0
            try:
                dr5_5 = gc.MainStart((values["start_date_dr5"]), (values["end_date_dr5"]), (int(values['dr5'])))
                dr5_result = dr5_5.get_dr1((int(values['dr5'])), 'dr5.5')
            except:
                dr5_result = 0
            try:
                total_dr = dr1_result + dr2_result + dr3_result + dr4_result + dr5_result
                if total_dr > 0:
                    layout.window['total_dr_all'].update(total_dr)
                    layout.window['sub_dr'].update(disabled=False)
                    layout.window['sub_dr_drawn'].update(disabled=False)
                    layout.window['combo-due'].update(disabled=False)
                else:
                    layout.sg.Popup("Please input valid data atlease in the first column.", title="Error!",
                                    icon=r'icon.ico')
                    layout.window['sub_dr'].update(disabled=True)
                    layout.window['sub_dr_drawn'].update(disabled=True)
                    layout.window['combo-due'].update(disabled=True)
                    layout.window['total_dr_all'].update(0)
            except:
                pass

        calculate_additional_components()

    if event == 'sub_dr_drawn':  # Submit to Drawn section
        if values['combo-due'] == "DR":
            layout.sg.Popup("Data submitted succesfully.", title="Success", icon=r'icon.ico')
            layout.window['main'].update(visible=True)
            layout.window['da'].update(visible=False)
            layout.window['old_dr_show'].update(total_dr)
            layout.window['old_dr'].update(0)
        elif values['combo-due'] == "MR":
            layout.sg.Popup("Data submitted succesfully.", title="Success", icon=r'icon.ico')
            layout.window['main'].update(visible=True)
            layout.window['da'].update(visible=False)
            layout.window['old_mr_show'].update(total_dr)
            layout.window['old_mr'].update(0)
        elif values['combo-due'] == "IR":
            layout.sg.Popup("Data submitted succesfully.", title="Success", icon=r'icon.ico')
            layout.window['main'].update(visible=True)
            layout.window['da'].update(visible=False)
            layout.window['old_ir_show'].update(total_dr)
            layout.window['old_ir'].update(0)
        elif values['combo-due'] == "COM":
            layout.sg.Popup("Data submitted succesfully.", title="Success", icon=r'icon.ico')
            layout.window['main'].update(visible=True)
            layout.window['da'].update(visible=False)
            layout.window['old_cp_show'].update(total_dr)
            layout.window['old_cp'].update(0)
        else:
            layout.sg.Popup("Please select the component from the dropdown list.", title="Error!", icon=r'icon.ico')

    if event == 'sub_dr':  # Submit to Due section
        if values['combo-due'] == "DR":
            layout.sg.Popup("Data submitted succesfully.", title="Success", icon=r'icon.ico')
            layout.window['main'].update(visible=True)
            layout.window['da'].update(visible=False)
            layout.window['new_dr_show'].update(total_dr)
            layout.window['new_dr'].update(0)
        elif values['combo-due'] == "MR":
            layout.sg.Popup("Data submitted succesfully.", title="Success", icon=r'icon.ico')
            layout.window['main'].update(visible=True)
            layout.window['da'].update(visible=False)
            layout.window['new_mr_show'].update(total_dr)
            layout.window['new_mr'].update(0)
        elif values['combo-due'] == "IR":
            layout.sg.Popup("Data submitted succesfully.", title="Success", icon=r'icon.ico', )
            layout.window['main'].update(visible=True)
            layout.window['da'].update(visible=False)
            layout.window['new_ir_show'].update(total_dr)
            layout.window['new_ir'].update(0)
        elif values['combo-due'] == "COM":
            layout.sg.Popup("Data submitted succesfully.", title="Success", icon=r'icon.ico')
            layout.window['main'].update(visible=True)
            layout.window['da'].update(visible=False)
            layout.window['new_cp_show'].update(total_dr)
            layout.window['new_cp'].update(0)
        else:
            layout.sg.Popup("Please select the component from the dropdown list.", title="Error!", icon=r'icon.ico')

    if event == "CALCULATE":  # Main event to calculate arrear amount
        try:
            # Lump sum variable
            lump_due = int(values['lump_due'])
            lump_drawn = int(values['lump_drawn'])
            lump_due_show = lump_due
            lump_drawn_show = lump_drawn

            ##################################### Drawn Section #################################3################

            old_basic = gc.MainStart((values["start_date"]), (values["end_date"]), (int(values['old_basic'])))
            old_basic_due = old_basic.get_dr1((int(values['old_basic'])), 'old_basic_show')

            if values['old_dr_show'] != '' and int(values['old_dr']) == 0:
                old_dr_due = int(values['old_dr_show'])
                pass
            else:
                old_dr = gc.MainStart((values["start_date"]), (values["end_date"]), (int(values['old_dr'])))
                old_dr_due = old_dr.get_dr1((int(values['old_dr'])), 'old_dr_show')

            if values['old_mr_show'] != '' and int(values['old_mr']) == 0:
                old_mr_due = int(values['old_mr_show'])
                pass
            else:
                old_mr = gc.MainStart((values["start_date"]), (values["end_date"]), (int(values['old_mr'])))
                old_mr_due = old_mr.get_dr1((int(values['old_mr'])), 'old_mr_show')

            if values['old_cp_show'] != '' and int(values['old_cp']) == 0:
                old_cp_due = int(values['old_cp_show'])
                pass
            else:
                old_cp = gc.MainStart((values["start_date"]), (values["end_date"]), (int(values['old_cp'])))
                old_cp_due = old_cp.get_dr1((int(values['old_cp'])), 'old_cp_show')

            if values['old_ir_show'] != '' and int(values['old_ir']) == 0:
                old_ir_due = int(values['old_ir_show'])
                pass
            else:
                old_ir = gc.MainStart((values["start_date"]), (values["end_date"]), (int(values['old_ir'])))
                old_ir_due = old_ir.get_dr1((int(values['old_ir'])), 'old_ir_show')

            total_drawn = old_basic_due + old_dr_due + old_mr_due + old_ir_due + lump_drawn_show - old_cp_due
            layout.window['total_drawn'].update(total_drawn)

            ################################### Due Section ########################################

            new_basic = gc.MainStart((values["start_date"]), (values["end_date"]), (int(values['new_basic'])))
            new_basic_due = new_basic.get_dr1((int(values['new_basic'])), 'new_basic_show')

            if values['new_dr_show'] != '' and int(values['new_dr']) == 0:
                new_dr_due = int(values['new_dr_show'])
                pass
            else:
                new_dr = gc.MainStart((values["start_date"]), (values["end_date"]), (int(values['new_dr'])))
                new_dr_due = new_dr.get_dr1((int(values['new_dr'])), 'new_dr_show')

            if values['new_mr_show'] != '' and int(values['new_mr']) == 0:
                new_mr_due = int(values['new_mr_show'])
                pass
            else:
                new_mr = gc.MainStart((values["start_date"]), (values["end_date"]), (int(values['new_mr'])))
                new_mr_due = new_mr.get_dr1((int(values['new_mr'])), 'new_mr_show')

            if values['new_cp_show'] != '' and int(values['new_cp']) == 0:
                new_cp_due = int(values['new_cp_show'])
                pass
            else:
                new_cp = gc.MainStart((values["start_date"]), (values["end_date"]), (int(values['new_cp'])))
                new_cp_due = new_cp.get_dr1((int(values['new_cp'])), 'new_cp_show')

            if values['new_ir_show'] != '' and int(values['new_ir']) == 0:
                new_ir_due = int(values['new_ir_show'])
                pass
            else:
                new_ir = gc.MainStart((values["start_date"]), (values["end_date"]), (int(values['new_ir'])))
                new_ir_due = new_ir.get_dr1((int(values['new_ir'])), 'new_ir_show')

            total_due = new_basic_due + new_dr_due + new_mr_due + new_ir_due + lump_drawn_show - new_cp_due
            layout.window['total_due'].update(total_due)
            total_arrear = total_due - total_drawn
            if total_drawn == 0 and total_due == 0:
                layout.window['arrear'].update(0)
            else:
                layout.window['arrear'].update(total_arrear)
            layout.window['report1'].update(disabled=False)
        except:
            layout.sg.popup("Please enter data in valid format (Dates etc.)", title="Error!", icon=r'icon.ico')
            layout.window['report1'].update(disabled=True)

    ########################################### Report Section ##############################################

    template_var = {"id": values['id'], "pen_name": values['name'], "bp_due": values['new_basic'],
                    "mr_due": values['new_mr'], "start_date": values['start_date'], "dr_due": values['new_dr'],
                    "end_date": values['end_date'], "cp_due": values['new_cp'], "ir_due": values['new_ir'],
                    "total_bp_due": values['new_basic_show'], "total_dr_due": values['new_dr_show'],
                    "total_mr_due": values['new_mr_show'], "total_cp_due": values['new_cp_show'],
                    "total_ir_due": values['new_ir_show'], "total_due": values['total_due'],
                    "bp_drawn": values['old_basic'], "dr_drawn": values['old_dr'],
                    "mr_drawn": values['old_mr'], "cp_drawn": values['old_cp'], "ir_drawn": values['old_ir'],
                    "total_bp_drawn": values['old_basic_show'], "total_dr_drawn": values['old_dr_show'],
                    "total_mr_drawn": values['old_mr_show'], "total_cp_drawn": values['old_cp_show'],
                    "total_ir_drawn": values['old_ir_show'], "lump_due": values['lump_due'],
                    "total_drawn": values['total_drawn'], "total_arrear": values['arrear']}
    if event == 'report1':  # Event to generate report
        try:
            html_out = layout.template_pen.render(template_var)  # Rendering variables to the report
            file_name = f"arrear_report_{layout.time_stamp}.html"  # Makes a dynamic filename everytime
            with open(f"./reports/{file_name}", "w") as f:
                f.write(html_out)  # Writing the data in the template
            f.close()  # Closing the report file
            layout.sg.webbrowser.open(url=f"{layout.current_directory}/reports/{file_name}", new=2)
        except:
            layout.sg.Popup("Something went Horribly wrong. Please try again.", title="ERROR!", icon=r'icon.ico')

layout.window.close()  # Closes the main window
