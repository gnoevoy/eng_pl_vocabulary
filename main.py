from wordfreq import zipf_frequency
import pandas as pd


def get_words_with_score(eng_words_file, pl_words_file):
    # Open txt files and save as lists
    with open(f"data/{eng_words_file}.txt") as f:
        en = f.read().splitlines()

    with open(f"data/{pl_words_file}.txt") as f:
        pl = f.read().splitlines()
        pl[0] = "ten"

    # Get a frequency usage score for each eng word
    score = [zipf_frequency(word, "en", wordlist="best") for word in en]

    return en, pl, score


def get_csv_file(eng_words, pl_words, score):
    # Create pandas dataframe
    df = pd.DataFrame({"eng_word": eng_words, "pl_word": pl_words, "score": score})
    mask = (df["eng_word"].str.len() > 2) & (df["score"] > 4)
    df = df[mask].sample(frac=1).reset_index(drop=True)
    df["id"] = range(1, len(df) + 1)

    # Reorder columns and save as csv file
    df.loc[:, ["id", "eng_word", "pl_word", "score"]].to_csv("data/words.csv", index=False, encoding="utf-8-sig")
    print("CSV file created successfully.")


def main():
    eng_words, pl_words, score = get_words_with_score("eng_words", "pl_words")
    get_csv_file(eng_words, pl_words, score)


if __name__ == "__main__":
    main()
