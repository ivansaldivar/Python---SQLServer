#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Cabecera.
import cgi

print("Content-Type: text/html; charset=utf-8\n\r")
print("")

with open("WebPage1.html") as f:
    print(f.read())

