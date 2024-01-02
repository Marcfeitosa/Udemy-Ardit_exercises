filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in zip(filenames):
    file = open(f"{filename}", "w")
    file.write("Hello")
    