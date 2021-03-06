# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 20:46:49 2020

@author: Krristen Michelle Nader
Best Bi-directional hits 
"""


# def blast_results(blastfile):
#     uni_hit={}
#     validate=0 
#     for x in blastfile:
#         if x.startswith("Query="):
#             get_key="".join(x.split('=')).split()[1]
#         else:
#             if(x.startswith("Sequences producing significant alignments: ")):
#                 validate=1 
#             if( x.startswith("\n") and validate==1):
#                 validate=2
#             if ( not x.startswith("\n") and validate==2):
#                 get_value=x.split()[0]
#                 uni_hit[get_key]=get_value
#                 validate=0       
#     blastfile.close()
#     return uni_hit

# uni_hit={}
# validate=0
# p=0
# for x in blast_merged_1:
#     if x.startswith("Query="):
#         get_key="".join(x.split('=')).split()[1]
#         uni_hit[get_key]=[]
#     else:
#         if(x.startswith("Sequences producing significant alignments: ")):
#             validate=1 
#         if( x.startswith("\n") and validate==1 and not x.startswith("Query") and not x.startswith("Sbjct") and not x.startswith(" ")):
#             validate=2
#         if ( not x.startswith("\n") and validate==2 and (x.startswith("YP") or x.startswith("WP"))):
#             get_value=x.split()[0]
#             if (get_value!=get_key):
#                 uni_hit[get_key].append(get_value)
#                 p=p+1
#                 if p==3:
#                     validate=0
                          
#     blastfile.close()
            
    
    
    
    
    
    
    
    
#easier way 
uni_hit_1={}
blast_merged_1=open("C:\\Users\\user\\Desktop\\assignmentGraded\\merged_db\\mergedDB_v1query.txt","r")

for x in blast_merged_1:
    if x.startswith("Query="):
        get_key="".join(x.split('=')).split()[1]
        uni_hit_1[get_key]=[]
    else:
        if x.startswith("YP") or x.startswith("WP"):
            uni_hit_1[get_key].append(x.split()[0])
        


uni_hit_2={}
blast_merged_2=open("C:\\Users\\user\\Desktop\\assignmentGraded\\merged_db\\mergedDB_v2query.txt","r")

for x in blast_merged_2:
    if x.startswith("Query="):
        get_key="".join(x.split('=')).split()[1]
        uni_hit_2[get_key]=[]
    else:
        if x.startswith("YP") or x.startswith("WP"):
            uni_hit_2[get_key].append(x.split()[0])                  
    
# find in paralogs
inpar_1={}
BBH_1={}
k=0
for keys in uni_hit_1:
    if len(uni_hit_1[keys])==1:
        k=k+1
    else:
        i=1
        while not uni_hit_1[keys][i].startswith("WP"):
                inpar_1[keys]=uni_hit_1[keys][i]
                i=i+1
        if uni_hit_1[keys][i].startswith("WP"):
            BBH_1[keys]=uni_hit_1[keys][i]
                
                
inpar_2={}
BBH_2={}
k=0
for keys in uni_hit_2:
    if len(uni_hit_2[keys])==1:
        k=k+1
    else:
        if uni_hit_2[keys][1].startswith("WP"):
            inpar_2[keys]=uni_hit_2[keys][i]
        else:
            if uni_hit_2[keys][1].startswith("YP"):
                BBH_2[keys]=uni_hit_2[keys][1]

def bidirectionalHits(uni_hit1,uni_hit2):
    BBH={}
    # check bidirectionality
    for key in uni_hit1:
        if uni_hit1[key] in uni_hit2 and uni_hit2[uni_hit1[key]]==key:
            BBH[key]=uni_hit1[key]
    return BBH
    
BBH=bidirectionalHits(BBH_1,BBH_2)





























# def preprocess(uni_hit):
#     for key in uni_hit:
#         if uni_hit[key].startswith(">"):       
#             uni_hit[key]=uni_hit[key].split(">")[1]
#     return uni_hit

# def merged_blast_results(blastfile):
#     uni_hit={}
#     validate=0 
#     for x in blastfile:
#         if x.startswith("Query="):
#             get_key="".join(x.split('=')).split()[1]
#         else:
#             if(x.startswith("Sequences producing significant alignments: ")):
#                 validate=1 
#             if( x.startswith("\n") and validate==1):
#                 validate=2
#             if ( not x.startswith("\n") and validate==2):
#                 get_value=x.split()[0]
#                 if ( get_value!=get_key):
#                     uni_hit[get_key]=get_value
#                     validate=0       
#     blastfile.close()
#     uni_hit=preprocess(uni_hit)
#     return uni_hit




# # number of orthologsc
# counter=0
# for key in bbh_merged:
#     if bbh_merged[key].startswith("YP")==False:
#         counter=counter+1
        
# # return set of paralogs
# def paralogs(uni_merged):
#     paralogs={}
#     for key in uni_merged:
#         keystart=key[0:2]
#         if uni_merged[key].startswith(keystart):
#             paralogs[key]=uni_merged[key]
#     return paralogs


# p_1=paralogs(uni_merged_1)
# p_2=paralogs(uni_merged_2)
      

# for keys in p_2:
#     if keys in bbh_merged:
#         print(keys)

# #'YP_501446.1': 'WP_010921909.1'       
# for key in bbh_merged:
#     list(uni_merged_1.keys())[list(uni_merged_1.values()).index(temp_key)]    
            
# blast_merged_1=open("C:\\Users\\user\\Desktop\\assignmentGraded\\merged_db\\mergedDB_v1query.txt","r")
# uni_merged_1=merged_blast_results(blast_merged_1)

# blast_merged_2=open("C:\\Users\\user\\Desktop\\assignmentGraded\\merged_db\\mergedDB_v2query.txt","r")
# uni_merged_2=merged_blast_results(blast_merged_2)




# bbh_merged=bidirectionalHits(uni_merged_1,uni_merged_2)

# inverse = {values[i]: keys[i] for i in range(len(values))} 

# 'YP_501428.1': 'WP_010922784.1',




# ##  BLAST COMMANDS
# makeblastdb -in GCF_000006785.2_ASM678v2_protein.faa -dbtype prot
# makeblastdb -in GCF_000013425.1_ASM1342v1_protein.faa -dbtype prot

# ## to do blast
# blastp -query GCF_000013425.1_ASM1342v1_protein.faa -db GCF_000006785.2_ASM678v2_protein.faa -out v2DB_v1query.txt
# blastp -query GCF_000006785.2_ASM678v2_protein.faa -db GCF_000013425.1_ASM1342v1_protein.faa -out v1DB_v2query.txt

# # merge
# makeblastdb -in merged_db.faa -dbtype prot
# blastp -query GCF_000006785.2_ASM678v2_protein.faa -db merged_db.faa -out mergedDB_v2query.txt
# blastp -query GCF_000013425.1_ASM1342v1_protein.faa -db merged_db.faa -out mergedDB_v1query.txt




# ########  inparalogs : 'WP_010922136.1': 'WP_002988070.1' co-orthologous to 'YP_500201.1'
    
# >WP_002988070.1 hypothetical protein [Streptococcus pyogenes]
# MFDSKQNLAKSQWGFIVITAVMDLVVIVATLLAKTSFQRYLVGGVAFVLTSFLILLVWGLKTAKKLQTRLDSKEVLDSKV
# RDDQKLPKYDERQKQILLKGYTIGFWFMIVVIWLSLFISRFTEGLVSASFLFTLALWGGLAVQTTYCNLSMGASIFYRHY
# LDAKEADE

# >YP_500201.1 DNA internalization-related competence protein ComEC/Rec2 [Staphylococcus aureus subsp. aureus NCTC 8325]
# MLSTFLFILLLYITYRKNKIVYAPISLFLIIFSAWYLHYSQQAIFNYINYIERNSQFNERAQVIQIQRQGSDTYKGRLSL
# KNEIYPFFLTDKKNFDLKKIESRNCIVKGQFKVNDNKFVTLKLQSIVVQSCLESNRSNLIEKHKQFIMNRIYDSGIKFPD
# RIMALITGDVKEVNEQFKERVKEIGIYHLLAVSGSHIAAIVFLIYQPLKRLNLPLFVIKGITIIVLALFAQYTNYAPSAV
# RAIIMTTLVLVITKQIKIKGIQLLAFAFIIMFILNPLVVYDIGFQFSFIISFFIMLLFPFLQQLSKLQSLFIITFIAQLA
# SFIVAIPSFHQLQWVGFLSNLIFVPYYSIILFPLSILFFITSHFIVGLTPLNYLVDLSFNFHDWLLDLFTRIKQSHFSVP
# KFNDWIFIVFIISVYYIFWLLAKRKYILVTFWTIIILTLLITFPTNSHHKITMLNVGQGDSILYEGGKNQNVLIDTGGKV
# IDDTKQPSYSISKYHILPTLNERGINELEYLILTHPHNDHIGEVEYIISHIKIKHIVIYNKGYSSNTLMLLSKLSHKYNI
# KLMDVRQVSSFKLGDSSFLFFDSFIPNSRDKNEYSIITMITYQNKKVLLMGDASKNNESLLLKKYNLPEIDILKVGHHGS
# KTSSSKEFIEMIKPKISLISSGKNNMYHLPNIEVVKRLQRIRSRIYNSQQNGQVTIDLDDNLKVDSSSYGNASGL
# 'WP_010922136.1': 'WP_002988070.1',
# 'YP_500201.1' 'YP_501162.1'
# blastfile_1=open("C:\\Users\\user\\Desktop\\assignmentGraded\\v1DB_v2query.txt","r")
# uni_hit1_2=blast_results(blastfile_1)
# blastfile_2=open("C:\\Users\\user\\Desktop\\assignmentGraded\\v2DB_v1query.txt","r")
# uni_hit2_1=blast_results(blastfile_2)

# BBH_1_2=bidirectionalHits(uni_hit1_2,uni_hit2_1)
