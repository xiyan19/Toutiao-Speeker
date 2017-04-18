# -*- coding: utf-8 -*-

"""
    此脚本用于今日头条文章自动刷评论。

    Last commit info:
    ~~~~~~~~~~~~~~~~~
    $LastChangedDate: 1/9/2017
    $Annotation: Create.
    $Author: xiyan19
"""


import sys, time
from splinter import Browser

browser = Browser('chrome')


def login(userName, password):
    browser.find_by_css('div.nav-login').click()
    browser.find_by_css('li.qzone').click()

    browser.windows.current = browser.windows[1]

    browser.find_by_css('input.input_id').fill(userName)
    browser.find_by_css('input.input_pwd').fill(password)
    browser.find_by_id('go').click()

    # '[-] ' + userName +' login failed!'
    print('[+] ' + userName +' login successed!')

    return


def chatter(url, context):
    browser.windows.current = browser.windows[0]
    browser.visit(url)
    browser.find_by_name('inputText').fill(context)
    browser.find_by_css('div.c-submit').click()
    print('[+] Chatter: ' + context)

    return


def logout(userName):
    browser.visit('http://web.toutiao.com/auth/logout/')

    print('[+] ' + userName +' logout successed!')


if __name__ == '__main__':
    homepage = 'http://www.toutiao.com'
    url = sys.argv[1]

    browser.visit(homepage)

    userName = ''
    password = ''
    login(userName, password)

    time.sleep(5)

    context = "挺有意思的！"
    chatter(url, context)

    logout(userName)

    return