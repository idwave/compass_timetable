#!/usr/bin/env python3

from services.create_timetable import read_timetable_from_csv
from config import SHEET_ID, SHEET_NAME
import pandas as pd
from datetime import datetime

DAYS = {
    0: 'понедельник',
    1: 'вторник',
    2: 'среда',
    3: "четверг",
    4: "пятница",
    5: "суббота",
    6: "воскресенье",
}


    
def check_time_interval(start_time, end_time):
    now = datetime.now().time()
    start = datetime.strptime(start_time, '%H:%M').time()
    end = datetime.strptime(end_time, '%H:%M').time()
    if start <= end:
        return start <= now <= end
    else:
        return start <=now or now <= end
    

def get_week_timetable(class_name):
    df = load_class_timetable(class_name) 
    return df

def get_day_timetable(class_name, day):
    df = load_class_timetable(class_name)
    df = df.loc[(df['day'] == day)]    
    return df

def get_today_timetable(class_name):
    day = datetime.today().weekday()
    df = get_day_timetable(class_name, DAYS[day])   
    return df if day < 5 else 'Выходной'

def get_tomorrow_timetable(class_name):
    day = datetime.today().weekday() + 1
    df = get_day_timetable(class_name, DAYS[day])   
    return df if day < 5 else 'Выходной'

def make_time_intervals(df):
    time_intervals = []
    for index, row in df.iterrows():
        start_time, end_time = str(row['time']).split('-')
        time_intervals.append(start_time)
        time_intervals.append(end_time)
    return time_intervals

def get_current_lesson(class_name):
    df = get_today_timetable(class_name)
    time_intervals = make_time_intervals(df)
    lesson_index = -1
    for i in range(len(time_intervals)-1):
        if check_time_interval(time_intervals[i],time_intervals[i+1]):
            lesson_index = i
    return df.reset_index(drop=True), lesson_index

        
def load_class_timetable(class_name):
    df = read_timetable_from_csv(SHEET_ID,SHEET_NAME)
    df = df.loc[(df['class_name'] == class_name)].reset_index(drop=True)
    return df

