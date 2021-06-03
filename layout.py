"""
########################################################################################
#  The main Graphical User Interface file of Arrear Pension Calculator App             #
#  Author : Sourav                                                                     #
########################################################################################
"""
import PySimpleGUI as sg  # Main GUI Module
from jinja2 import Environment, FileSystemLoader  # Module to generate reports
import datetime  # Default Datetime module
import os  # Default OS module

sg.theme("BlueMono")  # Application main theme
date_format = "%d/%m/%Y"  # Date format
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')  # Time stamp to generate dynamic report filename
current_directory = os.getcwd()  # Getting current working directory

env = Environment(loader=FileSystemLoader('./templates'))
template_pen = env.get_template("temp_report.html")  # Template file for Pension report

##################################### Main Menu ####################################
menu_def = [
    ['Menu       ',
     [
         'Home',
         '---',
         'About the App',
         "---",
         'Contact Me',
         '---',
         'Fork Me on Github',
         '---',
         'Check for Updates',
         '---',
         'Exit     ',
     ],
     ],
]
####################################### Start Page Layout ##################################################
home_layout = [
    [sg.Text("", size=(15, 1)), sg.Text("ARREAR PENSION CALCULATOR", size=(50, 1), font=(15), justification="center"),
     sg.Image(r'pysmall.png', enable_events=True, key='python1', tooltip="Click here to know more!")],
    [sg.Text("An open source application for calculating arrear pension between any given period", size=(100, 1),
             justification="center")],
    [sg.HSeparator()],
    [sg.Text("PPO ID: ", size=(10, 1)), sg.Input(size=(10, 1), enable_events=True, border_width=1, key='id'),
     sg.Text(size=(15, 1)),
     sg.Text("Pensioner's Name :", size=(15, 1)), sg.InputText(size=(32, 1), key='name', enable_events=True),
     ],
    [sg.HSeparator()],
    [sg.Text("Arrear From :", size=(10, 1)), sg.In("", size=(15, 1), key='start_date', enable_events=True),
     sg.CalendarButton(title="From Date", key="dof", enable_events=True, disabled=False, format=date_format,
                       no_titlebar=False, button_text="Choose Date"), sg.Text(size=(10, 1)),
     sg.Text("Arrear Upto :", size=(10, 1)), sg.In("", size=(15, 1), key='end_date', enable_events=True),
     sg.CalendarButton(title="Upto Date", key="dou", enable_events=True, disabled=False, format=date_format,
                       no_titlebar=False, button_text="Choose Date")
     ],
    [
        sg.Text("Please fill up Components Schedule to calculate applicable components if you have different periods."),
        sg.Button("Comp. Schedule", key='da_sh', enable_events=True, tooltip="Click to fill up Comp. Schedule")
    ],
    [sg.HSeparator()],
    [
        sg.Text("Due", size=(37, 1), font=(2)),
        sg.VSeparator(),
        sg.Text("Drawn", size=(30, 1), font=(2))
    ],
    [sg.HSeparator()]
]
first_column = [
    [
        sg.Text("Components :", size=(15, 1)), sg.Text("Per Month", size=(10, 1)), sg.VSeparator(),
        sg.Text("Total", size=(10, 1)),
    ],
    [sg.HSeparator()],
    [
        sg.Text("Basic Pension :", size=(13, 1)),
        sg.Input(key='new_basic', size=(14, 1), enable_events=True, default_text=int(0)),
        sg.Input(key='new_basic_show', size=(14, 1), disabled=True, enable_events=True),
    ],
    [
        sg.Text("Dearness Relief :", size=(13, 1)),
        sg.Input(key='new_dr', size=(14, 1), enable_events=True, default_text=int(0), disabled=False),
        sg.Input(key='new_dr_show', size=(14, 1), disabled=True, enable_events=True),
    ],
    [
        sg.Text("Medical Relief :", size=(13, 1)),
        sg.Input(key='new_mr', size=(14, 1), enable_events=True, default_text=int(0)),
        sg.Input(key='new_mr_show', size=(14, 1), disabled=True, enable_events=True),
    ],
    [
        sg.Text("Commuted \nPension :", size=(13, 2)),
        sg.Input(key='new_cp', size=(14, 2), enable_events=True, default_text=int(0)),
        sg.Input(key='new_cp_show', size=(14, 2), disabled=True, enable_events=True),
    ],
    [
        sg.Text("Interim \nRelief :", size=(13, 2)),
        sg.Input(key='new_ir', size=(14, 2), enable_events=True, default_text=int(0)),
        sg.Input(key='new_ir_show', size=(14, 2), disabled=True, enable_events=True),
    ],
    [sg.Text("Any other (Lump Sum) :", size=(27, 1)),
     sg.Input(key='lump_due', disabled=False, size=(14, 1), default_text=int(0))],
    [sg.Text("Total Due :", size=(13, 1)), sg.In("", key='total_due', disabled=True, size=(30, 1))]
]
second_column = [
    [
        sg.Text("Components :", size=(15, 1)), sg.Text("Per Month", size=(10, 1)), sg.VSeparator(),
        sg.Text("Total", size=(10, 1)),
    ],
    [sg.HSeparator()],
    [
        sg.Text("Basic Pension :", size=(13, 1)),
        sg.Input(key='old_basic', size=(14, 1), enable_events=True, default_text=int(0)),
        sg.Input(key='old_basic_show', size=(14, 1), disabled=True, enable_events=True),
    ],
    [
        sg.Text("Dearness Relief :", size=(13, 1)),
        sg.Input(key='old_dr', size=(14, 1), enable_events=True, default_text=int(0), disabled=False),
        sg.Input(key='old_dr_show', size=(14, 1), disabled=True, enable_events=True),
    ],
    [
        sg.Text("Medical Relief :", size=(13, 1)),
        sg.Input(key='old_mr', size=(14, 1), enable_events=True, default_text=int(0)),
        sg.Input(key='old_mr_show', size=(14, 1), disabled=True, enable_events=True),
    ],
    [
        sg.Text("Commuted \nPension :", size=(13, 2)),
        sg.Input(key='old_cp', size=(14, 2), enable_events=True, default_text=int(0)),
        sg.Input(key='old_cp_show', size=(14, 2), disabled=True, enable_events=True),
    ],
    [
        sg.Text("Interim \nRelief :", size=(13, 2)),
        sg.Input(key='old_ir', size=(14, 2), enable_events=True, default_text=int(0)),
        sg.Input(key='old_ir_show', size=(14, 2), disabled=True, enable_events=True),
    ],
    [sg.Text("Any other (Lump Sum) :", size=(27, 1)), sg.Input(key='lump_drawn', disabled=False, size=(14, 1),
                                                               default_text=int(0), enable_events=True)],
    [sg.Text("Total Drawn :", size=(13, 1)), sg.Input("", key='total_drawn', disabled=True, size=(30, 1))]
]

################################### Comp. Schedule Layout ################################################

da_layout = [
    # [sg.HSeparator()],
    [sg.Text("COMPONENTS SCHEDULE", size=(700, 1), font=(15), justification="center")],
    [sg.HSeparator()],
    [sg.Text("Please fill the details to calculate applicable Components for different periods", justification="center",
             size=(700, 2), )],
    [sg.HSeparator()],
    [sg.Text("From ", size=(5, 1)), sg.Text(size=(18, 1)), sg.Text("Upto ", size=(5, 1)), sg.Text(size=(20, 1)),
     sg.Text("Per Month", size=(15, 1)), sg.Text(size=(3, 1)), sg.Text("Total ", size=(5, 1))
     ],
    [sg.HSeparator()],
    [sg.In("", size=(10, 1), key='start_date_dr1', enable_events=True),
     sg.CalendarButton(title="From Date", key="drf1", enable_events=True, disabled=False, format=date_format,
                       no_titlebar=False, button_text="Choose Date"), sg.Text(size=(1, 1)),
     sg.In("", size=(10, 1), key='end_date_dr1', enable_events=True),
     sg.CalendarButton(title="Upto Date", key="dru1", enable_events=True, disabled=False, format=date_format,
                       no_titlebar=False, button_text="Choose Date"), sg.Text(size=(5, 1)),
     sg.Input(size=(15, 1), default_text=int(0), key='dr1', enable_events=True), sg.Text(size=(5, 1)),
     sg.Input(size=(15, 1), default_text=int(0), key='dr1.1', enable_events=True, disabled=True),
     ],
    [sg.In("", size=(10, 1), key='start_date_dr2', enable_events=True),
     sg.CalendarButton(title="From Date", key="drf2", enable_events=True, disabled=False, format=date_format,
                       no_titlebar=False, button_text="Choose Date"), sg.Text(size=(1, 1)),
     sg.In("", size=(10, 1), key='end_date_dr2', enable_events=True),
     sg.CalendarButton(title="Upto Date", key="dru2", enable_events=True, disabled=False, format=date_format,
                       no_titlebar=False, button_text="Choose Date"), sg.Text(size=(5, 1)),
     sg.Input(size=(15, 1), default_text=int(0), key='dr2', enable_events=True), sg.Text(size=(5, 1)),
     sg.Input(size=(15, 1), default_text=int(0), key='dr2.2', enable_events=True, disabled=True),
     ],
    [sg.In("", size=(10, 1), key='start_date_dr3', enable_events=True),
     sg.CalendarButton(title="From Date", key="drf3", enable_events=True, disabled=False, format=date_format,
                       no_titlebar=False, button_text="Choose Date"), sg.Text(size=(1, 1)),
     sg.In("", size=(10, 1), key='end_date_dr3', enable_events=True),
     sg.CalendarButton(title="Upto Date", key="dru3", enable_events=True, disabled=False, format=date_format,
                       no_titlebar=False, button_text="Choose Date"), sg.Text(size=(5, 1)),
     sg.Input(size=(15, 1), default_text=int(0), key='dr3', enable_events=True), sg.Text(size=(5, 1)),
     sg.Input(size=(15, 1), default_text=int(0), key='dr3.3', enable_events=True, disabled=True),
     ],
    [sg.In("", size=(10, 1), key='start_date_dr4', enable_events=True),
     sg.CalendarButton(title="From Date", key="drf4", enable_events=True, disabled=False, format=date_format,
                       no_titlebar=False, button_text="Choose Date"), sg.Text(size=(1, 1)),
     sg.In("", size=(10, 1), key='end_date_dr4', enable_events=True),
     sg.CalendarButton(title="Upto Date", key="dru4", enable_events=True, disabled=False, format=date_format,
                       no_titlebar=False, button_text="Choose Date"), sg.Text(size=(5, 1)),
     sg.Input(size=(15, 1), default_text=int(0), key='dr4', enable_events=True), sg.Text(size=(5, 1)),
     sg.Input(size=(15, 1), default_text=int(0), key='dr4.4', enable_events=True, disabled=True),
     ],
    [sg.In("", size=(10, 1), key='start_date_dr5', enable_events=True),
     sg.CalendarButton(title="From Date", key="drf5", enable_events=True, disabled=False, format=date_format,
                       no_titlebar=False, button_text="Choose Date"), sg.Text(size=(1, 1)),
     sg.In("", size=(10, 1), key='end_date_dr5', enable_events=True),
     sg.CalendarButton(title="Upto Date", key="dru5", enable_events=True, disabled=False, format=date_format,
                       no_titlebar=False, button_text="Choose Date"), sg.Text(size=(5, 1)),
     sg.Input(size=(15, 1), default_text=int(0), key='dr5', enable_events=True), sg.Text(size=(5, 1)),
     sg.Input(size=(15, 1), default_text=int(0), key='dr5.5', enable_events=True, disabled=True),
     ],
    [sg.HSeparator()],
    [
        sg.Text(size=(17, 1)), sg.Text("Total :"), sg.Input(size=(45, 1), key='total_dr_all', disabled=True),
    ],
    [
        sg.Text("Select Component type to submit :"),
        sg.Combo(['Select', 'DR', 'MR', 'IR', 'COM'], default_value="Select", enable_events=True, disabled=True,
                 key='combo-due', tooltip="Select applicable component from the list.")
    ],
    [
        sg.Text(size=(13, 1)),
        sg.Button("CALCULATE", key='cal_dr', enable_events=True, tooltip="Click to Calculate"),
        sg.Button("Submit to Due", key='sub_dr', size=(15, 1), enable_events=True, disabled=True,
                  tooltip="Click to Submit to Due section"),
        sg.Button("Submit to Drawn", key='sub_dr_drawn', size=(15, 1), enable_events=True, disabled=True,
                  tooltip="Click to Submit to Drawn section"),
        sg.Button("BACK", key='back', size=(10, 1), tooltip="Click to go back")
    ],
    [sg.HSeparator()],
    [sg.Text("Important Notes: ", font=(1))],
    [sg.Text("1. Please use this schedule if you have different rates of components for different periods.")],
    [sg.Text("2. Always click on CALCULATE button after making any changes and then click the applicable "
             "SUBMIT button to save.")],
    [sg.Text("2. DR = Dearness Relief, MR = Medical Relief, IR = Interim Relief, COM = Commuted Pension")],
    [sg.Image(r'python.png', enable_events=True, key='python', tooltip="Click here to know more!", )],
]

############################################## Main App Layout ##################################################
main_layout_app = [
    [sg.Column(home_layout, visible=True)],
    [sg.Column(first_column, visible=True),
     sg.VSeparator(),
     sg.Column(second_column, visible=True)],
    [sg.HSeparator()],
    [sg.Text("Total Arrear (Due - Drawn) :", size=(25, 1)), sg.In("", key='arrear', disabled=True, size=(50, 1))],
    [sg.Text("IMPORTANT : Please click CALCULATE button everytime you make a change."),
     sg.Text("Free-Software-movement", size=(20, 1), key="fsm", tooltip="Click here to know more.",
             font=("u"), enable_events=True)],
    [sg.HSeparator()],
    [sg.Text(size=(23, 1)),
     sg.Button("CALCULATE", tooltip="Click here to calculate arrear pension.", focus=True, size=(20, 1)),
     sg.Button("GENERATE REPORT", key='report1', tooltip="Click here to generate report.", focus=False, size=(20, 1),
               disabled=True)
     ]
]
main_layout = [
    [sg.Menu(menu_def, tearoff=False, key="menu")],
    [sg.Column(main_layout_app, key="main", visible=True),
     sg.Column(da_layout, key='da', visible=False)],
]
window = sg.Window("Arrear Pension Calculator Application", main_layout, size=(755, 600), resizable=False,
                   icon=r'icon.ico', enable_close_attempted_event=True)  # Creating the main window
new_menu_def = menu_def
