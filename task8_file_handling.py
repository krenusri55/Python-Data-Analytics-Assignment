introduction = (
    "Hello! My name is Ananya.\n"
    "I am a Computer Science student.\n"
    "I am learning Python for Data Analytics."
)

with open("introduction.txt", "w", encoding="utf-8") as file:
    file.write(introduction)

with open("introduction.txt", "r", encoding="utf-8") as file:
    content = file.read()

print("Contents of introduction.txt:")
print(content)
