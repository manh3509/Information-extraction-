import spacy
from spacy.matcher import Matcher 
from spacy import displacy
from IPython.display import Image, display
import glob
import pandas as pd
import re, locale
# tải mô hình ngôn ngữ tiếng anh
# 
nlp = spacy.load('en_core_web_sm',disable=['ner','textcat'])
nlp2 = spacy.load("en_core_web_sm")
pat = []
#rút trích tên riêng
def rule2(text):
    doc = nlp(text)
    pat = []
    for token in doc:
        phrase = ''
        # extract subject
        if (token.pos_=='PROPN'):
                    phrase += token.text + ' '      
        if  len(phrase)!=0:
            pat.append(phrase)
    return pat

def rule2_n(text):
    doc = nlp(text)
    pat = []
    for token in doc:
        phrase = ''
        # extract subject
        if (token.pos_=='NOUN'):
                    phrase += token.text + ' '      
        if  len(phrase)!=0:
            pat.append(phrase)
    return pat

def rule2_adj(text):
    doc = nlp(text)
    pat = []
    for token in doc:
        phrase = ''
        # extract subject
        if (token.pos_=='ADJ'):
                    phrase += token.text + ' '      
        if  len(phrase)!=0:
            pat.append(phrase)
    return pat

def rule2_adv(text):
    doc = nlp(text)
    pat = []
    for token in doc:
        phrase = ''
        # extract subject
        if (token.pos_=='ADV'):
                    phrase += token.text + ' '      
        if  len(phrase)!=0:
            pat.append(phrase)
    return pat

def rule2_adp(text):
    doc = nlp(text)
    pat = []
    for token in doc:
        phrase = ''
        # extract subject
        if (token.pos_=='ADP'):
                    phrase += token.text + ' '      
        if  len(phrase)!=0:
            pat.append(phrase)
    return pat   

def rule2_v(text):
    doc = nlp(text)
    pat = []
    for token in doc:
        phrase = ''
        # extract subject
        if (token.pos_=='VERB'):
                    phrase += token.text + ' '      
        if  len(phrase)!=0:
            pat.append(phrase)
    return pat


def rule2_mod(text,index):
    
    doc = nlp(text)

    phrase = ''
    
    for token in doc:
        
        if token.i == index:
            
            for subtoken in token.children:
                if (subtoken.pos_ == 'ADJ'):
                    phrase += ' '+subtoken.text
            break
    
    return phrase
def rule2_num(text):
    doc = nlp(text)
    pat = []
    for token in doc:
        phrase = ''
        # extract subject
        if (token.pos_=='NUM'):
            phrase += token.text + ' '      
        if  len(phrase)!=0:
            pat.append(phrase)
    return pat






###Bảng 1!!!
#############################################################################
def rule2_loc(text):
    doc = nlp2(text)
    pat = []
    for ent in doc.ents:
        phrase = ''
        if (ent.label_ == 'LOC'):
            phrase += ent.text + ' ' 
        if  len(phrase)!=0:
            pat.append(phrase)   
    return pat

def rule2_org(text):
    doc = nlp2(text)
    pat = []
    for ent in doc.ents:
        phrase = ''
        if (ent.label_ == 'ORG'):
            phrase += ent.text + ' ' 
        if  len(phrase)!=0:
            pat.append(phrase)   
    return pat
def rule2_geo(text):
    doc = nlp2(text)
    pat = []
    for ent in doc.ents:
        phrase = ''
        if (ent.label_ == 'GEO'):
            phrase += ent.text + ' ' 
        if  len(phrase)!=0:
            pat.append(phrase)   
    return pat
def rule2_per(text):
    doc = nlp2(text)
    pat = []
    for ent in doc.ents:
        phrase = ''
        if (ent.label_ == 'PERSON'):
            phrase += ent.text + ' ' 
        if  len(phrase)!=0:
            pat.append(phrase)   
    return pat
def rule2_gpe(text):
    doc = nlp2(text)
    pat = []
    for ent in doc.ents:
        phrase = ''
        if (ent.label_ == 'GPE'):
            phrase += ent.text + ' ' 
        if  len(phrase)!=0:
            pat.append(phrase)   
    return pat
def rule2_tim(text):
    doc = nlp2(text)
    pat = []
    for ent in doc.ents:
        phrase = ''
        if (ent.label_ == 'TIME'):
            phrase += ent.text + ' ' 
        if  len(phrase)!=0:
            pat.append(phrase)   
    return pat
def rule2_percent(text):
    doc = nlp2(text)
    pat = []
    for ent in doc.ents:
        phrase = ''
        if (ent.label_ == 'PERCENT'):
            phrase += ent.text + ' ' 
        if  len(phrase)!=0:
            pat.append(phrase)   
    return pat
#################################################################################
###Bảng 2!!!
#############################################################################
def rule2_art(text):
    doc = nlp2(text)
    pat = []
    for ent in doc.ents:
        phrase = ''
        if (ent.label_ == 'ART'):
            phrase += ent.text + ' ' 
        if  len(phrase)!=0:
            pat.append(phrase)   
    return pat

def rule2_eve(text):
    doc = nlp2(text)
    pat = []
    for ent in doc.ents:
        phrase = ''
        if (ent.label_ == 'EVE'):
            phrase += ent.text + ' ' 
        if  len(phrase)!=0:
            pat.append(phrase)   
    return pat
def rule2_nat(text):
    doc = nlp2(text)
    pat = []
    for ent in doc.ents:
        phrase = ''
        if (ent.label_ == 'NAT'):
            phrase += ent.text + ' ' 
        if  len(phrase)!=0:
            pat.append(phrase)   
    return pat
def rule2_date(text):
    doc = nlp2(text)
    pat = []
    for ent in doc.ents:
        phrase = ''
        if (ent.label_ == 'DATE'):
            phrase += ent.text + ' ' 
        if  len(phrase)!=0:
            pat.append(phrase)   
    return pat
def rule2_lan(text):
    doc = nlp2(text)
    pat = []
    for ent in doc.ents:
        phrase = ''
        if (ent.label_ == 'LANGUAGE'):
            phrase += ent.text + ' ' 
        if  len(phrase)!=0:
            pat.append(phrase)   
    return pat
def rule2_money(text):
    doc = nlp2(text)
    pat = []
    for ent in doc.ents:
        phrase = ''
        if (ent.label_ == 'MONEY'):
            phrase += ent.text + ' ' 
        if  len(phrase)!=0:
            pat.append(phrase)   
    return pat
def rule2_car(text):
    doc = nlp2(text)
    pat = []
    for ent in doc.ents:
        phrase = ''
        if (ent.label_ == 'CARDINAL'):
            phrase += ent.text + ' ' 
        if  len(phrase)!=0:
            pat.append(phrase)   
    return pat

def rule2_product(text):
    doc = nlp2(text)
    pat = []
    for ent in doc.ents:
        phrase = ''
        if (ent.label_ == 'PRODUCT'):
            phrase += ent.text + ' ' 
        if  len(phrase)!=0:
            pat.append(phrase)   
    return pat
#################################################################################




def rule3(text):
    
    doc = nlp(text)

    pat = []
    
    # lặp lại các mã thông báo
    for token in doc:
        phrase = ''
        # nếu từ là một danh từ chủ ngữ hoặc một danh từ tân ngữ
        if (token.pos_ == 'NOUN')\
            and (token.dep_ in ['dobj','pobj','nsubj','nsubjpass']):
            
            # lặp qua các nút con
            for subtoken in token.children:
                # nếu từ là một tính từ hoặc có một phụ thuộc ghép
                if (subtoken.pos_ == 'ADJ') or (subtoken.dep_ == 'compound'):
                    phrase += subtoken.text + ' '
                    
            if len(phrase)!=0:
                phrase += token.text
        
        if (token.pos_=='VERB'):
            
            # chỉ trích chủ ngữ danh từ hoặc đại từ
            for sub_tok in token.lefts:
                
                if (sub_tok.dep_ in ['nsubj','nsubjpass']) and (sub_tok.pos_ in ['NOUN','PROPN','PRON']):
                    
                    # tìm công cụ sửa đổi chủ đề
                    adj = rule2_mod(text,sub_tok.i)
                    
                    phrase += adj + ' ' + sub_tok.text

                    # lưu từ gốc của từ
                    phrase += ' '+token.lemma_ 

                    # kiểm tra đối tượng trực tiếp danh từ hoặc đại từ
                    for sub_tok in token.rights:
                        
                        if (sub_tok.dep_ in ['dobj']) and (sub_tok.pos_ in ['NOUN','PROPN']):
                            
                            # tìm kiếm công cụ sửa đổi đối tượng
                            adj = rule2_mod(text,sub_tok.i)
                            
                            phrase += adj+' '+sub_tok.text
        if token.pos_=='ADP':
    
            phrase = ''
            
            # nếu từ đứng đầu của nó là một danh từ
            if token.head.pos_=='NOUN':
                
                # nối danh từ và giới từ vào cụm từ
                phrase += token.head.text
                phrase += ' '+token.text

                # kiểm tra các nút ở bên phải của giới từ
                for right_tok in token.rights:
                    # nối nếu nó là một danh từ riêng hoặc danh từ riêng
                    if (right_tok.pos_ in ['NOUN','PROPN']):
                        phrase += ' '+right_tok.text
                            
        if  len(phrase)!=0:
            pat.append(phrase) 
    return pat

