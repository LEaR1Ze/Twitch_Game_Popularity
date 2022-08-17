from turtle import title
import requests
import tkinter as tk
from tkinter import *
from logging import root
import json
import re


def deep():
    wwww = wr2.get()
    wwww2 = wr.get()
    wwww3 = wr3.get()
    url = "https://twitch-game-popularity.p.rapidapi.com/game"

    querystring = {
    "name":"{}".format(wwww2),
    "year":"{}".format(wwww),
    "month":"{}".format(wwww3)
    }
    headers = {
    "X-RapidAPI-Key": "0e07727357msh7cecd389cc3b85bp109d82jsne462fa0189c6",
	"X-RapidAPI-Host": "twitch-game-popularity.p.rapidapi.com"
    }   

    response = requests.request("GET", url, headers=headers, params=querystring)

    teor = response.json()
    for g in teor:
        Rank = g["Rank"]
        Game = g["Game"]
        Month = g["Month"]
        Year = g["Year"]
        Hours_watched = g["Hours_watched"]
        Hours_Streamed = g["Hours_Streamed"]
        Peak_viewers = g["Peak_viewers"]
        Peak_channels = g["Peak_channels"]
        Streamers = g["Streamers"]
        Avg_viewers = g["Avg_viewers"]
        Avg_channels = g["Avg_channels"]
        Avg_viewer_ratio = g["Avg_viewer_ratio"]

        if g["Rank"] is None:
            wr4.config(text="Error")
        else:
            wr4.insert('1.0',"Rank: {}\nGame: {}\nMonth: {}\nYear: {}\nHours_watched: {}\nHours_Streamed: {}\nPeak_viewers: {}\nPeak_channels: {}\nStreamers: {}\nAvg_viewers: {}\nAvg_channels: {}\nAvg_viewer_ratio: {}"
            .format(Rank, Game, Month, Year, Hours_watched, Hours_Streamed, Peak_viewers, Peak_channels, Streamers, Avg_viewers, Avg_channels,  Avg_viewer_ratio))

w = tk.Tk()
w.title("Популярность игр на Твиче")
w.geometry("800x600")
wrr = tk.Label(text="Название игры")
wrr.pack()

wr = tk.Entry()
wr.pack()

wr5 = tk.Label(text="Год в котором хотите увидеть статистику")
wr5.pack()

wr2 = tk.Entry()
wr2.pack()

wrr2 = Label(text="Месяц в котором хотите увидеть статистику")
wrr2.pack()

wr3 = tk.Entry()
wr3.pack()

wrr3 = tk.Label(text="Статистика по игре")
wrr3.pack()

wr4 = tk.Text()
wr4.pack()

wr6 = tk.Button(text="Увидить статистику",command=deep)
wr6.pack()

w.mainloop()

