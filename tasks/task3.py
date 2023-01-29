know_english = ["Vasya", "Jimmy", "Max", "Peter", "Eric", "Zoi", "Felix", 'petuh', 'roma']
sportsmen = ["Don", 'roma', "Peter", "Eric", "Jimmy", "Mark"]
more_than_20_years = ["Peter", "Julie", "Jimmy", "Mark", 'roma', "Max"]


def find_athlets(know_english, sportsmen, more_than_20_years):
    return list(set(know_english) & set(sportsmen) & set(more_than_20_years))


print(find_athlets(know_english, sportsmen, more_than_20_years))
