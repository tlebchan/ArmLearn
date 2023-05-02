def get_progress_for_table():
    terms = []
    with open("./data/progress.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            term, definition, source = line.split(";")
            terms.append([cnt, term, definition])
            cnt += 1
    return terms


def write_progress(new_date, new_n):
    new_term_line = f"{new_date};{new_n};user"
    with open("./data/progress.csv", "r", encoding="utf-8") as f:
        existing_terms = [l.strip("\n") for l in f.readlines()]
        title = existing_terms[0]
        old_terms = existing_terms[1:]
    terms_sorted = old_terms + [new_term_line]
    terms_sorted.sort()
    new_terms = [title] + terms_sorted
    with open("./data/progress.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_terms))