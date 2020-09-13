#-*- coding: utf-8 -*-

import os.path
import pandas
import re
from libraries.ProjectPaths import make_data_path

##############################################
################# Kaomojis ###################
##############################################

def getKaomojiDict():
    data_path=make_data_path('Kaomoji.csv')
    kao_df = pandas.read_csv(data_path)
    kao_df.index += 1
    k_dict = dict(zip(kao_df.index, kao_df.Kaomoji))
    return k_dict

def Kaomoji_totag(text, k_dict):
    text_tagged = text
    kaomojis = [item for item in k_dict.items() if item[1] in text_tagged]
    for item in kaomojis:
        re_str = u'((?<![^\u4e00-\u9fff\s]){}(?=([\u4e00-\u9fff\s]|$)))'.format(re.escape(item[1]))
        tag = "<kao>{}</kao>".format(item[0])
        text_tagged = re.sub(re_str, tag ,text_tagged)
    return text_tagged

def Segmented_tagged(seg_text):
    seg_text_tagged = seg_text.replace("< k a o>","<kao>").replace("<k a o>","<kao>").replace("< k a o >","<kao>").replace("<k a o >","<kao>")
    seg_text_tagged = seg_text_tagged.replace("</k a o>","</kao>").replace("</k a o >","</kao>").replace("</ k a o>","</kao>").replace("</ k a o >","</kao>")
    seg_text_tagged = seg_text_tagged.replace(" </kao>","</kao>").replace("<kao> ","<kao>")
    return seg_text_tagged

def KaoTag_toKaomoji(seg_text_tagged, k_dict):
    kaomoji_tags = re.findall(u'((?<=\<kao\>)[0-9]*(?=\<\/kao\>))',seg_text_tagged)
    kaomojis = [int(tag) for tag in kaomoji_tags]
    seg_replaced = seg_text_tagged
    for kao in kaomojis:
        re_str = u'(<kao>{}</kao>)'.format(kao)
        kaomoji = k_dict.get(kao)
        seg_replaced = re.sub(re_str,kaomoji, seg_replaced)
    return seg_replaced

if __name__ == '__main__':
    pass

