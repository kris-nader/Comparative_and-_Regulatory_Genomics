# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 18:06:22 2020

@author: user
"""
import re 
import math
import matplotlib.pyplot as plt

          
def parse_alignment(path):
    temp_array=[]
    n=-1
    c=0    
    alignfile1=open(path,"r")
    temp_array=[]
    for x in alignfile1:  
        if not x.startswith("\n") and (x.startswith("WP") or x.startswith("YP")):
            temp_line=x.split(None,2)
            temp_array.append(temp_line[1])
            c=c+1
        else:
            if x.startswith("\n"):
                n=n+1
    return temp_array,c,n
      

def make_string(temp_array):
    temp_array0=temp_array[0]
    c=temp_array[1]
    n=temp_array[2]
    s=int(c/n)
    align_array=[str() for k in 'k' * int(c/n)]
    j=0
    for i in range(0,c):
        if j<=int(s-1):
            align_array[j]=list(align_array[j])+list(temp_array0[i])
            j=j+1
        else:
            j=0
            align_array[j]=list(align_array[j])+list(temp_array0[i])
            j=j+1
    return align_array,c,n


def positionalfreq(j,align_array): 
    align_array0=align_array[0]
    positional_freq={}
    for i in range(0,len(align_array0)):
        if align_array0[i][j] not in positional_freq:
            positional_freq[align_array0[i][j]]=1
        else:
            positional_freq[align_array0[i][j]]=positional_freq[align_array0[i][j]]+1
    return positional_freq   


#calculate the shannon entropy in that position
def calculate_conservation(align_array):
    shannon_entropty=[]
    simpson_diversity=[]
    c=align_array[1]
    n=align_array[2]
    s=int(c/n)
    for i in range(0,len(align_array[0][1])-1):
        running_sum=0
        running_diversity=0
        positional_freq=positionalfreq(i,align_array)
        for keys in positional_freq:
            running_sum=running_sum+((positional_freq[keys]/s)*math.log2(positional_freq[keys]/s))
            running_diversity=running_diversity+(positional_freq[keys]*(positional_freq[keys]-1))
        shannon_entropty.append((-1)*running_sum)
        simpson_diversity.append(+1-running_diversity/(s*(s-1)))
    return simpson_diversity,shannon_entropty


def plot_conservation(temp):
   x = [*range(0, len(temp[0]), 1)]
   fig, ax = plt.subplots()
   ax.plot(x, temp[1], '-b', label='Shannon Entropy',color="orange")
   ax.plot(x, temp[0], '-r', label='Simpson Diversity',color="pink")
   leg = ax.legend(); 
   plt.show()
  
      
def plot_portion_conservation(temp,start,end):
    x = [*range(start, end, 1)]
    fig, ax = plt.subplots()
    ax.plot(x, temp[1][start:end], '-b', label='Shannon Entropy',color="orange")
    ax.plot(x, temp[0][start:end], '-r', label='Simpson Diversity',color="pink")
    leg = ax.legend(); 
    plt.show()

def plot_portion_conservation_simpson(temp,start,end):
    x = [*range(start, end, 1)]
    fig, ax = plt.subplots()
    ax.plot(x, temp[0][start:end], '-r', label='Simpson Diversity',color="pink")
    leg = ax.legend(); 
    plt.show()

def analysis(path):
    temp_array=parse_alignment(path)  
    align_array=make_string(temp_array)  
    temp=calculate_conservation(align_array) 
    return(temp)
    

##############MAIN###############
alignfile1="C:\\Users\\user\\Desktop\\assignmentGraded\\new_algine\\seqdump.aln"
conservation=analysis(alignfile1)  
plot_conservation(conservation)
plot_portion_conservation(conservation,127,170)

plot_portion_conservation(conservation,300,450)
plot_portion_conservation(conservation,350,359)
plot_portion_conservation_simpson(conservation,300,450)
plot_portion_conservation_simpson(conservation,0,100)
plot_portion_conservation_simpson(conservation,100,200)
plot_portion_conservation_simpson(conservation,200,300)
plot_portion_conservation_simpson(conservation,300,400)
plot_portion_conservation_simpson(conservation,400,500)
plot_portion_conservation_simpson(conservation,500,600)
plot_portion_conservation_simpson(conservation,700,800)
plot_portion_conservation_simpson(conservation,800,900)
plot_portion_conservation_simpson(conservation,900,1000)
plot_portion_conservation_simpson(conservation,1000,1100)
plot_portion_conservation_simpson(conservation,1000,1100)
plot_portion_conservation_simpson(conservation,1100,1200)
plot_portion_conservation_simpson(conservation,1200,1300)
plot_portion_conservation_simpson(conservation,1400,1500)
plot_portion_conservation_simpson(conservation,1500,1600)


plot_conservation(conservation,163,200)
plot_portion_conservation(conservation,400,500)




