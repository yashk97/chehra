"""
Contains the function for generating course_wise report of attendance
"""
from .models import Course, Lecture, Student
import pandas as pd
import numpy as np


def generate(course_id):
    """
    Given the course_id it generates a CSV?Excel Sheet of the attendances so far
    for that coure
    :param course_id: Int, Course_id
    :return:
    """

    course = Course.objects.get(course_id=course_id)

    students = course.students
    lectures = course.lecture_set

    uids = [uid[0] for uid in
            students.values_list("uid").all()]
    names = [student.user.first_name + " " + student.user.last_name
             for student in students.all()]

    lect_nos = [l[0] for l in lectures.values_list("lect_no").all()]

    columns = ['Name', 'UID'] + lect_nos + ['Percentage']

    df = pd.DataFrame(columns=columns)

    df['Name'] = names
    df['UID'] = uids

    lecture_set = lectures.all()


    for lecture in lecture_set:
        lect_students = [uid[0] for uid in lecture.students.values_list("uid")]

        df[lecture.lect_no] = 0
        df[lecture.lect_no][df['UID'].isin(lect_students)] = 1

    df['Percentage'] = df.iloc[:, 2:-1].sum(axis=1).divide(len(lect_nos))

    for lecture in lecture_set:
        df[lecture.lect_no].loc[df[lecture.lect_no] == 1] = 'P'
        df[lecture.lect_no].loc[df[lecture.lect_no] == 0] = 'AB'

    print(df)


    return df
