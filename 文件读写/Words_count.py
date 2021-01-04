def count_words(file_name):
    """计算一个文件大致包含多少单词"""
    try:
        with open(file_name) as file_project:
            contens = file_project.read()
    except FileNotFoundError:
        message = "Sorry, the file " + file_name + " does not exist."
        print(message)
    else:
        #计算文件中大致包含多少个单词
        words = contens.split()
        num_words = len(words)
        print("The file " + file_name + " has about " + str(num_words) + " words.")

file_names = ["Document\Article.txt","Document\Program.txt","Document\document.txt"]

for file_name in file_names:
    count_words(file_name)
