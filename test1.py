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
    pass
wizard = Hero()

class DefendBuilding():
    level = 1
    ATK = 100
    HP = 500
    # 属性
    def action(self):
        print("防御")
        return None
    # 动作或功能
acher_tower = DefendBuilding()
acher_tower.action()
