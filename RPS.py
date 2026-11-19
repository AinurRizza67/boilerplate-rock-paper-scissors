# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def beat(move):    
    
    if move == "R":
        return "P"
    if move == "P":
        return "S"
    return "R"


def predict_quincy(my_history):

    choices = ["R", "R", "P", "P", "S"]
    return choices[(len(my_history) + 1) % 5]


def predict_kris(my_history):

    if len(my_history) == 0:
        return beat("R")
    return beat(my_history[-1])


def predict_mrugesh(my_history):
  
    seen = [""] + my_history
    last_ten = seen[-10:]
    most_frequent = max(set(last_ten), key=last_ten.count)
    if most_frequent == "":
        most_frequent = "S"
    return beat(most_frequent)


def predict_abbey(my_history):

    seen = ["R"] + my_history
    last = seen[-1]
    counts = {"R": 0, "P": 0, "S": 0}
    for i in range(len(seen) - 1):
        if seen[i] == last:
            counts[seen[i + 1]] += 1
    prediction = max(counts, key=counts.get)
    return beat(prediction)


predictors = [predict_quincy, predict_kris, predict_mrugesh, predict_abbey]


def player(prev_play, opponent_history=[], my_history=[]):

    if prev_play == "":
        opponent_history.clear()
        my_history.clear()
    else:
        opponent_history.append(prev_play)

    best_score = -1
    best_predictor = predict_quincy
    start = max(0, len(opponent_history) - 10)
    for predictor in predictors:
        score = 0
        for t in range(start, len(opponent_history)):
            if predictor(my_history[:t]) == opponent_history[t]:
                score += 1
        if score > best_score:
            best_score = score
            best_predictor = predictor

    guess = beat(best_predictor(my_history))
    my_history.append(guess)
    return guess

