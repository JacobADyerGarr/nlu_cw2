import numpy as np


def count_tokens(filename):
    raw_count = 0
    uniq_words = set()
    with (open(filename, 'r', encoding='utf-8')) as f:
        lines = f.readlines()
        for l in lines:
            l = l.strip('\n')
            l_split = l.split(" ")
            raw_count += len(l_split)
            l_set = set(l_split)
            uniq_words = uniq_words.union(l_set)
    return raw_count, len(list(uniq_words))


def count_unk(filename):
    word_counts = {}
    with (open(filename, 'r', encoding='utf-8')) as f:
        lines = f.readlines()
        for l in lines:
            l = l.strip('\n')
            words = l.split(" ")
            for w in words:
                if w not in word_counts:
                    word_counts[w] = 0
                word_counts[w] += 1

    unk_count = 0
    unk_words = []
    for w, count in word_counts.items():
        if count == 1:
            unk_count += 1
            unk_words.append(w)
    return unk_count, unk_words  # optional to return word list as well


def count_matches(file_en, file_de):
    uniq_words_en = set()
    uniq_words_de = set()

    _, unk_words_en = count_unk(file_en)
    _, unk_words_de = count_unk(file_de)

    unk_words_en = set(unk_words_en)
    unk_words_de = set(unk_words_de)

    with (open(file_en, 'r', encoding='utf-8')) as f_en:
        lines = f_en.readlines()
        for l in lines:
            l = l.strip('\n')
            l_split = l.split(" ")
            l_set = set(l_split)
            uniq_words_en = uniq_words_en.union(l_set)

    with (open(file_de, 'r', encoding='utf-8')) as f_de:
        lines = f_de.readlines()
        for l in lines:
            l = l.strip('\n')
            l_split = l.split(" ")
            l_set = set(l_split)
            uniq_words_de = uniq_words_de.union(l_set)

    uniq_words_en.difference_update(unk_words_en)
    uniq_words_de.difference_update(unk_words_de)

    matched_words = uniq_words_en.intersection(uniq_words_de)
    matches = len(list(matched_words))
    return matches, matched_words


def main():
    # print(count_tokens('europarl_raw/train.en'))
    # print(count_tokens('europarl_raw/train.de'))
    # print(count_unk('europarl_raw/train.en'))
    # print(count_unk('europarl_raw/train.de'))
    print(count_matches('europarl_raw/train.en', 'europarl_raw/train.de'))


if __name__ == '__main__':
    main()
