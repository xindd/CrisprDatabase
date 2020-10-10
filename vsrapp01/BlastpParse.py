#!/usr/bin
#-*-coding:utf-8-*-

import os
import subprocess
import sys
import time

def mkdir(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)
def Filt_ACRDB(blastpResult, resultFile):
    header = 'Query_ID\tHit_RSS_ID\tHit_ID\tHit_Family\tQuery_Start\tQuery_End\tHit_Start\tHit_End\tIdentity\tEvalue\n'
    resultFile.write(header)
    resultFile.flush()

    with open(blastpResult)as fin:
        lines = fin.readlines()
        for line in lines[0:]:
            query_id = line.strip('\n').split('\t')[0]
            hit_def = line.strip('\n').split('\t')[1]
            hit_rss_id = hit_def.split('|')[0]
            hit_id = hit_def.split('|')[1]
            hit_family = hit_def.split('|')[2]
            query_start = line.strip('\n').split('\t')[6]
            query_end = line.strip('\n').split('\t')[7]
            hit_start = line.strip('\n').split('\t')[8]
            hit_end = line.strip('\n').split('\t')[9]
            identity = line.strip('\n').split('\t')[2]
            evalue = line.strip('\n').split('\t')[10]
            strWrite = query_id + '\t' + hit_rss_id + '\t' + hit_id + '\t' + hit_family + '\t' + query_start +'\t' + query_end +'\t' + hit_start + '\t' + hit_end +'\t' + identity + '\t' + evalue + '\n'
            resultFile.write(strWrite)
            resultFile.flush()
def Filt_VSRDB(blastpResult, resultFile):
    header = 'Query_ID\tHit_RSS_ID\tHit_ID\tHit_Family\tHit_RNAi_Type\tQuery_Start\tQuery_End\tHit_Start\tHit_End\tIdentity\tEvalue\n'
    resultFile.write(header)
    resultFile.flush()
    with open(blastpResult)as fin:
        lines = fin.readlines()
        for line in lines[0:]:
            query_id = line.strip('\n').split('\t')[0]
            hit_def = line.strip('\n').split('\t')[1]
            hitTemp = hit_def.split('|')
            if len(hitTemp) == 4:
                hit_rss_id = hit_def.split('|')[0]
                hit_id = hit_def.split('|')[1]
                hit_family = hit_def.split('|')[2]
                hit_RNAi_Type = hit_def.split('|')[3]
            elif len(hitTemp) == 3:
                hit_rss_id = hit_def.split('|')[0]
                hit_id = hit_def.split('|')[1]
                hit_family = hit_def.split('|')[2]
                hit_RNAi_Type = ''


            query_start = line.strip('\n').split('\t')[6]
            query_end = line.strip('\n').split('\t')[7]
            hit_start = line.strip('\n').split('\t')[8]
            hit_end = line.strip('\n').split('\t')[9]
            identity = line.strip('\n').split('\t')[2]
            evalue = line.strip('\n').split('\t')[10]
            strWrite = query_id + '\t' + hit_rss_id + '\t' + hit_id + '\t' + hit_family + '\t'+hit_RNAi_Type+'\t' + query_start + '\t' + query_end + '\t' + hit_start + '\t' + hit_end + '\t' + identity + '\t' + evalue + '\n'
            resultFile.write(strWrite)
            resultFile.flush()

def Filt_VFDB(blastpResult, resultFile):
    header = 'Query_ID\tHit_RSS_ID\tHit_ID\tQuery_Start\tQuery_End\tHit_Start\tHit_End\tIdentity\tEvalue\n'
    resultFile.write(header)
    resultFile.flush()
    with open(blastpResult)as fin:
        lines = fin.readlines()
        for line in lines[0:]:
            query_id = line.strip('\n').split('\t')[0]
            hit_def = line.strip('\n').split('\t')[1]
            hit_rss_id = hit_def.split('(')[0]
            hit_id = hit_def.split('(')[1].split('|')[1].split(')')[0]
            query_start = line.strip('\n').split('\t')[6]
            query_end = line.strip('\n').split('\t')[7]
            hit_start = line.strip('\n').split('\t')[8]
            hit_end = line.strip('\n').split('\t')[9]
            identity = line.strip('\n').split('\t')[2]
            evalue = line.strip('\n').split('\t')[10]
            strWrite = query_id + '\t' + hit_rss_id + '\t' + hit_id + '\t' + query_start + '\t' + query_end + '\t' + hit_start + '\t' + hit_end + '\t' + identity + '\t' + evalue + '\n'
            resultFile.write(strWrite)
            resultFile.flush()


def Blastp_Various_DB(queryFileName,dbName,blastpResult):
    subprocess.call(
        "blastp -query  %s -db %s -evalue 10 -num_threads 20 -outfmt 6 -out %s " % (queryFileName,dbName,blastpResult), shell=True)


if __name__ == "__main__":
    queryFileName = sys.argv[1]
    dbName = sys.argv[2]
    dbMatch = dbName.split('/')[3]
    blastpResult = queryFileName.strip('.faa')+ '_' + dbName.split('/')[3] + '.txt'

    finalResult = queryFileName.strip('.faa')+ '_' + dbName.split('/')[3] + '_Filt' + '.txt'
    Blastp_Various_DB(queryFileName, dbName, blastpResult)
    resultFile = open(finalResult, 'w')
    if 'ACR' in dbMatch:
        Filt_ACRDB(blastpResult, resultFile)
    elif 'VSRnr' == dbMatch:
        Filt_VSRDB(blastpResult, resultFile)
    elif 'VF' == dbMatch:
        Filt_VFDB(blastpResult, resultFile)
