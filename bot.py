import random
import traceback
from telebot import types, TeleBot
import time
import threading
import config
import telebot

import os
from pymongo import MongoClient
import config
mainchat = -1001202711314
bot_username = 'horse_run_bot'
block = [787340171]
banchats = []
allow_bars = []

cazino_db = config.mongo_client.cazinobase
users = cazino_db.users
chats = cazino_db.chats
stats = cazino_db.stats
beecoins = cazino_db.beecoins

if stats.find_one({}) == None:
    stats.insert_one({})
    
#stats.update_one({},{'$set':{'id':100000}})

if beecoins.find_one({}) == None:
    beecoins.insert_one({'beecoins':50000})

beecoins.update_one({},{'$set':{'works':{'cleanready':True, 'barmenready':True, 'changelightready':True, 'fix_furniture':True}}})

bot = TeleBot(os.environ['cazino'])

for ids in chats.find({}):
    try:
        x = ids['notifications']
        y = ids['adminmode']
    except:
        chats.update_one({'id':ids['id']},{'$set':{'notifications':True, 'adminmode':False}})

users.update_many({},{'$set':{'working':False}})

def getbar():
    return {
        '0_0':[],
        '0_1':[],
        '0_2':[],
        '0_3':[],
        '0_4':[],
        '0_5':['chair'],
        '0_6':[],
        '0_7':[],
        '0_8':['enter'],
        '0_9':[],
        '0_10':[],
        '0_11':[],
        '0_12':[],
        '0_13':[],
        '0_14':[],
        '0_15':[],
        ################
        '1_0':[],
        '1_1':[],
        '1_2':[],
        '1_3':[],
        '1_4':[],
        '1_5':['table'],
        '1_6':[],
        '1_7':[],
        '1_8':[],
        '1_9':[],
        '1_10':[],
        '1_11':[],
        '1_12':['chair'],
        '1_13':['chair'],
        '1_14':['chair'],
        '1_15':[],
        ###################
        '2_0':[],
        '2_1':['chair'],
        '2_2':['table'],
        '2_3':['chair'],
        '2_4':[],
        '2_5':['chair'],
        '2_6':[],
        '2_7':[],
        '2_8':[],
        '2_9':[],
        '2_10':[],
        '2_11':['chair'],
        '2_12':['table'],
        '2_13':['table'],
        '2_14':['table'],
        '2_15':['chair'],
        #################
        '3_0':[],
        '3_1':[],
        '3_2':[],
        '3_3':[],
        '3_4':[],
        '3_5':[],
        '3_6':[],
        '3_7':[],
        '3_8':[],
        '3_9':[],
        '3_10':[],
        '3_11':[],
        '3_12':['chair'],
        '3_13':['chair'],
        '3_14':['chair'],
        '3_15':[],
        ##################################      
        '4_0':[],
        '4_1':[],
        '4_2':['chair'],
        '4_3':[],
        '4_4':[],
        '4_5':[],
        '4_6':[],
        '4_7':[],
        '4_8':[],
        '4_9':['chair'],
        '4_10':['table'],
        '4_11':[],
        '4_12':[],
        '4_13':[],
        '4_14':[],
        '4_15':[],
        ###########################
        '5_0':[],
        '5_1':['chair'],
        '5_2':['table'],
        '5_3':['chair'],
        '5_4':[],
        '5_5':[],
        '5_6':[],
        '5_7':[],
        '5_8':[],
        '5_9':[],
        '5_10':[],
        '5_11':[],
        '5_12':[],
        '5_13':[],
        '5_14':['chair'],
        '5_15':[],
        #########################
        '6_0':[],
        '6_1':[],
        '6_2':['chair'],
        '6_3':[],
        '6_4':[],
        '6_5':[],
        '6_6':['bartable'],
        '6_7':['bartable'],
        '6_8':['bartable'],
        '6_9':['bartable'],
        '6_10':['bartable'],
        '6_11':[],
        '6_12':[],
        '6_13':[],
        '6_14':['chair'],
        '6_15':['table'],
        ######################
        '7_0':[],
        '7_1':[],
        '7_2':[],
        '7_3':[],
        '7_4':[],
        '7_5':[],
        '7_6':['bartable'],
        '7_7':[],
        '7_8':[],
        '7_9':[],
        '7_10':['bartable'],
        '7_11':[],
        '7_12':[],
        '7_13':[],
        '7_14':['chair'],
        '7_15':[],
        ####################
        '8_0':['door'],
        '8_1':[],
        '8_2':[],
        '8_3':[],
        '8_4':['door'],
        '8_5':[],
        '8_6':['bartable'],
        '8_7':[],
        '8_8':['door'],
        '8_9':[],
        '8_10':['bartable'],
        '8_11':[],
        '8_12':['door'],
        '8_13':[],
        '8_14':[],
        '8_15':[],
         
    }

def createuser(user, coins = 300):
  return {
      'id':user.id,
      'name':user.first_name,
      'coins':coins,
      'reloadcoins':0,
      'lastbonus':0,
      'drinked':0,
      'bottle':False,
      'bar':{},
      'lvl':1,
      'lvlpoints':0,
      'exp':0,
      'strenght':1,
      'agility':1,
      'intelligence':1,
      'luck':1,
      'afk_until':0,
      'drunk':0,
      'supply':None,
      'food':None,
      'set':None,
      'current_supplies':{},
      'day_exp':80,
      'taken_exp':0,
      'reboot_time':0,
      'beecoins':0,
      'feed':100,
      'cooking_skill':1,
      'feelbad_until':0,
      'f_set':None,
      'current_foods':{},
      'now_cooking':False,
      'current_drink':None,
      'wait_ings':False,
      'govno':0,
      'cook':None,
      'portals':{'typical':0, 'rare':0, 'epic':0, 'legendary':0},
      'summons':{},
      'void_energy':0,
      'void_anomaly':0

  }

fightgames = {}

active = ['dec_armor', 'mana_void', 'shield_smash', 'rage', 'fireball', 'demon_inside', 'weakness', 'heal',
              'blood_ritual', 'speed_steal', 'mana_explosion', 'firegun', 'time_control', 'death_beam', 'void_blast', 'mana_destroy',
         'mana_drain', 'frost_arrow', 'wind_fury', 'light_charge']


    
npc_rares = {
    'typically':2,    # Количество скиллов
    'rare':3,
    'epic':4,
    'legendary':5
}

def getskillamount(x):
    return npc_rares[x]

def createboss():
    return {
        'maxhp':900,
        'hp':900,
        'maxmp':200,
        'mp':200,
        'mp_regen':3,        # За 1 секунду
        'dmg':100,
        'dmg_bonus':0,
        'disp':25,
        'armor':25,          # Блок урона от каждого удара
        'armor_bonus':0,
        'atkspeed_bonus':0,
        'atkspeed':3,         # Количество ходов в секунду равно (atkspeed / 10)
        'zombie':0,
        
    }
        

all_boss_skills = ['fat', 'fast', 'dec_armor', 'mana_void', 'steel_body', 'shield_smash', 'mana_steal', 'rage', 'gigant', 'antimage', 'fireball', 'mana_vampire',
'demon_inside', 'magic_shield', 'mage', 'magic_mirror', 'berserk', 'weakness', 'heal', 'blood_ritual', 'speed_steal', 'mana_explosion', 'death_revenge', 'zombie',
'vampire', 'warrior', 'titan_body', 'shield_fight', 'firegun', 'mana_eat', 'bower', 'mana_monster', 'time_control', 'death_beam', 'void_blast', 'ninja', 'big',
'mana_destroy', 'thorns', 'mana_block', 'killer', 'supremacy', 'fire_hands', 'regen', 'strong_hit', 'assasin', 'mana_drain', 'frost_arrow', 'wind_fury',
'pierce_claws', 'light_charge']

crafting = []

def getmanacost(x):
    return getskill(x, select = 'mana')

def getskill(x, select = 'name'):
    y = 'Неопознанный скилл'
    z = 'Неопознанное описание'
    i = 0
    if x == 'fat':
        y = 'Толстяк'
        z = 'Начало матча: +400 ХП, -1 манареген, -80 макс.мана'
    elif x == 'fast':
        y = 'Быстрый'
        z = 'Начало матча: +2 скорости атаки, -10 урона.'
    elif x == 'dec_armor':
        y = 'Уменьшение брони'
        z = 'Начало матча: +50 МП, +7 брони. Активный: тратит 45 МП и уменьшает броню соперника на 50 на 10 секунд. КД: 7 сек.'
        i = 45
    elif x == 'mana_void':
        y = 'Мана-взрыв'
        z = 'Начало матча: +1 манареген, +30 МП. Активный: тратит 120 МП и наносит сопернику урон, равный его максимальной мане. КД: 15 сек.'
        i = 120
    elif x == 'steel_body':
        y = 'Стальное тело'
        z = 'Начало матча: +25 брони.'
    elif x == 'shield_smash':
        y = 'Удар щитом'
        z = 'Активный: тратит 15 МП и наносит сопернику урон, равный (броня х3). КД: 6 сек.'
        i = 15
    elif x == 'mana_steal':
        y = 'Кража маны'
        z = 'Начало матча: +50 МП. Пассивная: каждую секунду ворует у соперника 1 маны.'
    elif x == 'rage':
        y = 'Бешенство'
        z = 'Активная: получает +3 скорости атаки, +50 урона и -15 брони на 10 секунд. КД 15 секунд.'
        i = 0
    elif x == 'gigant':
        y = 'Гигант'
        z = 'Начало матча: +1000 ХП, -150 МП, -1 скорость, +100 урона, +25 разброс урона. Пассивная: шанс 20% при ударе оглушить на 4 секунды.'
    elif x == 'antimage':
        y = 'Антимаг'
        z = 'Начало матча: количество МП становится равным 0. За каждую потерянную единицу маны получает +2 хп.'
    elif x == 'fireball':
        y = 'Огненный шар'
        z = 'Начало матча: +100 МП, +3 манареген. Активная: тратит 200 маны и наносит сопернику (МАКС.МП) урона. КД: 20 сек.'
        i = 200
    elif x == 'mana_vampire':
        y = 'Мана-вампир'
        z = 'Пассивная: когда соперник тратит ману, получает +1 хп за каждую потраченную единицу.'
    elif x == 'demon_inside':
        y = 'Внутренний демон'
        z = 'Активная: тратит 100 маны и получает +200 урона на одну атаку. Кд: 20 сек.'
        i = 100
    elif x == 'magic_shield':
        y = 'Магический щит'
        z = 'Пассивная: с шансом 20% отменяет заклинание соперника.'
    elif x == 'mage':
        y = 'Колдун'
        z = 'Пассивная: перезарядка и затраты маны на все скиллы -50%.'
    elif x == 'magic_mirror':
        y = 'Отражение магии'
        z = 'Пассивная: с шансом 20% тут же применяет скилл, который применил соперник. Не тратит ману.'
    elif x == 'berserk':
        y = 'Берсерк'
        z = 'Пассивная: любое влияние на ваш урон действует в 2 раза сильнее.'
    elif x == 'weakness':
        y = 'Ослабление'
        z = 'Начало матча: +50 МП. Активная: тратит 80 МП, соперник получает -50 к урону на 10 секунд. КД: 15 секунд.'
        i = 80
    elif x == 'heal':
        y = 'Лечение'
        z = 'Активная: тратит 40 МП и восстанавливает 250 ХП. КД: 10 сек.'
        i = 40
    elif x == 'blood_ritual':
        y = 'Кровавый ритуал'
        z = 'Начало матча: +150 ХП. Активная: тратит 20% от своего максимального ХП и наносит сопернику урон, равный (потраченные хп х2). КД: 13 сек.'
        i = 0
    elif x == 'speed_steal':
        y = 'Кража скорости'
        z = 'Активная: тратит 80 маны и ворует 1 скорости атаки у соперника на 15 секунд. КД: 22 сек.'
        i = 80
    elif x == 'mana_explosion':
        y = 'Мановыжигание'
        z = 'Начало матча: +100 МП. Наносит сопернику 1 урона за каждую его неиспользованную единицу маны. Тратит 100 маны. КД: 19 сек.'
        i = 100
    elif x == 'death_revenge':
        y = 'Посмертная месть'
        z = 'Пассивная: после смерти применяет 3 случайных заклинания. Если соперник умрет - побеждает.'
    elif x == 'zombie':
        y = 'Зомби'
        z = 'Пассивная: после первой смерти возрождается с 25% ХП.'
    elif x == 'vampire':
        y = 'Вампир'
        z = 'Пассивная: атаки крадут у соперника (15% от урона) жизней.'
    elif x == 'warrior':
        y = 'Воин'
        z = 'Начало матча: +60 урона, +50 разброс урона, -150 ХП, -5 брони.'
    elif x == 'titan_body':
        y = 'Титановое тело'
        z = 'Начало матча: +50 брони, -300 ХП.'
    elif x == 'shield_fight':
        y = 'Атака щитом'
        z = 'Пассивная: каждая атака отнимает у носителя 1 броню и наносит дополнительный урон, равный оставшейся броне.'
    elif x == 'firegun':
        y = 'Поток пламени'
        z = 'Активная: тратит 100 МП и наносит сопернику (6 х его броня) урона. КД: 10 сек.'
        i = 100
    elif x == 'mana_eat':
        y = 'Поедание маны'
        z = 'Пассивная: каждую секунду вы восстанавливаете ХП, равное (манареген х2).'
    elif x == 'bower':
        y = 'Лучник'
        z = 'Пассивная: +100 разброс урона, +100 МП, +25 урона.'
    elif x == 'mana_monster':
        y = 'Монстр из маны'
        z = 'Начало матча: +7 манареген, +400 МП. Пассивная: на заклинания вы тратите ХП, а при получении урона тратится МП вместо ХП. Если МП или ХП опустятся до 0, вы погибаете.'
    elif x == 'time_control':
        y = 'Контроль времени'
        z = 'Активная: тратит 70 МП и получает +20 к скорости на следующую секунду. КД: 6 сек.'
        i = 70
    elif x == 'death_beam':
        y = 'Луч смерти'
        z = 'Начало матча: 1 манареген. +50 МП. Активная: тратит 50 МП. Наносит 100 урона, восстанавливает столько же хп. КД: 23 сек.'
        i = 50
    elif x == 'void_blast':
        y = 'Взрыв пустоты'
        z = 'Активная: отнимает сопернику 35% ХП от его максимальных. Можно использовать 1 раз за бой.'
        i = 0
    elif x == 'ninja':
        y = 'Ниндзя'
        z = 'Пассивная: скорость атаки умножается на 2.'
    elif x == 'big':
        y = 'Огромный'
        z = 'Начало матча: ХП х2, МП х2, урон/1.7, -3 манареген.'
    elif x == 'mana_destroy':
        y = 'Уничтожение маны'
        z = 'Активная: тратит 60 МП и отнимает у соперника 60% от его максимального запаса МП. КД: 15 сек.'
        i = 60
    elif x == 'thorns':
        y = 'Шипы'
        z = 'Начало матча: -100 ХП. Пассивная: когда получает урон, имеет 20% шанс отменить его и перенаправить в соперника. Действует и на урон, нанесённый себе же.'
    elif x == 'mana_block':
        y = 'Манаблок'
        z = 'Начало матча: +1 манареген. Пассивная: когда получает урон, тратит (полученный урон) МП вместо ХП, пока имеется.'
    elif x == 'killer':
        y = 'Убийца'
        z = 'Начало матча: получает +100 урона, +1 скорость атаки, хп/2.'
    elif x == 'supremacy':
        y = 'Превосходство'
        z = 'Начало матча: +100 МП, +200 ХП, +1 скорость атаки, +1 манареген.'   
    elif x == 'fire_hands':
        y = 'Огненные атаки'
        z = 'Пассивная: каждая атака поджигает соперника на 3 секунды, что заставляет его терять 20 ХП и 20 МП каждую секунду. Длительность дебаффа: 3 сек. Огонь стакается.'    
    elif x == 'regen':
        y = 'Регенерация'
        z = 'Начало матча: +100 ХП. Пассивная: каждую секунду восстанавливает 5 ХП.' 
    elif x == 'strong_hit':
        y = 'Сокрушающий удар'
        z = 'Пассивная: каждая четвертая атака оглушает цель на 3 секунды.'
    elif x == 'assasin':
        y = 'Ассасин'
        z = 'Начало матча: урон увеличивается на значение, равное (количество брони х4). Броня становится равна 0.'    
    elif x == 'mana_drain':
        y = 'Высасывание маны'
        z = 'Активная: тратит 85 МП и высасывает из соперника 40% от его макс.МП. Цель получает урон, равный потерянной мане. КД: 14 сек.'    
        i = 85
    elif x == 'frost_arrow':
        y = 'Ледяная стрела'
        z = 'Активная: тратит 65 МП и наносит 75 урона за каждую единицу скорости соперника. Снижает скорость цели до 1 на 5 секунд. КД: 12 сек.'    
        i = 65
    elif x == 'wind_fury':
        y = 'Ураган'
        z = 'Активная: тратит 300 МП и наносит сопернику 500 урона. КД: 25 сек.'    
        i = 300
    elif x == 'pierce_claws':
        y = 'Пронзающие когти'
        z = 'Пассивная: атаки игнорируют броню соперника.'
    elif x == 'light_charge':
        y = 'Призыв молнии'
        z = 'Активная: тратит 10 маны и наносит сопернику 65 урона. КД: 1 сек.'  
        i = 10
        
    if select == 'name':
        return y
    elif select == 'description':
        return z
    elif select == 'mana':
        return i

#fat: +400 ХП, -1 mp_regen и -80 maxmp
#fast: +2 atkspeed, -20 dmg
#dec_armor: +50 maxmp. +7 armor. Тратит 45 МП и уменьшает броню соперника на 50 на 10 секунд. КД 7 секунд.
#mana_void: +1 mp_regen. +30 maxmp. Тратит 120 МП и наносит сопернику урон, равный его максимальной мане. КД 15 секунд.
#steel_body: +25 armor.
#shield_smash: Тратит 15 МП и наносит сопернику урон, равный (броня * 3).
#mana_steal: +50 maxmp. каждую секунду ворует у соперника 1 маны.
#rage: получает +3 скорости атаки, +50 урона и -15 брони на 10 секунд. КД 15 секунд.
#gigant: +1000 ХП, -150 maxmp, -1 atkspeed, +100 dmg, +25 disp, шанс 20% при ударе оглушить на 4 секунды.
#antimage: в начале боя мана становится 0. За каждую единицу маны получает +2 хп.
#fireball: +100 maxmp, +3 mp_regen. Тратит 200 маны и наносит сопернику (maxmp) урона. КД 20 секунд.
#mana_vampire: когда соперник тратит ману, получает +1 хп за каждую потраченную единицу.
#demon_inside: тратит 100 маны и получает +200 урона на одну атаку. КД 20 секунд.
#magic_shield: Пассивная. С шансом 20% отменяет заклинание соперника.
#mage: перезарядка и затраты маны на все скиллы -50%.
#magic_mirror: с шансом 15% тут же применяет скилл, который применил соперник. Не тратит ману.
#berserk: любой бонус урона, который действует на вас, действует в 3 раза сильнее.
#weakness: +50 maxmp. Тратит 80 МП. Соперник получает -50 к урону на 10 секунд. КД 15 секунд.
#heal: тратит 40 МП и восстанавливает 200 ХП. КД: 10 секунд.
#blood_ritual: тратит 20% от своего максимального ХП и наносит сопернику урон, равный (потраченные хп*1.5). КД: 13 секунд.
#speed_steal: Тратит 80 маны и ворует 1 скорости атаки у соперника на 15 секунд. КД: 22 секунд.
#mana_explosion: +100 maxmp. Наносит сопернику 1 урона за каждую его неиспользованную единицу маны. Тратит (нанесенный урон/2) маны. КД: 19 секунд.
#death_revenge: после смерти применяет 5 случайных заклинаний. Если соперник умрет - побеждает.
#zombie: после первой смерти возрождается с 25% ХП.
#vampire: атаки крадут у соперника (15% от урона) жизней.
#warrior: +60 dmg, +50 disp, -150 hp, -5 armor.
#titan_body: +50 armor, -300 hp.
#shield_fight: каждая атака отнимает у носителя 1 броню и наносит дополнительный урон, равный оставшейся броне.
#firegun: тратит 100 МП и наносит сопернику (6 * его броня) урона. КД: 10 сек.
#mana_eat: Каждую секунду вы восстанавливаете ХП, равное вашему восстановлению маны*2.
#bower: +100 disp, +100 MP, +25 dmg.
#mana_monster: +10 mp_regen, +400 mp. На заклинания вы тратите ХП, а при получении урона тратится мана вместо хп. Если мана или хп опустятся до 0, вы погибаете.
#time_control: Тратит 100 маны и получает +20 к скорости на следующую секунду. КД: 6 секунд.
#death_beam: +1 mp_regen. +50 mp. Тратит 50 маны. Наносит 100 урона, восстанавливает столько же хп. КД: 23 сек.
#void_blast: отнимает сопернику 35% ХП от его максимальных. 1 раз за бой.
#ninja: скорость атаки * 2.
#big: hp*2, mp*2, dmg/2, -3 mp_regen.
#mana_destroy: Тратит 50 маны и отнимает у соперника 60% от его максимального запаса маны. КД: 15 сек.


npc_name1 = ['нереальный', 'лютый', 'бешеный', 'адский', 'безумный', 'молниеносный', 'неотразимый', 'огромный', 'жирный', 'рьяный', 
            'дерзкий', 'совершенный', 'суровый', 'страшный', 'ужасающий', 'широкий', 'ядрёный', 'яростный', 'стойкий', 'солидный', 
            'сердитый', 'пожилой', 'смертоносный', 'буйствующий', 'свирепый', 'мстительный', 'убийственный']

npc_name2 = ['кобольд', 'мурлок', 'демон', 'абиссал', 'титан', 'вампир', 'паук', 'адский пёс', 'тролль', 'гном', 'хоббит', 'орк', 'энт',
            'гомункул', 'сатир', 'гнолл', 'кентавр', 'трогг', 'эфириал', 'ворген', 'бес', 'натрезим', 'дракон', 'магнатавр', 'анубисат',
            'эльф', 'оборотень', 'некрон', 'тифлинг']
    
npc_name3 = ['Брэндон', 'Верронн', 'Виктуар', 'Гарольд', 'Альберт', 'Гордон', 'Гудвин', 'Джерласс', 'Нуарт', 'Эйревелл', 'Жан', 'Иллирий',
            'Келлан', 'Кораллис', 'Люциус', 'Луи', 'Мэдисон', 'Квилгос', 'Меррин', 'Агиросион', 'Гомункулус', 'Харрин', 'Титаний', 'Симус',
             'Сехелис', 'Роджер', 'Рик', 'Магнус', 'Лагман', 'Одд', 'Торвальд', 'Эвен', 'Теодор', 'Берг', 'Моддан', 'Сурт', 'Хедин', 'Грим',
             'Релонтар', 'Неофилант', 'Арися', 'Ванесса', 'Иллиада', 'Рэм', 'Тирисс', 'Симус']

#users.update_many({},{'$set':{'portals':{'typical':0, 'rare':0, 'epic':0, 'legendary':0}, 'summons':{}}})

@bot.message_handler(commands=['brokenfight'])
def brokennf(m):
    if m.chat.id not in fightgames:
        bot.send_message(m.chat.id, 'В чате даже не идёт игра!')
        return
    game = fightgames[m.chat.id]
    
    if game['lastturnfight'] != None and time.time() - game['lastturnfight'] >= 15:
        del fightgames[game['id']]
        bot.send_message(m.chat.id, 'Удалил сломанную игру!')
    else:
        bot.send_message(m.chat.id, 'Ещё не прошло 15 секунд с прошлого хода, чтобы игра считалась сломанной!')
    
def portaltotext(x):
    y = 'Не определено'
    if x == 'typically':
        y = '⚪Обычный'
    elif x == 'rare':
        y = '🔵Редкий'
    elif x == 'epic':
        y = '🟣Эпический'
    elif x == 'legendary':
        y = '💠Легендарный'
    return y
        
#chats.update_many({},{'$set':{'realbar':createrealbar()}})

for ids in users.find({}):
    if ids['cook'] != None:
        users.update_one({'id':ids['id']},{'$set':{'cook.cooking':False}})

        
@bot.message_handler(commands=['chat_stats'])
def chatsssstats(m):
    if m.from_user.id not in [441399484, 376001833]:
        return
    i = 0
    for ids in chats.find({}):
        if ids['id'] < 0:
            i += 1
    bot.send_message(m.chat.id, 'Всего я знаю '+str(i)+' чатов!')
    
        
@bot.message_handler(commands=['book'])
def bookk(m):
    user = users.find_one({'id':m.from_user.id})
    if user == None:
        user = users.insert_one(createuser(m.from_user))
        user = users.find_one({'id':m.from_user.id})
    text = ''
    text1 = ''
    text2 = ''
    text3 = ''
    already = []
    for ids in user['summons']:
        for idss in user['summons'][ids]['skills']:
            if idss not in already:
                if len(text) > 2500:
                    text1 = text
                    text = ''
                if len(text) > 2500:
                    text2 = text
                    text = ''
                text += '*'+getskill(idss)+'*\n'+getskill(idss, select = 'description')+'\n\n'
                already.append(idss)
    try:
        bot.send_message(m.from_user.id, text, parse_mode = 'markdown')
        if text1 != '':
            bot.send_message(m.from_user.id, text1, parse_mode = 'markdown')
        if text2 != '':
            bot.send_message(m.from_user.id, text2, parse_mode = 'markdown')
            
        bot.send_message(m.chat.id, 'Отправил в ЛС.')
    except:
        bot.send_message(m.chat.id, 'Либо вы не открыли со мной личку, либо у вас нет ни одного босса!')
        bot.send_message(441399484, traceback.format_exc())

@bot.message_handler(commands=['summon'])
def summonn(m):
    user = users.find_one({'id':m.from_user.id})
    if user == None:
        user = users.insert_one(createuser(m.from_user))
        user = users.find_one({'id':m.from_user.id})
    nextt = False    
    kb = types.InlineKeyboardMarkup()
    for ids in user['portals']:
        if user['portals'][ids] > 0:
            kb.add(types.InlineKeyboardButton(text = portaltotext(ids)+'('+str(user['portals'][ids])+')', callback_data = 'summon_'+ids+'_'+str(m.from_user.id)))
            nextt = True
    if not nextt:
        bot.send_message(m.chat.id, 'У вас нет порталов для призыва босса!')
        return
    bot.send_message(m.chat.id, 'Выберите портал для призыва босса.', reply_markup = kb)
    
    
@bot.message_handler(commands=['give_stone'])
def givestoness(m):
    if m.from_user.id != 441399484:
        return
    try:
        users.update_one({'id':m.reply_to_message.from_user.id},{'$inc':{'portals.'+m.text.split(' ')[1]:int(m.text.split(' ')[2])}})
        bot.send_message(m.chat.id, 'Выдано '+m.text.split(' ')[2]+' камней "'+m.text.split(' ')[1]+'"!')
    except:
        bot.send_message(441399484, traceback.format_exc())
        bot.send_message(m.chat.id, 'Ошибка!')
                                                                         
    
@bot.message_handler(commands=['fighting'])
def fighting(m):
    if m.reply_to_message == None:
        bot.send_message(m.chat.id, 'Чтобы позвать кого-то на поединок боссов, нужно этой командой ответить на его сообщение!')
        return
    if m.reply_to_message.from_user.id == m.from_user.id:
        bot.send_message(m.chat.id, 'Нельзя бросать вызов самому себе!')
        return
    user = users.find_one({'id':m.from_user.id})
    if user == None:
        user = users.insert_one(createuser(m.from_user))
        user = users.find_one({'id':m.from_user.id})
    nextt = False
    for ids in user['summons']:
        nextt = True
    if not nextt:
        bot.send_message(m.chat.id, 'У вас даже нет боссов, чтобы бросать кому-то вызов!')
        return
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text = 'Принять вызов', callback_data = 'fighting_go_'+str(m.from_user.id)+'_'+str(m.reply_to_message.from_user.id)), types.InlineKeyboardButton(text = 'Отклонить вызов', callback_data = 'fighting_cancel_'+str(m.from_user.id)+'_'+str(m.reply_to_message.from_user.id)))
    bot.send_message(m.chat.id, m.reply_to_message.from_user.first_name+', принимаете ли вы вызов призывателя '+m.from_user.first_name+'?', reply_to_message_id = m.reply_to_message.message_id, reply_markup = kb)
    

@bot.message_handler(commands=['release'])
def releasse(m):
    user = users.find_one({'id':m.from_user.id})
    if user == None:
        user = users.insert_one(createuser(m.from_user))
        user = users.find_one({'id':m.from_user.id})
    if m.from_user.id != m.chat.id:
        bot.send_message(m.chat.id, 'Можно использовать только в личке!')
        return
    kb = types.InlineKeyboardMarkup()
    for ids in user['summons']:
        summon = user['summons'][ids]
        em = '?'
        if len(summon['skills']) == 2:
            x = portaltotext('typically')
        if len(summon['skills']) == 3:
            x = portaltotext('rare')
        if len(summon['skills']) == 4:
            x = portaltotext('epic')
        if len(summon['skills']) == 5:
            x = portaltotext('legendary')
        em = x[0]
        if len(summon['skills']) < 5:
            kb.add(types.InlineKeyboardButton(text = em+summon['name'], callback_data = 'fighting_release_'+str(user['summons'][ids]['id'])+'_'+str(user['id'])+'_'+str(m.chat.id)))
    bot.send_message(user['id'], 'Выберите босса, чтобы отпустить его обратно, в потусторонний мир. За это вы получите 🔮Энергию Пустоты, которая нужна для создания ☣Аномалии Пустоты. '+
                     'Расценки:\n⚪Обычный: 150🔮\n🔵Редкий: 250🔮\n🟣Эпический: 1000🔮\n💠Легендарный: 10000🔮', reply_markup = kb)

    
@bot.message_handler(commands=['release_legendary'])
def releasse(m):
    user = users.find_one({'id':m.from_user.id})
    if user == None:
        user = users.insert_one(createuser(m.from_user))
        user = users.find_one({'id':m.from_user.id})
    if m.from_user.id != m.chat.id:
        bot.send_message(m.chat.id, 'Можно использовать только в личке!')
        return
    kb = types.InlineKeyboardMarkup()
    for ids in user['summons']:
        summon = user['summons'][ids]
        em = '?'
        if len(summon['skills']) == 2:
            x = portaltotext('typically')
        if len(summon['skills']) == 3:
            x = portaltotext('rare')
        if len(summon['skills']) == 4:
            x = portaltotext('epic')
        if len(summon['skills']) == 5:
            x = portaltotext('legendary')
        em = x[0]
        if len(summon['skills']) == 5:
            kb.add(types.InlineKeyboardButton(text = em+summon['name'], callback_data = 'fighting_release_'+str(user['summons'][ids]['id'])+'_'+str(user['id'])+'_'+str(m.chat.id)))
    bot.send_message(user['id'], 'Выберите ЛЕГЕНДАРНОГО босса, чтобы отпустить его обратно, в потусторонний мир. За это вы получите 🔮Энергию Пустоты, которая нужна для создания ☣Аномалии Пустоты. '+
                     'Расценки:💠Легендарный: 10000🔮', reply_markup = kb)

    
@bot.message_handler(commands=['craft_anomaly'])
def craftanomally(m):
    user = users.find_one({'id':m.from_user.id})
    if user == None:
        user = users.insert_one(createuser(m.from_user))
        user = users.find_one({'id':m.from_user.id})
        
    if user['id'] not in crafting:
        bot.send_message(m.chat.id, 'Для крафта ☣Аномалии Пустоты вам нужно 2500🔮 Энергии Пустоты. Использовать её можно, чтобы '+
                         'поменять выбранный скилл босса на другой случайный. Для крафта ещё раз введите данную команду.')
        crafting.append(user['id'])
        threading.Timer(30, uncraft, args = [user['id']]).start()
    else:
        if user['void_energy'] >= 2500:
            users.update_one({'id':user['id']},{'$inc':{'void_energy':-2500, 'void_anomaly':1}})
            bot.send_message(m.chat.id, 'Вы поколдовали, добавили в кипящий котёл половину ананаса, щипотку океанской соли, распылили Энергию Пустоты - и у вас получилась одна ☣Аномалия Пустоты!')
        else:
            bot.send_message(m.chat.id, 'Не хватает Энергии Пустоты!')
            
            
@bot.message_handler(commands=['use_anomaly'])
def craftanomally(m):
    user = users.find_one({'id':m.from_user.id})
    if user == None:
        user = users.insert_one(createuser(m.from_user))
        user = users.find_one({'id':m.from_user.id})
        
    if m.from_user.id != m.chat.id:
        bot.send_message(m.chat.id, 'Можно использовать только в личке!')
        return
        
    if user['void_anomaly'] <= 0:
        bot.send_message(m.chat.id, 'Для этого нужна одна Аномалия Пустоты (/craft_anomaly)!')
        return
    
    kb = types.InlineKeyboardMarkup()
    for ids in user['summons']:
        summon = user['summons'][ids]
        em = '?'
        if len(summon['skills']) == 2:
            x = portaltotext('typically')
        if len(summon['skills']) == 3:
            x = portaltotext('rare')
        if len(summon['skills']) == 4:
            x = portaltotext('epic')
        if len(summon['skills']) == 5:
            x = portaltotext('legendary')
        em = x[0]
        summon = user['summons'][ids]
        kb.add(types.InlineKeyboardButton(text = em+summon['name'], callback_data = 'fighting_choiceboss_'+str(user['summons'][ids]['id'])+'_'+str(user['id'])))
    
    bot.send_message(m.chat.id, 'Выберите босса, у которого хотите заменить скилл. Затем выберите скилл, который хотите заменить. Новый скилл будет случайным (тем же самым стать не может)!', reply_markup = kb)
    
            
            
@bot.message_handler(commands=['jesus'])
def jeasiuuus(m):
    if m.from_user.id not in [376001833, 441399484]:
        bot.send_message(m.chat.id, 'Вы не Иисус!')
        return
    try:
        users.update_one({'id':m.reply_to_message.from_user.id},{'$set':{'drunk':0}})
        bot.send_message(m.chat.id, 'Иисус '+m.from_user.first_name+' превратил алкоголь у вас в крови в воду!', reply_to_message_id = m.reply_to_message.message_id)
    except:
        bot.send_message(m.chat.id, 'Выберите, кого хотите заисусить!')
        
        
def uncraft(id):
    try:
        crafting.remove(id)
    except:
        pass
        
    
    
@bot.callback_query_handler(func=lambda call: 'fighting' in call.data)
def fightsssss(call):
  try:
    user = users.find_one({'id':call.from_user.id})
    if user == None:
        return
    if call.data.split('_')[1] != 'choiceskill':
        if user['id'] != int(call.data.split('_')[3]):
            bot.answer_callback_query(call.id, 'Не ваше меню!')
            return
    
    option = call.data.split('_')[1]
    if option == 'cancel':
        medit(call.from_user.first_name+' отклоняет вызов!', call.message.chat.id, call.message.message_id)
        return
    elif option == 'go':
        nextt = False
        for ids in user['summons']:
            nextt = True
        if not nextt:
            medit(call.from_user.first_name+', у вас нет ни одного босса для состязания!', call.message.chat.id, call.message.message_id)
            return
        if call.message.chat.id in fightgames:
            medit('В этом чате уже идёт битва!', call.message.chat.id, call.message.message_id)
            return
        user2 = users.find_one({'id':int(call.data.split('_')[2])})
        fightgames.update(createfightgame(call.message.chat.id, int(call.data.split('_')[2]), int(call.data.split('_')[3]), user2['name'], user['name']))
        medit('Похоже, сейчас будет жарко... Посетители, помогите организовать ринг! Бой начинается!', call.message.chat.id, call.message.message_id)
        name2 = user2['name']
        bot.send_message(call.message.chat.id, user['name']+', '+name2+', выбирайте боссов для состязания у меня в ЛС. Если за 2 минуты вы этого не сделаете, поединок отменится!')
        
        try:
            kb = types.InlineKeyboardMarkup()
            for ids in user['summons']:
                summon = user['summons'][ids]
                em = '?'
                if len(summon['skills']) == 2:
                    x = portaltotext('typically')
                if len(summon['skills']) == 3:
                    x = portaltotext('rare')
                if len(summon['skills']) == 4:
                    x = portaltotext('epic')
                if len(summon['skills']) == 5:
                    x = portaltotext('legendary')
                em = x[0]
                kb.add(types.InlineKeyboardButton(text = em+user['summons'][ids]['name'], callback_data = 'fighting_select_'+str(user['summons'][ids]['id'])+'_'+str(user['id'])+'_'+str(call.message.chat.id)))
            bot.send_message(user['id'], 'Выберите бойца для состязания на ринге "'+call.message.chat.title+'"!', reply_markup = kb)
        
            kb = types.InlineKeyboardMarkup()
            for ids in user2['summons']:
                summon = user2['summons'][ids]
                em = '?'
                if len(summon['skills']) == 2:
                    x = portaltotext('typically')
                if len(summon['skills']) == 3:
                    x = portaltotext('rare')
                if len(summon['skills']) == 4:
                    x = portaltotext('epic')
                if len(summon['skills']) == 5:
                    x = portaltotext('legendary')
                em = x[0]
                kb.add(types.InlineKeyboardButton(text = em+user2['summons'][ids]['name'], callback_data = 'fighting_select_'+str(user2['summons'][ids]['id'])+'_'+str(user2['id'])+'_'+str(call.message.chat.id)))
            bot.send_message(user2['id'], 'Выберите бойца для состязания на ринге "'+call.message.chat.title+'"!', reply_markup = kb)
        except:
            bot.send_message(call.message.chat.id, 'А, нет... Кто-то из вас не открыл ЛС со мной! Отменяю поединок.')
            bot.send_message(441399484, traceback.format_exc())
            del fightgames[call.message.chat.id]
            return
        game = fightgames[call.message.chat.id]
        t = threading.Timer(120, endselect, args = [game])
        t.start()
        game['choicetimer'] = t
        
    elif option == 'select':
        game = fightgames[int(call.data.split('_')[4])]
        if call.from_user.id != game['user1'] and call.from_user.id != game['user2']:
            medit('Вас нет в этой игре!', call.message.chat.id, call.message.message_id)
            return
        if game['started']:
            medit('Игра уже началась!', call.message.chat.id, call.message.message_id)
            return
        boss = call.data.split('_')[2]
        bs = None
        for ids in user['summons']:
            if str(user['summons'][ids]['id']) == str(boss):
                bs = user['summons'][ids]
        if bs == None:
            bot.answer_callback_query(call.id, 'У вас нет этого босса!')
            return
        else:
            if call.from_user.id == game['user1']:
                us = '1'
            else:
                us = '2'
            game['fighter'+us] = bs
            medit('Вы успешно выбрали босса "'+bs['name']+'"!', call.message.chat.id, call.message.message_id)
            checkfightready(game)
            
    elif option == 'release':
        boss = call.data.split('_')[2]
        bs = None
        for ids in user['summons']:
            if str(user['summons'][ids]['id']) == str(boss):
                bs = user['summons'][ids]
        if bs == None:
            bot.answer_callback_query(call.id, 'У вас нет этого босса!')
            return
        
        summon = bs
        em = '?'
        if len(summon['skills']) == 2:
            x = portaltotext('typically')
            energy = 150
        if len(summon['skills']) == 3:
            x = portaltotext('rare')
            energy = 250
        if len(summon['skills']) == 4:
            x = portaltotext('epic')
            energy = 1000
        if len(summon['skills']) == 5:
            x = portaltotext('legendary')
            energy = 10000
        em = x[0]
        
        users.update_one({'id':user['id']},{'$unset':{'summons.'+str(bs['id']):1}})
        users.update_one({'id':user['id']},{'$inc':{'void_energy':energy}})
        medit('Выбран босс: '+bs['name']+'.', call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'Вы отпустили босса '+bs['name']+' обратно в его мир... Из открывшегося портала вы получили '+str(energy)+'🔮.')
        
    elif option == 'choiceboss':
        bs = None
        for ids in user['summons']:
            if str(user['summons'][ids]['id']) == call.data.split('_')[2]:
                bs = user['summons'][ids]
        if bs == None:
            medit('У вас нет этого босса!', call.message.chat.id, call.message.message_id)
            
        kb = types.InlineKeyboardMarkup()
        for ids in bs['skills']:
            kb.add(types.InlineKeyboardButton(text = getskill(ids), callback_data = 'fighting_choiceskill_'+str(bs['id'])+' '+ids+' '+str(user['id'])))
        medit('Выберите скилл для изменения его на другой случайный. Выбранный босс: '+bs['name']+'.', call.message.chat.id, call.message.message_id, reply_markup = kb)
        
    elif option == 'choiceskill':
        bb = call.data.split('_')[2].split(' ')[0]
        
        bs = None
        for ids in user['summons']:
            if str(user['summons'][ids]['id']) == bb:
                bs = user['summons'][ids]
        if bs == None:
            medit('У вас нет этого босса!', call.message.chat.id, call.message.message_id)
            
        skill = call.data.split(' ')[1]
        if skill not in bs['skills']:
            print(bs['skills'])
            print(skill)
            medit('У этого босса нет данного скилла!', call.message.chat.id, call.message.message_id)
            return
        
        if user['void_anomaly'] <= 0:
            medit('У вас нет Аномалий Пустоты!', call.message.chat.id, call.message.message_id)
            return
        
        new_skill = random.choice(all_boss_skills)
        while new_skill in bs['skills']:
            new_skill = random.choice(all_boss_skills)
        users.update_one({'id':user['id']},{'$pull':{'summons.'+str(bs['id'])+'.skills': skill}})
        users.update_one({'id':user['id']},{'$push':{'summons.'+str(bs['id'])+'.skills': new_skill}})
        users.update_one({'id':user['id']},{'$inc':{'void_anomaly':-1}})
        medit('Вы вызвали босса, разбили аномалию пустоты и произнесли заклинание... Его скилл "'+getskill(skill)+'" поменялся на "'+getskill(new_skill)+'"!', call.message.chat.id, call.message.message_id)
        
        
  except:
    bot.send_message(441399484, traceback.format_exc())
           


def endselect(game):
    try:
        bot.send_message(game['id'], 'Время выбора бойцов вышло! Удаляю игру.')
        del fightgames[game['id']]
    except:
        bot.send_message(441399484, traceback.format_exc())
    

def checkfightready(game):
    if game['fighter1'] != None and game['fighter2'] != None:
        game['choicetimer'].cancel()
        threading.Timer(random.randint(1, 40)/10, startfightgame, args = [game]).start()
        
    else:
        pass

def createfightgame(gameid, user1, user2, user1name, user2name):
    return {gameid:{
        'id':gameid,
        'user1':user1,
        'user1name':user1name,
        'user2':user2,
        'user2name':user2name,
        'fighter1':None,
        'fighter2':None,
        'started':False,
        'msg':None,
        'turn':1,
        'timer':2,     # раз во сколько секунд обновляется игра
        'choicetimer':None,
        'spellids':0,
        'dmgtaken1':0,
        'dmgtaken2':0,
        'text':'',
        'starttime':time.time(),
        'lastturnfight':time.time()
    }
           }

        


def getmessage(game):
    text = ''
    f1 = game['fighter1']
    f2 = game['fighter2']
    text += 'Босс "'+f1['name']+'" ('+game['user1name']+'):\n'
    text += '  ♥'+str(f1['hp'])+'/'+str(f1['maxhp'])+'\n'
    text += '  💧'+str(f1['mp'])+'/'+str(f1['maxmp'])+' (🔼'+str(f1['mp_regen'])+')\n'
    text += '  🥊'+str(f1['dmg']+f1['dmg_bonus'])+' (🎲'+str(f1['disp'])+')\n'
    text += '  🛡'+str(f1['armor']+f1['armor_bonus'])+'\n'
    spd = f1['atkspeed']+f1['atkspeed_bonus']
    for ids in f1['set_speed']:
        if f1['set_speed'][ids]['duration'] > 0:
            spd = f1['set_speed'][ids]['bonus']
    if 'ninja' in f1['skills']:
        spd = spd*2   
    text += '  🤺'+str(spd)+'\n'
    if game['dmgtaken1'] > 0:
        text += '  💔-'+str(game['dmgtaken1'])+'\n'
    elif game['dmgtaken1'] < 0:
        text += '  💚+'+str(game['dmgtaken1'])[1:]+'\n'
    if f1['stunned'] > 0:
        text += '  🌀\n'
    fire = False
    for ids in f1['fire_damage']:
        if f1['fire_damage'][ids]['duration'] >= 1:
            fire = True
    if fire:
        text += '  🔥\n'
        
    text += '\n'
    text += 'Босс "'+f2['name']+'" ('+game['user2name']+'):\n'
    text += '  ♥'+str(f2['hp'])+'/'+str(f2['maxhp'])+'\n'
    text += '  💧'+str(f2['mp'])+'/'+str(f2['maxmp'])+' (🔼'+str(f2['mp_regen'])+')\n'
    text += '  🥊'+str(f2['dmg']+f2['dmg_bonus'])+' (🎲'+str(f2['disp'])+')\n'
    text += '  🛡'+str(f2['armor']+f2['armor_bonus'])+'\n'
    spd = f2['atkspeed']+f2['atkspeed_bonus']
    for ids in f2['set_speed']:
        if f2['set_speed'][ids]['duration'] > 0:
            spd = f2['set_speed'][ids]['bonus']
    if 'ninja' in f2['skills']:
        spd = spd*2   
    text += '  🤺'+str(spd)+'\n'
    if game['dmgtaken2'] > 0:
        text += '  💔-'+str(game['dmgtaken2'])+'\n'
    elif game['dmgtaken2'] < 0:
        text += '  💚+'+str(game['dmgtaken2'])[1:]+'\n'
    if f2['stunned'] > 0:
        text += '  🌀\n'
    fire = False
    for ids in f2['fire_damage']:
        if f2['fire_damage'][ids]['duration'] >= 1:
            fire = True
    if fire:
        text += '  🔥\n'
        
    text += '\n'
    text += '⏲: '+str(game['turn'])+' сек.'
    return text
    
    
    

def startfightgame(game):
  try:
    if game['started'] == True:
        return
    game['started'] = True
    bot.send_message(441399484, str(game['fighter1']['name']))
    bot.send_message(441399484, str(game['fighter2']['name']))
        
    threading.Timer(game['timer'], next_turn_fight, args = [game]).start()
    
    game['fighter1'].update({'speedpoints':1, 'stunned':0, 'spend_mp':0, 'do_dmg':0, 'buff_armor':{}, 'buff_damage':{}, 'buff_speed':{},
                            'cds':{}, 'nexthits_dmg':{}, 'lost_armor':0, 'fire_damage':{}, 'hits_until_stun':3, 'set_speed':{}})
    
    game['fighter2'].update({'speedpoints':1, 'stunned':0, 'spend_mp':0, 'do_dmg':0, 'buff_armor':{}, 'buff_damage':{}, 'buff_speed':{},
                            'cds':{}, 'nexthits_dmg':{}, 'lost_armor':0, 'fire_damage':{}, 'hits_until_stun':3, 'set_speed':{}})
    
    fighters = [game['fighter1'], game['fighter2']]
    for ids in fighters:
        cf = ids
        if 'fat' in cf['skills']:
            cf['hp'] += 400
            cf['maxhp'] += 400
            cf['mp_regen'] -= 1
            cf['maxmp'] -= 80
            cf['mp'] -= 80
            
        if 'fast' in cf['skills']:
            cf['atkspeed'] += 2
            cf['dmg'] -= 10
            if 'berserk' in cf['skills']:
                cf['dmg'] -= 10
        
        if 'dec_armor' in cf['skills']:
            cf['maxmp'] += 50
            cf['mp'] += 50
            cf['armor'] += 7
            
        if 'mana_void' in cf['skills']:
            cf['mp_regen'] += 1
            cf['maxmp'] += 30
            cf['mp'] += 30
            
        if 'steel_body' in cf['skills']:
            cf['armor'] += 25
        
        if 'mana_steal' in cf['skills']:
            cf['maxmp'] += 50
            cf['mp'] += 50
            
        if 'gigant' in cf['skills']:
            cf['hp'] += 1000
            cf['maxhp'] += 1000
            cf['maxmp'] -= 150
            cf['mp'] -= 150
            cf['atkspeed'] -= 1
            cf['dmg'] += 100
            if 'berserk' in cf['skills']:
                cf['dmg'] += 100
            cf['disp'] += 25
  
        if 'fireball' in cf['skills']:
            cf['maxmp'] += 100
            cf['mp'] += 100
            cf['mp_regen'] += 3
            
        if 'weakness' in cf['skills']:
            cf['maxmp'] += 50
            cf['mp'] += 50
            
        if 'blood_ritual' in cf['skills']:
            cf['maxhp'] += 150
            cf['hp'] += 150
            
        if 'mana_explosion' in cf['skills']:
            cf['maxmp'] += 100
            cf['mp'] += 100
            
        if 'zombie' in cf['skills']:
            cf['zombie'] += 1
            
        if 'warrior' in cf['skills']:
            cf['dmg'] += 60
            if 'berserk' in cf['skills']:
                cf['dmg'] += 60
            cf['disp'] += 50
            cf['hp'] -= 150
            cf['maxhp'] -= 150
            cf['armor'] -= 5
            
        if 'titan_body' in cf['skills']:
            cf['armor'] += 50
            cf['hp'] -= 300
            cf['maxhp'] -= 300
            
        if 'bower' in cf['skills']:
            cf['disp'] += 100
            cf['mp'] += 100
            cf['maxmp'] += 100
            cf['dmg'] += 25
            
        if 'mana_monster' in cf['skills']:
            cf['mp_regen'] += 7
            cf['mp'] += 400
            cf['maxmp'] += 400
            
        if 'death_beam' in cf['skills']:
            cf['mp_regen'] += 1
            cf['mp'] += 50
            cf['maxmp'] += 50
            
        if 'big' in cf['skills']:
            cf['hp'] = cf['hp']*2
            cf['maxhp'] = cf['maxhp']*2
            cf['mp'] = cf['mp']*2
            cf['maxmp'] = cf['maxmp']*2
            
            coef = 1.5
            if 'berserk' in cf['skills']:
                coef = coef*2
            cf['dmg'] = int(cf['dmg']/coef)
            cf['mp_regen'] -= 3
            
        if 'antimage' in cf['skills']:
            cf['hp'] += (cf['maxmp']*2)
            cf['maxhp'] += (cf['maxmp']*2)
            cf['maxmp'] = 0
            cf['mp'] = 0
            
        if 'thorns' in cf['skills']:
            cf['hp'] -= 100
            cf['maxhp'] -= 100
            
        if 'mana_block' in cf['skills']:
            cf['mp_regen'] += 1
            
        if 'killer' in cf['skills']:
            cf['dmg'] += 100
            if 'berserk' in cf['skills']:
                cf['dmg'] += 100
            cf['atkspeed'] += 1
            cf['hp'] = int(cf['hp']/2)
            cf['maxhp'] = int(cf['maxhp']/2)
            
        if 'supremacy' in cf['skills']:
            cf['maxmp'] += 100
            cf['mp'] += 100
            cf['hp'] += 200
            cf['maxhp'] += 200
            cf['atkspeed'] += 1
            cf['mp_regen'] += 1
            cf['atkspeed'] += 1
            
        if 'regen' in cf['skills']:
            cf['hp'] += 100
            cf['maxhp'] += 100
            
        if 'assasin' in cf['skills']:
            cf['dmg'] += (4*cf['armor'])
            if 'berserk' in cf['skills']:
                cf['dmg'] += (4*cf['armor'])*1
            cf['armor'] = 0

    msg = bot.send_message(game['id'], getmessage(game))
    game['msg'] = msg
  except:
    bot.send_message(441399484, traceback.format_exc())
            
    
def next_turn_fight(game):
  try:
    game['lastturnfight'] = time.time()
    f1 = game['fighter1']
    f2 = game['fighter2']
    
    f1['mp'] += f1['mp_regen']
    if f1['mp'] > f1['maxmp']:
        f1['mp'] = f1['maxmp']
    f2['mp'] += f2['mp_regen']
    if f2['mp'] > f2['maxmp']:
        f2['mp'] = f2['maxmp']
        
    units = []
    units.append(f1)
    units.append(f2)
    for ids in units:
        f1 = ids
        speed = 0
        speed += (f1['atkspeed'] + f1['atkspeed_bonus'])/10
        
        for ids in f1['set_speed']:
            if f1['set_speed'][ids]['duration'] > 0:
                speed = f1['set_speed'][ids]['bonus']
                f1['set_speed'][ids]['duration'] -= 1
                
        if 'ninja' in f1['skills']:
            speed = speed*2
        if f1['stunned'] <= 0:
            f1['speedpoints'] += speed
            
        if f1['stunned'] <= 0:
            while f1['speedpoints'] >= 1:
                f1['speedpoints'] -= 1
                get_turn(game, f1)
        
        
    threading.Timer(game['timer'], end_turn_fight, args = [game]).start()
  except:
    bot.send_message(441399484, traceback.format_exc())
            
    
def end_turn_fight(game):
  try:
    units = [game['fighter1'], game['fighter2']]
    dead = []
    
    for ids in units:
        cf = ids
        if cf['id'] == game['fighter1']['id']:
            target = game['fighter2']
        else:
            target = game['fighter1']
        cf['armor_bonus'] = 0
        cf['dmg_bonus'] = 0
        cf['atkspeed_bonus'] = 0
    mdt = False
    for ids in units:
        cf = ids
        if cf['id'] == game['fighter1']['id']:
            target = game['fighter2']
            enm = '2'
            me = '1'
        else:
            target = game['fighter1']
            enm = '1'
            me = '2'
        cf['stunned'] -= 1
        #####################
        mp = cf['spend_mp']
        dmg = cf['do_dmg']
        ####################
        
        if 'regen' in target['skills']:
            dmg -= 5
        
        for ids in target['fire_damage']:
            if target['fire_damage'][ids]['duration'] >= 1:
                dmg += target['fire_damage'][ids]['bonus']
                target['mp'] -= target['fire_damage'][ids]['bonus']
                target['fire_damage'][ids]['duration'] -= 1
                
        if 'mana_block' in target['skills']:
            mana_block = dmg
            if target['mp'] < mana_block:
                mana_block = target['mp']
            target['mp'] -= mana_block
            dmg -= mana_block
        if 'mana_monster' not in cf['skills']:
            cf['mp'] -= mp
        else:
            cf['hp'] -= mp
        
        cf['spend_mp'] = 0
        if 'mana_vampire' in target['skills']:
            target['hp'] += cf['spend_mp']
            game['dmgtaken'+enm] -= cf['spend_mp']
            
        if cf['mp'] < 0:
            cf['mp'] = 0

        if 'thorns' in target['skills'] and random.randint(1, 100) <= 20:
            if 'mana_monster' not in cf['skills']:
                cf['hp'] -= dmg
            else:
                cf['mp'] -= dmg
            game['dmgtaken'+me] += dmg
            dmg = 0
            game['text'] += '💢'+cf['name']+' наносит урон, но шипы соперника блокируют его и возвращают атакующему!\n'
            
        if 'mana_monster' not in target['skills']:
            target['hp'] -= dmg
        else:
            target['mp'] -= dmg
        if cf['do_dmg'] != 0:
            mdt = True
        game['dmgtaken'+enm] += dmg
        cf['do_dmg'] = 0
        for ids in cf['buff_armor']:
            if cf['buff_armor'][ids]['duration'] >= 1:
                cf['armor_bonus'] += cf['buff_armor'][ids]['bonus']
                cf['buff_armor'][ids]['duration'] -= 1
                
        for ids in cf['buff_damage']:
            if cf['buff_damage'][ids]['duration'] >= 1:
                cf['dmg_bonus'] += cf['buff_damage'][ids]['bonus']
                cf['buff_damage'][ids]['duration'] -= 1
                
        for ids in cf['buff_speed']:
            if cf['buff_speed'][ids]['duration'] >= 1:
                cf['atkspeed_bonus'] += cf['buff_speed'][ids]['bonus']
                cf['buff_speed'][ids]['duration'] -= 1
                
        for ids in cf['cds']:
            cf['cds'][ids] -= 1  
            
        if 'mana_eat' in cf['skills']:
            cf['hp'] += (cf['mp_regen']*2)
            
        cf['armor'] -= cf['lost_armor']
        cf['lost_armor'] = 0
        if cf['hp'] > cf['maxhp']:
            cf['hp'] = cf['maxhp']
        if cf['mp'] > cf['maxmp']:
            cf['mp'] = cf['maxmp']
        if cf['mp'] < 0:
            cf['mp'] = 0
        
        if cf['hp'] <= 0 or ('mana_monster' in cf['skills'] and cf['mp'] <= 0):
            if cf['zombie'] <= 0:
                if 'death_revenge' in cf['skills']:
                    if cf['id'] == game['fighter1']['id']:
                       target = game['fighter2']
                       enm = '2'
                    else:
                       target = game['fighter1']
                       enm = '1'
                    game['text'] += '👁️‍🗨️|'+cf['name']+' погибает, но перед смертью взывает к Йогг-Сарону...\n'
                    i = 0
                    while i < 3:
                        use_skill(game, cf, random.choice(active), True)
                        i+=1
                    if 'mana_monster' not in target['skills']:
                        target['hp'] -= cf['do_dmg']
                    else:
                        target['mp'] -= cf['do_dmg']
                        
                    if target['hp'] <= 0 or ('mana_monster' in target['skills'] and target['mp'] <= 0):
                        if target['zombie'] <= 0:
                            dead = [target]
                            game['text'] += '👁️‍🗨️|'+cf['name']+' уничтожил соперника, буквально вырвав победу у него из рук (или что там у него)!\n'
                            if game['text'] != '' or mdt:
                                try:
                                    medit(getmessage(game), game['id'], game['msg'].message_id)
                                except:
                                    pass
                                try:
                                    bot.send_message(game['id'], game['text'])
                                except:
                                    pass
                            end_game_fight(game, dead)
                            return
                            
                        else:
                            dead.append(cf)
                            game['text'] += '💀|'+target['name']+' умер, но воскрес в виде зомби!\n'
                    else:
                        dead.append(cf)
                        game['text'] += '☠|'+cf['name']+' не уничтожил соперника силой Йогг-Сарона, и погиб окончательно!\n'
                else:    
                    dead.append(cf)
            else:
                cf['zombie'] -= 1
                cf['hp'] = (cf['maxhp']/100)*25
                if 'mana_monster' in cf['skills']:
                    cf['mp'] = (cf['maxmp']/100)*25
                game['text'] += '💀|'+cf['name']+' умер, но воскрес в виде зомби!\n'
            
    for ids in units:
        cf = ids
        if cf['hp'] > cf['maxhp']:
            cf['hp'] = cf['maxhp']

    if game['text'] != '' or mdt:
        try:
            medit(getmessage(game), game['id'], game['msg'].message_id)
        except:
            pass
        try:
            bot.send_message(game['id'], game['text'])
        except:
            pass
        game['text'] = ''

    game['dmgtaken1'] = 0
    game['dmgtaken2'] = 0
        
            
    if len(dead) > 0:
        end_game_fight(game, dead)
    else:
        game['turn'] += 1
        threading.Timer(game['timer'], next_turn_fight, args = [game]).start()
        
  except:
    bot.send_message(441399484, traceback.format_exc())
            
         

        
def end_game_fight(game, dead):
  try:
    if len(dead) >= 2:
        try:
            bot.send_message(game['id'], 'Ничья! Оба босса мертвы! Игра окончена.')
        except:
            pass
        del fightgames[game['id']]
    else:
        if dead[0]['id'] == game['fighter1']['id']:
            win = game['fighter2']
            loose = game['fighter1']
            name = game['user2name']
        else:
            win = game['fighter1']
            loose = game['fighter2']
            name = game['user1name']
        try:
            bot.send_message(game['id'], 'И наш победитель - '+win['name']+'! Его призыватель - '+name+'! Толпа ликует! Поздравляем победителей!')
            bot.send_message(game['id'], 'Бой окончен!')
        except:
            pass
        del fightgames[game['id']]
  except:
    bot.send_message(441399484, traceback.format_exc())
                   
        
    
def get_turn(game, boss):
    activ = False
    acts = ['attack']
    for ids in boss['skills']:
        if ids in active:
            activ = True
           
    if activ:
        acts.append('skill')
    act = random.choice(acts)
    if act == 'attack':
        do_hit(game, boss)
        
    elif act == 'skill':
        actives = []
        for ids in boss['skills']:
            if ids in active:
                needmana = getmanacost(ids)
                if 'mage' in boss['skills']:
                    needmana = int(needmana/2)
                if 'mana_monster' not in boss['skills']:
                    if needmana <= boss['mp']:
                        if ids not in boss['cds']:
                            actives.append(ids)
                        elif boss['cds'][ids] <= 0:
                            actives.append(ids)
                else:
                    if needmana < boss['hp']:
                        if ids not in boss['cds']:
                            actives.append(ids)
                        elif boss['cds'][ids] <= 0:
                            actives.append(ids)
        if len(actives) > 0:
            skill = random.choice(actives)
            use_skill(game, boss, skill)
        else:
            do_hit(game, boss)
 

female = ['Арися', 'Ванесса', 'Иллиада', 'Рэм', 'Тирисс']
    
    
def do_hit(game, boss):
    
    if game['fighter1']['id'] == boss['id']:
        target = game['fighter2']
        me = '1'
    else:
        target = game['fighter1']
        me = '2'
    dmg = random.randint(boss['dmg']-boss['disp'], boss['dmg']+boss['disp'])
    dmg += boss['dmg_bonus']
    if 'berserk' in boss['skills']:
        dmg += boss['dmg_bonus']*1
    for ids in boss['nexthits_dmg']:
        if boss['nexthits_dmg'][ids]['duration'] >= 1:
            dmg += boss['nexthits_dmg'][ids]['bonus']
            boss['nexthits_dmg'][ids]['duration'] -= 1
            
    if 'shield_fight' in boss['skills']:
        boss['lost_armor'] += 1
        dmg += boss['armor']
    
    if 'pierce_claws' not in boss['skills']:
        dmg -= (target['armor'] + target['armor_bonus'])
    d = 'л'
    if boss['name'] in female:
        d = 'ла'
    if 'gigant' in boss['skills']:
        if random.randint(1, 100) <= 20:
            target['stunned'] += 5
            game['text'] += '🌀|'+boss['name']+' оглуши'+d+' соперника на 4 секунды!\n'
            
    if 'strong_hit' in boss['skills']:
        if boss['hits_until_stun'] <= 0:
            target['stunned'] += 4
            game['text'] += '🌀|'+boss['name']+' четвёртым ударом оглуши'+d+' соперника на 3 секунды!\n'
            boss['hits_until_stun'] = 3
        else:
            boss['hits_until_stun'] -= 1
            
            
    if dmg < 0:
        dmg = 0
    if 'vampire' in boss['skills']:
        target['do_dmg'] -= int((dmg/100)*15)
        
    if dmg > 0:    
        boss['do_dmg'] += dmg
        
    if 'fire_hands' in boss['skills']:
        target['fire_damage'].update({getskillid(game):{'bonus':20, 'duration':3}})
    
    
def use_skill(game, boss, skill, notspendmana = False):
    d = 'л'
    h = 'Его'
    if boss['name'] in female:
        d = 'ла'
        h = 'Её'
    cd = 0
    if game['fighter1']['id'] == boss['id']:
        target = game['fighter2']
        me = '1'
    else:
        target = game['fighter1']
        me = '2'
    mp = 0
    mp = getskill(skill, 'mana')
    if 'magic_shield' in target['skills'] and random.randint(1, 100) <= 20:
        game['text'] += '🔷|'+boss['name']+' применяет заклинание, но соперник отменяет его магическим щитом!\n'
        
    elif skill == 'dec_armor':
        mp = 45
        target['buff_armor'].update({getskillid(game):{'bonus':-50, 'duration':10}})
        game['text'] += '⏬|'+boss['name']+' снижает броню соперника на 50 на 10 секунд!\n'
        cd = 8
            
    elif skill == 'mana_void':
        mp = 120
        boss['do_dmg'] += target['maxmp']
        cd = 16
        game['text'] += '💔|'+boss['name']+' взрывает ману соперника на '+str(target['maxmp'])+' урона!\n'
    
    elif skill == 'shield_smash':
        mp = 15
        boss['do_dmg'] += (boss['armor']+boss['armor_bonus'])*3
        cd = 5
        game['text'] += '💔|'+boss['name']+' бьёт соперника щитом на '+str((boss['armor']+boss['armor_bonus'])*3)+' урона!\n'
        
    elif skill == 'rage':
        boss['buff_damage'].update({getskillid(game):{'bonus':50, 'duration':10}})
        boss['buff_speed'].update({getskillid(game):{'bonus':3, 'duration':10}})
        boss['buff_armor'].update({getskillid(game):{'bonus':-15, 'duration':10}})
        cd = 16
        game['text'] += '⏫|'+boss['name']+' входит в ярость и повышает свои характеристики (урон+50, скорость+3, броня-15) на 10 секунд!\n'
        
    elif skill == 'fireball':
        mp = 200
        boss['do_dmg'] += boss['maxmp']
        cd = 21
        game['text'] += '💔|'+boss['name']+' создаёт огненный шар и запускает его в соперника на '+str(boss['maxmp'])+' урона!\n'
        
        
    elif skill == 'demon_inside':
        mp = 100
        boss['nexthits_dmg'].update({getskillid(game):{'bonus':200, 'duration':1}})
        cd = 21
        game['text'] += '⏫|'+boss['name']+' выпускает внутреннего демона! '+h+' следующая атака нанесёт на 200 урона больше!\n'

        
    elif skill == 'weakness':
        mp = 80
        target['buff_damage'].update({getskillid(game):{'bonus':-50, 'duration':10}})
        cd = 16
        game['text'] += '⏬|'+boss['name']+' ослабляет соперника! Следующие 10 секунд он будет наносить на 50 урона меньше!\n'

        
    elif skill == 'heal':
        mp = 40
        target['do_dmg'] -= 200
        cd = 11
        game['text'] += '💚|'+boss['name']+' лечится на 200 ХП!\n'

        
    elif skill == 'blood_ritual':
        boss['do_dmg'] += int((boss['maxhp']/100)*20 * 2)
        target['do_dmg'] += int((boss['maxhp']/100)*20)
        cd = 14
        game['text'] += '💔|'+boss['name']+' жертвует '+str(int((boss['maxhp']/100)*20))+' ХП для нанесения урона сопернику! Тот получает '+str(int((boss['maxhp']/100)*20 * 2))+' урона!\n'

        
    elif skill == 'speed_steal':
        mp = 80
        boss['buff_speed'].update({getskillid(game):{'bonus':1, 'duration':15}})
        target['buff_speed'].update({getskillid(game):{'bonus':-1, 'duration':15}})
        cd = 23 
        game['text'] += '⏫⏬|'+boss['name']+' крадёт у соперника 1 скорости на 15 секунд!\n'
            
    elif skill == 'mana_explosion':
        mp = 100
        boss['do_dmg'] += target['mp']
        cd = 20
        game['text'] += '💔|'+boss['name']+' выжигает ману соперника. Тот получает '+str(target['mp'])+' урона!\n'
           
            
    elif skill == 'firegun':
        mp = 100
        boss['do_dmg'] += (target['armor']*6)
        cd = 12
        game['text'] += '🔥|'+boss['name']+' Поджигает врага! Защищавшая соперника броня поджарила его на '+str(target['armor']*6)+' урона!\n'
           
            
    elif skill == 'time_control':
        mp = 100
        boss['buff_speed'].update({getskillid(game):{'bonus':20, 'duration':1}})
        cd = 7
        game['text'] += '⏳|'+boss['name']+' манипулирует временем, получая дополнительные 20 скорости на следующую секунду!\n'
           
            
    elif skill == 'death_beam':
        mp = 50
        boss['do_dmg'] += 100
        target['do_dmg'] -= 100
        cd = 10
        game['text'] += '💔💚|'+boss['name']+' выпускает из глаз луч смерти, нанося сопернику '+str(100)+' урона, и восстанавливая себе столько же ХП!\n'
           
            
    elif skill == 'void_blast':
        boss['do_dmg'] += int((target['maxhp']/100)*35)
        cd = 99999
        game['text'] += '🖤|'+boss['name']+' взывает к силам Пустоты, вытягивая из соперника '+str(int((target['maxhp']/100)*35))+' ХП!\n'
        
        
    elif skill == 'mana_destroy':
        mp = 50
        cd = 16
        target['spend_mp'] += int((target['maxmp']/100)*70)
        game['text'] += '⚡|'+boss['name']+' уничтожает '+str(int((target['maxmp']/100)*60))+' МП соперника!\n'
        
    elif skill == 'mana_drain':
        cd = 15
        target['spend_mp'] += int((target['maxmp']/100)*40)
        game['text'] += '💧💔|'+boss['name']+' высасывает '+str(int((target['maxmp']/100)*40))+' МП у соперника, нанося столько же урона!\n'
        boss['do_dmg'] += int((target['maxmp']/100)*40)
        
    elif skill == 'frost_arrow':
        cd = 13
        boss['do_dmg'] += int(target['atkspeed']*75)
        boss['set_speed'].update({getskillid(game):{'bonus':1, 'duration':5}})
        game['text'] += '❄|'+boss['name']+' создаёт ледяную стрелу и запускает её в соперника, нанося '+str(target['atkspeed']*75)+' урона и снижая его скорость хода до 1 на 5 секунд!\n'
  
    elif skill == 'wind_fury':
        cd = 26
        boss['do_dmg'] += 500
        game['text'] += '🌪|'+boss['name']+' призывает ураган, который наносит сопернику 500 урона!\n'
        
    elif skill == 'light_charge':
        cd = 2
        boss['do_dmg'] += 65
        game['text'] += '🌩|'+boss['name']+' создаёт молнию, и бьёт ей соперника на 65 урона!\n'
  
    if 'mage' in boss['skills']:
        cd = int(cd/2)
        mp = int(mp/2)
        
    if not notspendmana:
        boss['spend_mp'] += int(mp)
    
    if not notspendmana:
        if skill not in boss['cds']:
            boss['cds'].update({skill:cd})
        else:
            boss['cds'][skill] = cd
        
    if 'magic_mirror' in target['skills'] and random.randint(1, 100) <= 20:
        game['text'] += '✡|'+boss['name']+' применяет заклинание... Но его соперник делает то же самое!\n'
        use_skill(game, target, skill, True)
            
 

def getskillid(game):
    x = game['spellids']
    game['spellids'] += 1
    return x
  
    

cooks = {   
            'Новичок':{
                'strenght':15,
                'agility':10,
                'intelligence':1,
                'luck':20,
                'cooking_skill':1,
                'drunk':0,
                'cost':25,
                'name':'Новичок'
            },
            'Любитель':{
                'strenght':20,
                'agility':1,
                'intelligence':20,
                'luck':15,
                'cooking_skill':10,
                'drunk':0,
                'cost':50,
                'name':'Любитель'
            },
            'Профессионал':{
                'strenght':25,
                'agility':60,
                'intelligence':40,
                'luck':25,
                'cooking_skill':100,
                'drunk':0,
                'cost':90,
                'name':'Профессионал'
            
            }
        }


@bot.message_handler(commands=['enter_bar'])
def enterbar(m):
    pass

@bot.message_handler(commands=['givebee'])
def givebee(m):
    if m.from_user.id == 441399484:
        try:
            users.update_one({'id':m.reply_to_message.from_user.id},{'$inc':{'beecoins':int(m.text.split(' ')[1])}})
            beecoins.update_one({},{'$inc':{'beecoins':-int(m.text.split(' ')[1])}})
            bot.send_message(m.chat.id, 'Success!')

        except:
            bot.send_message(m.chat.id, 'Error!')

@bot.message_handler(commands=['barwork'])
def helpwork(m):
  try:
    if m.from_user.id in block:
        return
    global mainchat
    if m.chat.id != mainchat and m.chat.id != -1001478240928:
        bot.send_message(m.chat.id, 'Пока что эта опция доступна только в основном чате игры!')
        return
    user = users.find_one({'id':m.from_user.id})
    if user == None:
        user = users.insert_one(createuser(m.from_user))
        user = users.find_one({'id':m.from_user.id})
    if user['drunk'] >= 100:
        bot.send_message(m.chat.id, 'Сначала протрезвей, а потом работай!')
        return
    if time.time() - user['afk_until'] < 0:
        bot.send_message(m.chat.id, 'Вы спите!')
        return
    if user['working']:
        bot.send_message(m.chat.id, 'Вы уже заняты делом!')
        return
    works = []
    x = beecoins.find_one({})
    for ids in x['works']:
        if x['works'][ids] == True:
            works.append(ids)
    if 'barmenready' in works and user['cooking_skill'] < 15:
        works.remove('barmenready')
    if len(works) == 0:
        bot.send_message(m.chat.id, '_Владелец бара_: Подходящей тебе работы в баре сейчас нет, приходи позже.', parse_mode = 'markdown')
        return
    users.update_one({'id':user['id']},{'$set':{'working':True}})
    work = random.choice(works)
    text = 'Ошибка, @Loshadkin.'
    if work == 'cleanready':
        text = '_Владелец бара_: Так... В баре слишком много битого стекла, уборщики не справляются. Начинай уборку, через 10 минут проверю.'
        t = 600
    elif work == 'barmenready':
        text = '_Владелец бара_: Наши бармены не справляются с заказами. Помоги с заказами хотя бы на ближайшие 20 минут.'
        t = 1200
    elif work == 'changelightready':
        text = '_Владелец бара_: В баре сломалась лампочка. Думаю, пяти минут тебе на это дело хватит.'
        t = 300
    elif work == 'fix_furniture':
        text = '_Владелец бара_: После очередной драки в баре не осталось целой мебели... Почини хотя бы пару стульев за 15 минут.'
        t = 900
    threading.Timer(t, endwork, args = [user, work, m.chat.id]).start()
    
    beecoins.update_one({},{'$set':{'works.'+work:False}})
    if work != 'cleanready':
        resetwork(work, False)
    bot.send_message(m.chat.id, text, parse_mode = 'markdown', reply_to_message_id = m.message_id)
  except:
    bot.send_message(441399484, traceback.format_exc())
   
@bot.message_handler(commands=['hire_cook'])
def hirecook(m):
    if m.from_user.id in block:
        return
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text = 'Новичок', callback_data = 'hire_new'))
    kb.add(types.InlineKeyboardButton(text = 'Любитель', callback_data = 'hire_medium'))
    kb.add(types.InlineKeyboardButton(text = 'Профессионал', callback_data = 'hire_pro'))
    text = 'Выберите бармена, которого собираетесь нанять на час. Он будет делать случайные напитки из вашего ассортимента поставки.\n\n'
    for ids in cooks:
        text += '*'+ids+'*:\n'
        text += '💪Сила: '+str(cooks[ids]['strenght'])+'\n'
        text += '🤺Ловкость: '+str(cooks[ids]['agility'])+'\n'
        text += '🧠Интеллект: '+str(cooks[ids]['intelligence'])+'\n'
        text += '🍀Удача: '+str(cooks[ids]['luck'])+'\n'
        text += '🥪Умение готовить: '+str(cooks[ids]['cooking_skill'])+'\n'
        text += 'Цена: '+str(cooks[ids]['cost'])+'🐝\n'
        text += '\n'
    bot.send_message(m.chat.id, text, reply_markup = kb, parse_mode='markdown', reply_to_message_id = m.message_id)
    
    
   
def resetwork(work, x):
    if x == True:
        beecoins.update_one({},{'$set':{'works.'+work:True}})
    else:
        if work == 'changelightready':
            t = random.randint(200, 400)
        elif work == 'barmenready':
            t = random.randint(1000, 1600)
        elif work == 'fix_furniture':
            t = random.randint(700, 1100)
        threading.Timer(t, resetwork, args = [work, True]).start()

def endwork(user, work, chat):
  try:
    coins = 0
    x = beecoins.find_one({})
    if work == 'cleanready':
        coins = int(x['beecoins']*0.0002)
    elif work == 'barmenready':
        coins = int(x['beecoins']*0.0004)
    elif work == 'changelightready':
        coins = int(x['beecoins']*0.0001)
    elif work == 'fix_furniture':
        coins = int(x['beecoins']*0.0003)
    name1 = config.make_safe_html(user['name'])
    bot.send_message(chat, '<a href="tg://user?id='+str(user['id'])+'">'+name1 + '</a>'+', ты неплохо поработал. Держи награду - '+str(coins)+'🐝.', parse_mode='html')
    users.update_one({'id':user['id']},{'$inc':{'beecoins':coins}})
    beecoins.update_one({},{'$inc':{'beecoins':-coins}})
    users.update_one({'id':user['id']},{'$set':{'working':False}})
  except:
    bot.send_message(441399484, traceback.format_exc())

users.update_many({},{'$set':{'now_cooking':False, 'wait_ings':False, 'working':False}})

#users.update_many({},{'$set':{'cook':None}})

for ids in users.find({}):
    if ids['current_drink'] != None:
        users.update_one({'id':ids['id']},{'$inc':{'current_supplies.'+ids['current_drink']+'.amount':6}})

        
#for ids in users.find({}):
#    pts = 0
#    pts += ids['strenght']-1
#    pts += ids['intelligence']-1
#    pts += ids['luck']-1
#    pts += ids['agility']-1
#    pts += ids['cooking_skill']-1
#    users.update_one({'id':ids['id']},{'$inc':{'lvlpoints':pts}})
#    users.update_one({'id':ids['id']},{'$set':{'strenght':1}})
#    users.update_one({'id':ids['id']},{'$set':{'intelligence':1}})
#    users.update_one({'id':ids['id']},{'$set':{'luck':1}})
#    users.update_one({'id':ids['id']},{'$set':{'agility':1}})
#    users.update_one({'id':ids['id']},{'$set':{'cooking_skill':1}})
#bot.send_message(441399484, 'Статы сброшены!')
    
    
games = {}
duels = {}
govnos1 = ['мягкий', 'жидкий', 'твердый', 'вонючий', 'поносный']
govnos2 = ['пердун', 'обосрыш', 'какиш', 'мякиш', 'кусок', 'шептун']

toupdate = {'distance':0, 'stun':0, 'bonus':0, 'void':0}

horses = [
  {
    'name':'Красная лошадь',
    'ability':'bkb',        # На неё нельзя повлиять способностями
    'index':1
  },
  {
    'name':'Синяя лошадь',
    'ability':'accelerate',  # Имеет шанс ускориться
    'index':2
  },
  {
    'name':'Жёлтая лошадь',
    'ability':'hit',         # Имеет шанс остановить на один ход рядом бегущих лошадей
    'index':3
  },
  {
    'name':'Чёрная лошадь',
    'ability':'stable',       # Постоянно бежит с одной и той же скоростью
    'index':4
  },
  {
    'name':'Морозная лошадь',
    'ability':'slowdown',      # Замедляет рандомное число лошадей каждый ход
    'index':5
  },
  {
    'name':'Ненормальная лошадь',
    'ability':'random_move',    # Двигается быстрее, но имеет шанс двинуться назад
    'index':6
  },
  {
    'name':'Дорогая лошадь',
    'ability':'bonus_reward',   # Даёт бонусные монеты тем, кто на нее поставил, если занимает топ-3
    'index':7
  },
  {
    'name':'Робо-лошадь',
    'ability':'catch',    # Бежит быстрее, если впереди есть лошади
    'index':8
  },
  {
    'name':'Токсичная лошадь',
    'ability':'kick',    # Имеет шанс выкинуть любую лошадь из игры
    'index':9
  },
  {
    'name':'Быстрая лошадь',
    'ability': 'small_reward',   # Быстрая лошадь, дающая уменьшенную награду за победу
    'index':10
  },
  {
      'name':'Межпространственная лошадь',
      'ability':'teleport',
      'index':11
  },
  {
      'name':'Лошадь-экскаватор',
      'ability':'change_distance',
      'index':12
  },
  {
      'name':'Лошадь-колдун',
      'ability':'coldun',
      'index':13
  },
  {
      'name':'Случайная лошадь',
      'ability':'random_horse',
      'index':14
  },
    {
        'name':'Войд-лошадь',
        'ability':'stoptime',
        'index':15
    }
]


alcos = {
    #'wine':{'name':'Вино', 'exp':3, 'drunk':21, 'cost':200, 'owner':None, 'adress':'wine'},
    #'pivo':{'name':'Пиво', 'exp':1, 'drunk':7, 'cost':50, 'owner':None, 'adress':'pivo'},
    #'portvein':{'name':'Портвейн', 'exp':4, 'drunk':23, 'cost':350, 'owner':None, 'adress':'portvein'},
    #'kumis':{'name':'Кумыс', 'exp':2, 'drunk':9, 'cost':150, 'owner':None, 'adress':'kumis'},
    #'koniak':{'name':'Коньяк', 'exp':6, 'drunk':49, 'cost':350, 'owner':None, 'adress':'koniak'},
    #'dzin':{'name':'Джин', 'exp':7, 'drunk':45, 'cost':250, 'owner':None, 'adress':'dzin'},
    #'vodka':{'name':'Водка', 'exp':1, 'drunk':40, 'cost':50, 'owner':None, 'adress':'vodka'},
    #'tekila':{'name':'Текила', 'exp':6, 'drunk':34, 'cost':500, 'owner':None, 'adress':'tekila'},
    #'viski':{'name':'Виски', 'exp':6, 'drunk': 39, 'cost':400, 'owner':None, 'adress':'viski'},
    #'yager':{'name':'Ягер', 'exp':9, 'drunk': 38, 'cost':500, 'owner':None, 'adress':'yager'}
    
}

foods = {
    
    
}

waits = []


for ids in users.find({}):
    for idss in ids['current_supplies']:
        s = ids['current_supplies'][idss]
        s.update({'adress':idss.replace(' ', '#')})
        try:
          #  if time.time() - s['date'] < 2592000:
                alcos.update({s['name']:s})
            #else:
         #       try:
        #            users.update_one({'id':ids['id']},{'$unset':{'current_supplies.'+idss:1}})
         #       except:
          #          bot.send_message(441399484, traceback.format_exc())
        #        try:
         #           bot.send_message(ids['id'], 'Время вашего напитка "'+s['name']+'" истекло!')
        #        except:
       #             pass
        except:
            pass
    #for idss in ids['current_foods']:
   #     s = ids['current_foods'][idss]
 #       s.update({'adress':idss.replace(' ', '#')})
#        if time.time() - s['date'] < 2592000:
  #          foods.update({s['name']:s})
#        else:
 #           try:
  #              users.update_one({'id':ids['id']},{'$unset':{'current_foods.'+idss:1}})
    #        except:
 #               bot.send_message(441399484, traceback.format_exc())
#            try:
 #               bot.send_message(ids['id'], 'Время вашего продукта "'+s['name']+'" истекло!')
#            except:
#                pass

i = 0          
for ids in alcos:
    alcos[ids].update({'id':str(i)})
    x = users.find_one({'id':alcos[ids]['owner']})
    alcos[ids].update({'ownername':x['name']})
    users.update_one({'id':alcos[ids]['owner']},{'$set':{'current_supplies.'+alcos[ids]['name']+'.id':str(i)}})
    i+=1
    
i = 0          
for ids in foods:
    foods[ids].update({'id':str(i)})
    i+=1
          
        
            
def createplayer(user):
    return {user.id:{
        'id':user.id,
        'name':user.first_name,
        'bets':{}
    }
           }



def createchat(chat):
    return {
    'id':chat.id,
    'adminmode':False
    }

#def waitr(id):
#    try:
#        wait.remove(id)
#    except:
#        pass
#

#@bot.message_handler(commands=['cwork'])
#def cwork(m):
#    if m.from_user.id in wait:
#        bot.send_message(m.chat.id, 'Можно получать бикоины🐝 раз в 20 минут!')
#        return
#    x = random.randint(1, 10)
#    users.update_one({'id':m.from_user.id},{'$inc':{'beecoins':x}})
#    wait.append(m.from_user.id)
#    bot.send_message(m.chat.id, 'Получено '+str(x)+' бикоинов🐝')
#    threading.Timer(20*60, waitr, args = [m.from_user.id]).start())

@bot.message_handler(commands=['switch_mode'])
def swm(m):
    user = bot.get_chat_member(m.chat.id, m.from_user.id)
    if user.status not in ['administrator', 'creator']:
        bot.send_message(m.chat.id, 'Только администратор чата может делать это!')
        return
    chat = chats.find_one({'id':m.chat.id})
    if chat == None:
        chats.insert_one(createchat(m.chat))
        chat = chats.find_one({'id':m.chat.id})
    if chat['adminmode'] == False:
        s = True
        bot.send_message(m.chat.id, 'Теперь только админ сможет запустить скачки.')

    else:
        s = False
        bot.send_message(m.chat.id, 'Теперь все смогут запустить скачки.')
    chats.update_one({'id':chat['id']},{'$set':{'adminmode':s}})
    
    


@bot.message_handler(commands=['start'])
def start(m):
    if m.from_user.id in block:
        return
    user = users.find_one({'id':m.from_user.id})
    if user == None:
        user = users.insert_one(createuser(m.from_user))
        user = users.find_one({'id':m.from_user.id})
    if user['wait_ings'] == False:
        bot.send_message(m.chat.id, 'Здравствуй! Этот бот про скачки лошадей. Нажми /help, чтобы подробнее узнать об игре.')
    else:
      if m.from_user.id not in waits:
        if user['wait_ings'] == True:
            allow = False
            try:
                c = m.text.split(' ')[1]
                if c == user['code']:
                    allow = True
            except:
                pass
            if allow:
                users.update_one({'id':user['id']},{'$set':{'wait_ings':False}})
                bot.send_message(m.chat.id, 'Успешно добавлены нужные ингредиенты!')
            else:
                bot.send_message(m.chat.id, 'Вы не перешли по кнопке!')
                waits.append(m.from_user.id)
                threading.Timer(3, wremove, args = [m.from_user.id]).start()

 
def wremove(id):
    try:
        waits.remove(id)
    except:
        pass


@bot.message_handler(commands=['create_supply'])
def createsupply(m):
    if m.from_user.id in block:
        return
    user = users.find_one({'id':m.from_user.id})
    if user == None:
        user = users.insert_one(createuser(m.from_user))
        user = users.find_one({'id':m.from_user.id})
    if m.chat.id != m.from_user.id:
        bot.send_message(m.chat.id, 'Можно использовать только в личке!')
        return
    if user['supply'] == None:
        users.update_one({'id':user['id']},{'$set':{'supply':{'name':'Название', 'drunk':30, 'cost':200}}})
        user = users.find_one({'id':m.from_user.id})
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text = 'Название', callback_data = 'set_name'))
    kb.add(types.InlineKeyboardButton(text = 'Опьянение', callback_data = 'set_drunk'))
    kb.add(types.InlineKeyboardButton(text = 'Цена', callback_data = 'set_cost'))
    text = 'Создайте напиток, чтобы организовать поставку его в бар. Цена поставки на месяц - (стоимость напитка) монет. Вам будет отчисляться по 100% от его стоимости за покупку. Текущий напиток:\n'
    text += 'Название: "'+user['supply']['name']+'"\n'
    text += 'Опьянение: '+str(user['supply']['drunk'])+'%\n'
    text += 'Цена: '+str(user['supply']['cost'])+'💰'
    bot.send_message(m.chat.id, text, reply_markup = kb)
    
@bot.message_handler(commands=['create_food'])
def createfood(m):
    if m.from_user.id in block:
        return
    user = users.find_one({'id':m.from_user.id})
    if user == None:
        user = users.insert_one(createuser(m.from_user))
        user = users.find_one({'id':m.from_user.id})
    if m.chat.id != m.from_user.id:
        bot.send_message(m.chat.id, 'Можно использовать только в личке!')
        return
    if user['food'] == None:
        users.update_one({'id':user['id']},{'$set':{'food':{'name':'Название', 'sitost':30, 'cost':200}}})
        user = users.find_one({'id':m.from_user.id})
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text = 'Название', callback_data = 'f_set_name'))
    kb.add(types.InlineKeyboardButton(text = 'Питательность', callback_data = 'f_set_feed'))
    kb.add(types.InlineKeyboardButton(text = 'Цена', callback_data = 'f_set_cost'))
    text = 'Создайте продукт, чтобы организовать его поставку в бар. Вам будет отчисляться по 100% от его стоимости за покупку. Вам нужно будет готовить продукт, чтобы он был в наличии. Чем выше питательность, тем тяжелее процесс приготовления. Текущий продукт:\n'
    text += 'Название: "'+user['food']['name']+'"\n'
    text += 'Питательность: '+str(user['food']['sitost'])+'%\n'
    text += 'Цена: '+str(user['food']['cost'])+'💰'
    bot.send_message(m.chat.id, text, reply_markup = kb)
 

    
@bot.message_handler(commands=['deploy_food'])
def deploy_food(m):
    if m.from_user.id in block:
        return
    user = users.find_one({'id':m.from_user.id})
    if user == None:
        user = users.insert_one(createuser(m.from_user))
        user = users.find_one({'id':m.from_user.id})
    if m.from_user.id != m.chat.id:
        bot.send_message(m.chat.id, 'Можно использовать только в личке!')
        return
    
    if user['food'] == None:
        bot.send_message(m.chat.id, 'Вы ещё не произвели продукт (/create_food)!')
        return
    if user['coins'] < user['food']['cost']:
        bot.send_message(m.chat.id, 'Для этого действия нужно (стоимость продукта) монет!')
        return
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text = 'Начать поставку продукта в бар', callback_data = 'deploy_food'))
    text = 'Вы действительно готовы начать поставку вашего продукта в бар? Это будет стоить вам (стоимость продукта) монет, и через месяц '+\
    'контракт закончится. Вам будет отчисляться 100% от стоимости товара за каждую покупку.\n'+\
    'Итоговые характеристики продукта:\n'
    text += 'Название: "'+user['food']['name']+'"\n'
    text += 'Питательность: '+str(user['food']['sitost'])+'%\n'
    text += 'Цена: '+str(user['food']['cost'])+'💰'
    bot.send_message(m.chat.id, text, reply_markup = kb)
    

@bot.message_handler(commands=['gauss'])
def gausss(m):
    try:
        res = -1
        x = int(m.text.split(' ')[1])
        y = int(m.text.split(' ')[2])
        res = random.gauss(x, y)
        bot.send_message(m.chat.id, 'random.gauss(ср. значение '+str(x)+', ср. отклонение '+str(y)+') = '+str(res))
    except:
        pass

    
@bot.message_handler(commands=['reset_stats'])
def resetstats(m):
    if m.from_user.id != 441399484:
        return
    idd = stats.find_one({})['id']
    stats.remove({})
    stats.insert_one({'id':idd})
    bot.send_message(m.chat.id, 'Успешно очищена статистика!')
    
    
@bot.message_handler(commands=['simulate'])
def simulate(m):
    if m.from_user.id != 441399484:
        return
    t1 = time.time()
    try:
        x = int(m.text.split(' ')[1])
    except:
        return
    i = 0
    horse_stats = {}
    while i < x:
        spisok = cazino(None)
        try:
            for ids in spisok:
                if ids not in horse_stats:
                    horse_stats.update({ids:{'wins':0, 'games':0}})
            for ids in spisok:
                if spisok[ids] == 'win':
                    horse_stats[ids]['wins'] += 1
                    horse_stats[ids]['games'] += 1
                else:
                    horse_stats[ids]['games'] += 1
        except:
            pass
        i+=1
    s = stats.find_one({})
    for ids in horse_stats:
        h = horse_stats[ids]
        if str(ids) not in s:
            stats.update_one({},{'$set':{str(ids):{'games':0, 'wins':0}}}) 
            
    for ids in horse_stats:
        h = horse_stats[ids]
        stats.update_one({},{'$inc':{str(ids)+'.games':h['games'], str(ids)+'.wins':h['wins']}})
    t2 = time.time()
    t = t2-t1
    bot.send_message(m.chat.id, str(x)+' тестовых игр успешно завершены! Это заняло '+str(t)+' секунд.')
            
    
@bot.message_handler(commands=['duel'])
def duelll(m):
    return
    if m.reply_to_message == None:
        bot.send_message(m.chat.id, 'Этим нужно ответить на сообщение!')
        return
    if m.reply_to_message.from_user.is_bot:
        bot.send_message(m.chat.id, 'Это бот!')
        return
    if m.reply_to_message.from_user.id == m.from_user.id:
        bot.send_message(m.chat.id, 'Нельзя вызывать на дуэль себя!')
        return
    user = users.find_one({'id':m.from_user.id})
    if user == None:
        user = users.insert_one(createuser(m.from_user))
        user = users.find_one({'id':m.from_user.id})
    user2 = users.find_one({'id':m.reply_to_message.from_user.id})
    if user2 == None:
        bot.send_message(m.chat.id, 'Ошибка!')
        return
    try:
        cost = int(m.text.split(' ')[1])
    except:
        cost = 5
    if user['beecoins'] < cost:
        bot.send_message(m.chat.id, 'Недостаточно бикоинов (нужно '+str(cost)+')!')
        return
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text = 'Принять', callback_data = 'duel_accept_'+str(m.reply_to_message.from_user.id)+'_'+str(m.from_user.id)+'_'+str(cost)))
    kb.add(types.InlineKeyboardButton(text = 'Отказаться', callback_data = 'duel_decline_'+str(m.reply_to_message.from_user.id)+'_'+str(m.from_user.id)))
    bot.send_message(m.chat.id, user['name']+' вызывает '+user2['name']+' на дуэль!', reply_markup = kb)
    
    
    
    
@bot.message_handler(commands=['deploy_supply'])
def deploy_supply(m):
    if m.from_user.id in block:
        return
    user = users.find_one({'id':m.from_user.id})
    if user == None:
        user = users.insert_one(createuser(m.from_user))
        user = users.find_one({'id':m.from_user.id})
    if m.from_user.id != m.chat.id:
        bot.send_message(m.chat.id, 'Можно использовать только в личке!')
        return
    
    if user['supply'] == None:
        bot.send_message(m.chat.id, 'Вы ещё не произвели напиток (/create_supply)!')
        return
    if user['coins'] < user['supply']['cost']:
        bot.send_message(m.chat.id, 'Для этого действия нужно (стоимость напитка) монет!')
        return
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text = 'Начать поставку напитка в бар', callback_data = 'deploy_napitok'))
    text = 'Вы действительно готовы начать поставку вашего напитка в бар? Это будет стоить вам (стоимость напитка) монет, и через месяц '+\
    'контракт закончится. Вам будет отчисляться 100% от стоимости товара за каждую покупку.\n'+\
    'Итоговые характеристики напитка:\n'
    text += 'Название: "'+user['supply']['name']+'"\n'
    text += 'Опьянение: '+str(user['supply']['drunk'])+'%\n'
    text += 'Цена: '+str(user['supply']['cost'])+'💰'
    bot.send_message(m.chat.id, text, reply_markup = kb)
    
    
@bot.message_handler(commands=['choose_stats'])
def chostats(m):
    if m.from_user.id in block:
        return
    user = users.find_one({'id':m.from_user.id})
    if user == None:
        user = users.insert_one(createuser(m.from_user))
        user = users.find_one({'id':m.from_user.id})
    if user['lvlpoints'] <= 0:
        bot.send_message(m.chat.id, 'У вас нет очков для распределения!')
        return
    
    if len(m.text.split(' ')) < 3:
        bot.send_message(m.chat.id, 'Для распределения очков умений напишите команду в следующем формате:\n'+\
                     '/choose\_stats stat amount\nГде stat - характеристика (одна из следующих: `сила` `ловкость` `интеллект` `удача` `умение_готовить`), '+\
                     'amount - количество очков, которое вы хотите потратить на улучшение характеристики.', parse_mode = 'markdown')
        return
    else:
        try:
            stat = m.text.split(' ')[1].lower()
            amount = int(m.text.split(' ')[2])
            if amount <= 0:
                bot.send_message(m.chat.id, 'Нужно число больше нуля!')
                return
            s = None
            if stat == 'сила':
                s = 'strenght'
            elif stat == 'ловкость':
                s = 'agility'
            elif stat == 'интеллект':
                s = 'intelligence'
            elif stat == 'удача':
                s = 'luck'
            elif stat == 'умение_готовить':
                s = 'cooking_skill'
            if s == None:
                bot.send_message(m.chat.id, 'Такой характеристики не существует!')
                return
            if user['lvlpoints'] < amount:
                bot.send_message(m.chat.id, 'У вас недостаточно очков умений!')
                return
            users.update_one({'id':user['id']},{'$inc':{s:amount, 'lvlpoints':-amount}})
            bot.send_message(m.chat.id, 'Вы успешно прокачали характеристику "'+stat+'" на '+str(amount)+'!')
        except:
            bot.send_message(m.chat.id, 'Неверный формат!')
            bot.send_message(441399484, traceback.format_exc())
    
 

@bot.message_handler(commands=['throw'])
def throw(m):
    if m.from_user.id in block:
        return
    user = users.find_one({'id':m.from_user.id})
    if user == None:
        user = users.insert_one(createuser(m.from_user))
        user = users.find_one({'id':m.from_user.id})
    if user['drunk'] >= 100 or user['afk_until'] > time.time():
        bot.send_message(m.chat.id, 'Вы спите!')
        return
    if user['bottle'] != False and user['bottle'] != True:
        if m.reply_to_message != None:
            user2 = users.find_one({'id':m.reply_to_message.from_user.id})
            if user2 == None:
                uvorot = False
            else:
                chance = 25 - (user['agility'] - user2['agility'])
                if chance < 10:
                    chance = 10
                if chance > 90:
                    chance = 90
                if random.randint(1, 100) <= chance:
                    uvorot = True
                else:
                    uvorot = False
            if user2 != None:
                if user2['drunk'] >= 100 or user2['afk_until'] > time.time():
                    uvorot = False
            if uvorot:
                tt = m.text.split('/throw ')
                if len(tt) > 1:
                    text = user['name']+' с криком "'+tt[1]+'" бросает пустой '+user['bottle']+' прямо в '+m.reply_to_message.from_user.first_name+\
                    ', но тот ловко уворачивается, и '+user['bottle']+' разбивается об пол!'
                else:
                    text = user['name']+' бросает пустой '+user['bottle']+' прямо в '+m.reply_to_message.from_user.first_name+\
                    ', но тот ловко уворачивается, и '+user['bottle']+' разбивается об пол!'
            else:
                tt = m.text.split('/throw ')
                if len(tt) > 1:
                    text = user['name']+' с криком "'+tt[1]+'" бросает пустой '+user['bottle']+' прямо в '+m.reply_to_message.from_user.first_name+\
                    '!'
                else:
                    text = user['name']+' бросает пустой '+user['bottle']+' прямо в '+m.reply_to_message.from_user.first_name+\
                    '!'
            bot.send_message(m.chat.id, text)
            users.update_one({'id':user['id']},{'$set':{'bottle':False}})
            
        else:
            if (user['intelligence'] <= 5 or user['drunk'] >= 70) and random.randint(1, 100) <= 25:
                tt = m.text.split('/throw ')
                if len(tt) > 1:
                    text = user['name']+' с криком "'+tt[1]+'" разбивает пустой '+user['bottle']+' об голову и отключается!'
                else:
                    text = user['name']+' разбивает пустой '+user['bottle']+' об голову и отключается!'
                users.update_one({'id':user['id']},{'$set':{'afk_until': time.time() + 180}})
            else:
                tt = m.text.split('/throw ')
                if len(tt) > 1:
                    text = user['name']+' с криком "'+tt[1]+'" разбивает пустой '+user['bottle']+' об пол!'
                else:
                    text = user['name']+' разбивает пустой '+user['bottle']+' об пол!'
            bot.send_message(m.chat.id, text)
            
            users.update_one({'id':user['id']},{'$set':{'bottle':False}})
        if random.randint(1, 100) <= 20:
            beecoins.update_one({},{'$set':{'works.cleanready':True}})
        
                                    
    else:
        bot.send_message(m.chat.id, 'Нечего бросать! Сначала выпей!')
    


                                    
@bot.message_handler(commands=['help'])
def help(m):
    if m.from_user.id in block:
        return
    user = users.find_one({'id':m.from_user.id})
    if user == None:
        user = users.insert_one(createuser(m.from_user))
        user = users.find_one({'id':m.from_user.id})
    text = 'Здесь вы будете делать ставки на лошадей. Всё просто: чем выше итоговое место вашей лошади, тем больше награда. '+\
    'Можно поставить сразу на несколько лошадей. Чтобы начать скачки в чате, добавьте туда бота и напишите /cazino. Чтобы '+\
    'сделать ставку на лошадь, напишите /bet index. Индекс каждой лошади можно посмотреть в списке, который вам даст игра после команды '+\
    '/cazino. Каждый игрок ставит одинаковое количество монет на каждую лошадь. Чтобы выставить своё требование ставки, напишите команду '+\
    '/cazino в таком формате:\n/cazino 150\nГде 150 - количество требуемых монет для каждой ставки. Число может быть любым.\n'+\
    'У каждой лошади есть способности, которые помогают ей во время скачек, либо повышают/понижают награду за неё в конце игры. Посмотреть '+\
    'список способностей лошадей можно по команде /horses. Если в игре 2 или больше человека, общий пул монет умножается на 1.5. Удачи в ставках!'
    try:
        bot.send_message(m.from_user.id, text)
        bot.send_message(m.chat.id, 'Отправил помощь вам в ЛС.')
    except:
        bot.send_message(m.chat.id, 'Сначала откройте личку со мной!')
      
    
@bot.message_handler(commands=['bar'])
def barr(m):
    if m.from_user.id in block:
        return
    user = users.find_one({'id':m.from_user.id})
    if user == None:
        return
    if user['drunk'] >= 100 or user['afk_until'] > time.time():
        bot.send_message(m.chat.id, 'Вы спите!')
        return
    kb = userskb(m.from_user)
   # kb = barkb(m.from_user)
    text = 'Список баров:'
    bot.send_message(m.chat.id, text, reply_markup = kb)
    
def userskb(user):
    kb = types.InlineKeyboardMarkup()
    
    kbs = [[]]
    i = 0
    sp = []
    for ids in alcos:
        s = alcos[ids]
        if str(s['owner']) not in sp and s['owner'] != None:
            if len(kbs[i]) > 1:
                kbs.append([])
                i+=1
            allow = False
            if s['owner'] in allow_bars:
                kbs[i].append(types.InlineKeyboardButton(text = s['ownername']+'', callback_data = 'lookuser_'+str(s['owner'])+' '+str(user.id)))
                sp.append(str(s['owner']))
    for ids in kbs:
        kb.add(*ids)
    kb.add(types.InlineKeyboardButton(text = 'Выйти из меню', callback_data = 'goaway '+str(user.id)))
    return kb



def barkb(user, whos):
    kbs = [[]]
    i = 0
    kb = types.InlineKeyboardMarkup()
    #kb.add(types.InlineKeyboardButton(text = 'Вино\n200💰', callback_data = 'look_wine '+str(user.id)), types.InlineKeyboardButton(text = 'Пиво\n50💰', callback_data = 'look_pivo '+str(user.id)))
    #kb.add(types.InlineKeyboardButton(text = 'Портвейн\n350💰', callback_data = 'look_portvein '+str(user.id)), types.InlineKeyboardButton(text = 'Кумыс\n150💰', callback_data = 'look_kumis '+str(user.id)))
    #kb.add(types.InlineKeyboardButton(text = 'Коньяк\n350💰', callback_data = 'look_koniak '+str(user.id)), types.InlineKeyboardButton(text = 'Джин\n250💰', callback_data = 'look_dzin '+str(user.id)))
    #kb.add(types.InlineKeyboardButton(text = 'Водка\n50💰', callback_data = 'look_vodka '+str(user.id)), types.InlineKeyboardButton(text = 'Текила\n500💰', callback_data = 'look_tekila '+str(user.id)))
    u2 = users.find_one({'id':int(whos)})
    for ids in alcos:
            s = alcos[ids]
            if str(s['owner']) == str(whos):
              if u2['current_supplies'][s['name']]['amount'] > 0:
                if len(kbs[i]) > 1:
                    kbs.append([])
                    i+=1
                kbs[i].append(types.InlineKeyboardButton(text = s['name']+'\n'+str(s['cost'])+'💰', callback_data = 'look_'+str(s['id'])+' '+str(user.id)))
    for ids in kbs:
        kb.add(*ids)
    kb.add(types.InlineKeyboardButton(text = 'Назад', callback_data = 'gomennu '+str(user.id)))
    return kb


def nextlvl(user):
    exp = 2 + int(user['lvl']/50)
    if user['exp'] >= exp:
        users.update_one({'id':user['id']},{'$inc':{'lvl':1, 'exp':-exp, 'lvlpoints':1}})
        user = users.find_one({'id':user['id']})
        try:
            nextlvl(user)
        except:
            pass

    
@bot.message_handler(commands=['drink'])
def drink(m):
    if m.from_user.id in block:
        return
    user = users.find_one({'id':m.from_user.id})
    if user == None:
        return
    if user['drunk'] >= 100 or user['afk_until'] > time.time():
        bot.send_message(m.chat.id, 'Вы спите!')
        return
    text = 'Нажмите на напиток, чтобы выпить.'
    kb = types.InlineKeyboardMarkup()
    for ids in user['bar']:
        if user['bar'][ids] > 0:
            try:
                kb.add(types.InlineKeyboardButton(text = alcos[ids.replace('#', ' ')]['name']+' ('+str(user['bar'][ids])+')', callback_data = 'drink_'+alcos[ids.replace('#', ' ')]['id']+' '+str(user['id'])))      
            except:
                pass
    kb.add(types.InlineKeyboardButton(text = 'Закрыть меню', callback_data = 'close '+str(user['id'])))  
    bot.send_message(m.chat.id, text, reply_markup = kb)
           
    
@bot.message_handler(commands=['give_drink'])
def givedrink(m):
    if m.from_user.id in block:
        return
    user = users.find_one({'id':m.from_user.id})
    if user == None:
        return
    if user['drunk'] >= 100 or user['afk_until'] > time.time():
        bot.send_message(m.chat.id, 'Вы спите!')
        return
    try:
        text = 'Нажмите на напиток, чтобы угостить '+m.reply_to_message.from_user.first_name+'.'
    except:
        bot.send_message(m.chat.id, 'Этой командой нужно ответить на сообщение своего друга!')
        return
    kb = types.InlineKeyboardMarkup()
    for ids in user['bar']:
      try:
        if user['bar'][ids] > 0:
            kb.add(types.InlineKeyboardButton(text = alcos[ids.replace('#', ' ')]['name']+' ('+str(user['bar'][ids])+')', callback_data = 'give_'+alcos[ids.replace('#', ' ')]['id']+' '+str(user['id'])+' '+str(m.reply_to_message.from_user.id)))   
      except:
        pass   
    kb.add(types.InlineKeyboardButton(text = 'Закрыть меню', callback_data = 'close '+str(user['id'])))  
    bot.send_message(m.chat.id, text, reply_markup = kb)
    
   

@bot.message_handler(commands=['cook_drink'])
def cookdrink(m):
    user = users.find_one({'id':m.from_user.id})
    if user == None:
        user = users.insert_one(createuser(m.from_user))
        user = users.find_one({'id':m.from_user.id})
    if m.chat.id != m.from_user.id:
        bot.send_message(m.chat.id, 'Можно готовить напитки только в личке!')
        return
    if len(user['current_supplies']) == 0:
        bot.send_message(m.chat.id, 'У вас нет ни одного поставляемого напитка!')
        return
    kb = types.InlineKeyboardMarkup()
    
    for ids in user['current_supplies']:
      try:
        sp = user['current_supplies'][ids]
        for idss in alcos:
            if alcos[idss]['id'] == sp['id']:
                idd = alcos[idss]['id']
        try:
            kb.add(types.InlineKeyboardButton(text = sp['name'], callback_data = 'cook_'+str(idd)))
        except:
            pass
      except:
        pass
    bot.send_message(m.chat.id, 'Выберите напиток, который собираетесь готовить. Это будет стоить вам 20% от стоимости напитка.', reply_markup = kb)


def cooking(user, a, progress, p, skill, start, cooker=False):
    if start:
        start = False
        threading.Timer(random.randint(skill[0], skill[1]), cooking, args = [user, a, progress, p, skill, start, cooker]).start()
    else:
        if cooker == False:
            if users.find_one({'id':user['id']})['wait_ings'] == True:
                bot.send_message(user['id'], 'Вы пропустили время добавления ингредиентов!')
                users.update_one({'id':user['id']},{'$set':{'wait_ings':False}})
            else:
                failchance = 15
                failchance -= user['cooking_skill']/2
                fca = (user['drunk']/2) - 15
                if fca < 0:
                    fca = 0
                failchance += fca
                if random.randint(1, 100) <= failchance:
                    bot.send_message(user['id'], 'Упс! Вы добавили не те ингредиенты!')
                else:
                    progress += 25
                ch = user['luck']/2
                if ch > 35:
                    ch = 35
                if random.randint(1, 100) <= ch:
                    progress += 25
                    bot.send_message(user['id'], 'Так как вы очень удачливый, вам удалось увеличить прогресс создания напитка!')
            if p > 0:
                kb = types.InlineKeyboardMarkup()
                kb.add(types.InlineKeyboardButton(text = 'Добавить ингредиенты', callback_data = 'addings'))
                bot.send_message(user['id'], 'Нажмите, чтобы добавить нужные ингредиенты в ваш напиток.', reply_markup = kb)
                users.update_one({'id':user['id']},{'$set':{'wait_ings':True}})
                p -= 1
                threading.Timer(random.randint(skill[0], skill[1]), cooking, args = [user, a, progress, p, skill, start, cooker]).start()
            else:
                if progress >= 100:
                    am = 6
                    lk = user['luck']
                    if lk > 50:
                        lk = 50
                    if random.randint(1, 100) <= lk and random.randint(1, 100) <= user['strenght']*4:
                        am += 3
                        if random.randint(1, 100) <= user['strenght']*4:
                            am += random.randint(3, 4)
                    bot.send_message(user['id'], 'Вы успешно приготовили '+str(am)+' штук напитка "'+a['name']+'"!')
                    users.update_one({'id':user['id']},{'$inc':{'current_supplies.'+a['name']+'.amount':am}})
                else:
                    bot.send_message(user['id'], 'Вам не удалось приготовить "'+a['name']+'". Попробуйте увеличить скилл приготовления напитков!')
                users.update_one({'id':user['id']},{'$set':{'now_cooking':False}})
                users.update_one({'id':user['id']},{'$set':{'current_drink':None}})
        else:
            failchance = 15
            failchance -= cooker['cooking_skill']/2
            if random.randint(1, 100) <= failchance:
                pass
            else:
                progress += 25
            ch = cooker['luck']/2
            if ch > 35:
                ch = 35
            if random.randint(1, 100) <= ch:
                progress += 25
            if p > 0:
                p -= 1
                threading.Timer(random.randint(skill[0], skill[1]), cooking, args = [user, a, progress, p, skill, start, cooker]).start()
            else:
                if progress >= 100:
                    am = 6
                    lk = cooker['luck']
                    if lk > 50:
                        lk = 50
                    if random.randint(1, 100) <= lk and random.randint(1, 100) <= cooker['strenght']*4:
                        am += 3
                        if random.randint(1, 100) <= cooker['strenght']*4:
                            am += random.randint(3, 4)
                    users.update_one({'id':cooker['owner']},{'$inc':{'current_supplies.'+a['name']+'.amount':am}})
                else:
                    pass
                try:
                    users.update_one({'id':cooker['owner']},{'$set':{'cook.cooking':False}})
                except:
                    pass
            
    
@bot.callback_query_handler(func=lambda call: True)
def barrrr(call):
  try:
    if call.from_user.id in block:
        return
    user = users.find_one({'id':call.from_user.id})
    if user == None:
        return
    if user['drunk'] >= 100 or user['afk_until'] > time.time():
        bot.answer_callback_query(call.id, 'Вы спите!')
        return

    if 'lookuser' in call.data:
        if int(call.data.split(' ')[1]) != call.from_user.id:
            bot.answer_callback_query(call.id, 'Не ваше меню!')
            return
        us = call.data.split('_')[1].split(' ')[0]
        uname = users.find_one({'id':int(us)})['name']
        kb = barkb(call.from_user, us)
        text = 'Владелец бара - '+uname+'.'
        medit(text, call.message.chat.id, call.message.message_id, reply_markup = kb, parse_mode = 'html')
        
    elif 'summon' in call.data:
        if call.from_user.id != int(call.data.split('_')[2]):
            bot.answer_callback_query(call.id, 'Не ваше меню!')
            return
        prt = call.data.split('_')[1]
        if user['portals'][prt] > 0:
            bossid = stats.find_one({})['id']
            stats.update_one({},{'$inc':{'id':1}})
            bossname = random.choice(npc_name1).title()+' '+random.choice(npc_name2)+' '+random.choice(npc_name3)
            boss_skills = []
            skillamount = getskillamount(prt)
            while len(boss_skills) < skillamount:
                x = random.choice(all_boss_skills)
                if x not in boss_skills:
                    boss_skills.append(x)
            boss = createboss()
            bskills = ''
            boss.update({'name':bossname, 'id':bossid, 'skills':boss_skills})
           
            for ids in boss['skills']:
                bskills += '*'+getskill(ids)+'*\n'
            users.update_one({'id':user['id']},{'$set':{'summons.'+str(bossid): boss}})       
            users.update_one({'id':user['id']},{'$inc':{'portals.'+prt:-1}})
            medit('Призывается босс "'+portaltotext(prt)+'"!', call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, 'Открываем портал...')
            time.sleep(2)
            bot.send_message(call.message.chat.id, 'Надеемся, что не рванёт...')
            time.sleep(3)
            bot.send_message(call.message.chat.id, '*ВЗРЫВ*')
            time.sleep(2)
            bot.send_message(call.message.chat.id, 'Б%$@&! Ладно, босс всё равно призвался. Встречайте...')
            time.sleep(2)
            bot.send_message(call.message.chat.id, 'Босс "'+boss['name']+'"! Его способности:\n'+bskills, parse_mode = 'markdown')
            
            
           
     
    elif 'addings' in call.data:
        if user['wait_ings'] == False:
            return
        if user['wait_ings'] == True:
            users.update_one({'id':user['id']},{'$set':{'wait_ings':False}})
            medit('Успешно добавлены нужные ингредиенты!', call.message.chat.id, call.message.message_id)
            
    elif 'hire' in call.data:
        cook = call.data.split('_')[1]
        if cook == 'new':
            c = cooks['Новичок'].copy()
        elif cook == 'medium':
            c = cooks['Любитель'].copy()
        elif cook == 'pro':
            c = cooks['Профессионал'].copy()
        c.update({'work_until':time.time() + 60*60, 'cooking':False, 'owner':user['id']})
        
        if user['cook'] != None:
            medit('У вас уже работает один бармен!', call.message.chat.id, call.message.message_id)
            return
        if user['beecoins'] < c['cost']:
            medit('Недостаточно 🐝бикоинов!', call.message.chat.id, call.message.message_id)
            return
        medit('Успешно нанят бармен "'+c['name']+'"!', call.message.chat.id, call.message.message_id)
            
        bot.send_message(441399484, user['name']+' нанял бармена '+c['name']+'!')
        users.update_one({'id':user['id']},{'$inc':{'beecoins':-c['cost']}})
        beecoins.update_one({},{'$inc':{'beecoins':c['cost']}})
        users.update_one({'id':user['id']},{'$set':{'cook':c}})
       
    
    elif 'look' in call.data:
        if call.data[0] != 'f':
            if int(call.data.split(' ')[1]) != call.from_user.id:
                bot.answer_callback_query(call.id, 'Не ваше меню!')
                return
            alc = call.data.split('_')[1].split(' ')[0]
            
            for ids in alcos:
                if alcos[ids]['id'] == alc:
                    a = alcos[ids]
            own = users.find_one({'id':a['owner']})
            am = own['current_supplies'][a['name']]['amount']
            text = a['name']+'. Цена: '+str(a['cost'])+'💰. В наличии: '+str(am)+'. Нажмите "Купить" для приобретения.\n'
            if a['owner'] != None:
                name1 = config.make_safe_html(own['name'])
                text += 'Поставщик: '+'<a href="tg://user?id=' + str(own['id']) + '">' + name1 + '</a>'
            kb = types.InlineKeyboardMarkup()
            kb.add(types.InlineKeyboardButton(text = 'Купить', callback_data = 'buy_'+alc+' '+str(user['id'])))
            kb.add(types.InlineKeyboardButton(text = 'В меню', callback_data = 'menu '+str(user['id'])+' '+str(own['id'])))
            medit(text, call.message.chat.id, call.message.message_id, reply_markup = kb, parse_mode = 'html')
        else:
            if int(call.data.split(' ')[1]) != call.from_user.id:
                bot.answer_callback_query(call.id, 'Не ваше меню!')
                return
            fd = call.data.split('_')[1].split(' ')[0]
            for ids in foods:
                if foods[ids]['id'] == fd:
                    a = foods[ids]
                    adr = ids
            am = 0
            own = users.find_one({'id':a['owner']})
            am = own['current_foods'][adr]['amount']
            text = 'Продукт "'+a['name']+'". Цена: '+str(a['cost'])+'💰 В наличии: '+str(am)+'. Нажмите "Купить" для приобретения.\n'
            if a['owner'] != None:
                name1 = config.make_safe_html(own['name'])
                text += 'Поставщик: '+'<a href="tg://user?id=' + str(own['id']) + '">' + name1 + '</a>'
            kb = types.InlineKeyboardMarkup()
            kb.add(types.InlineKeyboardButton(text = 'Купить', callback_data = 'f_buy_'+fd+' '+str(user['id'])))
            kb.add(types.InlineKeyboardButton(text = 'В меню', callback_data = 'menu '+str(user['id'])+' '+str(own['id'])))
            medit(text, call.message.chat.id, call.message.message_id, reply_markup = kb, parse_mode = 'html')
            
    elif 'cook' in call.data:
        if user['now_cooking'] == True:
            medit('Вы уже готовите что-то!', call.message.chat.id, call.message.message_id)
            return
        alc = call.data.split('_')[1] 
        for ids in alcos:
            if alcos[ids]['id'] == alc:
                a = alcos[ids]
        cst = int((a['cost']/100)*20)
        if user['coins'] < cst:
            bot.send_message(call.message.chat.id, 'Приготовление напитка стоит 20% от его стоимости ('+str(cst)+')!')
            return
        users.update_one({'id':user['id']},{'$set':{'now_cooking':True}})
        users.update_one({'id':user['id']},{'$inc':{'coins':-cst}})
        min = int(30-(user['agility']/2))
        max = int(60-(user['agility']/3))
        if min < 4:
            min = 4
        if max < 15:
            max = 15
        popitki = 4
        progress = -25
        if user['intelligence'] >= 20:
            popitki -= 1
            progress += 25
        if user['intelligence'] >= 40:
            popitki -= 1
            progress += 25 
       
        
        cooking(user, a, progress, popitki, [min, max], True)
        medit('Вы успешно начали приготовление напитка "'+a['name']+'!', call.message.chat.id, call.message.message_id)
        users.update_one({'id':user['id']},{'$set':{'current_drink':a['name']}})
    
    elif 'give' in call.data:
        if int(call.data.split(' ')[1]) != call.from_user.id:
            bot.answer_callback_query(call.id, 'Не ваше меню!')
            return
        alc = call.data.split('_')[1].split(' ')[0]
        for ids in alcos:
            if alcos[ids]['id'] == alc:
                a = alcos[ids]
                adr = a['adress']
        try:
            if user['bar'][adr] <= 0:
                bot.answer_callback_query(call.id, 'У вас такого нет!')
                return
        except:
            adr = adr.replace('#', ' ')
            if user['bar'][adr] <= 0:
                bot.answer_callback_query(call.id, 'У вас такого нет!')
                return
        user2 = users.find_one({'id':int(call.data.split(' ')[2])})
        if user2 == None:
            return
        users.update_one({'id':user['id']},{'$inc':{'bar.'+adr:-1}})
        if alc in user2['bar']:
            users.update_one({'id':user2['id']},{'$inc':{'bar.'+adr:1}})
        else:
            users.update_one({'id':user2['id']},{'$set':{'bar.'+adr:1}})
        medit('Вы угостили '+user2['name']+' напитком "'+a['name']+'"!', call.message.chat.id, call.message.message_id)
        
    elif 'buy' in call.data:
        if call.data[0] != 'f':
            alc = call.data.split('_')[1].split(' ')[0]
            for ids in alcos:
                if alcos[ids]['id'] == alc:
                    a = alcos[ids]
                    adr = a['adress']
            own = users.find_one({'id':a['owner']})
            if own['current_supplies'][a['name']]['amount'] < 1:
                bot.answer_callback_query(call.id, 'Нет в наличии!')
                return
            if user['coins'] >= a['cost']:
                if adr in user['bar']:
                    if user['bar'][adr] < 5:       
                        users.update_one({'id':user['id']},{'$inc':{'bar.'+adr:1, 'coins':-a['cost']}})
                    else:
                        bot.answer_callback_query(call.id, 'У вас есть место только для пяти напитков одного типа!')
                        return
                else:
                    
                    users.update_one({'id':user['id']},{'$set':{'bar.'+adr:1}})
                    users.update_one({'id':user['id']},{'$inc':{'coins':-a['cost']}})
                users.update_one({'id':own['id']},{'$inc':{'current_supplies.'+a['name']+'.amount':-1}})
                if a['owner'] != None:
                    users.update_one({'id':a['owner']},{'$inc':{'coins':int(a['cost'])}})
                bot.answer_callback_query(call.id, '✅Бармен успешно выполняет ваш заказ на "'+a['name']+'"!')
            else:
                bot.answer_callback_query(call.id, '❌Недостаточно монет! Сначала заработай на ставках!')
        else:
            pass
            
    elif 'menu' in call.data:
        if int(call.data.split(' ')[1]) != call.from_user.id:
            bot.answer_callback_query(call.id, 'Не ваше меню!')
            return
        us = call.data.split(' ')[2]
        kb = barkb(call.from_user, us)
        uname = users.find_one({'id':int(us)})['name']
        
        text = 'Владелец бара - '+uname+'.'
        medit(text, call.message.chat.id, call.message.message_id, reply_markup = kb)
    
           
    elif 'goaway' in call.data:
        if int(call.data.split(' ')[1]) != call.from_user.id:
            bot.answer_callback_query(call.id, 'Не ваше меню!')
            return
        medit('Вы вышли из бара.', call.message.chat.id, call.message.message_id)
    
    elif 'gomennu' in call.data:
        if int(call.data.split(' ')[1]) != call.from_user.id:
            bot.answer_callback_query(call.id, 'Не ваше меню!')
            return
        kb = userskb(call.from_user)
        medit('Список баров:', call.message.chat.id, call.message.message_id, reply_markup = kb)
    

    elif 'close' in call.data:
        if user['id'] == int(call.data.split(' ')[1]):
            medit('Меню закрыто.', call.message.chat.id, call.message.message_id)
        else:
            bot.answer_callback_query(call.id, 'Не ваше меню!')
        
    elif 'set' in call.data:
        if call.data[0] != 'f':
            stat = call.data.split('_')[1]
            if stat == 'name':
                s = 'название'
            elif stat == 'cost':
                s = 'цена'
            elif stat == 'drunk':
                s = 'опьянение'
            users.update_one({'id':user['id']},{'$set':{'set':stat}})
            medit('Теперь пришлите мне характеристику "'+s+'" следующим сообщением.', call.message.chat.id, call.message.message_id)
        else:
            return
            stat = call.data.split('_')[1]
            if stat == 'name':
                s = 'название'
            elif stat == 'feed':
                s = 'питательность'
            elif stat == 'cost':
                s = 'цена'
            users.update_one({'id':user['id']},{'$set':{'f_set':stat}})
            medit('Теперь пришлите мне характеристику "'+s+'" следующим сообщением.', call.message.chat.id, call.message.message_id)
        
        
    elif 'drink' in call.data:
        if int(call.data.split(' ')[1]) != user['id']:
            bot.answer_callback_query(call.id, 'Не ваше меню!')
            return
        alc = call.data.split('_')[1].split(' ')[0]
        for ids in alcos:
            if alcos[ids]['id'] == alc:
                a = alcos[ids]
                adr = a['adress']
        if user['drunk'] >= 100:
            medit('Вы спите! Протрезвейте, а потом пейте опять.', call.message.chat.id, call.message.message_id)
            return
        try:
          if user['bar'][adr] <= 0:
            medit('У вас этого нет! Сначала закажите алкоголь в /bar!', call.message.chat.id, call.message.message_id)
            return
        except:
          adr = adr.replace('#', ' ')
          if user['bar'][adr] <= 0:
            medit('У вас этого нет! Сначала закажите алкоголь в /bar!', call.message.chat.id, call.message.message_id)
            return
        exp = a['drunk']/20
        if exp < 0:
            exp = 0
        if user['taken_exp'] == 0:
            users.update_one({'id':user['id']},{'$set':{'reboot_time':time.time() + 86400}})
        if exp > user['day_exp'] - user['taken_exp']:
            exp = user['day_exp'] - user['taken_exp']
        users.update_one({'id':user['id']},{'$inc':{'exp':exp, 'drunk':a['drunk'], 'bar.'+adr:-1, 'drinked':1}})
        users.update_one({'id':user['id']},{'$set':{'bottle':'бокал'}})
        text = '?'
        if a['name'] == 'Вино':
            text = user['name']+' выпил бокал вина!'
        elif a['name'] == 'Пиво':
            text = user['name']+' выпил бокал пива!'
        elif a['name'] == 'Портвейн':
            text = user['name']+' выпил бокал портвейна!'
        elif a['name'] == 'Кумыс':
            text = user['name']+' выпил бокал кумыса!'
        elif a['name'] == 'Коньяк':
            text = user['name']+' выпил бокал коньяка!'
        elif a['name'] == 'Джин':
            text = user['name']+' выпил бокал джина!'
        elif a['name'] == 'Водка':
            text = user['name']+' выпил стакан водки!'
            users.update_one({'id':user['id']},{'$set':{'bottle':'стакан'}})
        elif a['name'] == 'Текила':
            text = user['name']+' выпил рюмку текилы!'
        else:
            text = user['name']+' выпил бокал напитка "'+a['name']+'"!'
        medit(text, call.message.chat.id, call.message.message_id)
        user = users.find_one({'id':user['id']})
        if user['drunk'] < 0:
            users.update_one({'id':user['id']},{'$set':{'drunk':0}})
        nextlvl(user)
        if user['drunk'] >= 100:
            bot.send_message(call.message.chat.id, user['name']+' настолько много выпил, что завалился спать прямо в баре.')
            
    elif 'duel' in call.data:
        player = int(call.data.split('_')[2])
        player1 = int(call.data.split('_')[3])
        if player != call.from_user.id:
            bot.answer_callback_query(call.id, 'Не ваше меню!')
            return
        if call.data.split('_')[1] == 'decline':
            medit(call.from_user.first_name+' отклонил вызов.', call.message.chat.id, call.message.message_id)
            return
        elif call.data.split('_')[1] == 'accept':
            pl1 = users.find_one({'id':player1})
            pl2 = users.find_one({'id':player})
            cost = call.data.split('_')[4]
            x = createduel(call.message.chat.id, [pl2, pl1], cost)
            duels.update(x)
            duel = duels[call.message.chat.id]
            medit('Дуэль начинается! Играем в "'+x['name']+'"!', call.message.chat.id, call.message.message_id)
            d_next_turn(duel)
            
    elif 'take advantage' in call.data:
        try:
            duel = duels[call.message.chat.id]
        except:
            return
        attr = call.data.split('_')[1]
        try:
            player = duel['players'][call.from_user.id]
        except:
            return
        for ids in duel['players']:
            if duel['players'][ids]['id'] != player['id']:
                player2 = duel['players'][ids]
        if player['id'] != duel['current_player']:
            bot.answer_callback_query(call.id, 'Не ваш ход!')
            return
        if duel['type'] == 'draka':
            if attr == 'strenght':
                medit('Выбран аттрибут: сила.', call.message.chat.id, call.message.message_id)
                chance = random.gauss(50, 25)
                str_b = player['strenght'] - player2['strenght']
                lim = 20
                if str_b > lim:
                    str_b = lim
                if str_b < -lim:
                    str_b = -lim
                chance -= str_b
                
                if player2['agility'] > player['agility']:
                    ag_b = int((player['agility'] - player2['agility'])/1.5)
                else:
                    ag_b = 0
                lim = 15
                if ag_b > lim:
                    ag_b = lim
                if ag_b < -lim:
                    ag_b = -lim
                    
                chance -= ag_b
                text = ''
                if random.randint(1, 100) <= chance:
                    succ = True
                else:
                    succ = False
                if succ:
                    preim = random.randint(20, 45)
                    text += player['name']+' бьёт '+player2['name']+' и получает '+str(preim)+'% преимущества!'
                else:
                    text += player['name']+' бьёт '+player2['name']+', но не попадает!'
                
    
    elif call.data == 'deploy_napitok':
        
        if user['supply'] == None:
            medit('Вы еще не создали напиток!', call.message.chat.id, call.message.message_id)
            return
        if user['coins'] < user['supply']['cost']:
            medit('У вас недостаточно монет!', call.message.chat.id, call.message.message_id)
            return
        if len(user['current_supplies']) >= 10:
            medit('Максимальное число одновременных поставок в бар - 10!', call.message.chat.id, call.message.message_id)
            return
        if user['supply']['name'] in user['current_supplies']:
            medit('Вы уже поставляете напиток с таким названием!', call.message.chat.id, call.message.message_id)
            return
        disallow = False
        for ids in users.find({}):
            for idss in ids['current_supplies']:
                try:
                  if ids['current_supplies'][idss]['name'] == user['supply']['name']:
                    disallow = True
                except:
                    pass
        if disallow:
            medit('Кто-то уже поставляет напиток с таким названием!', call.message.chat.id, call.message.message_id)
            return
        users.update_one({'id':user['id']},{'$set':{'current_supplies.'+user['supply']['name']:addsupply(user['supply'], user['id'])}})
        users.update_one({'id':user['id']},{'$inc':{'coins':-(user['supply']['cost'])}})
        medit('Вы успешно начали поставку своего напитка в бар! Чтобы начать готовить - /cook_drink. Он появится в ассортименте в течение 24ч, для ускорения процесса можно написать @Loshadkin.', call.message.chat.id, call.message.message_id)
        
    elif call.data == 'deploy_food':
        
        if user['food'] == None:
            medit('Вы еще не создали продукт!', call.message.chat.id, call.message.message_id)
            return
        if user['coins'] < user['food']['cost']:
            medit('У вас недостаточно монет!', call.message.chat.id, call.message.message_id)
            return
        if len(user['current_foods']) >= 10:
            medit('Максимальное число одновременных поставок еды в бар - 10!', call.message.chat.id, call.message.message_id)
            return
        if user['food']['name'] in user['current_foods']:
            medit('Вы уже поставляете продукт с таким названием!', call.message.chat.id, call.message.message_id)
            return
        disallow = False
        for ids in users.find({}):
            for idss in ids['current_foods']:
                if ids['current_foods'][idss]['name'] == user['food']['name']:
                    disallow = True
        if disallow:
            medit('Кто-то уже поставляет продукт с таким названием!', call.message.chat.id, call.message.message_id)
            return
        users.update_one({'id':user['id']},{'$set':{'current_foods.'+user['food']['name']:addfood(user['food'], user['id'])}})
        users.update_one({'id':user['id']},{'$inc':{'coins':-(user['food']['cost'])}})
        medit('Вы успешно начали поставку своего продукта в бар! Он появится в ассортименте в течение 24ч, для ускорения процесса можно написать @Loshadkin.', call.message.chat.id, call.message.message_id)
  
  except:
    bot.send_message(441399484, traceback.format_exc())            
        

@bot.message_handler(commands=['cook'])
def cook(m):
    pass
       
        
def addsupply(sup, id):
    sup.update({'date':time.time(), 'owner':id, 'amount':0})
    return sup

def addfood(food, id):
    food.update({'date':time.time(), 'owner':id, 'amount':0})
    return food
        


def d_next_turn(duel):
    p = None
    ps = []
    lt = -1
    for ids in duel['players']:
        player = duel['players'][ids]
        if player['lastturn'] >= lt:
            lt = player['lastturn']
            ps.append(player)
    p = random.choice(ps)
    duel['current_player'] = p['id']
    kb = duelkb()
    bot.send_message(duel['id'], p['name']+', выберите, с помощью чего хотите получить преимущество в дуэли.', reply_markup = kb)
    t = threading.Timer(60, d_end_turn, args = [duel])
    t.start()
    game['timer'] = t
    

def d_end_turn(duel):
    pass
    
    
def duelkb():
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text = '💪Сила', callback_data = 'take advantage_strenght'))
    kb.add(types.InlineKeyboardButton(text = '🤺Ловкость', callback_data = 'take advantage_agility'))
    kb.add(types.InlineKeyboardButton(text = '🧠Интеллект', callback_data = 'take advantage_intelligence'))
    kb.add(types.InlineKeyboardButton(text = '🍀Удача', callback_data = 'take advantage_luck'))
    return kb
    
    
@bot.message_handler(commands=['me'])
def mee(m):
    if m.from_user.id in block:
        return
    user = users.find_one({'id':m.from_user.id})
    if user == None:
        user = users.insert_one(createuser(m.from_user))
        user = users.find_one({'id':m.from_user.id})
    text = 'Ваш профиль:\n'
    text += 'Монеты: 💰'+str(user['coins'])+'\n'
    text += 'Бикоины: 🐝'+str(user['beecoins'])+'\n'
    if user['drunk'] > 0:
        text += '❗Вы пьяны на '+str(user['drunk'])+'%!\n'
    text += 'Выпито: '+str(user['drinked'])+'🍷\n'
    text += 'Уровень: '+str(user['lvl'])+'🏅\n'
    text += 'Очки распределения характеристик: '+str(user['lvlpoints'])+'➕\n'
    text += '💪Сила: '+str(user['strenght'])+'\n'
    text += '🤺Ловкость: '+str(user['agility'])+'\n'
    text += '🧠Интеллект: '+str(user['intelligence'])+'\n'
    text += '🍀Удача: '+str(user['luck'])+'\n'
    text += '🥪Умение готовить: '+str(user['cooking_skill'])+'\n'
    text += '🔮Энергия пустоты: '+str(user['void_energy'])+'\n'
    text += '☣Аномалия пустоты: '+str(user['void_anomaly'])+'\n'
    
    bot.send_message(m.chat.id, text)
    
 
@bot.message_handler(commands=['horses'])
def horsessss(m):
    if m.from_user.id in block:
        return
    user = users.find_one({'id':m.from_user.id})
    text = '🔴Красная лошадь - на эту лошадь нельзя повлиять никакими способностями, но если кто-то пытается - эта лошадь только ускоряется.\n\n'+\
    '🔵Синяя лошадь - имеет 25% шанс каждый ход ускориться на 47 единиц!\n\n'+\
    '🌕Жёлтая лошадь - имеет 25% шанс плюнуть в лошадей перед собой и ускориться на 40 единиц, остановив их передвижение на ход.\n\n'+\
    '⚫Чёрная лошадь - постоянно бежит с одной и той же скоростью - 48 единиц (остальные лошади бегут на 25-50 единиц каждый ход).\n\n'+\
    '🌨Морозная лошадь - каждый ход замедляет случайное число лошадей на 7-12 единиц, так же ускоряется на 2 единицы за каждую замедленную лошадь.\n\n'+\
    '💊Ненормальная лошадь - имеет скорость выше, чем у остальных (45-75 единиц), но имеет 10% шанс двинуться назад, а не вперёд.\n\n'+\
    '💶Дорогая лошадь - имеет 0.5% шанс купить победу каждый ход. Если она окажется в числе победителей, награда за неё увеличится в 6 раз!\n\n'+\
    '🤖Робо-лошадь - если перед ней есть соперники, то она бежит быстрее на 10-12 единиц.\n\n'+\
    '🤬Токсичная лошадь - имеет 7% шанс каждый ход оскорбить любую лошадь, от чего та сойдёт с дистанции, а эта лошадь ускорится на 150 единиц.\n\n'+\
    '🌪Быстрая лошадь - двигается быстрее остальных (28-70 единиц).\n\n'+\
    '👽Межпространственная лошадь - имеет шанс 12% применить телепорт. Если лошадь не на первом месте, то она меняется местами с первой. Иначе '+\
      'она меняется местами с последней лошадью.\n\n'+\
    '🔨Лошадь-экскаватор - уменьшает длину дистанции вдвое в начале игры и начинает гонку с дистанции 140!\n\n'+\
    '🔮Лошадь-колдун - в начале игры получает способность случайной лошади из игры.\n\n'+\
    '❓Случайная лошадь - в начале игры превращается в лошадь, которой нет в этой игре.\n\n'+\
    '🟣Войд-лошадь - имеет 12% шанс каждый ход остановить время на два хода для всех остальных лошадей, у которых нет этой способности.'
    try:
        bot.send_message(m.from_user.id, text)
        bot.send_message(m.chat.id, 'Отправил лошадей вам в ЛС.')
    except:
        bot.send_message(m.chat.id, 'Сначала откройте личку со мной!')
    

@bot.message_handler(commands=['reboot'])
def reboott(m):
    if m.from_user.id == 441399484:
        users.update_many({},{'$set':{'day_exp':80}})
        bot.send_message(m.chat.id, 'Yes.')
    
    
@bot.message_handler(commands=['bonus'])
def bonus(m):
    if m.from_user.id in block:
        return
    user = users.find_one({'id':m.from_user.id})
    if user == None:
        user = users.insert_one(createuser(m.from_user))
        user = users.find_one({'id':m.from_user.id})
    if user['drunk'] >= 100 or user['afk_until'] > time.time():
        bot.send_message(m.chat.id, 'Вы спите!')
        return
    if time.time() - user['lastbonus'] >= 3600:
        x = int(random.randint(100, 250))
        if user['coins'] <= 0:
            x += 1000
        users.update_one({'id':user['id']},{'$set':{'lastbonus':time.time()}})
        users.update_one({'id':user['id']},{'$inc':{'coins':x}})
        bot.send_message(m.chat.id, 'Открываем коробку с бонусом... Получено '+str(x)+'💰!', reply_to_message_id = m.message_id)
    else:
        mins = 60 - (int((user['lastbonus'] - time.time()) / 60) * -1)
        bot.send_message(m.chat.id, 'Открывать бонус можно раз в час! Осталось '+str(mins)+' минут!')
    
    
@bot.message_handler(commands=['cazino'])
def cazinooo(m):
    cazino(m)
    
    
def cazino(m):
    if m != None:
        if m.from_user.id in block:
            return
        user = users.find_one({'id':m.from_user.id})
        if user == None:
            user = users.insert_one(createuser(m.from_user))
            user = users.find_one({'id':m.from_user.id})
        chat = chats.find_one({'id':m.chat.id})
        if chat != None:
            if chat['adminmode'] and bot.get_chat_member(m.chat.id, m.from_user.id).status not in ['administrator', 'creator']:
                bot.send_message(m.chat.id, 'Включен админ-мод!')
                return
        if user['drunk'] >= 100 or user['afk_until'] > time.time():
            bot.send_message(m.chat.id, 'Вы спите!')
            return
        if m.chat.id not in games:
            game = creategame(m)
            x = m.text.split(' ')
    
            games.update(game)
            game = games[m.chat.id]
            try:
                if int(x[1]) >= 0:
                    game['minimum'] = int(x[1])
            except:
                pass
            indexes = ''
            for ids in game['horses']:
                a = game['horses'][ids]
                indexes += htoe(a['name'])+a['name']+': `'+str(a['index'])+'`\n'
            bot.send_message(m.chat.id, 'Скачки стартуют со взносом *'+str(game['minimum'])+'*! /bet index, чтобы поставить на лошадь. '+
                             'Для начала забега напишите /go. Индексы лошадей текущего забега:\n'+indexes, parse_mode = 'markdown')
        else:
            bot.send_message(m.chat.id, 'Скачки уже в процессе!')
            return
    else:
        game = creategame(m)
        games.update(game)
        return go(None)
    
    
@bot.message_handler(commands=['blind_bet'])
def cazino22345(m):
    if m.from_user.id in block:
        return
    user = users.find_one({'id':m.from_user.id})
    if user == None:
        user = users.insert_one(createuser(m.from_user))
        user = users.find_one({'id':m.from_user.id})
    chat = chats.find_one({'id':m.chat.id})
    if chat != None:
        if chat['adminmode'] and bot.get_chat_member(m.chat.id, m.from_user.id).status not in ['administrator', 'creator']:
            bot.send_message(m.chat.id, 'Включен админ-мод!')
            return
    if user['drunk'] >= 100 or user['afk_until'] > time.time():
        bot.send_message(m.chat.id, 'Вы спите!')
        return
    if m.chat.id not in games:
        
        tp = False
        if m.from_user.id == 441399484:
            try:
                g = m.text.split(' ')[2]
                if g == 'test':
                    tp = True
            except:
                pass
        if tp:
            c = False
            t = False
            while c == False or t == False:
                game = creategame(m, bets = 1, mode = 'blind', tp = tp)
                c = False
                t = False
                for ids in game[m.chat.id]['horses']:
                    if game[m.chat.id]['horses'][ids]['ability'] == 'coldun':
                        c = True
                    if game[m.chat.id]['horses'][ids]['ability'] == 'teleport':
                        t = True
        else:
            game = creategame(m, bets = 1, mode = 'blind', tp = tp)
                
        games.update(game)
        game = games[m.chat.id]       
               
            
        x = m.text.split(' ')
        
        
        try:
            if int(x[1]) >= 0:
                game['minimum'] = int(x[1])
        except:
            pass
        indexes = ''
        for ids in game['horses']:
            a = game['horses'][ids]
            indexes += htoe(a['name'])+a['name']+': `'+str(a['index'])+'`\n'
        bot.send_message(m.chat.id, 'Скачки стартуют со взносом *'+str(game['minimum'])+'*! /bet, чтобы поставить на СЛУЧАЙНУЮ лошадь забега. '+
                         'Для начала забега напишите /go. Какие лошади будут в игре - узнаете после начала!\n', parse_mode = 'markdown')
    else:
        bot.send_message(m.chat.id, 'Скачки уже в процессе!')
        return
    
    
    
@bot.message_handler(commands=['give'])
def givee(m):

    if m.from_user.id == 441399484:
        try:
            users.update_one({'id':m.reply_to_message.from_user.id},{'$inc':{'coins':int(m.text.split(' ')[1])}})
        except:
            pass

@bot.message_handler(commands=['stats'])
def statistic(m):
  if m.from_user.id == 441399484:
    text = 'Статистика:\n\n'
    s = stats.find_one({})
    for ids in s:
        try:
            h = None
            for idss in horses:
                if str(idss['index']) == ids:
                    h = idss
            if h != None:
                text += htoe(h['name'])+h['name']+': '+str(s[ids]['wins'])+'/'+str(s[ids]['games'])+' побед, винрейт '+\
                str(round((s[ids]['wins']/s[ids]['games'])*100, 2))+'%\n\n'
        except:
            pass
    bot.send_message(m.chat.id, text)
        
@bot.message_handler(commands=['bet'])
def bett(m):
    if m.from_user.id in block:
        return
    user = users.find_one({'id':m.from_user.id})
    if user == None:
        user = users.insert_one(createuser(m.from_user))
        user = users.find_one({'id':m.from_user.id})
    if user['drunk'] >= 100 or user['afk_until'] > time.time():
        bot.send_message(m.chat.id, 'Вы спите!')
        return
    if m.chat.id in games:
        if games[m.chat.id]['started'] == True:
            bot.send_message(m.chat.id, 'Скачки уже в процессе!')
            return
        
        game = games[m.chat.id]
        if game['mode'] == None:
            x = m.text.split(' ')
            if len(x) < 2:
                bot.send_message(m.chat.id, 'После /bet укажите индекс лошади!')
                return
            x = x[1]
            h = None
            game = games[m.chat.id]
            for ids in game['horses']:
                a = game['horses'][ids]
                if str(a['index']) == x:
                    h = a
            if h == None:
                bot.send_message(m.chat.id, 'Лошади с индексом "'+x+'" нет в этой игре!', reply_to_message_id = m.message_id)
                return
            if m.from_user.id not in game['players']:
                game['players'].update(createplayer(m.from_user))
            if h['index'] in game['players'][m.from_user.id]['bets']:
                bot.send_message(m.chat.id, 'Вы уже поставили на эту лошадь!')
                return
            
            if user['coins'] >= game['minimum']:
              if len(game['players'][m.from_user.id]['bets']) < game['maxbets']:
             
                game['players'][m.from_user.id]['bets'].update(createbet(m.from_user, game, h))
                game['cache'] += game['minimum']
                users.update_one({'id':user['id']},{'$inc':{'coins':-game['minimum'], 'reloadcoins':game['minimum']}})
                bot.send_message(m.chat.id, 'Вы успешно поставили на лошадь!')
              else:
                bot.send_message(m.chat.id, 'Максимальное число ставок - '+str(game['maxbets'])+'!')
                return
            else:
                bot.send_message(m.chat.id, 'Недостаточно монет (нужно '+str(game['minimum'])+')!')

        elif game['mode'] == 'blind':
            if user['coins'] >= game['minimum']:
              if m.from_user.id not in game['players']:
                game['players'].update(createplayer(m.from_user))
              if len(game['players'][m.from_user.id]['bets']) < game['maxbets']:
                
                hs = []
                for ids in game['horses']:
                    hs.append(game['horses'][ids])
                h = random.choice(hs)
                game['players'][m.from_user.id]['bets'].update(createbet(m.from_user, game, h))
                game['cache'] += game['minimum']
                users.update_one({'id':user['id']},{'$inc':{'coins':-game['minimum'], 'reloadcoins':game['minimum']}})
                bot.send_message(m.chat.id, 'Вы успешно поставили на случайную лошадь!')
              else:
                bot.send_message(m.chat.id, 'Максимальное число ставок - '+str(game['maxbets'])+'!')
                return
            else:
                bot.send_message(m.chat.id, 'Недостаточно монет (нужно '+str(game['minimum'])+')!')
            
            
def unlock(id):
    try:
        banchats.remove(id)
    except:
        pass 

       
@bot.message_handler(commands=['brokengame'])
def brokenn(m):
    if m.chat.id not in games:
        bot.send_message(m.chat.id, 'В чате даже не идёт игра!')
        return
    game = games[m.chat.id]
    if game['starttime'] != None and time.time() - game['starttime'] >= 300:
        del games[game['id']]
        bot.send_message(m.chat.id, 'Удалил сломанную игру!')
    else:
        bot.send_message(m.chat.id, 'Ещё не прошло 5 минут, чтобы игра считалась сломанной!')


@bot.message_handler(commands=['go'])
def gooo(m):
    if m.chat.id not in banchats:
        banchats.append(m.chat.id)
        threading.Timer(2, unlock, args = [m.chat.id]).start()
    else:
        return
    if m != None:
        threading.Timer((random.randint(1, 20)/10), go, args = [m]).start()
    else:
        go(m)

def go(m):
  try:
    if m != None:
        if m.chat.id not in games:
            bot.send_message(m.chat.id, 'Игра ещё не была создана!')
            return
        game = games[m.chat.id]
        if game['started'] == True:
            return
        if m.from_user.id in block:
            return
        user = users.find_one({'id':m.from_user.id})
        if user == None:
            user = users.insert_one(createuser(m.from_user))
            user = users.find_one({'id':m.from_user.id})
        if user['drunk'] >= 100 or user['afk_until'] > time.time():
            bot.send_message(m.chat.id, 'Вы спите!')
            return
        if True:
            if time.time() - game['createtime'] < 60:
                bot.send_message(m.chat.id, 'Ещё не прошла минута со старта! Подождите, пока все, кто хочет, сделают ставку!')
                return
            games[m.chat.id]['started'] = True
            games[m.chat.id]['starttime'] = time.time()
            if game['mode'] == 'blind':
                bets = ''
                for ids in game['players']:
                    player = game['players'][ids]
                    for idss in player['bets']:
                        h = player['bets'][idss]['horse']
                    for ids in horses:
                        if ids['index'] == h:
                            h = ids.copy()
                    bets += player['name']+': '+htoe(h['name'])+h['name']+'\n\n'
                bot.send_message(game['id'], 'Ставки:\n\n'+bets)
            s = stats.find_one({})
            for ids in game['horses']:
                h = game['horses'][ids]
                if str(h['index']) not in s:
                    stats.update_one({},{'$set':{str(h['index']):{'games':0, 'wins':0}}})                         
    else:
        game = games[1]
    for ids in game['horses']:
        h = game['horses'][ids]
        if h['ability'] == 'random_horse':
            hs = []
            hs_not = []
            for ids in game['horses']:
                hs.append(game['horses'][ids])
            for ids in horses:
                allow = True
                for idss in hs:
                    if idss['index'] == ids['index']:
                        allow = False
                if allow:
                    hs_not.append(ids)
            newh = random.choice(hs_not).copy()
            newh.update(toupdate)
            newh['index'] = h['index']
            if game['stats_test'] == False:
                tobet = []
                for ids in game['players']:
                    for idss in game['players'][ids]['bets']:
                        if idss == h['index']:
                            tobet.append(ids)
                for ids in tobet:
                    game['players'][ids]['bets'].update(createbet(game['players'][ids], game, newh))
            del game['horses'][h['index']]
            game['horses'].update({newh['index']:newh.copy()})
            if game['stats_test'] == False:
                bot.send_message(game['id'], '❓Случайная лошадь превращается в '+htoe(newh['name'])+newh['name']+'!')
            game['allhorses'].update({newh['index']:newh})
    ll = []
    for ids in game['horses']:
        h = game['horses'][ids]
        if h['ability'] == 'coldun':
            hs = []
            for ids in game['horses']:
                if game['horses'][ids]['index'] != h['index']:
                    hs.append(game['horses'][ids])
            newh = random.choice(hs)
            newh = newh.copy()
            h['ability'] = newh['ability']
            if game['tp'] == True:
                h['ability'] = 'teleport'
                newh['name'] = 'Межпространственная лошадь'
                newh['ability'] = 'teleport'
            if game['stats_test'] == False:
                bot.send_message(game['id'], htoe(h['name'])+h['name']+' получает способность лошади '+htoe(newh['name'])+newh['name']+'!')
            if newh['ability'] == 'teleport':
                ll = []
                need = 5
                i = 0
                index = -1
                while i < need:
                    nh = newh.copy()
                    nh['index'] = index
                    index -= 1
                    ll.append(nh)
                    i += 1
                if game['stats_test'] == False:
                    try:
                        bot.send_message(game['id'], 'О нет, пространство сломано!')
                    except:
                        pass
    for hh in ll:
        game['horses'].update({hh['index']:hh})
                   
    for ids in game['horses']:
        if game['horses'][ids]['ability'] == 'change_distance':
            game['lenght'] -= (game['lenght']/2)
            game['horses'][ids]['distance'] = 140
    #for ids in game['horses']:
    #    h = game['horses'][ids]
    #    if h['ability'] == 'bonus_reward' and random.randint(1, 100) <= 5:
    #        h['distance'] = game['lenght']
    #        if game['stats_test'] == False:
    #            game['text'] += htoe(h['name'])+h['name']+' купила победу в скачках!'
    if game['stats_test'] == False:
        if len(game['players']) > 1:
            if game['mode'] == None:
                game['cache'] = int(game['cache'] * 1.5)
            elif game['mode'] == 'blind':
                game['cache'] = int(game['cache'] * 3)
    if game['stats_test'] == False:
        bot.send_message(m.chat.id, 'Скачки начинаются!')
        msg = bot.send_message(m.chat.id, results(game))
        game['msg'] = msg
    if game['stats_test'] == False:
        threading.Timer(5, next_turn, args=[game]).start()
    else:
        return next_turn(game)
  except:
    bot.send_message(441399484, traceback.format_exc())
    del games[game['id']]
    bot.send_message(m.chat.id, 'Ошибка! Сбрасываю игру.')
        
@bot.message_handler(commands=['notifications'])
def notees(m):
    if m.chat.id == m.from_user.id:
        return
    chat = chats.find_one({'id':m.chat.id})
    if chat == None:
        chats.insert_one(createchat(m.chat))
        chat = chats.find_one({'id':m.chat.id})
    if bot.get_chat_member(m.chat.id, m.from_user.id).status not in ['administrator', 'creator']:
        bot.send_message(m.chat.id, 'Только администратор может делать это!')
        return
    if chat['notifications'] == True:
        chats.update_one({'id':m.chat.id},{'$set':{'notifications':False}})
        bot.send_message(m.chat.id, 'Уведомления о перезагрузке отключены!')
    else:
        chats.update_one({'id':m.chat.id},{'$set':{'notifications':False}})
        bot.send_message(m.chat.id, 'Уведомления о перезагрузке включены!')
        

@bot.message_handler()
def allms(m):
    chat = chats.find_one({'id':m.chat.id})
    if chat == None:
        chats.insert_one(createchat(m.chat))
    if m.chat.id != m.from_user.id:
        return
    if m.from_user.id in block:
        return
    user = users.find_one({'id':m.from_user.id})
    if user == None:
        user = users.insert_one(createuser(m.from_user))
        user = users.find_one({'id':m.from_user.id})
    if user['name'] != m.from_user.first_name:
        users.update_one({'id':user['id']},{'$set':{'name':m.from_user.first_name}})
    if user['set'] != None:
        if user['supply'] == None:
            users.update_one({'id':user['id']},{'$set':{'set':None}})
           
            bot.send_message(m.chat.id, 'Сначала создайте напиток (/create_supply)!')
            return
        if user['set'] == 'cost':
            try:
                cost = int(m.text)
            except:
                bot.send_message(m.chat.id, 'Нужно числовое значение!')
                return
            if cost < 1:
                bot.send_message(m.chat.id, 'Цена должна быть выше нуля!')
                return
            users.update_one({'id':user['id']},{'$set':{'supply.cost':cost, 'set':None}})
            bot.send_message(m.chat.id, 'Успешно установлена цена напитка: '+str(cost)+'💰.')
            
        elif user['set'] == 'name':
            if '#' in m.text:
                bot.send_message(m.chat.id, 'Недопустимый символ: "#"!')
                return
            if '.' in m.text:
                bot.send_message(m.chat.id, 'Недопустимый символ: "."!')
                return
            users.update_one({'id':user['id']},{'$set':{'supply.name':m.text, 'set':None}})
            bot.send_message(m.chat.id, 'Успешно установлено название напитка: "'+m.text+'".')
        
        elif user['set'] == 'drunk':
            try:
                drunk = int(m.text)
            except:
                bot.send_message(m.chat.id, 'Нужно числовое значение!')
                return
            if drunk > 300 or drunk < -25:
                bot.send_message(m.chat.id, 'Нужно значение от -25 до 300!')
                return
            users.update_one({'id':user['id']},{'$set':{'supply.drunk':drunk, 'set':None}})
            bot.send_message(m.chat.id, 'Успешно установлено опьянение напитка: '+str(drunk)+'%.')
            
    if user['f_set'] != None:
        pass
   #     if user['food'] == None:
 #           users.update_one({'id':user['id']},{'$set':{'f_set':None}})
#           
 #           bot.send_message(m.chat.id, 'Сначала создайте продукт (/create_food)!')
 #           return
 #       if user['f_set'] == 'cost':
 #           try:
 #               cost = int(m.text)
 #           except:
 #               bot.send_message(m.chat.id, 'Нужно числовое значение!')
 #               return
 #           if cost < 1:
  #              bot.send_message(m.chat.id, 'Цена должна быть выше нуля!')
  #              return
 #           users.update_one({'id':user['id']},{'$set':{'food.cost':cost, 'f_set':None}})
 #           bot.send_message(m.chat.id, 'Успешно установлена цена продукта: '+str(cost)+'💰.')
 #           
#        elif user['f_set'] == 'name':
   #         if '#' in m.text:
#                bot.send_message(m.chat.id, 'Недопустимый символ: "#"!')
 #               return
 #           users.update_one({'id':user['id']},{'$set':{'food.name':m.text, 'f_set':None}})
#            bot.send_message(m.chat.id, 'Успешно установлено название продукта: "'+m.text+'".')
#        
#        elif user['f_set'] == 'feed':
#            try:
#                fd = int(m.text)
#            except:
#                bot.send_message(m.chat.id, 'Нужно числовое значение!')
#                return
#            if fd > 100 or fd < 0:
#                bot.send_message(m.chat.id, 'Нужно значение от 0 до 100!')
#                return
#            users.update_one({'id':user['id']},{'$set':{'food.sitost':fd, 'f_set':None}})
#            bot.send_message(m.chat.id, 'Успешно установлена питательность продукта: '+str(fd)+'%.')
           


def next_turn(game):
  try:
    for ids in game['horses']:
        a = game['horses'][ids]
        if a['void'] <= 0:
            min = 25
            max = 50
            z = '+'
            bonus = 0
            if a['stun'] <= 0:
                if a['ability'] == 'accelerate' and random.randint(1,100) <= 25:
                    bonus += 47
                elif a['ability'] == 'stable':
                    min = 48
                    max = 48
                elif a['ability'] == 'random_move':
                    min = 45
                    max = 75
                    if random.randint(1,100) <= 10:
                        z = '-'
                elif a['ability'] == 'small_reward':
                    min = 28
                    max = 70
                if z == '+':
                    a['distance'] += random.randint(min, max)+bonus+a['bonus']
                else:
                    a['distance'] -= (random.randint(min, max)+bonus+a['bonus'])
                a['bonus'] = 0
            a['stun'] -= 1
            if a['stun']< 0:
                a['stun'] = 0
        
    
    topop = []
    for ids in game['horses']:
        a = game['horses'][ids]
        if a['void'] <= 0:
            if a['ability'] == 'hit' and random.randint(1, 100) <= 25:
                targets = []
                for idss in game['horses']:
                    b = game['horses'][idss]
                    if a['distance'] - b['distance'] >= -300 and a['distance'] - b['distance'] <= 20 and a['index'] != b['index']:
                        targets.append(b)
                if len(targets) > 0:
                    target = random.choice(targets)
                    if target['ability'] != 'bkb':
                        target['stun'] += 1
                        if game['stats_test'] == False:
                            game['text'] += htoe(a['name'])+a['name']+' плюнула в '+htoe(target['name'])+target['name']+'! Она пропустит следующий ход.\n'
                        a['distance'] += 40
                    else:
                        b['stun'] += 1
                        if game['stats_test'] == False:
                            game['text'] += htoe(a['name'])+a['name']+' плюнула в '+htoe(target['name'])+target['name']+', но та увернулась и плюнула в ответ!\n'
                        target['distance'] += 40
                
            elif a['ability'] == 'slowdown':
                try:
                    amount = random.randint(1, len(game['horses'])-1)
                except:
                    amount = 0
                targets = []
                hs = []
                for ids in game['horses']:
                    hs.append(game['horses'][ids])
                while len(targets) < amount:
                    x = random.choice(hs)
                    if x not in targets and x['index'] != a['index']:
                        targets.append(x)
                #game['text'] += htoe(a['name'])+a['name']+' замедляет следующих лошадей на 6 единиц:\n'
                for idss in targets:
                    if idss['ability'] != 'bkb':
                        idss['bonus'] -= random.randint(7, 12)
                        a['bonus'] += 2
                    else:
                        idss['bonus'] += random.randint(4, 7)
                
            elif a['ability'] == 'catch':
                allow = False
                for idss in game['horses']:
                    b = game['horses'][idss]
                    if b['distance'] > a['distance']:
                        allow = True
                if allow:
                    if a['stun'] <= 0:
                        a['distance'] += random.randint(10, 12)
                    
            elif a['ability'] == 'kick' and random.randint(1, 100) <= 7:
                if len(game['horses']) > 1:
                    hs = []
                    for ids in game['horses']:
                        hs.append(game['horses'][ids])
                    k = random.choice(hs)
                    while k['index'] == a['index']:
                        k = random.choice(hs)
                    if k['ability'] != 'bkb':
                        if game['stats_test'] == False:
                            game['text'] += htoe(a['name'])+a['name']+' оскорбляет '+htoe(k['name'])+k['name']+' на лошадином и ускоряется! Та теряет веру в себя и сходит с дистанции.\n'
                        topop.append(k)
                        a['distance'] += 150
                    else:
                        if game['stats_test'] == False:
                            game['text'] += htoe(a['name'])+a['name']+' оскорбляет '+htoe(k['name'])+k['name']+' на лошадином, но та только ускоряется!\n' 
                            k['distance'] += 250
                            
            elif a['ability'] == 'stoptime' and random.randint(1,100) <= 12:
                hs = []
                for ids in game['horses']:
                    hs.append(game['horses'][ids])
                for ids in hs:
                    if ids['ability'] != 'stoptime':
                        if ids['ability'] != 'bkb':
                            ids['void'] += 3
                        else:
                            pass
                                                
                if game['stats_test'] == False:
                    game['text'] += htoe(a['name'])+a['name']+' останавливает время для всех остальных лошадей на 2 хода!\n'
                            
            elif a['ability'] == 'teleport' and random.randint(1,100) <= 12:
                hs = []
                for ids in game['horses']:
                    hs.append(game['horses'][ids])
                first = None
                fd = 0
                for ids in hs:
                    if fd < ids['distance']:
                        fd = ids['distance']
                        first = ids
                if first['index'] != a['index']:
                    if first['ability'] != 'bkb':
                        f = first['distance']
                        first['distance'] = a['distance']
                        a['distance'] = f
                        if game['stats_test'] == False:
                            game['text'] += htoe(a['name'])+a['name']+' меняется местами с первой лошадью - '+htoe(first['name'])+first['name']+'!\n'
                    else:
                        if game['stats_test'] == False:
                            game['text'] += htoe(a['name'])+a['name']+' пытается поменяться местами с '+htoe(first['name'])+first['name']+', но та отправляет её копытом обратно в портал!\n'
                            first['distance'] += 50
                   
                else:
                    
                    last = None
                    fd = 2000
                    for ids in hs:
                        if fd > ids['distance']:
                            fd = ids['distance']
                            last = ids
                    if last['ability'] != 'bkb':
                        f = last['distance']
                        last['distance'] = a['distance']
                        a['distance'] = f
                        if game['stats_test'] == False:
                            game['text'] += htoe(a['name'])+a['name']+' меняется местами с последней лошадью - '+htoe(last['name'])+last['name']+'!\n'
                    else:
                        if game['stats_test'] == False:
                            game['text'] += htoe(a['name'])+a['name']+' пытается поменяться местами с '+htoe(last['name'])+last['name']+', но та отправляет её копытом обратно в портал!\n'
                            last['distance'] += 50

    for ids in game['horses']:
      if game['horses'][ids]['void'] <= 0:
        if game['horses'][ids]['ability'] == 'bonus_reward' and random.randint(1, 1000) <= 5:
            game['horses'][ids]['distance'] = game['lenght']
            if game['stats_test'] == False:
                game['text'] += htoe(game['horses'][ids]['name'])+game['horses'][ids]['name']+' купила победу!\n'
                            
         
    for ids in game['horses']:
        a = game['horses'][ids]
        a['void'] -= 1
        if a['void']< 0:
            a['void'] = 0  
            
    for ids in topop:
        try:
            game['horses'].pop(ids['index'])
        except:
            pass
    try:
        if game['stats_test'] == False:
            msg = bot.send_message(game['id'], game['text'])
            game['delmsgs'].append(msg)
    except:
        pass
    return resets(game)
  except:
    bot.send_message(441399484, traceback.format_exc())
            
     
def resets(game):
    for ids in game['horses']:
        a = game['horses'][ids]
        
    game['text'] = ''
    win = []
    if game['stats_test'] == False:
        try:
            medit(results(game), game['id'], game['msg'].message_id)
        except:
            pass
    for ids in game['horses']:
        a = game['horses'][ids]
        if a['distance'] >= game['lenght']:
            win.append(a)
    itog = []
    if len(win) > 0:
        while len(win) > 0:
            maxd = 0
            w = None
            for ids in win:
                if ids['distance'] > maxd:
                    maxd = ids['distance']
                    w = ids
            itog.append(w)
            win.remove(w)
    for ids in itog:
        game['winners'].append(ids)
        game['horses'].pop(ids['index'])
    if len(game['winners']) >= 3 or len(game['horses']) == 0: 
        return endgame(game)
    else:
        if game['stats_test'] == False:
            threading.Timer(4, next_turn, args=[game]).start()
        else:
            return next_turn(game)
    

def endgame(game):
    s = stats.find_one({})
    for ids in game['allhorses']:
        h = game['allhorses'][ids]
        if str(h['index']) not in s:
            stats.update_one({},{'$set':{str(h['index']):{'games':0, 'wins':0}}}) 
    spisok = {}
    text = 'Результаты забега:\n'
    i = 1
    dell = []
    if game['stats_test'] == False:
        for ids in game['delmsgs']:
            try:
                bot.delete_message(game['id'], ids.message_id)
            except:
                pass
    for ids in game['winners']:
        if i <= 3:
            if game['stats_test'] == False:
                text += str(i)+' место: '+htoe(ids['name'])+ids['name']+'\n'
                stats.update_one({},{'$inc':{str(ids['index'])+'.wins':1}})
            else:
                spisok.update({ids['index']:'win'})
        else:
            dell.append(ids)
        i += 1
    for ids in dell:
        game['winners'].remove(ids)
        
    if game['stats_test'] == False:
        try:
            bot.send_message(game['id'], text)
        except:
            pass
    text = ''
    if game['stats_test'] == False:
        time.sleep(5)
    if game['stats_test'] == False:
        pl1 = []
        pl2 = []
        pl3 = []
        pl3c = int((game['cache']/100)*10)
        pl2c = int((game['cache']/100)*30)
        game['cache'] -= pl3c
        game['cache'] -= pl2c
    
        pl1c = game['cache']
        game['cache'] -= pl1c
                
                
        for ids in game['players']:
            try:
              if game['winners'][0]['index'] in game['players'][ids]['bets']:
                pl1.append(game['players'][ids])
            except:
              pass
            try:
              if game['winners'][1]['index'] in game['players'][ids]['bets']:
                pl2.append(game['players'][ids])
            except:
              pass
            try:
              if game['winners'][2]['index'] in game['players'][ids]['bets']:
                pl3.append(game['players'][ids])
            except:
              pass
        p1_upd = 0
        p2_upd = 0
        p3_upd = 0
        poll = 0
        dis = []
        if len(pl1) == 0:
            poll += pl1c
            dis.append('1')
        if len(pl2) == 0:
            poll += pl2c
            dis.append('2')
        if len(pl3) == 0:
            poll += pl3c
            dis.append('3')
            
        if poll > 0:
            bot.send_message(441399484, 'poll>0')
            if '1' in dis:
                if '2' not in dis and '3' not in dis:
                    pl2c += int((poll/100)*70)
                    pl3c += poll-int((poll/100)*70)
                    try:
                        bot.send_message(441399484, '1 in, 2n3 not')
                    except:
                        pass
                elif '2' not in dis:
                    pl2c += poll
                    bot.send_message(441399484, '1 in, 2 not')
           
                elif '3' not in dis:
                    pl3c += poll
                    bot.send_message(441399484, '1 in, 3 not')
           
            elif '2' in dis:
                if '1' not in dis and '3' not in dis:
                    pl1c += int((poll/100)*90)
                    pl3c += poll-int((poll/100)*90)
                    bot.send_message(441399484, '2 in, 1n3 not')
           
                elif '1' not in dis:
                    pl1c += poll
                    bot.send_message(441399484, '2 in, 1 not')
           
                elif '3' not in dis:
                    pl3c += poll
                    bot.send_message(441399484, '2 in, 3 not')
           
            elif '3' in dis:
                if '1' not in dis and '2' not in dis:
                    pl1c += int((poll/100)*70)
                    pl2c += poll-int((poll/100)*70)
                    bot.send_message(441399484, '3 in, 1n2 not')
           
                elif '1' not in dis:
                    pl1c += poll
                    bot.send_message(441399484, '3 in, 1 not')
           
                elif '2' not in dis:
                    pl2c += poll
                    bot.send_message(441399484, '3 in, 2 not')
           
        br = 6  
        try:
          if game['winners'][0]['ability'] == 'bonus_reward':
            pl1c = pl1c * br 
        except:
          pass
            
        try:
          if game['winners'][1]['ability'] == 'bonus_reward':
            pl2c = pl2c * br
        except:
          pass
            
        try:
          if game['winners'][2]['ability'] == 'bonus_reward':
            pl3c = pl3c * br
        except:
          pass
            
        try:
          if game['winners'][0]['ability'] == 'small_reward':
            pl1c = int(pl1c / 1)
        except:
          pass
            
        try:
          if game['winners'][1]['ability'] == 'small_reward':
            pl2c = int(pl2c / 1) 
        except:
          pass
            
        try:
          if game['winners'][2]['ability'] == 'small_reward':
            pl3c = int(pl3c / 1)
        except:
          pass
        
        
        if len(pl1) > 0:
            p1_upd = int(pl1c/len(pl1))
    
        if len(pl2) > 0:
            p2_upd = int(pl2c/len(pl2))
    
        if len(pl3) > 0:
            p3_upd = int(pl3c/len(pl3))
        
        
        
        
        text += 'Следующие участники получают '+str(p1_upd)+' монет за первую лошадь:\n'
        for ids in pl1:
            text += ids['name']+' '
            users.update_one({'id':ids['id']},{'$inc':{'coins':p1_upd}})
        text += '\n\n'
    
        text += 'Следующие участники получают '+str(p2_upd)+' монет за вторую лошадь:\n'
        for ids in pl2:
            text += ids['name']+' '
            users.update_one({'id':ids['id']},{'$inc':{'coins':p2_upd}})
        text += '\n\n'
        
        text += 'Следующие участники получают '+str(p3_upd)+' монет за третью лошадь:\n'
        for ids in pl3:
            text += ids['name']+' '
            users.update_one({'id':ids['id']},{'$inc':{'coins':p3_upd}})
        for ids in game['players']:
            a = game['players'][ids]
            for idss in game['players'][ids]['bets']:
                users.update_one({'id':a['id']},{'$inc':{'reloadcoins':-game['minimum']}})
   
    dtext = ''
    to_pasyuk = ''
    if game['stats_test'] == False:
        if game['mode'] == 'blind' and game['minimum'] >= 500:
            for ids in pl1:
                coef = 1.2
                x = random.randint(1, 1000)
                stone = None
                if x <= 500*coef:
                    stone = 'typically'
                if x <= 200*coef:
                    stone = 'rare'
                if x <= 75*coef:
                    stone = 'epic'
                if x <= 5:
                    stone = 'legendary'
                if stone != None:
                    dtext += ids['name']+': '+portaltotext(stone)+'\n'
                    bot.send_message(441399484, str(users.update_one({'id':ids['id']},{'$inc':{'portals.'+stone:1}})))
                    to_pasyuk += ids['name']+' получает '+portaltotext(stone)+'!\n'
                
            for ids in pl2:
                coef = 1.1
                x = random.randint(1, 1000)
                stone = None
                if x <= 500*coef:
                    stone = 'typically'
                if x <= 200*coef:
                    stone = 'rare'
                if x <= 75*coef:
                    stone = 'epic'
                if x <= 4:
                    stone = 'legendary'
                if stone != None:
                    dtext += ids['name']+': '+portaltotext(stone)+'\n'
                    bot.send_message(441399484, str(users.update_one({'id':ids['id']},{'$inc':{'portals.'+stone:1}})))
                    to_pasyuk += ids['name']+' получает '+portaltotext(stone)+'!\n'
                    
            for ids in pl3:
                coef = 1
                x = random.randint(1, 1000)
                stone = None
                if x <= 500*coef:
                    stone = 'typically'
                if x <= 200*coef:
                    stone = 'rare'
                if x <= 75*coef:
                    stone = 'epic'
                if x <= 3:
                    stone = 'legendary'
                if stone != None:
                    dtext += ids['name']+': '+portaltotext(stone)+'\n'
                    bot.send_message(441399484, str(users.update_one({'id':ids['id']},{'$inc':{'portals.'+stone:1}})))
                    to_pasyuk += ids['name']+' получает '+portaltotext(stone)+'!\n'
                
    if game['stats_test'] == False:
        for ids in game['allhorses']:
            h = game['allhorses'][ids]
            stats.update_one({},{'$inc':{str(h['index'])+'.games':1}})
    else:
        for ids in game['allhorses']:
            h = game['allhorses'][ids]
            if h['index'] not in spisok:
                spisok.update({h['index']:'lost'})
        
    if game['stats_test'] == False:
        text += '\n\n'
        try:
            bot.send_message(game['id'], text)
        except:
            pass
        text = ''
        time.sleep(3)
        if dtext != '':
          try:
            bot.send_message(441399484, 'Следующие участники нашли на ипподроме камни призыва:\n'+dtext)
        
            bot.send_message(game['id'], 'Следующие участники нашли на ипподроме камни призыва:\n'+dtext)
          except:
            pass
        time.sleep(4)
        bot.send_message(game['id'], 'Конец забега!')
        del games[game['id']]
    else:
        try:
            del games[1]
        except:
            pass
        return spisok
    
        
            
    
    
        
def results(game):
    text = ''
    for ids in game['horses']:
        a = game['horses'][ids]
        if a['bonus'] < 0:
            text += '❄'
        text += htoe(a['name'])+a['name']+': '+str(int((a['distance']/game['lenght'])*100))+'%\n'
    return text


def createduel(id, players, cost):
    pls = {}
    for ids in players:
        pls.update(createduelplayer(ids))
    name = '?'
    types = ['draka', 'chess', 'throw_bottles']
    
    x = random.choice(types)
    if x == 'draka':
        name = 'Драка'
    elif x == 'chess':
        name = 'Шахматы'
    elif x == 'throw_bottles':
        name = 'Бросание бутылок'
    return {id:{
        'id':id,
        'name':name,
        'players':pls,
        'bet':cost,
        'type':x,
        'current_player':None
    }
           }

def createduelplayer(player):
    x = {player['id']:player}
    x.update({
        'progress':0,
        'lastturn':0        # ходов назад
    })
    return x

   
def createbet(user, game, h):
    return {h['index']:{
        'cache':game['minimum'],
        'horse':h['index']
    }
           }


def creategame(m, count = 7, lenght = 1000, minimum = 50, cache = 0, bets = 3, mode = None, tp = False):
    h = {}
    while len(h) < count:
        x = random.choice(horses).copy()
        if x['index'] not in h:
            h.update({x['index']:x})
    for ids in h:
        h[ids].update(toupdate)
    if m != None:
        return {m.chat.id:{
          'id':m.chat.id,
          'players':{},
          'horses':h,
          'lenght':lenght,
          'minimum':minimum,
          'started':False,
          'msg':None,
          'turn':1,
          'text':'',
          'winners':[],
          'cache':cache,
          'delmsgs':[],
          'createtime':time.time(),
          'allhorses':h.copy(),
          'mode':mode,
          'maxbets':bets,
          'stats_test':False,
          'tp':tp,
          'starttime':None
            
        }
               }
    else:
        return {1:{
          'id':1,
          'horses':h,
          'lenght':lenght,
          'msg':None,
          'turn':1,
          'winners':[],
          'allhorses':h.copy(),
          'stats_test':True,
          'tp':tp
            
        }
               }
  
    
def htoe(h):
    x = '❓'
    if h == 'Красная лошадь':
        x = '🔴'
    elif h == 'Синяя лошадь':
        x = '🔵'
    elif h == 'Жёлтая лошадь':
        x = '🌕'
    elif h == 'Чёрная лошадь':
        x = '⚫'
    elif h == 'Морозная лошадь':
        x = '🌨'
    elif h == 'Ненормальная лошадь':
        x = '💊'
    elif h == 'Дорогая лошадь':
        x = '💶'
    elif h == 'Робо-лошадь':
        x = '🤖'
    elif h == 'Токсичная лошадь':
        x = '🤬'
    elif h == 'Быстрая лошадь':
        x = '🌪'
    elif h == 'Межпространственная лошадь':
      x = '👽'
    elif h == 'Лошадь-экскаватор':
      x = '🔨'
    elif h == 'Лошадь-колдун':
      x = '🔮'
    elif h == 'Случайная лошадь':
      x = '❓'
    elif h == 'Войд-лошадь':
      x = '🟣'
    return x
    
  
def check():
    threading.Timer(120, check).start()
    for ids in users.find({}):
        if ids['drunk'] >= 100:
            users.update_one({'id':ids['id']},{'$inc':{'drunk':-1}})
        elif ids['drunk'] > 0:
            users.update_one({'id':ids['id']},{'$inc':{'drunk':-2}})
    for ids in users.find({}):
        if ids['drunk'] < 0:
            users.update_one({'id':ids['id']},{'$set':{'drunk':0}})
    for ids in users.find({}):
        try:
            if time.time() - ids['reboot_time'] > 0:
                users.update_one({'id':ids['id']},{'$set':{'taken_exp':0}})
        except:
            pass

        
def check2():
    threading.Timer(20, check2).start()
    for ids in users.find({}):
        if ids['cook'] != None:
            if time.time() - ids['cook']['work_until'] > 0:
                users.update_one({'id':ids['id']},{'$set':{'cook':None}})
            else:
                if ids['cook']['cooking'] == False:
                    drs = []
                    for idss in ids['current_supplies']:
                        drs.append(ids['current_supplies'][idss])
                    if len(drs) == 0:
                        pass
                    else:
                        dr = random.choice(drs)
                        min = int(30-(ids['cook']['agility']/2))
                        max = int(60-(ids['cook']['agility']/3))
                        if min < 4:
                            min = 4
                        if max < 15:
                            max = 15
                        popitki = 4
                        progress = -25
                        if ids['cook']['intelligence'] >= 20:
                            popitki -= 1
                            progress += 25
                        if ids['cook']['intelligence'] >= 40:
                            popitki -= 1
                            progress += 25 
                        users.update_one({'id':ids['id']},{'$set':{'cook.cooking':True}})
                        cooking(ids, dr, progress, popitki, [min, max], True, cooker=ids['cook'])
                    
                    
def checkbars():
    threading.Timer(120, checkbars).start()
    for ids in alcos:
        s = alcos[ids]
        if s['owner'] != None: 
            allow = False
            owner = users.find_one({'id':s['owner']})
            for ids in owner['current_supplies']:
                if owner['current_supplies'][ids]['amount'] > 0:
                    allow = True
            if allow:
                allow_bars.append(owner['id'])
            else:
                try:
                    allow_bars.remove(owner['id'])
                except:
                    pass
   


        
check()
check2()       
checkbars()  
     
        
        
def medit(message_text, chat_id, message_id, reply_markup=None, parse_mode=None):
    return bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=message_text,
                                    reply_markup=reply_markup,
                                    parse_mode=parse_mode)

    
    
    
for ids in users.find({}):
    text = ''
    if ids['reloadcoins'] > 0:
        users.update_one({'id':ids['id']},{'$inc':{'coins':ids['reloadcoins']}})
        users.update_one({'id':ids['id']},{'$set':{'reloadcoins':0}})
        text += ids['name']+' получает '+str(ids['reloadcoins'])+' монет.\n'
    else:
        users.update_one({'id':ids['id']},{'$set':{'reloadcoins':0}})
    if text != '':
        bot.send_message(441399484, text)
 

def createchat(chat):
    return {
        'id':chat.id,
        'title':chat.title,
        'notifications':True,
        'adminmode':False
    }
   

for ids in chats.find({}):
    try:
        bot.send_message(441399484, ids)
    except:
        pass
    if ids['notifications'] == True:
        try:
            if ids['id'] < 0:
                bot.send_message(ids['id'], 'Бот был перезагружен, все текущие игры были удалены. Если вы хотите отключить эти уведомления, нажмите команду /notifications.')
        except:
            pass
