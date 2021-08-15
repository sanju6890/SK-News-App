from tkinter import *

import requests
import json
import webbrowser

root = Tk()
root.title("SK News App")
root.iconbitmap("app_icon.ico")
root.geometry("1080x720")
root.minsize(1080,720)
root.maxsize(1080,720)
root.configure(bg='tan1')


def india_news():
    list_box.delete(0,END)
    url="http://newsapi.org/v2/top-headlines?country=in&apiKey=3e33ba1948eb4504b47af11904512730"
    # creating url request
    news = requests.get(url) 
    # creating python object from json
    news_dict = json.loads(news.text)
    contents = news_dict['articles']
    list_box.insert(END,"INDIA NEWS...")
    i = 1
    for content in contents:
        headline = f"{i}. {content['title']}"
        list_box.insert(END,headline)
        # discription = content['description']
        # list_box.insert(END,discription)
        i = i+1

def health_news():
    list_box.delete(0,END)
    url = "http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=3e33ba1948eb4504b47af11904512730"
    # creating url request
    news = requests.get(url) 
    # creating python object from json
    news_dict = json.loads(news.text)
    contents = news_dict['articles']
    list_box.insert(END,"HEALTH NEWS...")
    i = 1
    for content in contents:
        headline = f"{i}. {content['title']}"
        list_box.insert(END,headline)
        # discription = content['description']
        # list_box.insert(END,discription)
        i = i+1

def science_news():
    list_box.delete(0,END)
    url="http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=3e33ba1948eb4504b47af11904512730"
    # creating url request
    news = requests.get(url) 
    # creating python object from json
    news_dict = json.loads(news.text)
    contents = news_dict['articles']
    list_box.insert(END,"SCIENCE NEWS...")
    i = 1
    for content in contents:
        headline = f"{i}. {content['title']}"
        list_box.insert(END,headline)
        # discription = content['description']
        # list_box.insert(END,discription)
        i = i+1

def tech_news():
    list_box.delete(0,END)
    url="http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=3e33ba1948eb4504b47af11904512730"
    # creating url request
    news = requests.get(url) 
    # creating python object from json
    news_dict = json.loads(news.text)
    contents = news_dict['articles']
    list_box.insert(END,"TECHNOLOGY NEWS...")
    i = 1
    for content in contents:
        headline = f"{i}. {content['title']}"
        list_box.insert(END,headline)
        # discription = content['description']
        # list_box.insert(END,discription)
        i = i+1

def enter_news():
    list_box.delete(0,END)
    url="http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=3e33ba1948eb4504b47af11904512730"
    # creating url request
    news = requests.get(url) 
    # creating python object from json
    news_dict = json.loads(news.text)
    contents = news_dict['articles']
    list_box.insert(END,"ENTERTAINMENT NEWS...")
    i = 1
    for content in contents:
        headline = f"{i}. {content['title']}"
        list_box.insert(END,headline)
        # discription = content['description']
        # list_box.insert(END,discription)
        i = i+1

def sports_news():
    list_box.delete(0,END)
    url="http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=3e33ba1948eb4504b47af11904512730"
    # creating url request
    news = requests.get(url) 
    # creating python object from json
    news_dict = json.loads(news.text)
    contents = news_dict['articles']
    list_box.insert(END,"SPORTS NEWS...")
    i = 1
    for content in contents:
        headline = f"{i}. {content['title']}"
        list_box.insert(END,headline)
        # discription = content['description']
        # list_box.insert(END,discription)
        i = i+1

def business_news():
    list_box.delete(0,END)
    url="http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=3e33ba1948eb4504b47af11904512730"
    # creating url request
    news = requests.get(url) 
    # creating python object from json
    news_dict = json.loads(news.text)
    contents = news_dict['articles']
    list_box.insert(END,"BUSINESS NEWS...")
    i = 1
    for content in contents:
        headline = f"{i}. {content['title']}"
        list_box.insert(END,headline)
        # discription = content['description']
        # list_box.insert(END,discription)
        i = i+1

def get_full_story():
    slug = list_box.get(ACTIVE)
    url=f'https://www.google.com/search?q={slug}'
    webbrowser.get().open(url)
    

# App's Header
header = Label(root, text='Get The Latest News Updates',bg="blue",fg="white",font=("Times", "21", "bold italic"),borderwidth=5, relief=SUNKEN)
header.pack(pady=10)

# List Box to display the news content
list_box= Listbox(root, bg="black", fg="yellow", font=("Times", "14", "italic"), relief = SUNKEN, borderwidth=10, width=110, height=20)
list_box.pack(pady=5)

# Control frame
frame=Frame(root, borderwidth = 5, bg = 'black', relief = SUNKEN)
frame.pack(pady=20)

india = Button(frame, text='India',bg="purple1",fg="white",font=("Times", "11", "bold"),borderwidth=5,width=12,command=india_news)
health = Button(frame, text='Health',bg="purple1",fg="white",font=("Times", "11", "bold"),borderwidth=5,width=12,command=health_news)
science = Button(frame, text='Science',bg="purple1",fg="white",font=("Times", "11", "bold"),borderwidth=5,width=12,command=science_news)
technology = Button(frame, text='Technology',bg="purple1",fg="white",font=("Times", "11", "bold"),borderwidth=5,width=12,command=tech_news)
entertainment = Button(frame, text='Entertainment',bg="purple1",fg="white",font=("Times", "11", "bold"),borderwidth=5,width=12,command=enter_news)
business = Button(frame, text='Business',bg="purple1",fg="white",font=("Times", "11", "bold"),borderwidth=5,width=12,command=business_news)
sports = Button(frame, text='Sports',bg="purple1",fg="white",font=("Times", "11", "bold"),borderwidth=5,width=12,command=sports_news)

# Position all the buttons in the control frame
india.grid(row=0, column=0, padx=10)
health.grid(row=0, column=1, padx=10)
science.grid(row=0, column=2, padx=10)
technology.grid(row=0, column=3, padx=10)
entertainment.grid(row=0, column=4, padx=10)
business.grid(row=0, column=5, padx=10)
sports.grid(row=0, column=6, padx=10)

button=Button(root, text='Get Full Story',bg="purple1",fg="white",font=("Times", "11", "bold"),borderwidth=5,command=get_full_story)
button.pack(pady=10)
# Copy Right Label
label = Label(root, text='SANJAY KUMAR (C) 2021',font=("Times", "11", "bold"),borderwidth=5)
label.pack(pady=10)

root.mainloop()