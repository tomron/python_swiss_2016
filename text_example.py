# -*- coding: utf-8 -*-

print len(u'ü')  # 1
print len('ü')   # 2
print len(u'ü'.encode('utf-8')) # 2
print len(u'ü'.encode('latin1'))  # 1
print u'ü'.encode('utf-8')  # terminal encoding is utf-8
print u'ü'.encode('latin1') # it cannot understand the latin1 byte
