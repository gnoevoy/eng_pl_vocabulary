import pandas as pd
import numpy as np
import random


def get_values(df, col, n1, n2):
    # pick up new random values
    new_values = df.query("is_passed == False")
    new_values_lst = random.choices(new_values[col].to_list(), k=n1)

    # update table
    df["is_passed"] = np.where(df[col].isin(new_values_lst), True, df["is_passed"])

    # select passed values
    passed_values = df.query("is_passed == True")
    passed_values_lst = random.choices(passed_values[col].to_list(), k=n2)

    return new_values_lst, passed_values_lst


def main():
    # Import CSV files
    words = pd.read_csv("data/words.csv")
    phrases = pd.read_csv("data/phrases.csv")

    new_words, passed_words = get_values(words, "word", 10, 10)
    new_phrases, passed_phrases = get_values(phrases, "phrase", 3, 3)

    # save changes to the CSV files
    words.to_csv("data/words.csv", index=False)
    phrases.to_csv("data/phrases.csv", index=False)

    print("New words:", new_words)
    print("Passed words:", passed_words)
    print("")
    print("New phrases:", new_phrases)
    print("Passed phrases:", passed_phrases)


if __name__ == "__main__":
    main()
