#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2017-07-28 12:36:22
# @Author  : Chen Qiqian (qiqianchen@gmail.com)
# @Link    : https://github.com/ChenQiqian
# @Version : $Id$ 1.0

people = []


def create_list(p=30):  # create a list of 30 person
    global people
    tmp_l = []
    while len(tmp_l) < p:
        tmp_l.append([])
    people = tmp_l


def fill_in_list(p=30, e=6):  # fill the enemy into the person's list
    global people
    last = 1
    tmp = 0
    for person in range(p):
        for i in range(30):
            if len(people[person]) >= e:
                last = tmp + 1
                break
            tmp = last + i
            if tmp > (p - 1):
                tmp = tmp - (p - 1) + person
            people[person].append(tmp)
        for enemy in people[person]:
            if person not in people[enemy]:
                people[enemy].append(person)


def give_all_poss(p=30):
    tmp = []
    for p1 in range(p):
        for p2 in range(p):
            for p3 in range(p):
                poss = [p1, p2, p3]
                if p1 == p2 or p1 == p3 or p2 == p3:
                    continue
                tmp.append(poss)
    return tmp


def get_right_count(poss_list):
    count = 0
    for poss in poss_list:
        score = 0
        if poss[0] in people[poss[1]]:
            score += 1
        else:
            score -= 1

        if poss[0] in people[poss[2]]:
            score += 1
        else:
            score -= 1

        if poss[2] in people[poss[1]]:
            score += 1
        else:
            score -= 1
        if score == 3 or score == -3:
            count += 1
    return(count / (3 * 2 * 1))


# calculate the number of possibilties
create_list()
fill_in_list()
result = get_right_count(give_all_poss())
print("Numbers:" + str(int(result)))

"""
problem:
议会中共有30位议员，任何两位议员或者为政友，或者为政敌。
今知，每位议员都刚好有六个政敌。
现要在其中选择三个议员组成一个委员会，使其中任何两人都是政敌或任何两人都是政友。
试求这样的委员会的数目。
————1990年苏联数学竞赛题
"""
