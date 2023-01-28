names = ["Vasya", "Alice", "Petya", "Jenny", "Fedya", "Viola", "Mark", "Chris", "Margo", 'Kolya']
birthday_years = [1962, 1995, 2000, None, None, None, None, 1998, 2001, 1995]
genders = ["Male", "Female", "Male", "Female", "Male", None, None, None, None, 'Male']


def find_military(names, birthday_years, genders):
    lis = []
    undetected = []

    for i in range(len(names)):
        if birthday_years[i] == None or genders[i] == None:
            undetected.append([names[i]])
        elif genders[i] == 'Male' and (birthday_years[i] > 1991 and birthday_years[i] < 2004):
            lis.append([names[i]])
    return lis, undetected


print(find_military(names, birthday_years, genders))
