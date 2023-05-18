
import pandas as pd
import os
import re

from pandas.core.indexes.category import contains
from .helper import DAYS_RU, TEACHERS_DIC
from .download_from_drive import get_csv_from_drive

DF_COLUMNS = ["class_name", "day", "subject", "teacher", "room", "number"]

TIME_SET = {1: '09:00-09:45',
           2: '09:55-10:35',
           3: '10:50-11:30',
           4: '11:50-12:30',
           5: '12:40-13:20',
           6: '13:30-14:10',
           7: '14:15-14:35',
           8: '14:40-15:20',
           9: '15:30-16:10',
           10: '16:12-17:00',
           11: '17:10-17:50',
            }

def get_classnames(df_to_parse):
    result = []
    for col in df_to_parse.columns:
        result.append(col) if 'класс' in col else None
    return result

def dic_of_classes_with_labels(sheet_id, sheet_name):
    df = read_timetable_from_csv(sheet_id, sheet_name)
    all_classes = df['class_name'].unique()
    classes = {}
    for class_name in all_classes:
        key = re.findall(r"\d+",class_name)[0]
        value = re.findall(r"\D",class_name)[0].lower()
        if key in classes.keys():
            classes[key].append(value)
        else:
            classes[key] = [value]

    return classes


def create_timetable(sheet_id, sheet_name):
    df_to_parse = get_csv_from_drive(sheet_id, sheet_name)
    df_to_parse.columns = df_to_parse.columns.str.lower()
    return create_timetable_from_df(df_to_parse)

def create_timetable_from_df(df_to_parse):
    df = pd.DataFrame(columns = DF_COLUMNS)
    class_names = get_classnames(df_to_parse)
    print(class_names)
    for class_name in class_names:
        df = pd.concat([df, get_timetable_by_class(df_to_parse, class_name)], ignore_index = True)
    df = add_time_column(df)
    write_to_csv(df)
    return df

def write_to_csv(df):
    df.to_csv('df.csv', index=False)
    return df

def get_timetable_by_class(df_to_parse, class_name):
    df = pd.DataFrame(columns = DF_COLUMNS)
    room_col = df_to_parse.columns.get_loc(class_name) + 1
    for i, row in enumerate(df_to_parse[class_name]):
        if row in DAYS_RU.keys():
            current_day = row
            lesson_number = 1
            flag = 1
        else:
            subject, teacher = get_subject_and_teacher(str(row))
            room = df_to_parse.iloc[i, room_col]
            if 'обед' in subject:
                df.loc[len(df)] = [class_name, current_day, subject, ' ', room, lesson_number]
                flag = 0
            if flag == 1:
                df.loc[len(df)] = [class_name, current_day, subject, teacher, room, lesson_number]
                lesson_number += 1

    return df

def add_time_column(df):
    df['time'] = None
    df['time'] = df['number'].map(TIME_SET)

    return df


def get_subject_and_teacher(row):
    row = row.replace('\n', ' ')
    data = [x.strip() for x in re.split(' с | со', row)]
    subject = data[0]
    teacher_name = TEACHERS_DIC[data[1]] if len(data) > 1 else 'None'
    return subject, teacher_name


def read_timetable_from_csv(sheet_id, sheet_name):
    if os.path.exists('df.csv'):
        df = pd.read_csv('df.csv')
    else:
        df = create_timetable(sheet_id, sheet_name)
    return df

