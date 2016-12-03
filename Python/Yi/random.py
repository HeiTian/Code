#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import qianGuaHua
import kunGuaHua

chuYao = (random.choice('阴阳'))
erYao = (random.choice('阴阳'))
sanYao = (random.choice('阴阳'))
siYao = (random.choice('阴阳'))
wuYao = (random.choice('阴阳'))
shangYao = (random.choice('阴阳'))

huaGua =str(chuYao) + str(erYao) + str(sanYao) + str(siYao) + str(wuYao) + str(shangYao)
print (huaGua)

if chuYao == '阳':
    qianGuaHua.draw_chuYaoYang_star_flag()
else:
    kunGuaHua.draw_chuYaoYin_star_flag()

if erYao == '阳':
    qianGuaHua.draw_erYaoYang_star_flag()
else:
    kunGuaHua.draw_erYaoYin_star_flag()

if sanYao == '阳':
    qianGuaHua.draw_sanYaoYang_star_flag()
else:
    kunGuaHua.draw_sanYaoYin_star_flag()

if siYao == '阳':
    qianGuaHua.draw_siYaoYang_star_flag()
else:
    kunGuaHua.draw_siYaoYin_star_flag()

if wuYao == '阳':
    qianGuaHua.draw_wuYaoYang_star_flag()
else:
    kunGuaHua.draw_wuYaoYin_star_flag()

if shangYao == '阳':
    qianGuaHua.draw_shangYaoYang_star_flag()
else:
    kunGuaHua.draw_shangYaoYin_star_flag()




