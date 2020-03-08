#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, create_engine, Integer, or_
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class Stat(Base):
    # 表的名字:
    __tablename__ = 'stats'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    uuid = Column(String(100))
    username = Column(String(100))
    kills = Column(Integer)
    deaths = Column(Integer)
    lms = Column(Integer)
    brackets = Column(Integer)
    party_vs_party_wins = Column(Integer)
    elo_nodebuffelo = Column(Integer)
    elo_debuffelo = Column(Integer)
    elo_builduhcelo = Column(Integer)
    elo_gappleelo = Column(Integer)
    elo_soupelo = Column(Integer)
    elo_comboelo = Column(Integer)
    elo_sumoelo = Column(Integer)
    elo_sumobestof3elo = Column(Integer)
    elo_nodebuffelopremium = Column(Integer)
    elo_hcfelo = Column(Integer)
    elo_axepvpelo = Column(Integer)
    global_elo = Column(Integer)
    elo_abcelo = Column(Integer)
    elo_abc = Column(Integer)
    elo_potion = Column(Integer)
    elo_bedwars = Column(Integer)

    # fights = relationship('Fight')


class Fight(Base):
    __tablename__ = 'fights'

    id = Column(Integer, primary_key=True)
    playback = Column(String(100))
    winners = Column(String(1000))
    losers = Column(String(1000))
    kit_info = Column(String(128))
    arena = Column(String(1000))
    started = Column(Integer)
    ended = Column(Integer)
    winners_old_elos = Column(String(128))
    losers_old_elos = Column(String(128))
    winners_new_elos = Column(String(128))
    losers_new_elos = Column(String(128))
    inventories = Column(String(5000))
    hits = Column(String(16))
    longest_combo = Column(String(16))
    potions_thrown = Column(String(16))
    potions_missed = Column(String(16))
    potion_accuracy = Column(String(16))


# 初始化数据库连接:
# engine = create_engine('mysql+mysqlconnector://minecraft:goodview@lxcmcdb:3306/YoStrikePractice')
# 创建DBSession类型:
# DBSession = sessionmaker(bind=engine)

# 创建session对象:
# session = DBSession()
# 创建新User对象:
# new_user = User(id='5', name='Bob')
# 添加到session:
# session.add(new_user)
# 提交即保存到数据库:
# session.commit()
# 关闭session:
# session.close()

# 创建Session:
# session = DBSession()

# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
# user = session.query(User).filter(User.username == 'yoztw').one()
# stat = session.query(Stat).filter(Stat.username == 'yoztw').first()
# 打印类型和对象的name属性:
# print('type:', type(stat))
# print('uuid:', stat.uuid)
# print('username:', stat.username)

# for stat in session.query(Stat).filter(Stat.username == 'chsliu'):
# 打印类型和对象的name属性:
# print('type:', type(stat))
# print('uuid:', stat.uuid)
# print('username:', stat.username)
# print('kills:', stat.kills)
# print('deaths:', stat.deaths)
# print('lms:', stat.lms)
# print('brackets:', stat.brackets)
# print('party_vs_party_wins:', stat.party_vs_party_wins)

# 关闭Session:
# session.close()

# def init():
# 初始化数据库连接:
# engine = create_engine('mysql+mysqlconnector://minecraft:goodview@lxcmcdb:3306/YoStrikePractice')
# 创建DBSession类型:
# DBSession = sessionmaker(bind=engine)

# 创建Session:
# session = DBSession()

# def query(username):
#     return session.query(Stat).filter(Stat.username == username)

# def close():
# 关闭Session:
# session.close()

class StrikeDB():
    def __init__(self):
        # print("__init__")
        # 初始化数据库连接:
        engine = create_engine('mysql+mysqlconnector://minecraft:goodview@lxcmcdb:3306/YoStrikePractice')
        # 创建DBSession类型:
        self.DBSession = sessionmaker(bind=engine)
        self.isOpen = False
        self.openSession()

    def openSession(self):
        # 创建Session:
        if self.isOpen != True:
            try:
                self.session = self.DBSession()
                self.isOpen = True
            except:
                print("StrikeDB session 開啟失敗")

    def getStatByUsername(self, username):
        results = None
        try:
            self.openSession()
            results = self.session.query(Stat).filter(Stat.username == username)
        except:
            print("StrikeDB query 執行失敗")
            self.closeSession()
        return results

    def getFightByUsername(self, username):
        results = None
        try:
            self.openSession()
            stats = self.getStatByUsername(username)
            if stats is None: return results
            if len(stats.all()) == 0: return results
            for stat in stats:
                name = str(stat.uuid)+":"+username
                results = self.session.query(Fight).filter(or_(Fight.winners == name,Fight.losers == name))
                # results = self.session.query(Fight).filter(Fight.winners == name)
                if len(results.all()) > 0: break
        except:
            print("StrikeDB query 執行失敗")
            self.closeSession()
        return results

    def closeSession(self):
        if self.isOpen:
            # 关闭Session:
            self.session.close()
            self.isOpen = False

    def __del__(self):
        # print("__del__")
        self.closeSession()
