#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import random
import os

def match2(c2):
  switch = {
    "aa": [u'ꜳ'],
    "ae": [u'æ'],
    "oo": [u'ꝏ'],
    "au": [u'ꜷ'],
    "tz": [u'ꜩ']
  }
  arr = switch.get(cc, [cc])
  return random.choice(arr)

def match(c):
  switch = {
    'a': [u'à', u'á', u'â', u'ä', u'ã', u'å', u'ā', u'ⱥ'],
    'b': [u'ƀ'],
    'c': [u'ç', u'ć', u'č', 'ꞓ', 'ȼ'],
    'd': [u'đ', u'ɖ'],
    'e': [u'è', u'é', u'ê', u'ë', u'ē', u'ė', u'ę', 'ɇ'],
    'f': [u'ſ'],
    'g': [u'ꞡ', u'ǥ'],
    'h': [u'ɦ', u'ḥ'],
    'i': [u'î', u'ï', u'í', u'ī', u'į', u'ì'],
    'j': [u'ɉ'],
    'k': [u'ꝅ', 'ꝁ'],
    'l': [u'ł', 'ƚ'],
    'n': [u'ñ', u'ń'],
    'o': [u'ô', u'ö', u'ò', u'ø', u'ō', u'õ', 'ꝋ'],
    'q': [u'ꝙ', u'ꝗ'],
    'r': [u'ɍ', u'ꞧ'],
    's': [u'ś', u'š'],
    'u': [u'û', u'ü', u'ù', u'ú', u'ū', 'ʉ'],
    'v': [u'ꝟ'],
    'y': [u'ÿ'],
    'z': [u'ž', u'ź', u'ż'],

    'A': [u'À', u'Á', u'Â', u'Ã', u'Ä', u'Å', u'Ā', u'Ă', u'Ą', u'Ⱥ'],
    'B': [u'Ɓ', u'Ƀ'],
    'C': [u'Ç', u'Ć', u'Ĉ', u'Ċ', u'Č', u'Ƈ', u'Ȼ'],
    'D': [u'Ð', u'Ď', u'Đ', u'Ɗ'],
    'E': [u'È', u'È', u'É', u'Ê', u'Ë', u'Ē', u'Ĕ', u'Ė', u'Ę', u'Ě'],
    'F': [u'Ƒ'],
    'G': [u'Ĝ', u'Ğ', u'Ġ', u'Ģ', u'Ɠ'],
    'H': [u'Ĥ', u'Ħ'],
    'I': [u'Ì', u'Í', u'Î', u'Ï'],
    'K': [u'Ķ'],
    'L': [u'Ĺ', u'Ļ', u'Ľ', u'Ŀ', u'Ł'],
    'N': [u'Ñ', u'Ń', u'Ņ', u'Ň'],
    'O': [u'Ò', u'Ó', u'Ô', u'Õ', u'Ö', u'Ø', u'Ō', u'Ơ'],
    'R': [u'Ȑ', u'Ȓ', u'Ɍ'],
    'S': [u'Ș'],
    'T': [u'Ⱦ', u'Ţ', u'Ť', u'Ŧ'],
    'U': [u'Ù', u'Ú', u'Û', u'Ü', 'Ǖ', u'Ǘ'],
    'Y': [u'Ý', u'Ɏ'],
    'Z': [u'Ź']
  }
  arr = switch.get(c, [c])
  return random.choice(arr)

for c in " ".join(sys.argv[1:]):
  sys.stdout.write(match(c))
sys.stdout.write("\n")
