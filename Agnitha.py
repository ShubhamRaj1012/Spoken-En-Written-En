# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yMfOW1zTUiXFTZVQU6TV1IeAYhCMarwz
"""

def get_rules():
    rules = {"Numbers":{
                        "zero": 0,
                        "one" : 1,
                        "two": 2,
                        "three": 3,
                        "four": 4,
                        "five": 5,
                        "six": 6,
                        "seven": 7,
                        "eight": 8,
                        "nine": 9,
                        "ten": 10,
                        "twenty": 20,
                        "thirty": 30,
                        "forty": 40,
                        "fifty": 50,
                        "sixty": 60,
                        "seventy": 70,
                        "eighty": 80,
                        "ninety": 90,
                        "hundred": 100
                        },
            "Tuples": {
                         "single":1,
                         "double":2,
                         "triple":3,
                         "quadruple":4,
                         "quintuple":5,
                         "sextuple":6,
                         "septuple":7,
                         "octuple":8,
                         "nonuple":9,
                         "decuple":10
                      },
            "General": {
                          "C M": "CM",
                          "P M": "PM",
                          "D M": "DM",
                          "A M": "AM"
                       }
            }
    return rules


def punc_check(word):
    front=""
    last=""
    if(len(word)>1):
        if word[-1]==',' or word[-1]=='.':
            last=word[-1]
            word=word[:-1]
        if word[0]==',' or word[0]=='.':
            front=word[0]
            word=word[1:]
    return front,word,last


class final:

    def __init__(self):

        self.rules=get_rules()
        self.para=""
        self.ouptut_para=""

    
    def init_input(self):

        self.para=input("\n[IN]:Enter Your para of spoken english:\n\t")

        if not self.para:
            raise ValueError("[Error]: You entered nothing.")

    
    def final_output(self):
        print("\n[OUT]:The input Spoken English para: \n\n \" "+ self.para+"\"")
        print("\nConverted Written English para: \n\n \"" +self.ouptut_para+"\"")

    
    def Convert(self):
        
        words_of_para=self.para.split()

        
        numbers=self.rules['Numbers']
        tuples=self.rules['Tuples']
        general=self.rules['General']
        i=0
        no_of_words=len(words_of_para)
      
        while i<no_of_words: 
            
            front,word,last=punc_check(words_of_para[i])
            
            if i+1!= no_of_words:
            
                front_n,next_word,last_n=punc_check(words_of_para[i+1])
                if word.lower() in numbers.keys() and (next_word.lower()=='dollars' or next_word.lower()=='dollar'):
                    self.ouptut_para=self.ouptut_para+" "+front+"$"+str(numbers[word.lower()])+last
                    i=i+2

                elif word.lower() in tuples.keys() and len(next_word)==1:
                    self.ouptut_para=self.ouptut_para+" "+front_n+(next_word*tuples[word.lower()])+last_n
                    i=i+2
                elif (word+" "+next_word) in general.keys():
                    self.ouptut_para=self.ouptut_para+" "+front+word+next_word+last_n
                    i=i+2
                else:
                    self.ouptut_para=self.ouptut_para+" "+words_of_para[i]
                    i=i+1
            else:
                self.ouptut_para=self.ouptut_para+" "+words_of_para[i]
                i=i+1



def convert_sp_to_wr():
    obj_spoken=final()
    obj_spoken.init_input()
    obj_spoken.Convert()
    obj_spoken.final_output()