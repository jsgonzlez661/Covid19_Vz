#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Jose Gonzalez ~ All rights reserved. MIT license.
import os
from make_requests import *
from make_functions import *
from config import TOKEN
import telebot

bot = telebot.TeleBot(token=TOKEN, parse_mode=None)


# jsgonzlez661: Shows message welcome
@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg = "Te damos la bienvenida a este bot\nAqui podras obtener la informacion actualizada\nsobre el Coronavirus (COVID-19) en Venezuela\n/positivos - Numero de Casos Positivos\n/recuperados - Numero de Casos Recuperados\n/fallecidos - Numero de Personas Fallecidas\n/graficas - Muestra los tipos de grafica\n/edad - Muestra la distribución de casos por edad\n/estados - Muestra la distribución de casos por estados\n/genero - Muestra la distribución de casos por genero\n/lista - Muestra la lista de los estados con presencia confirmada de contagio"
    bot.reply_to(message, msg)


# jsgonzlez661: Shows case positive
@bot.message_handler(commands=['positivos'])
def Confirmed(message):
    msg = "Casos Positivos: " + case_confirmed
    bot.reply_to(message, msg)


# jsgonzlez661: Shows case recovery
@bot.message_handler(commands=['recuperados'])
def Recovered(message):
    msg = "Casos Recuperados: " + case_recovered
    bot.reply_to(message, msg)


# jsgonzlez661: Shows case deaths
@bot.message_handler(commands=['fallecidos'])
def Deaths(message):
    msg = "Fallecidos: " + case_deaths
    bot.reply_to(message, msg)


# jsgonzlez661: Shows graph for gender distribution
@bot.message_handler(commands=['genero'])
def ByGender_pie(message):
    bot.reply_to(message, 'Distribución por genero\nHombres: ' + str(distribuid_male) +
                 '\nMujeres: ' + str(distribuid_female) + '\n' +
                 DataGET.make_graph("pie", 'Distribución por genero', bygender))


# jsgonzlez661: Shows graph for age distribution
@bot.message_handler(commands=['edad'])
def ByGender_pie(message):
    bot.reply_to(message, 'Distribución por edad: \n' +
                 DataGET.make_graph("bar", 'Distribución por edad', byagerange))


# jsgonzlez661: Shows the list of chart types
@bot.message_handler(commands=['graficas'])
def ByGender_pie(message):
    msg = "Distribución por:\n/genero\n/edad\n/estados"
    bot.reply_to(message, msg)


# jsgonzlez661: Shows graph for states distribution
@bot.message_handler(commands=['estados'])
def ByGender_pie(message):
    bot.reply_to(message, 'Distribución por estados: \n' +
                 DataGET.make_graph("bar", 'Distribución por estados', bystate))


# jsgonzlez661: Shows the list of chart types
@bot.message_handler(commands=['lista'])
def echo_all(message):
    states = list_states(bystate)
    msg = ""
    for state in states:
        msg = msg + '/' + state + '\n'
    bot.reply_to(message, msg)


# jsgonzlez661: Shows the number of confirmed cases in the state
@bot.message_handler(commands=list_states(bystate))
def ByState(message):
    state = message.text
    value = find_state_data(bystate, state)
    msg = 'Casos Confirmados en ' + state + ': ' + str(value)
    bot.reply_to(message, msg)

while True: 
    try:
        bot.polling(none_stop=True)
    except telebot.apihelper.ApiException:
        bot.polling(none_stop=True)

