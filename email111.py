#!/usr/bin/python
# -*- coding: utf8 -*-
import zmail
import os
import io
import sys

server = zmail.server('2176298760@qq.com', 'hhkjftdraelweaag',smtp_host='smtp.qq.com',smtp_port=465,smtp_ssl=False,pop_host='pop.qq.com',pop_port=995,pop_tls=False)
mail = server.get_latest()

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
zmail.show(mail)
