raw_votes = ["Python", "python", "JavaScript", "PYTHON", "javaScript", "C++"]


clean_votes = set()

for raw in raw_votes:

    format = raw.strip().capitalize()

    clean_votes.add(format)


print("---CLean---")
print(list(clean_votes))
