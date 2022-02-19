def main(words):
    answer_dict = {}
    for i in words:
        if i in answer_dict:
            answer_dict[i] = answer_dict[i] + 1
        else:
            answer_dict[i] = 1
    return answer_dict

words = ["red", "fish", "blue", "fish", "green", "fish", "blue"]
print(main(words))
