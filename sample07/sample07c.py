subjects = ["国語","数字","料理","社会","英語"]
for i, subject in enumerate(subjects, start=1):
    print(f"{i}時限目:{subject}")

j = 1
for subject in subjects:
    print(f"{j}時限目:{subject}")
    j += 1