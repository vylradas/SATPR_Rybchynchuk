print("Work of Rybchynchuk Vladyslav AP-31")
print("Lab 7")
import copy
# Заданий профіль голосування 
votes = [ 
    (4, ['A', 'B', 'C', 'D']), 
    (4, ['A', 'C', 'D', 'B']), 
    (3, ['C', 'A', 'B', 'D']), 
    (9, ['B', 'C', 'A', 'D']), 
]  

def relative_majority(profile): 
    return max(profile[0][1], key=lambda x: sum(vote[0] for vote in profile if vote[1][0] == x)) 
 
def absolute_majority(profile):
    remaining_candidates = list(profile[0][1])  # Кандидати, які ще не вийшли з гри
    votes_required = sum(vote[0] for vote in profile) // 2 + 1  # Потрібна кількість голосів для перемоги
    
    while len(remaining_candidates) > 1:
        candidate_scores = {candidate: 0 for candidate in remaining_candidates}
        
        for vote in profile:
            for i, candidate in enumerate(remaining_candidates):
                if vote[1][0] == candidate:
                    candidate_scores[candidate] += vote[0]
                    break
        
        # Визначення переможця
        winner = min(candidate_scores, key=candidate_scores.get)
        
        if candidate_scores[winner] >= votes_required:
            return winner
        else:
            # Вибування переможця і перерозподіл голосів
            remaining_candidates.remove(winner)
            for vote in profile:
                if vote[1][0] == winner:
                    # Переведення голосів за вибувшого кандидата до інших залишившихся кандидатів
                    vote[1][0] = min(remaining_candidates, key=lambda x: candidate_scores[x])
                    
    return remaining_candidates[0]

def borda(profile):
    num_candidates = len(profile[0][1])
    scores = {candidate: 0 for candidate in profile[0][1]}

    for vote in profile:
        for i, candidate in enumerate(vote[1]):
            scores[candidate] += num_candidates - i - 1

    return max(scores, key=scores.get)

def condorcet(profile):
    winners = []
    for candidate in profile[0][1]:
        if all(candidate in vote[1][:2] for vote in profile):
            winners.append(candidate)

    if len(winners) == 1:
        return winners[0]
    elif len(winners) == 2:
        return winners
    else:
        return None  
 
def copeland(profile):
    scores = {candidate: 0 for candidate in profile[0][1]}
    defeated_count = {candidate: 0 for candidate in profile[0][1]}
    
    for i, candidate1 in enumerate(profile[0][1]):
        for j, candidate2 in enumerate(profile[0][1]):
            if i != j:
                for vote in profile:
                    if candidate1 in vote[1] and candidate2 in vote[1]:
                        if vote[1].index(candidate1) < vote[1].index(candidate2):
                            scores[candidate1] += 1
                            defeated_count[candidate2] += 1
                        elif vote[1].index(candidate1) > vote[1].index(candidate2):
                            scores[candidate2] += 1
                            defeated_count[candidate1] += 1

    winners = [candidate for candidate in scores if scores[candidate] == max(scores.values())]
    return winners, defeated_count

def simpson(profile):
    scores = {candidate: 0 for candidate in profile[0][1]}
    defeated_count = {candidate: 0 for candidate in profile[0][1]}

    for i, candidate1 in enumerate(profile[0][1]):
        for j, candidate2 in enumerate(profile[0][1]):
            if i != j:
                for vote in profile:
                    if candidate1 in vote[1] and candidate2 in vote[1]:
                        try:
                            if vote[1].index(candidate1) < vote[1].index(candidate2):
                                scores[candidate1] += 1
                                defeated_count[candidate2] += 1
                            elif vote[1].index(candidate1) > vote[1].index(candidate2):
                                scores[candidate2] += 1
                                defeated_count[candidate1] += 1
                        except ValueError:
                            # Ігноруємо помилку, якщо кандидат не знайдений в голосі
                            pass

    winners = [candidate for candidate in scores if scores[candidate] == max(scores.values())]
    return winners, defeated_count 

# Визначення переможців за різними методами 
winners = { 
    "Relative Majority": relative_majority(copy.deepcopy(votes)), 
    "Absolute Majority": absolute_majority(copy.deepcopy(votes)), 
    "Borda": borda(copy.deepcopy(votes)), 
    "Condorcet": condorcet(copy.deepcopy(votes)), 
    "Copeland": copeland(copy.deepcopy(votes)), 
    "Simpson": simpson(copy.deepcopy(votes)), 
} 

# Виведення переможців 
for method, winner in winners.items(): 
    print(f"{method}: {winner}")