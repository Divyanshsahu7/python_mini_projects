#Lerning adda project
import  webbrowser

class lerning:
	def __init__(self,language,playlist):
		self.language=language
		self.playlist=playlist

python = lerning("python", "https://www.youtube.com/watch?v=t2_Q2BRzeEE&list=PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0")
java = lerning("java","https://www.youtube.com/watch?v=ntLJmHOJ0ME&list=PLu0W_9lII9agS67Uits0UnJyrYiXhDS6q")
cplus = lerning("c++","https://www.youtube.com/watch?v=j8nAHeVKL08&list=PLu0W_9lII9agpFUAlPFe_VNSlXW5uE0YL")
php = lerning("php","https://www.youtube.com/watch?v=at19OmH2Bg4&list=PLu0W_9lII9aikXkRE0WxDt1vozo3hnmtR&pp=0gcJCXwEOCosWNin")
c = lerning("c","https://www.youtube.com/watch?v=7Dh73z3icd8&list=PLu0W_9lII9aiXlHcLx-mDH1Qul38wD3aR")


languages={"python":python , "java":java , "php":php , "c":c , "cplus":cplus }

print("++++++++++WELCOME TO LERNING ADAA++++++++++++")
user_language=input("Enter the language which you want  to study : ").lower()

if user_language in languages:
 link=languages[user_language].playlist
 print(f"your playlist is opening : {link}")
 webbrowser.open(link)
else:
        print("Sorry for in conveinence ! we add this language later.")
        print("Thank you for visting ! ")