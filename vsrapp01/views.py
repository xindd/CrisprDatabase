# coding=utf-8
from django.db.models import Max, Count, Q
from django.shortcuts import render, redirect
from vsrapp01 import models
import json
from django.http import HttpResponseRedirect, HttpResponse
import urllib
# import urllib2
import ssl
import time
import os
import re
from collections import Counter
# from BlastpParse import *
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Create your views here.


def indexn(request):
    return HttpResponseRedirect('VSR/index/')


def index(request):
    return render(request, 'index.html')


def vsrbytype(typename):
    if typename == 'general':
        data = models.VsrRnaiTable.objects.all()
    else:
        data = models.VsrRnaiTable.objects.filter(rnai_inhibited__contains=typename)
    get_class = data.values('class_field')
    ls = []
    for i in list(get_class):
        l = i.values()
        ls.extend(l)
    classfield = list(set(ls))
    dataset = {}
    for _ in classfield:
        d = data.filter(class_field=_).values('rss_id', 'organism', 'rnai_inhibited',
                                              'accession', 'short_name', 'taxon_id')
        number = 0
        for nu in d:
            if nu['accession'] is not None and nu['accession'] != '':
                number += 1
        for a in d:
            a['length'] = number
        dataset[_] = d
    return dataset


def browse(request, pagename):
    if pagename == '':
        titleset = ['vsr_b_id', 'family', 'anti_type', 'source', 'tested', 'mechanism']
        # , 'pubmed', 'accession', 'taxonomy', 'seq', 'size_seq', 'locus_tag', 'coded_by', 'db_xref']
        colnames = []
        for i in titleset:
            colnames.append({'title': i})
        dataset = models.VsrBacteriaTable.objects.all().values()
        datalist = []
        for i in dataset:
            tmp = []
            for j in titleset:
                tmp.append(i[j])
            tmp[0] = '<a href=' + tmp[0] + '>' + tmp[0] + '</a>'
            datalist.append(tmp)

        return render(request, '../backup/browse.html', {'colnames': json.dumps(colnames),
                                                         'datalist': json.dumps(datalist),
                                                         })
    elif pagename == 'Anti-CRISPRs':
        dataset = models.AntiTable2.objects.all().values()
        data = models.Knowned30Antidomains.objects.all()
        get_class = dataset.values('family')
        ls = []
        for i in list(get_class):
            l = i.values()
            ls.extend(l)
        classfield = list(set(ls))
        dataset2 = {}
        for _ in classfield:
            d = dataset.filter(family=_).values()
            for x in d:
                x['yes_verified'] = len(d.filter(validated='yes'))
                x['homologs_num'] = len(d.values()) - len(d.filter(validated='yes'))
            dataset2[_] = d
        keys = dataset2.keys()
        keys = sorted(keys)
        dlist = []
        for k in keys:
            dlist.append(dataset2[k])
        dataset2 = zip(keys, dlist)
        anti_newick = ['AcrF6', 'AcrF7', 'AcrF8', 'AcrF9', 'AcrIIA1', 'AcrIIA2', 'AcrIIA3', 'AcrIIA4', 'AcrIIC1',
                       'AcrIIC2', 'AcrIIC3']
        # print dataset2
        # data_js = {}
        # for cla in classfield:
        #     d = data.filter(proteinid=cla).values()
        #     d_list = []
        #     for name in d:
        #         tmp = name['neighbor_protein_location'].split(']')
        #         strand = tmp[1]
        #         start = int(name['neighbor_protein_location'].split(':')[0][1:])
        #         end = int(tmp[0].split(':')[1])
        #         if name['neighbor_domain_name'] == 'None':
        #             domainname = ''
        #         else:
        #             domainname = name['neighbor_domain_name'].split(':')[-1]
        #         if cla == name['neighbor_proteinid']:
        #             jslist = [0, start, end, strand, domainname, 'center']
        #         else:
        #             jslist = [0, start, end, strand, domainname, 'no']
        #
        #         d_list.append(jslist)
        #     d_list.sort(key=lambda x: int(x[0]))
        #     a = 0.0
        #     for m in d_list:
        #         a += m[2]-m[1]
        #
        #     for i in range(len(d_list)):
        #         if i == 0:
        #             d_list[i][2] = (d_list[i][2] - d_list[i][1])*11/a + 2
        #             d_list[i][1] = 0
        #         else:
        #             d_list[i][2] = (d_list[i][2] - d_list[i][1])*11/a + d_list[i-1][2] + 2
        #             d_list[i][1] = d_list[i-1][2]
        #     data_dic = []
        #     for js in d_list:
        #         if len(js) == 0:
        #             data_dic.append({'name': '', 'value': [0,0,0,0], 'center': 'no'})
        #         else:
        #             data_dic.append({'name': js[4], 'value': js[0:4], 'center': js[5]})
        #     data_js[cla] = data_dic
        return render(request, 'Anti-CRISPR.html', {'dataset': dataset2,
                                                    'anti_newick': anti_newick
                                                    # 'datajs': json.dumps(data_js)
                                                    })
    elif pagename == 'VSR':
        return render(request, 'VSR.html')
    elif pagename == 'General':
        dataset = vsrbytype('general')
        return render(request, 'browse-general.html', {'dataset': dataset})
    elif pagename == 'plant':
        dataset = vsrbytype('lant')
        return render(request, 'browse-general.html', {'dataset': dataset})
    elif pagename == 'Insect':
        dataset = vsrbytype('nsect')
        return render(request, 'browse-general.html', {'dataset': dataset})
    elif pagename == 'mamal':
        dataset = vsrbytype('mal')
        return render(request, 'browse-general.html', {'dataset': dataset})
    elif pagename == 'class':
        # 1
        antitable = list(
            models.AntiTable2.objects.all().values('id', 'family', 'source_organism', 'crispr_type_inhibited'))
        category_list = models.AntiTable2.objects.all().values('crispr_type_inhibited').annotate(
            Count('crispr_type_inhibited'))
        antijs = []
        antititle = []
        for n in category_list:
            antititle.append(n['crispr_type_inhibited'])
            antijs.append({'value': n['crispr_type_inhibited__count'], 'name': n['crispr_type_inhibited']})
        antitable = json.dumps(antitable)
        antijs = json.dumps(antijs)
        antititle = json.dumps(antititle)
        # 2
        rnaijs = [
            {'value': len(models.VsrRnaiTable.objects.filter(rnai_inhibited__contains='lant')), 'name': 'plant'},
            {'value': len(models.VsrRnaiTable.objects.filter(rnai_inhibited__contains='ammal')), 'name': 'mammal'},
            {'value': len(models.VsrRnaiTable.objects.filter(rnai_inhibited__contains='sect')), 'name': 'insect'}]
        rnaijs = json.dumps(rnaijs)
        rnaititle = json.dumps(['plant', 'mammal', 'insect'])
        rnaitable = json.dumps(
            list(models.VsrRnaiTable.objects.all().values('rss_id', 'short_name', 'organism', 'rnai_inhibited')))

        # 3
        pdbann = models.AntiAnnotationInfo.objects.exclude(pdb='').values('id', 'pdb')
        pdbidlist = [x[0] for x in pdbann.values_list('id')]
        pdbtable = []
        pdbtitle = []
        for pdbid in pdbann:
            pdbanti = \
                models.AntiTable2.objects.filter(id=pdbid['id']).values('id', 'family', 'crispr_type_inhibited')[0]
            pdbanti['pdb'] = pdbid['pdb']  # [x.strip() for x in pdbid['pdb'].split(',')]
            pdbtable.append(pdbanti)
            pdbtitle.append(pdbanti['crispr_type_inhibited'])
        pdbjs = dict(Counter(pdbtitle))
        tmp = []
        for key, value in pdbjs.items():
            tmp.append({'value': value, 'name': key})
        pdbtitle = json.dumps(list(pdbjs.keys()))
        pdbjs = json.dumps(tmp)
        pdbtable = json.dumps(pdbtable)

        # 4
        pdb2table = models.VsrRnaiTable.objects.exclude(structure_pdb_code_field='').values('rss_id', 'short_name',
                                                                                            'organism',
                                                                                            'rnai_inhibited',
                                                                                            'structure_pdb_code_field')
        pdb2js = [{'value': len(pdb2table.filter(rnai_inhibited__contains='lant')), 'name': 'plant'},
                  {'value': len(pdb2table.filter(rnai_inhibited__contains='ammal')), 'name': 'mammal'},
                  {'value': len(pdb2table.filter(rnai_inhibited__contains='sect')), 'name': 'insect'}]
        pdb2js = json.dumps(pdb2js)
        pdb2title = json.dumps(['plant', 'mammal', 'insect'])
        pdb2table = json.dumps(list(pdb2table))

        # 5[genomeisland, phage, prophage]
        prophagetable = models.AntiAnnotationInfo2.objects.filter(genome_region__contains='prophage')
        phagetable = models.AntiAnnotationInfo2.objects.exclude(genome_region__contains='prophage').filter(genome_region__contains='phage')
        genometable = models.AntiAnnotationInfo2.objects.filter(Q(genome_region__contains='GI'))
        mgetable = models.AntiAnnotationInfo2.objects.filter(Q(genome_region__contains='phage') |
                                                             Q(genome_region__contains='GI') |
                                                             Q(genome_region__contains='prophage')
                                                             ).values()
        mgejs = [{'value': len(prophagetable), 'name': 'Prophage'},
                 {'value': len(phagetable), 'name': 'Phage'},
                 {'value': len(genometable), 'name': 'Genomic island'}]
        mgejs = json.dumps(mgejs)
        mgetitle = json.dumps(['Prophage', 'Phage', 'Genomic island'])
        mgetable = json.dumps(list(mgetable))

        #  6
        strategytable = list(models.VsrMechansim.objects.all().values())
        strategy_list = models.VsrMechansim.objects.all().values('strategy').annotate(
            Count('strategy'))
        strategyjs = []
        strategytitle = []
        for n in strategy_list:
            strategytitle.append(n['strategy'])
            strategyjs.append({'value': n['strategy__count'], 'name': n['strategy']})
        strategytable = json.dumps(strategytable)
        strategyjs = json.dumps(strategyjs)
        strategytitle = json.dumps(strategytitle)
        return render(request, 'search-statistic.html', locals())

def browse_detail(request, protein_name):
    dataset = models.AntiTable2.objects.filter(accession=protein_name).values()
    AntiAnnotationInfo = models.AntiAnnotationInfo.objects.filter(accession=protein_name).values('uniprot_entry',
                                                                                                 'taxon_id',
                                                                                                 'locus_tag',
                                                                                                 'coded_by',
                                                                                                 'genome_region',
                                                                                                 'pdb',
                                                                                                 'dip',
                                                                                                 'intact'
                                                                                                 )
    if len(AntiAnnotationInfo) == 0:
        AntiAnnotationInfo = {'pdb': '', 'dip': '', 'intact': ''}
    else:
        AntiAnnotationInfo = AntiAnnotationInfo[0]
        pdbtmp = [x.strip() for x in AntiAnnotationInfo['pdb'].split(',')]
        if pdbtmp == ['']:
            pdbtmp = ''
        AntiAnnotationInfo['pdb'] = pdbtmp
    dna = models.AntiDna.objects.filter(accession=protein_name).values()
    dataset = dataset[0]
    if len(dna) != 0:
        dataset['gene'] = dna[0]['gene']
    else:
        dataset['gene'] = ''
    mechan = models.AnticrisprMechanisms.objects.filter(family=dataset['family']).values()
    if mechan[0]['figure'] == None or mechan[0]['figure'] == '':
        mechan = 'none'
    else:
        mechan = mechan[0]
    return render(request, 'browse-protein-detail.html', {'dataset': dataset,
                                                          'AntiAnnotationInfo': AntiAnnotationInfo,
                                                          'mechan': mechan
                                                          })


def browse_VSR_detail(request, vsr_name):
    dataset = models.VsrRnaiTable.objects.filter(rss_id=vsr_name).values()
    dataset = dataset[0]
    string = dataset['mechanism_of_action']
    dataset['mechanism_of_action'] = re.sub(r'.(\d{2,20}).',
                                            r"<a href='https://www.ncbi.nlm.nih.gov/pubmed/\1'><span class='am-icon-file-text-o'></span></a>",
                                            string)
    mechan = models.VsrMechansim.objects.filter(vsr_id=vsr_name).values()
    # print vsr_name
    if len(mechan) == 0:
        mechan = ''
        pic = ''
    else:
        mechan = mechan[0]
        # print mechan
        mechan['reference'] = mechan['reference'].split(';')
        pic = models.VsrPicture.objects.filter(strategy=mechan['strategy']).values()
        if len(pic) == 0:
            pic = ''
        else:
            pic = pic[0]

    return render(request, 'browse-VSR-detail.html', {'dataset': dataset,
                                                      'mechan': mechan,
                                                      'pic': pic,
                                                      })


def browse_anti_detail(request, anti_name):
    dataset = models.Knowned30Antidomains.objects.filter(proteinid=anti_name).values()
    return render(request, 'Knowned30AntiDomains.html', {'dataset': dataset})


def browse_homologs(request, protein_name):
    # get accession
    antitable = models.AntiTable2.objects.filter(family=protein_name).values()
    data_js = {}
    dataset = []
    for anti in antitable:
        homoprotein = models.Knowned30Antidomains2.objects.filter(anti_accession=anti['accession']).values()
        d_list = []
        for name in homoprotein:
            center = 'no'
            if name['neighbor_proteinid'] == anti['accession']:
                center = 'yes'
                dataset.append([anti['accession'], name['neighbor_def'], name['anti_id']])

            # tmp = name['neighbor_protein_location'].split(']')
            strand = re.findall(r'](\(.\))', name['neighbor_protein_location'])[0]
            start = int(re.findall(r'(\d*):', name['neighbor_protein_location'])[0])
            end = int(re.findall(r'(\d*)\]', name['neighbor_protein_location'])[0])
            # start = int(name['neighbor_protein_location'].split(':')[0][1:].strip())
            # print tmp[0].split(':')[1]
            # end = int(tmp[0].split(':')[1].strip())
            if name['neighbor_def'] == 'None':
                domainname = ''
            else:
                domainname = name['neighbor_def'].split(':')[-1]
            jslist = [start, end, domainname, strand, center]
            d_list.append(jslist)
        d_list.sort(key=lambda x: x[0])
        cen = 6
        for k in range(len(d_list)):
            if d_list[k][4] == 'yes':
                cen = k
        cha = 6 - cen

        d_list2 = []
        for ls in d_list:
            ls.append(d_list.index(ls) + cha)
            d_list2.append(ls)
        if cha<0:
            d_list2 = d_list2[cen-5:]
        data_js[anti['accession']] = d_list2
    # print dataset
    return render(request, 'browse-homologs.html', {'datalist': dataset,
                                                    'datajs': json.dumps(data_js)})


def browse_phylogenetic(request, family_name):
    try:
        with open(os.path.join(BASE_DIR, 'Anti_Newick', family_name + '.Newick'), 'r') as f:
            newick = f.readlines()[0].strip('\n')
            newick = re.sub(r'\'',  r"", newick)
            height = len(re.findall(',', newick))
            if height < 13:
                height = 300
            elif height<30:
                height = 400
            elif height < 60:
                height = 600
            elif height < 120:
                height = 1150
            return render(request, 'browse-phylogenetic.html', {'newick': json.dumps(newick),
                                                                'height':height
                                                                })
    except Exception:
        return render(request, 'index.html')


def analyze(request):
    return render(request, 'analyze-blastp.html')


def analyze_result(request):
    if request.method == 'POST':
        upfile = request.FILES.get('upfile')
        upsequence = request.POST.get('sequence')
        if upfile is None and upsequence is None:
            return render(request, 'analyze-blastp.html', {'error': 1})
        # 如果上传文件
        elif upfile is not None and upsequence is None:
            # 上传文件的文件名
            jobid = str(int(time.time()))
            models.Jobtable.objects.create(jobid=jobid, email='11@qq.com')
            try:
                with open(os.path.join(BASE_DIR, 'upfile', jobid), 'wb') as f:
                    for chunk in upfile.chunks():
                        f.write(chunk)
                return HttpResponseRedirect('/VSR/analyze_run/' + jobid)
            except IOError:
                return render(request, 'analyze-blastp.html', {'error': 1})
        # 如果上传序列
        elif upfile is None and upsequence is not None:
            if upsequence == '':
                return render(request, 'analyze-blastp.html', {'error': 1})
            else:
                jobid = str(int(time.time()))
                models.Jobtable.objects.create(jobid=jobid, email='11@qq.com')
                try:
                    with open(os.path.join(BASE_DIR, 'upfile', jobid), 'w') as f:
                        f.write(upsequence)
                    return HttpResponseRedirect('/VSR/analyze_run/' + jobid)
                except IOError:
                    return render(request, 'analyze-blastp.html', {'error': 1})
        elif upfile is not None and upsequence is not None:
            # 上传文件的文件名
            jobid = str(int(time.time()))
            models.Jobtable.objects.create(jobid=jobid, email='11@qq.com')
            try:
                with open(os.path.join(BASE_DIR, 'upfile', jobid), 'wb') as f:
                    for chunk in upfile.chunks():
                        f.write(chunk)
                return HttpResponseRedirect('/VSR/analyze_run/' + jobid)
            except IOError:
                return render(request, 'analyze-blastp.html', {'error': 1})
    else:
        return render(request, 'analyze-blastp.html', {'error': 1})


def analyze_search(request):
    if request.method == 'POST':
        keywords = request.POST.get('keywords')
        classname = request.POST.get('classname')
        # print classname
        if keywords:
            if classname == 'ACR_ID':
                antires = models.AntiTable2.objects.filter(Q(id__icontains=keywords))
                antilen = len(antires)
            elif classname == 'VSR_ID':
                vsrres = models.VsrRnaiTable.objects.filter(Q(rss_id__icontains=keywords))
                vsrlen = len(vsrres)
            elif classname == 'Accession':
                antires = models.AntiTable2.objects.filter(Q(accession__icontains=keywords))
                antilen = len(antires)
                vsrres = models.VsrRnaiTable.objects.filter(Q(accession__icontains=keywords))
                vsrlen = len(vsrres)
            elif classname == 'Organism':
                antires = models.AntiTable2.objects.filter(Q(source_organism__icontains=keywords))
                antilen = len(antires)
                vsrres = models.VsrRnaiTable.objects.filter(Q(organism__icontains=keywords))
                vsrlen = len(vsrres)
            elif classname == 'Family_ACR':
                antires = models.AntiTable2.objects.filter(Q(family__icontains=keywords))
                antilen = len(antires)
            elif classname == 'Family_Genus_VSR':
                vsrres = models.VsrRnaiTable.objects.filter(Q(family_genus__icontains=keywords))
                vsrlen = len(vsrres)
            elif classname == 'Pubmed_ID':
                antires = models.AntiTable2.objects.filter(Q(reference__icontains=keywords))
                antilen = len(antires)
                vsrres = models.VsrRnaiTable.objects.filter(Q(reference__icontains=keywords))
                vsrlen = len(vsrres)
            else:
                antires = models.AntiTable2.objects.filter(Q(id__icontains=keywords) |
                                                           Q(accession__icontains=keywords) |
                                                           Q(accession__icontains=keywords) |
                                                           Q(source_organism__icontains=keywords)|
                                                           Q(family__icontains=keywords) |
                                                           Q(reference__icontains=keywords)
                                                           )
                antilen = len(antires)
                vsrres = models.VsrRnaiTable.objects.filter(Q(rss_id__icontains=keywords) |
                                                            Q(accession__icontains=keywords) |
                                                            Q(organism__icontains=keywords) |
                                                            Q(family_genus__icontains=keywords) |
                                                            Q(reference__icontains=keywords)
                                                            )
                vsrlen = len(vsrres)
            # print list(set([x[0] for x in models.AntiTable2.objects.all().values_list('family')]))
            return render(request, 'search.html', locals())


        else:
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')


def file2dic(filelines):
    keys = [x for x in filelines[0].strip('\n').split('\t')]
    dataset = []
    for value in filelines[1:]:
        dataset.append(dict(zip(keys, value.strip('\n').split('\t'))))
    return dataset


def analyze_change_format(proteinid, picdata):
    data_js = {}
    dataset = {}
    for pdb in proteinid:
        homoprotein = []
        for p in picdata:
            if pdb == p['Homo_ProteinID']:
                homoprotein.append(p)
        d_list = []
        for name in homoprotein:
            center = 'no'
            if name['Homo_Neighbor_ProteinID'] == pdb:
                center = 'yes'
                dataset[pdb] = name['Homo_Neighbor_Domain_Def']
            strand = re.findall(r'](\(.\))', name['Homo_Neighbor_Protein_Location'])[0]
            start = int(re.findall(r'(\d*):', name['Homo_Neighbor_Protein_Location'])[0])
            end = int(re.findall(r'(\d*)\]', name['Homo_Neighbor_Protein_Location'])[0])
            if name['Homo_Neighbor_Domain_Name'] == 'None':
                domainname = ''
            else:
                domainname = name['Homo_Neighbor_Domain_Name'].split(':')[-1]
            jslist = [start, end, domainname, strand, center]
            d_list.append(jslist)
        cen = 6
        for k in range(len(d_list)):
            if d_list[k][4] == 'yes':
                cen = k
        cha = 6 - cen
        d_list2 = []
        for ls in d_list:
            ls.append(d_list.index(ls) + cha)
            d_list2.append(ls)
        data_js[pdb] = d_list2
    return data_js, dataset


def analyze_run(request, jobid):
    if jobid == '' or len(models.Jobtable.objects.filter(jobid=jobid).values('start_time')) == 0:
        return render(request, 'badrequest.html')
    else:
        jobstarttime = models.Jobtable.objects.filter(jobid=jobid).values('start_time')
        if jobstarttime[0]['start_time'] is None:
            # 如果没有run开始，添加开始时间
            models.Jobtable.objects.filter(jobid=jobid).update(start_time=str(int(time.time())))
            # 开始后台计算
            inputname = str(jobid)
            outputname = str(jobid)
            res = os.system(
                'nohup bash /var/www/html/VSR/blast_result/procedure.bash  %s %s &' % (inputname, outputname))
            if res == 0:
                return render(request, 'analyze-run-wating.html', {'costime': 0})
            else:
                return render(request, 'badrequest.html', {'runfiled': 'Failed to run and try again later'})
        else:
            # 如果run开始，获取结束时间
            jobendtime = models.Jobtable.objects.filter(jobid=jobid).values('end_time')
            # 如果没有结束时间
            if jobendtime[0]['end_time'] is None:
                try:
                    # 判断作业是否完成
                    with open(os.path.join(BASE_DIR, 'blast_result', jobid, jobid + '.log'), 'r') as logfile:
                        res = logfile.readlines()
                        res = ''.join(res).strip('\n').split('\n')
                        if res[0] == '':
                            jobfinished = False
                            step = 1
                        else:
                            if 'step6' in res:
                                if res[-1] == 'step6':
                                    jobfinished = False
                                    step = 6
                                else:
                                    jobfinished = True
                                    step = 6
                                    logtime = res[-1]
                            else:
                                jobfinished = False
                                step = int(res[-1][-1])
                except IOError:
                    return render(request, 'badrequest.html', {'runfiled': 'Failed to run and try again later'})
                if jobfinished:
                    # 如果作业完成，将日志时间戳加入数据库
                    models.Jobtable.objects.filter(jobid=jobid).update(end_time=logtime)
                    s2etime = models.Jobtable.objects.filter(jobid=jobid).values('start_time', 'end_time')
                    costtime = int(s2etime[0]['end_time']) - int(s2etime[0]['start_time'])
                    m, s = divmod(costtime, 60)
                    h, m = divmod(m, 60)
                    try:
                        with open(os.path.join(BASE_DIR, 'blast_result', jobid, 'HomoIDInfo.txt'), 'r') as family:
                            blastres = file2dic(list(family.readlines()))
                        with open(os.path.join(BASE_DIR, 'blast_result', jobid, 'HomologyDomains_MinEvalue.txt'),
                                  'r') as picture:
                            picdata = file2dic(list(picture.readlines()))
                        blastresult = []
                        proteinid = []
                        for b in blastres:
                            proteinid.append(b['Homoloty_Protein_ID'])
                            for p in picdata:
                                if b['Homoloty_Protein_ID'] == p['Homo_Neighbor_ProteinID']:
                                    b['Evalue'] = p['evalue']
                                    b['Identity'] = p['identity']
                                    blastresult.append(b)
                        data_js, dataset = analyze_change_format(proteinid, picdata)
                        return render(request, 'analyze-run-result.html', {'costime': "%02d:%02d:%02d" % (h, m, s),
                                                                           'startime': jobid,
                                                                           'blastres': blastres,
                                                                           'datalist': dataset,
                                                                           'datajs': json.dumps(data_js)
                                                                           })
                    except Exception:
                        return render(request, 'badrequest.html',
                                      {'runfiled': 'Failed to return result, please check data format or job id'})
                else:
                    costtime = int(time.time()) - int(jobstarttime[0]['start_time'])
                    m, s = divmod(costtime, 60)
                    h, m = divmod(m, 60)
                    return render(request, 'analyze-run-wating.html',
                                  {'costime': "%02d:%02d:%02d" % (h, m, s), 'step': step})
            # 如果结束
            else:
                s2etime = models.Jobtable.objects.filter(jobid=jobid).values('start_time', 'end_time')
                costtime = int(s2etime[0]['end_time']) - int(s2etime[0]['start_time'])
                m, s = divmod(costtime, 60)
                h, m = divmod(m, 60)
                try:
                    with open(os.path.join(BASE_DIR, 'blast_result', jobid, 'HomoIDInfo.txt'), 'r') as family:
                        blastres = file2dic(list(family.readlines()))
                    with open(os.path.join(BASE_DIR, 'blast_result', jobid, 'HomologyDomains_MinEvalue.txt'),
                              'r') as picture:
                        picdata = file2dic(list(picture.readlines()))

                    blastresult = []
                    proteinid = []
                    for b in blastres:
                        proteinid.append(b['Homoloty_Protein_ID'])
                        for p in picdata:
                            if b['Homoloty_Protein_ID'] == p['Homo_Neighbor_ProteinID']:
                                b['Evalue'] = p['evalue']
                                b['Identity'] = p['identity']
                                blastresult.append(b)
                    data_js, dataset = analyze_change_format(proteinid, picdata)

                    return render(request, 'analyze-run-result.html', {'costime': "%02d:%02d:%02d" % (h, m, s),
                                                                       'startime': jobid,
                                                                       'blastres': blastres,
                                                                       'datalist': dataset,
                                                                       'datajs': json.dumps(data_js)
                                                                       })
                except Exception:
                    return render(request, 'badrequest.html',
                                  {'runfiled': 'Failed to return result, please check data format or job id'})


def deposit(request, data):
    if data=='':
        return render(request, 'deposit.html')
    else:
        time.sleep(2)
        return render(request, 'deposit.html', {'submit':1})


def download(request):
   return render(request, 'download.html')


def help(request):
    return render(request, 'help.html')


def visualize_get_pdb(typename):
    data = models.VsrRnaiTable.objects.filter(rnai_inhibited__contains=typename).values()
    dataset = []
    for i in data:
        pdb = i['structure_pdb_code_field']
        if pdb != '' and pdb is not None:
            i['pdbstructure'] = [k.strip() for k in pdb.split(';')]
            dataset.append(i)
    return dataset


def url_get_pdb_picture():
    import webbrowser
    import time
    import os
    dataset = models.VsrRnaiTable.objects.all().values()
    pdbid = []
    for i in dataset:
        if i['structure_pdb_code_field'] != '':
            aa = [k.strip() for k in i['structure_pdb_code_field'].split(';')]
            pdbid.extend(aa)
    pdbid = list(set(pdbid))
    aaa = [s[:-4] for s in os.listdir('E:/pic')]
    # print len(list(set(aaa).intersection(set(pdbid))))
    # print pdbid
    num = 0
    for i in pdbid:
        if i not in aaa:
            if num < 6:
                webbrowser.open(
                    'https://www.ncbi.nlm.nih.gov/Structure/icn3d/full.html?pdbid=' + i + '&command=export%20canvas')
                num += 1
                time.sleep(6)
            else:
                time.sleep(6)
                os.system('taskkill /F /IM chrome.exe')
                num = 0


def visualize(request, visualname):
    if visualname == 'structure':
        return render(request, 'visual-structure.html')
    elif visualname == 'acrs':
        data = models.AntiAnnotationInfo.objects.all().values()
        dataset = []
        for i in data:
            anti = models.AntiTable2.objects.filter(id=i['id']).values()[0]
            pdb = i['pdb']
            if pdb != '':
                i['pdbstructure'] = [k.strip() for k in pdb.split(',')]
                i['organism'] = anti['source_organism']
                i['size_aa_field'] = anti['size_seq']
                i['family'] = anti['family']
                dataset.append(i)
        return render(request, 'visual-structure-class-acrs.html', {'dataset': dataset})
    elif visualname == 'plant':
        dataset = visualize_get_pdb('lant')
        # url_get_pdb_picture()
        return render(request, 'visual-structure-class.html', {'dataset': dataset})
    elif visualname == 'insect':
        dataset = visualize_get_pdb('nsect')
        return render(request, 'visual-structure-class.html', {'dataset': dataset})
    elif visualname == 'mammal':
        dataset = visualize_get_pdb('mal')
        return render(request, 'visual-structure-class.html', {'dataset': dataset})
        # dataset = models.ProtinStructure.objects.all().values()
        # pdbid = []
        # leftinfo = []
        # for i in dataset:
        #     pdbid.extend(i['structure'].split(','))
        #     # ls = {'id': i['id'], 'name': i['name'], 'accession': i['accession'], 'length': i['length'],
        #     #      'organism': i['organism'], 'structure': i['structure']}
        #     leftinfo.append([unicode(i['id']), i['name'], i['accession'], i['length'],
        #                      i['organism'], i['structure'], i['structure'].split(',')])
        # # print leftinfo
        # # save png
        # # import webbrowser
        # # import time
        # # for i in pdbid:
        # #     webbrowser.open('https://www.ncbi.nlm.nih.gov/Structure/icn3d/full.html?pdbid='+i+'&command=export%20canvas')
        # #     time.sleep(3)
        # return render(request, 'visual-structure.html', {'leftinfo': leftinfo,
        #                                                  'pdbid': json.dumps(pdbid)})
    elif visualname == 'interaction':
        dataset = models.Knowned30Antidomains2.objects.all().values()
        pdbid = []
        leftinfo = []
        for i in dataset:
            pdbid.extend(i['structure'].split(','))
            # ls = {'id': i['id'], 'name': i['name'], 'accession': i['accession'], 'length': i['length'],
            #      'organism': i['organism'], 'structure': i['structure']}
            leftinfo.append([str(i['id']), i['name'], i['accession'], i['length'],
                             i['organism'], i['structure'], i['structure'].split(',')])
        return render(request, 'visual-interaction.html', {'leftinfo': leftinfo,
                                                           'pdbid': json.dumps(pdbid)})
    elif visualname == 'mechanism':
        return render(request, 'visual-mechanism.html')
    elif visualname == 'type':
        acrdata = models.AntiAnnotationInfo.objects.all()
        plantdata = models.VsrRnaiTable.objects.filter(rnai_inhibited__contains='lant')
        insectdata = models.VsrRnaiTable.objects.filter(rnai_inhibited__contains='sect')
        mammaldata = models.VsrRnaiTable.objects.filter(rnai_inhibited__contains='mmal')
        return render(request, 'visual-type.html', locals())


def visualize_detail(request, familyname):
    if familyname[0:3]=='Acr':
        dataset = models.AnticrisprMechanisms2.objects.filter(Q(family=familyname)|
                                                              Q(family__icontains=familyname+',') |
                                                              Q(family__icontains=','+familyname)
                                                              ).values()
        return render(request, 'visual-mechanism-detail.html', locals())
    else:
        # print familyname
        dataset = models.VsrMechansim2.objects.filter(strategy__icontains=familyname).values().distinct()
        return render(request, 'visual-mechanism-detail2.html', locals())


def protein_detail(request, pdbid):
    return render(request, 'protein_structure_detail.html', {'pdbid': pdbid})


def analyze_sequence(request):
    return render(request, 'analyze_sequence.html')


def general_align(request):
    proteinlist = request.POST.getlist('cbx')
    if len(proteinlist) == 0:
        return HttpResponseRedirect('/VSR/browse/VSR')
    else:
        try:
            ssl._create_default_https_context = ssl._create_unverified_context
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
            test_data = {
                'alignQuery': ' '.join(proteinlist),  # 'P0C783 Q66125',
                'program': 'CLUSTALO',
                'redirect': 'yes',
                'landingPage': 'no',
                'url2': ''
            }
            test_data_urlencode = urllib.urlencode(test_data)
            requrl = "https://www.uniprot.org/align/"
            req = urllib2.Request(url=requrl, data=test_data_urlencode, headers=headers)
            res_data = urllib2.urlopen(req)
        except Exception:
            return HttpResponseRedirect('/VSR/browse/VSR')
        # print ' '.join(proteinlist)
        # print res_data.geturl()
        return redirect(res_data.geturl())


def search(request):
    return render(request, 'newsearch.html')


def blast_run(queryname, dbname):
    queryFileName = queryname
    dbName = dbname
    dbMatch = dbName.split('/')[3]
    blastpResult = queryFileName.strip('.faa') + '_' + dbName.split('/')[3] + '.txt'
    finalResult = queryFileName.strip('.faa') + '_' + dbName.split('/')[3] + '_Filt' + '.txt'
    Blastp_Various_DB(queryFileName, dbName, blastpResult)
    resultFile = open(finalResult, 'w')
    if 'ACRvalidated' in dbMatch:
        Filt_ACRDB(blastpResult, resultFile)
    elif 'ACRnr' in dbMatch:
        Filt_ACRDB(blastpResult, resultFile)
    elif 'VSRnr' == dbMatch:
        Filt_VSRDB(blastpResult, resultFile)
    elif 'VF' == dbMatch:
        Filt_VFDB(blastpResult, resultFile)


def blast(request):
    if request.method == 'POST':
        selectdatabases = request.POST.getlist('selectname')[0]
        algo = request.POST.getlist('radioName')[0]
        urlid = ''
        vfyes = 'true'

        if selectdatabases == 'ACRvalidated':
            titlename = 'Blastp against the verified anti-CRISPRs'
            url = 'browse_detail/'
            dbname = '/zrom/blastdb/ACRvalidated'
        elif selectdatabases == 'ACRnr':
            titlename = 'Blastp against all anti-CRISPR non-redundant sequences'
            url = 'browse_detail/'
            dbname = '/zrom/blastdb/ACRnr'
        elif selectdatabases == 'VSRnr':
            titlename = 'Blastp against all VSR non-redundant sequences'
            url = 'browse_VSR_detail/'
            dbname = '/zrom/blastdb/VSRnr'
        elif selectdatabases == 'VF':
            titlename = 'Blastp against experimentally verified Virulence Factors sequences'
            url = ''
            vfyes = 'false'
            dbname = '/zrom/blastdb/VF'
        else:
            return render(request, 'newsearch.html', {'error': 1})
        upfile = request.FILES.get('upfile')
        upsequence = request.POST.get('sequence')
        if upfile is None and upsequence is None:
            return render(request, 'newsearch.html', {'error': 1})
        # 如果上传文件
        elif upfile is not None and upsequence is None:
            # 上传文件的文件名
            jobid = str(int(time.time()))
            try:
                with open(os.path.join(BASE_DIR, 'upfile', jobid), 'wb') as f:
                    for chunk in upfile.chunks():
                        f.write(chunk)
            except IOError:
                return render(request, 'newsearch.html', {'error': 1})
        # 如果上传序列
        elif upfile is None and upsequence is not None:
            if upsequence == '':
                return render(request, 'newsearch.html', {'error': 1})
            else:
                jobid = str(int(time.time()))
                try:
                    with open(os.path.join(BASE_DIR, 'upfile', jobid), 'w') as f:
                        f.write(upsequence)
                except IOError:
                    return render(request, 'newsearch.html', {'error': 1})
        elif upfile is not None and upsequence is not None:
            # 上传文件的文件名
            jobid = str(int(time.time()))
            try:
                with open(os.path.join(BASE_DIR, 'upfile', jobid), 'wb') as f:
                    for chunk in upfile.chunks():
                        f.write(chunk)
            except IOError:
                return render(request, 'newsearch.html', {'error': 1})
        try:
            # 运行程序
            blast_run('/var/www/html/VSR/upfile/' + jobid, dbname)
            # 分析结果
            finalResult = '/var/www/html/VSR/upfile/' + jobid + '_' + selectdatabases + '_Filt' + '.txt'
            with open(finalResult, 'r') as fileline:
                dataset = file2dic(fileline)
            return render(request, 'analyze-run-result.html', {'blastres': dataset, 'urllink': url, 'vfyes': vfyes, 'title': titlename})
        except Exception:
            return render(request, 'newsearch.html', {'error': 1})
    else:
        return render(request, 'newsearch.html', {'error': 1})

