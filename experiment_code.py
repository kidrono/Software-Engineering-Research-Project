import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

tofes1 = pd.read_excel("tofes1.xlsx")
tofes2 = pd.read_excel("tofes2.xlsx")
tofes_num = 2
q1_lambda = "q1_lambda"
q1_lambda_level = "q1_lamda_level"
q2_def = "q2_def"
q2_def_level = "q2_def_level"
q1_def = "q1_def"
q1_def_level = "q1_def_level"
q2_lambda = "q2_lambda"
q2_lambda_level = "q2_lambda_level"
if tofes_num == 1:
    tofes = tofes1
    tofes_cols = [q1_def, q1_def_level, q2_lambda, q2_lambda_level]
else:
    tofes = tofes2
    tofes_cols = [q1_lambda, q1_lambda_level, q2_def, q2_def_level]

men = []
women = []
gender = [women, men]
for i in range(len(tofes["gender"])):
    if tofes["gender"][i] == "man":
        men.append(i)
    else:
        women.append(i)

beginners = []
intermediates = []
experienced = []
experience_level = [beginners, intermediates, experienced]
for i in range(len(tofes["experience level"])):
    if tofes["experience level"][i] == 1:
        beginners.append(i)
    elif tofes["experience level"][i] == 2:
        intermediates.append(i)
    elif tofes["experience level"][i] == 3:
        experienced.append(i)

py_beginners = []
py_intermediates = []
py_experienced = []
python_level = [py_beginners, py_intermediates, py_experienced]
for i in range(len(tofes["python level"])):
    if tofes["python level"][i] == 1:
        py_beginners.append(i)
    elif tofes["python level"][i] == 2:
        py_intermediates.append(i)
    elif tofes["python level"][i] == 3:
        py_experienced.append(i)


def mean_score_by_bio(bio, question_col):
    """
    the average "challenging rate" of some question by specific biographic type (men, women, experience level and more)
    :param bio: list of indexes of participants with the same biographic type
    :param question_col: the question we want to check
    :return: the average "challenging rate" of the participants in the question
    """
    total = 0
    summed = 0
    for i in bio:
        if tofes[question_col][i] >= 0:
            total += tofes[question_col][i]
            summed += 1
    if summed == 0:
        return -1
    return total / summed


def median_by_bio(bio, question_col):
    """
    the median "challenging rate" of some question by specific biographic type (men, women, experience level and more)
    :param bio: list of indexes of participants with the same biographic type
    :param question_col: the question we want to check
    :return: the median "challenging rate" of the participants in the question
    """
    return tofes[question_col][bio].median()


def success_by_bio(bio, question_col):
    """
    the success rate of some question by specific biographic type (men, women, experience level and more)
    :param bio: list of indexes of participants with the same biographic type
    :param question_col: the question we want to check
    :return: the success rate of the participants in the question
    """
    successes = 0
    fails = 0
    for i in bio:
        answer = tofes[question_col][i]
        if answer == 1:
            successes += 1
        elif answer == 0:
            fails += 1
    rate = successes / (successes + fails)
    return rate


def results_by_gender():
    """
    prints the results analysis by the gender of the participants
    :return: 2 lists of the final scores, first list for women and second for men.
    """
    print("women average experience:", mean_score_by_bio(women, "experience level"))
    print("women " + tofes_cols[0] + " success rate:", success_by_bio(women, tofes_cols[0]))
    print("women " + tofes_cols[0] + " score:", mean_score_by_bio(women, tofes_cols[1]))
    print("women " + tofes_cols[2] + " success rate:", success_by_bio(women, tofes_cols[2]))
    print("women " + tofes_cols[2] + " score:", mean_score_by_bio(women, tofes_cols[3]))

    print("men average experience:", mean_score_by_bio(men, "experience level"))
    print("men " + tofes_cols[0] + " success rate:", success_by_bio(men, tofes_cols[0]))
    print("men " + tofes_cols[0] + " score:", mean_score_by_bio(men, tofes_cols[1]))
    print("men " + tofes_cols[2] + " success rate:", success_by_bio(men, tofes_cols[2]))
    print("men " + tofes_cols[2] + " score:", mean_score_by_bio(men, tofes_cols[3]))

    return [success_by_bio(women, tofes_cols[2]), mean_score_by_bio(women, tofes_cols[3])], [
        success_by_bio(men, tofes_cols[2]), mean_score_by_bio(men, tofes_cols[3])]


def results_by_experience():
    """
    prints the results analysis by the experience level of the participants
    """
    for i in range(3):
        print("experience level", i + 1, tofes_cols[0] + " success rate:",
              success_by_bio(experience_level[i], tofes_cols[0]))
        print("experience level", i + 1, "average " + tofes_cols[0] + " score:",
              mean_score_by_bio(experience_level[i], tofes_cols[1]))
        print("experience level", i + 1, tofes_cols[2] + " success rate:",
              success_by_bio(experience_level[i], tofes_cols[2]))
        print("experience level", i + 1, "average " + tofes_cols[2] + " score:",
              mean_score_by_bio(experience_level[i], tofes_cols[3]))


def results_by_python():
    """
    prints the results analysis by the python level of the participants
    """
    for i in range(3):
        print("python level", i + 1, tofes_cols[0] + " success rate:",
              success_by_bio(experience_level[i], tofes_cols[0]))
        print("python level", i + 1, "average " + tofes_cols[0] + " score:",
              mean_score_by_bio(experience_level[i], tofes_cols[1]))
        print("python level", i + 1, tofes_cols[2] + " success rate:",
              success_by_bio(experience_level[i], tofes_cols[2]))
        print("python level", i + 1, "average " + tofes_cols[2] + " score:",
              mean_score_by_bio(experience_level[i], tofes_cols[3]))


def success_to_feel_correlation(bio, q_col, q_level_col):
    """
    calculates 2 values - the average "challenging rate" of the ones that answered correct and the
    the average "challenging rate" of the ones that answered wrong
    """
    successes = 0
    successes_score = 0
    fails = 0
    fails_score = 0
    for i in bio:
        answer = tofes[q_col][i]
        if answer == 1:
            successes += 1
            successes_score += tofes[q_level_col][i]
        elif answer == 0 and tofes[q_level_col][i] > 0:
            fails += 1
            fails_score += tofes[q_level_col][i]
    successes_rate = successes_score / successes
    fails_rate = fails_score / fails
    return successes_rate, fails_rate


def total_results():
    """
    prints all the results for all the different biographic types (gender, experience and python level)
    """
    print("total " + tofes_cols[0] + " success rate:", success_by_bio(range(len(tofes["gender"])), tofes_cols[0]))
    print("total " + tofes_cols[0] + " score:", mean_score_by_bio(range(len(tofes["gender"])), tofes_cols[1]))
    print("total " + tofes_cols[2] + " success rate:", success_by_bio(range(len(tofes["gender"])), tofes_cols[2]))
    print("total " + tofes_cols[2] + " score:", mean_score_by_bio(range(len(tofes["gender"])), tofes_cols[3]))

    print(success_to_feel_correlation(range(len(tofes["gender"])), tofes_cols[0], tofes_cols[1]))
    print(success_to_feel_correlation(range(len(tofes["gender"])), tofes_cols[2], tofes_cols[3]))
    return [success_by_bio(range(len(tofes["gender"])), tofes_cols[2]),
            mean_score_by_bio(range(len(tofes["gender"])), tofes_cols[3])]


total = total_results()
women_result, men_result = results_by_gender()


# results_by_experience()
# results_by_python()

def plot_gender_success():
    plt.bar(["women", "men"], [women_result[0], men_result[0]], color='blue', width=0.5)
    plt.ylabel("Success rate")
    plt.title('Success rate by gender:' + tofes_cols[2])
    plt.show()


def plot_gender_difficulty():
    plt.bar(["women", "men"], [women_result[1], men_result[1]], color='maroon', width=0.5)
    plt.ylabel("difficulty level")
    plt.title('difficulty by gender:' + tofes_cols[2])
    plt.show()


total_q2_lambda_success_rate = 0.6666666666666666
total_q2_lambda_difficulty = 4.266666666666667
q2_lambda_correlation_of_true = 3.6
q2_lambda_correlation_of_false = 5.6

total_q2_def_success_rate = 0.3333333333333333
total_q2_def_difficulty = 3.7058823529411766
q2_def_correlation_of_true = 3.3333333333333335
q2_def_correlation_of_false = 3.909090909090909


def plot_total_success():
    plt.bar(["lambda", "def"], [total_q2_lambda_success_rate, total_q2_def_success_rate], color='orange', width=0.5)
    plt.ylabel("Success rate")
    plt.title('Success rate by lambda or def:')
    plt.show()


def plot_total_difficulty():
    plt.bar(["lambda", "def"], [total_q2_lambda_difficulty, total_q2_def_difficulty], color='green', width=0.5)
    plt.ylabel("Difficulty level")
    plt.title('Difficulty by lambda or def')
    plt.show()


def box_plot_total_difficulty():
    new_df = pd.concat([tofes1, tofes2], axis=1, join='inner')
    new_df.boxplot(column=[q2_lambda_level, q2_def_level], grid=False)
    plt.title("Difficulty by lambda or def")
    plt.ylabel("Difficulty level")
    plt.show()


def box_plot_gender_difficulty_q2_lambda():
    women_data = tofes1[q2_lambda_level][women].dropna()
    men_data = tofes1[q2_lambda_level][men]
    data = [men_data, women_data]
    plt.boxplot(data)
    plt.title("Difficulty by gender - Q2 lambda")
    plt.xlabel("Men - Women")
    plt.ylabel("Difficulty level")
    # show plot
    plt.show()


def box_plot_gender_difficulty_q2_def():
    women_data = tofes2[q2_def_level][women].dropna()
    men_data = tofes2[q2_def_level][men].dropna()
    data = [men_data, women_data]
    plt.boxplot(data)
    plt.title("Difficulty by gender - Q2 def")
    plt.xlabel("Men - Women")
    plt.ylabel("Difficulty level")
    # show plot
    plt.show()


def box_plot_experience_difficulty_q2_lambda():
    beginners_data = tofes1[q2_lambda_level][beginners].dropna()
    intermediates_data = tofes1[q2_lambda_level][intermediates].dropna()
    experienced_data = tofes1[q2_lambda_level][experienced].dropna()
    data = [beginners_data, intermediates_data, experienced_data]
    plt.boxplot(data)
    plt.title("Difficulty by experience - Q2 lambda")
    plt.xlabel("Beginners - Intermediates - Experienced")
    plt.ylabel("Difficulty level")
    # show plot
    plt.show()


def box_plot_experience_difficulty_q2_def():
    beginners_data = tofes2[q2_def_level][beginners].dropna()
    intermediates_data = tofes2[q2_def_level][intermediates].dropna()
    experienced_data = tofes2[q2_def_level][experienced].dropna()
    data = [beginners_data, intermediates_data, experienced_data]
    plt.boxplot(data)
    plt.title("Difficulty by experience - Q2 def")
    plt.xlabel("Beginners - Intermediates - Experienced")
    plt.ylabel("Difficulty level")
    # show plot
    plt.show()


# box_plot_total_difficulty()
# plot_gender_difficulty()
# box_plot_experience_difficulty_q2_lambda()
# box_plot_gender_difficulty_q2_def()
box_plot_experience_difficulty_q2_def()
