text = "I hate coding in this CSE303 course.CSE303 is very complicated"
count = 0
sub = "CSE303"
for i in range(len(text) - len(sub) + 1):
    if text[i:i+len(sub)] == sub:
        count += 1
print(f"'{sub}' appears {count} times.")