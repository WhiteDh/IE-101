def time_of_couple(num):
    if num == 1:
        return "1) (8:30 - 9:40"
    elif num == 2:
        return "2) (10:00 - 11:10"
    elif num == 3:
        return "3) (11:30 - 12:40"
    elif num == 4:
        return "4) (13:00 - 14:10"
    elif num == 5:
        return "5) (14:30 - 15:40"
    elif num == 6:
        return "6) (16:00 - 17:10"
    elif num == 7:
        return "7) (17:30 - 18:40"


monday_par = f"{7 * ' '}({time_of_couple(2)})\n{15 * ' '}<a href='https://docs.google.com/spreadsheets/d/1_NAxUAbaeVJyPgVNi8J2J6EpO_Bd4G0EEHFqJJAjFoo/edit#gid=0&range=C6'>Філософія</a>\n{15 * ' '}Практика\n{15 * ' '}Деркач В.Л.\n\n" \
             f"{7 * ' '}({time_of_couple(3)})\n{15 * ' '}<a href='https://docs.google.com/spreadsheets/d/1_NAxUAbaeVJyPgVNi8J2J6EpO_Bd4G0EEHFqJJAjFoo/edit#gid=0&range=C10'>Соціологія</a>\n{15 * ' '}Лекція\n{15 * ' '}Попов В.Ж.\n\n" \
             f"{7 * ' '}({time_of_couple(4)})\n{15 * ' '}<a href='https://docs.google.com/spreadsheets/d/1_NAxUAbaeVJyPgVNi8J2J6EpO_Bd4G0EEHFqJJAjFoo/edit#gid=0&range=C14'>Філософія</a>\n{15 * ' '}Лекція\n{15 * ' '}Деркач В.Л.\n\n" \
             f"{7 * ' '}({time_of_couple(5)})\n{15 * ' '}<a href='https://docs.google.com/spreadsheets/d/1_NAxUAbaeVJyPgVNi8J2J6EpO_Bd4G0EEHFqJJAjFoo/edit#gid=0&range=C18'>Прикладна інформатика</a>\n{15 * ' '}Лабораторна\n{15 * ' '}Безкоровайний В.С.\n\n"




monday_nep = f"{7 * ' '}({time_of_couple(2)})\n{15 * ' '}<a href='https://docs.google.com/spreadsheets/d/1_NAxUAbaeVJyPgVNi8J2J6EpO_Bd4G0EEHFqJJAjFoo/edit#gid=0&range=C92'>Прикладна інформатика</a>\n{15 * ' '}Лабораторна\n{15 * ' '}Безкоровайний В.С.\n\n" \
             f"{7 * ' '}({time_of_couple(3)})\n{15 * ' '}<a href='https://docs.google.com/spreadsheets/d/1_NAxUAbaeVJyPgVNi8J2J6EpO_Bd4G0EEHFqJJAjFoo/edit#gid=0&range=C96'>Математика</a>\n{15 * ' '}Практика\n{15 * ' '}Лютий О.І.\n\n" \
             f"{7 * ' '}({time_of_couple(4)})\n{15 * ' '}<a href='https://docs.google.com/spreadsheets/d/1_NAxUAbaeVJyPgVNi8J2J6EpO_Bd4G0EEHFqJJAjFoo/edit#gid=0&range=C100'>Математика</a>\n{15 * ' '}Лабораторна\n{15 * ' '}Лютий О.І.\n\n" \


tuesday_par = f"{7 * ' '}({time_of_couple(1)})\n{15 * ' '}Фізичне виховання\n{15 * ' '}Практика{15 * ' '}\n\n" \
              f"{7 * ' '}({time_of_couple(2)})\n{15 * ' '}<a href='https://docs.google.com/spreadsheets/d/1_NAxUAbaeVJyPgVNi8J2J6EpO_Bd4G0EEHFqJJAjFoo/edit#gid=0&range=C28'>Прикладна інформатика</a>\n{15 * ' '}Лекція\n{15 * ' '}Безкоровайний В.С.\n\n" \
              f"{7 * ' '}({time_of_couple(3)})\n{15 * ' '}<a href='https://docs.google.com/spreadsheets/d/1_NAxUAbaeVJyPgVNi8J2J6EpO_Bd4G0EEHFqJJAjFoo/edit#gid=0&range=C32'>Вступ до спеціальності</a>\n{15 * ' '}Лекція\n{15 * ' '}\n\n"




tuesday_nep = f"{7 * ' '}({time_of_couple(1)})\n{15 * ' '}Фізичне виховання\n{15 * ' '}Практика{15 * ' '}\n\n" \
              f"{7 * ' '}({time_of_couple(2)})\n{15 * ' '}<a href='https://docs.google.com/spreadsheets/d/1_NAxUAbaeVJyPgVNi8J2J6EpO_Bd4G0EEHFqJJAjFoo/edit#gid=0&range=C106'>Соціологія</a>\n{15 * ' '}Практика\n{15 * ' '}Попов В.Ж.\n\n" \
              f"{7 * ' '}({time_of_couple(3)})\n{15 * ' '}<a href='https://docs.google.com/spreadsheets/d/1_NAxUAbaeVJyPgVNi8J2J6EpO_Bd4G0EEHFqJJAjFoo/edit#gid=0&range=C110'>Соціологія</a>\n{15 * ' '}Практика\n{15 * ' '}Попов В.Ж.\n\n" \
              f"{7 * ' '}({time_of_couple(4)})\n{15 * ' '}<a href='https://docs.google.com/spreadsheets/d/1_NAxUAbaeVJyPgVNi8J2J6EpO_Bd4G0EEHFqJJAjFoo/edit#gid=0&range=C112'>Прикладна інформатика</a>\n{15 * ' '}Лабораторна\n{15 * ' '}Безкоровайний В.С.\n\n"



wednesday_par = f"{7 * ' '}({time_of_couple(2)})\n{15 * ' '}<a href='https://docs.google.com/spreadsheets/d/1_NAxUAbaeVJyPgVNi8J2J6EpO_Bd4G0EEHFqJJAjFoo/edit#gid=0&range=C48'>Математика</a>\n{15 * ' '}Практика\n{15 * ' '}Лютий О.І.\n\n" \
                f"{7 * ' '}({time_of_couple(3)})\n{15 * ' '}<a href='https://docs.google.com/spreadsheets/d/1_NAxUAbaeVJyPgVNi8J2J6EpO_Bd4G0EEHFqJJAjFoo/edit#gid=0&range=C50'>Психологія</a>\n{15 * ' '}Практика\n{15 * ' '}Дубовик С.М.\n\n" \
                f"{7 * ' '}({time_of_couple(4)})\n{15 * ' '}<a href='https://docs.google.com/spreadsheets/d/1_NAxUAbaeVJyPgVNi8J2J6EpO_Bd4G0EEHFqJJAjFoo/edit#gid=0&range=C52'>Психологія та педагогіка</a>\n{15 * ' '}Практика\n{15 * ' '}Дубовик С.М.\n\n"



wednesday_nep = f"{7 * ' '}({time_of_couple(1)})\n{15 * ' '}<a href='https://docs.google.com/spreadsheets/d/1_NAxUAbaeVJyPgVNi8J2J6EpO_Bd4G0EEHFqJJAjFoo/edit#gid=0&range=C118'>Філософія</a>\n{15 * ' '}Практика\n{15 * ' '}доц. Деркач В.Л\n\n" \
                f"{7 * ' '}({time_of_couple(2)})\n{15 * ' '}<a href='https://docs.google.com/spreadsheets/d/1_NAxUAbaeVJyPgVNi8J2J6EpO_Bd4G0EEHFqJJAjFoo/edit#gid=0&range=C118'>Філософія</a>\n{15 * ' '}Практика\n{15 * ' '}доц. Деркач В.Л\n\n"




thursday_par = f"{7 * ' '}({time_of_couple(3)})\n{15 * ' '}<a href='https://docs.google.com/spreadsheets/d/1_NAxUAbaeVJyPgVNi8J2J6EpO_Bd4G0EEHFqJJAjFoo/edit#gid=0&range=C62'>Соціологія</a>\n{15 * ' '}Практика\n{15 * ' '}Попов В.Ж.\n\n" \
               f"{7 * ' '}({time_of_couple(4)})\n{15 * ' '}<a href='https://docs.google.com/spreadsheets/d/1_NAxUAbaeVJyPgVNi8J2J6EpO_Bd4G0EEHFqJJAjFoo/edit#gid=0&range=C64'>Вступ до спеціальності</a>\n{15 * ' '}Практика\n{15 * ' '}Осипова О.І.\n\n" \
               f"{7 * ' '}({time_of_couple(5)})\n{15 * ' '}<a href='https://docs.google.com/spreadsheets/d/1_NAxUAbaeVJyPgVNi8J2J6EpO_Bd4G0EEHFqJJAjFoo/edit#gid=0&range=C68'>Вступ до спеціальності</a>\n{15 * ' '}Практика\n{15 * ' '}Осипова О.І.\n\n"



thursday_nep = f"{7 * ' '}({time_of_couple(1)})\n{15 * ' '}<a href='https://docs.google.com/spreadsheets/d/1_NAxUAbaeVJyPgVNi8J2J6EpO_Bd4G0EEHFqJJAjFoo/edit#gid=0&range=C134'>Вступ до спеціальності</a>\n{15 * ' '}Практика\n{15 * ' '}Осипова О.І.\n\n" \
               f"{7 * ' '}({time_of_couple(2)})\n{15 * ' '}<a href='https://docs.google.com/spreadsheets/d/1_NAxUAbaeVJyPgVNi8J2J6EpO_Bd4G0EEHFqJJAjFoo/edit#gid=0&range=C138'>Прикладна інформатика</a>\n{15 * ' '}Лабораторна\n{15 * ' '}Безкоровайний В.С.\n\n" \
               f"{7 * ' '}({time_of_couple(4)})\n{15 * ' '}<a href='https://docs.google.com/spreadsheets/d/1_NAxUAbaeVJyPgVNi8J2J6EpO_Bd4G0EEHFqJJAjFoo/edit#gid=0&range=C146'>Психологія та педагогіка</a>\n{15 * ' '}Практика\n{15 * ' '}Дубовик С.М.\n\n"




friday_par = f"{10 * ' '}({time_of_couple(2)})\n{15 * ' '}<a href='https://docs.google.com/spreadsheets/d/1_NAxUAbaeVJyPgVNi8J2J6EpO_Bd4G0EEHFqJJAjFoo/edit#gid=0&range=C76'>Іноземна мова</a>\n{15 * ' '}Практика\n{15 * ' '}\n\n" \
             f"{10 * ' '}({time_of_couple(3)})\n{15 * ' '}<a href='https://docs.google.com/spreadsheets/d/1_NAxUAbaeVJyPgVNi8J2J6EpO_Bd4G0EEHFqJJAjFoo/edit#gid=0&range=C80'>Математика</a>\n{15 * ' '}Лекція\n{15 * ' '}Лютий О.І.\n\n" \
             f"{10 * ' '}({time_of_couple(4)})\n{15 * ' '}<a href='https://docs.google.com/spreadsheets/d/1_NAxUAbaeVJyPgVNi8J2J6EpO_Bd4G0EEHFqJJAjFoo/edit#gid=0&range=C84'>Математика</a>\n{15 * ' '}Практика\n{15 * ' '}Лютий О.І.\n\n" \



friday_nep = f"{10 * ' '}({time_of_couple(2)})\n{15 * ' '}<a href='https://docs.google.com/spreadsheets/d/1_NAxUAbaeVJyPgVNi8J2J6EpO_Bd4G0EEHFqJJAjFoo/edit#gid=0&range=C156'>Іноземна мова</a>\n{15 * ' '}Практика\n{15 * ' '}\n\n" \
             f"{10 * ' '}({time_of_couple(3)})\n{15 * ' '}<a href='https://docs.google.com/spreadsheets/d/1_NAxUAbaeVJyPgVNi8J2J6EpO_Bd4G0EEHFqJJAjFoo/edit#gid=0&range=C160'>Психологія та педагогіка</a>\n{15 * ' '}Практика\n{15 * ' '}Дубовик С.М.\n\n" \




saturday_par = "відпочивай краще"

saturday_nep = "відпочивай краще"

sunday_par = "відпочинок"

sunday_nep = "відпочинок"

par_week = [monday_par, tuesday_par, wednesday_par, thursday_par, friday_par, saturday_par, sunday_par]
nep_week = [monday_nep, tuesday_nep, wednesday_nep, thursday_nep, friday_nep, saturday_nep, sunday_nep]

count = 0
