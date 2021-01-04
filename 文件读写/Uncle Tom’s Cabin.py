file_name =  "Document/Article.txt"

try:
    with open(file_name) as file_project:
        contents = file_project.read()

except FileNotFoundError:
    message = "Sorry, the file " + file_name + " does not exist."
    print(message)

else:
    # 计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print("The file " + file_name + " has about " + str(num_words) + " words.")
