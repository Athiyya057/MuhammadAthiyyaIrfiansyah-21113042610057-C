languages = ["Python", "Java", "C++", "JavaScript"]

print(languages)

print(languages[0])

languages[1] = "C"

languages.append("PHP")
print(languages)

languages.insert(1, "HTML")
print(languages)

languages.remove("PHP")
print(languages)

del languages[0]
print(languages)

languages.pop()
print(languages)

print(sorted(languages))

languages.sort()
print(languages)

languages.reverse()
print(languages)

print(len(languages))