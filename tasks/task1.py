candidates = [
    {"name": "Vasya", "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores": 0},
    {"name": "Fedya", "scores": {"math": 33, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
    {"name": "Petya", "scores": {"math": 100, "russian_language": 100, "computer_science": 100}, "extra_scores": 4},
    {"name": "Roma", "scores": {"math": 92, "russian_language": 85, "computer_science": 64}, "extra_scores": 5},
    {"name": "Petuh", "scores": {"math": 93, "russian_language": 84, "computer_science": 64}, "extra_scores": 5},
    {"name": "Dubinin", "scores": {"math": 93, "russian_language": 48, "computer_science": 100}, "extra_scores": 5}
]

class Candidate(candidates):
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores



#
#
# def find_top_20(candidates):
#     for candidate in candidates:
#         candidate['summ_scores_main'] = candidate['scores']['math'] + candidate['scores']['russian_language'] + \
#                                         candidate['scores']['computer_science'] + candidate['extra_scores']
#         candidate['summ_scores_proff'] = candidate['scores']['math'] + candidate['scores']['computer_science']
#
#     set_list_main_scores = sorted(set([i['summ_scores_main'] for i in candidates]), reverse=True)
#     top = 1
#
#     result_list = []
#     for score in set_list_main_scores:
#         list_scores_check_duplicates = list(filter(lambda x: x['summ_scores_main'] == score, candidates))
#         if len(list_scores_check_duplicates) != 1:
#             list_scores_check_duplicates = sorted(list_scores_check_duplicates, key=lambda x: x['summ_scores_proff'],
#                                                   reverse=True)
#             for dict_candidat in list_scores_check_duplicates:
#                 dict_candidat['top_lvl'] = top
#                 top += 1
#                 result_list.append(dict_candidat)
#         else:
#             dict_candidat = list_scores_check_duplicates[0]
#             dict_candidat['top_lvl'] = top
#             top += 1
#             result_list.append(dict_candidat)
#
#     top_names = []
#     top_candidates_info = sorted(result_list, key=lambda x: x['top_lvl'], reverse=False)
#     for top_candidate in top_candidates_info:
#         top_names.append(top_candidate['name'])
#
#     return top_names[:20]
#
#
# print(find_top_20(candidates))
