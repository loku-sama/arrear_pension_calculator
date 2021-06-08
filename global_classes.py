"""
########################################################################################
#  The main Class and Global functions file of Arrear Pension Calculator App           #
#  Author : Sourav                                                                     #
########################################################################################
"""
from dateutil import relativedelta  # Dateutil module to calculate periods between two dates
from datetime import datetime  # Default Datetime module
import layout  # Importing Layout file to make GUI


def print_number_of_days(y, m):
    """ Function for calculating total no. of days in a month """
    leap = 0
    if y % 400 == 0:
        leap = 1
    elif y % 100 == 0:
        leap = 0
    elif y % 4 == 0:
        leap = 1
    if m == 2:
        return 28 + leap
    months = [1, 3, 5, 7, 8, 10, 12]
    if m in months:
        return 31
    return 30


def get_arrear(pension, total_months, diff_month, diff_day, total_days_in_start, extra_day_in_end, extra_day_in_start,
               total_days_in_end, diff_year):
    """ Main function for calculating the arrear amount between 2 given dates """
    arrear_basic = 0
    if total_months == 0 and diff_year == 0:
        arrear_basic = pension * (diff_day + 1) / total_days_in_start
        return round(arrear_basic)
    if diff_month >= 1:
        p = pension * diff_month
    else:
        p = 0
    if extra_day_in_end >= 1:
        q = pension * extra_day_in_end / total_days_in_end
    else:
        q = 0
    if extra_day_in_start < total_days_in_start:
        s = pension * extra_day_in_start / total_days_in_start
    else:
        s = 0
    arrear_basic = p + q + s
    return round(arrear_basic)


class MainStart:
    def __init__(self, start_date1, end_date1, dr1):  # Class constructor function
        self.start_date1 = start_date1 = datetime.strptime(str(start_date1), "%d/%m/%Y")
        self.end_date1 = end_date1 = datetime.strptime(str(end_date1), "%d/%m/%Y")
        self.diff1 = diff1 = relativedelta.relativedelta(end_date1, start_date1)
        self.difference1 = difference1 = relativedelta.relativedelta(end_date1, start_date1)
        self.start_year1 = start_year1 = start_date1.year
        self.end_year1 = end_year1 = end_date1.year
        self.start_month1 = start_month1 = start_date1.month
        self.end_month1 = end_month1 = end_date1.month
        self.start_day1 = start_day1 = start_date1.day
        self.end_day1 = end_day1 = end_date1.day
        self.Diff_year1 = Diff_year1 = difference1.years
        self.Diff_month1 = Diff_month1 = difference1.months
        self.Diff_days1 = Diff_days1 = difference1.days
        self.total_days_in_start_month1 = total_days_in_start_month1 = print_number_of_days(start_year1, start_month1)
        self.total_days_in_end_month1 = total_days_in_end_month1 = print_number_of_days(end_year1, end_month1)
        self.extra_day_in_start_date1 = extra_day_in_start_date1 = (total_days_in_start_month1 - start_date1.day) + 1
        self.extra_day_in_end_date1 = extra_day_in_end_date1 = end_date1.day
        self.months_in_days1 = months_in_days1 = (Diff_month1 * 30) + Diff_days1 + (Diff_year1 * 12 * 30)
        self.dr1 = int(dr1)

    def get_dr1(self, dr1, up_field):
        """ Additional function for calculating the arrear amount between 2 given dates """
        try:
            if self.start_day1 == 1 and self.extra_day_in_end_date1 == self.total_days_in_end_month1:
                exact_months1 = round((
                        self.months_in_days1 - self.extra_day_in_start_date1 - self.extra_day_in_end_date1) / 30) + 1
            elif self.start_day1 == 1 and self.Diff_year1 == 0:
                exact_months1 = self.Diff_month1
            elif self.end_day1 != self.total_days_in_end_month1 and self.start_day1 == 1:
                exact_months1 = round(
                    (self.months_in_days1 - self.extra_day_in_start_date1 - self.extra_day_in_end_date1) / 30) + 1
            else:
                exact_months1 = round(
                    (self.months_in_days1 - self.extra_day_in_start_date1 - self.extra_day_in_end_date1) / 30)

            dr1_due = get_arrear(dr1, self.Diff_month1, exact_months1, self.Diff_days1, self.total_days_in_start_month1,
                                 self.extra_day_in_end_date1, self.extra_day_in_start_date1,
                                 self.total_days_in_end_month1, self.Diff_year1)
            layout.window[up_field].update(dr1_due)
            return dr1_due
        except:
            pass
