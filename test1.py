#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test1.py
# @Author: Hu
# @Date  : 2018/12/23
# @Desc  : demo


def doc():
    '''
    This is a test project
    '''
    help(doc)
    doc.__doc__


class Hero():
    name = "英雄"
    level = 1
    ATK = 50
    HP = 200

    def introduction(self):
        print("英雄的攻击力是{}".format(self.ATK))
        print("英雄的生命值是{}".format(self.HP))
        print("英雄的名字是{}".format(self.name))
        return None

    def action(self):
        print("攻击")
wizard = Hero()
wizard.name = "法师"


class DefendBuilding():
    name = "建筑"
    level = 1
    ATK = 100
    HP = 500
    # 属性

    def action(self):
        print("防御")
        return None
    # 动作或功能


class resource():

    name = "资源"
    count = "1000"

    def action1(self):
        self.name = "圣水"
        self.count = 2000
        print("{0}的数量是{1}".format(self.name, self.count))

# acher_tower = DefendBuilding()
# bacher_tower.action()
# print("弓箭塔的等级是:", acher_tower.level)
# print("弓箭塔的攻击力是:", acher_tower.ATK)

# print(DefendBuilding.__dict__)

# wizard.action()
# wizard.introduction()
