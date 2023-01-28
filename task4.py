# pip install pandas openpyxl
import pandas as pd

students_avg_scores = {'Max': 4.964, 'Eric': 4.962, 'Peter': 4.923, 'Mark': 4.957, 'Julie': 4.95, 'Jimmy': 4.973,
                       'Felix': 4.937, 'Vasya': 4.911, 'Don': 4.936, 'Zoi': 4.937}


def make_report_about_top3(students_avg_scores):
    sort_students = dict(sorted(students_avg_scores.items(), key=lambda item: -item[1]))
    dict_df = {'name': list(sort_students.keys()), 'scores': list(sort_students.values())}
    df = pd.DataFrame(dict_df).head(3)
    df.to_excel('./top_students.xlsx')
    return './top_students.xlsx'


make_report_about_top3(students_avg_scores)
