# KBQA调研--工业界

**目录**

[KBQA调研--工业界](#KBQA调研工业界)

&emsp;&emsp;[1.&nbsp;任务](#1-任务)

&emsp;&emsp;&emsp;&emsp;[1.1&nbsp;任务定义](#11-任务定义)

&emsp;&emsp;&emsp;&emsp;[1.2&nbsp;数据集](#12-数据集)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[1.2.0&nbsp;CCKS和NLPCC比赛数据](#120-CCKS和NLPCC比赛数据)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[1.2.0.1&nbsp;CCKS&nbsp;2019](#1201-CCKS-2019)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[1.2.0.2&nbsp;NLPCC&nbsp;2018](#1202-NLPCC-2018)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[1.2.1&nbsp;通用知识图谱](#121-通用知识图谱)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[1.2.2&nbsp;领域知识图谱](#122-领域知识图谱)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[1.2.3&nbsp;Common&nbsp;Sense&nbsp;Knowledge&nbsp;Graph](#123-Common-Sense-Knowledge-Graph)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[1.2.4&nbsp;Encyclopedia&nbsp;Knowledge&nbsp;Graph](#124-Encyclopedia-Knowledge-Graph)

&emsp;&emsp;&emsp;&emsp;[1.3&nbsp;评测标准](#13-评测标准)

&emsp;&emsp;[2.&nbsp;方法总结](#2-方法总结)

&emsp;&emsp;&emsp;&emsp;[2.1&nbsp;基于规则的方法（github上demo项目的多数方法）](#21-基于规则的方法（github上demo项目的多数方法）)

&emsp;&emsp;&emsp;&emsp;[2.2&nbsp;CCKS&nbsp;+&nbsp;NLPCC](#22-CCKS--NLPCC)

&emsp;&emsp;[3.&nbsp;相关工作](#3-相关工作)

&emsp;&emsp;&emsp;&emsp;[3.1&nbsp;NLPCC+CCKS论文集&笔记](#31-NLPCCCCKS论文集笔记)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[3.1.1&nbsp;CCKS论文集&笔记](#311-CCKS论文集笔记)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[3.1.2&nbsp;NLPCC论文集&笔记](#312-NLPCC论文集笔记)

&emsp;&emsp;&emsp;&emsp;[3.2&nbsp;知识图谱Talk&nbsp;Slides](#32-知识图谱Talk-Slides)

&emsp;&emsp;&emsp;&emsp;[3.3&nbsp;企业知识图谱产品说明](#33-企业知识图谱产品说明)

## 1. 任务

### 1.1 任务定义

工业界的KGQA系统目的是为用户提供一个用自然语言来提问的界面，使用他们的自己的术语以及语言习惯，通过查询知识图谱得到一个简介精确的答案。[Introduction to Neural Network based Approaches for Question Answering over Knowledge Graphs](https://arxiv.org/pdf/1907.09361.pdf)



![img](https://raw.githubusercontent.com/BDBC-KG-NLP/KBQA-Survey/master/KBQA%20Industry/pictures/KBQA-example.JPEG)

<center style="font-size:14px;color:#C0C0C0;text-decoration:underline">图1.知识图谱示例</center> 
### 1.2 数据集

没有固定的工业界数据集，图谱参照领域内的app数据进行的爬取整理，问题多来自企业客服或是app收集的问题，这部分来源未知。一下列出一些代表性的工业知识图谱。

#### 1.2.0 CCKS和NLPCC比赛数据

##### 1.2.0.1 CCKS 2019

[知识库 密码(huc8)](https://pan.baidu.com/share/init?surl=MOv9PCTcALVIiodUP4bQ2Q)，[问答](https://github.com/duterscmy/ccks2019-ckbqa-4th-codes/tree/master/data)

##### 1.2.0.2 NLPCC 2018

[知识库](https://pan.baidu.com/s/1dEYcQXz)，[问答](https://github.com/msra-nlc/ChineseKBQA)

#### 1.2.1 通用知识图谱

+ Google Knowledge Graph
+ Microsoft Satori & Probase

#### 1.2.2 领域知识图谱

+ Facebook 社交知识图谱
+ Amazon 商品知识图谱
+ 阿里巴巴商品知识图谱
+ [学术知识图谱](https://www.acemap.info/)

#### 1.2.3 Common Sense Knowledge Graph

+ 通常挖掘词之间的Linguistic Knowledge
+ 较为在意的Relation: isA Relation, isPropertyOf Relation
+ e.g. WordNet, KnowItAll, NELL, Microsoft Concept Graph

#### 1.2.4 Encyclopedia Knowledge Graph

+ 通常挖掘Entities和Entities之间的Facts
+ e.g. Freebase, Yago, Google Knowledge Graph

### 1.3 评测标准

这个企业内部没有具体写明，提到的都在学术界有使用，这里给出NLPCC比赛的测评方法

+ **Mean Reciprocal Rank (MRR)**

  <a href="https://www.codecogs.com/eqnedit.php?latex=MRR=\frac{1}{|Q|}\sum_{i=1}^{|Q|}\frac{1}{rank_i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?MRR=\frac{1}{|Q|}\sum_{i=1}^{|Q|}\frac{1}{rank_i}" title="MRR=\frac{1}{|Q|}\sum_{i=1}^{|Q|}\frac{1}{rank_i}" /></a>

  + |Q|代表问题总数，rank_i代表第一个正确的答案在答案集合C_i中的位置
  + 如果C_i中没有正确答案，<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{1}{rank_i}=0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{1}{rank_i}=0" title="\frac{1}{rank_i}=0" /></a>

+ **Accuracy@N**

  <a href="https://www.codecogs.com/eqnedit.php?latex=Accuracy@N=\frac{1}{|Q|}\sum_{i=1}^{|Q|}\delta(C_i,A_i)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Accuracy@N=\frac{1}{|Q|}\sum_{i=1}^{|Q|}\delta(C_i,A_i)" title="Accuracy@N=\frac{1}{|Q|}\sum_{i=1}^{|Q|}\delta(C_i,A_i)" /></a>

  + 当答案集合C_i中至少有一个出现在gold answerA_i中，<a href="https://www.codecogs.com/eqnedit.php?latex=\delta(C_i,A_i)=1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\delta(C_i,A_i)=1" title="\delta(C_i,A_i)=1" /></a>，否则为0

+ **Averaged F1**

  <a href="https://www.codecogs.com/eqnedit.php?latex=AveragedF1=\frac{1}{|Q|}\sum_{i=1}^{|Q|}F_i" target="_blank"><img src="https://latex.codecogs.com/gif.latex?AveragedF1=\frac{1}{|Q|}\sum_{i=1}^{|Q|}F_i" title="AveragedF1=\frac{1}{|Q|}\sum_{i=1}^{|Q|}F_i" /></a>

  + F_i是Q_i问题产生答案的F1值，如果A_i和C_i无交集F1为0



## 2. 方法总结

### 2.1 基于规则的方法（github上demo项目的多数方法）

代表项目：[豆瓣影评问答](https://github.com/weizhixiaoyi/DouBan-KGQA) 

+ 实体识别
  + 词表 ，字符串相似度（或BiLSTM-CRF）
+ 属性链接
  + 词表，字符串相似度 （或CNN等分类模型）
+ 答案推理
  + 规则模板转换得到SPARQL语句
  + （或TransE表示学习的方法进行答案推理）

### 2.2 CCKS + NLPCC

+ **实体识别**
  + 规则
    + 自定义字典(分词，词频，倒排索引)
    + 停用词
    + 字符串匹配(jaccord，编辑距离)
  + 辅助工具
    + NER工具包识别人名，地点，机构等
  + 神经网络
    + Bert/BiLSTM + CRF
+ **实体链接**
  + 规则 
    + 实体名称和问题的字符串匹配度(char/word)
    + 图谱子图与问题的匹配度
    + 实体类型与问题的匹配度
    + 实体长度
    + 实体在图谱中关系个数/出现频率
    + 实体与疑问词距离
    + ...
  + 模型
    + lambdarank
    + xgboost
    + logistic regression
+ **关系模型1：关系识别与排序**(1/2hop)
  + 关系和问题的语义相似度（bert-bilstm-fc-cosine）
  + 关系值和问题的语义相似度（bert-bilstm-fc-cosine）
  + 关系和问题的字符覆盖率
+ **关系模型2：路径排序**
  + 将链接到的实体和 **实体的1/2跳关系** 组成路径，通过bert-similarity模型进行训练
  + 路径与问题的jaccard，编辑距离
  + 自身定义的模板匹配度...
+ **关系模型3：规则匹配排序**
  + 将问题分割为多个部分，参照word/phrases in the kb + existing word segmentation tools，将问题分为各部分都和kb中实体/属性/关系相似的部分，按分值高低与知识图谱对应部分进行链接。
  + 将问题分为单跳，多跳类型（共8种），记录下各自的结构，与问题中分割出的问题结构进行相似度比较
+ **问句类型选择**
  + bert/cnn/rnn分类模型确定单跳/多跳种类

一般针对单跳问题：**实体识别+实体链接+关系模型**

针对多跳问题：**实体识别+实体链接+问句类型选择+关系模型 / 实体识别+实体链接+关系匹配(路径排序)**

## 3. 相关工作

### 3.1 NLPCC+CCKS论文集&笔记

#### 3.1.1 CCKS论文集&笔记

+ [2019](CCKS+NLPCC papers&notes/CCKS/CCKS2019)

+ [2018](CCKS+NLPCC papers&notes/CCKS/CCKS2018)

#### 3.1.2 NLPCC论文集&笔记

+ [2018](CCKS+NLPCC papers&notes/NLPCC/NLPCC2018)
+ [2017](CCKS+NLPCC papers&notes/NLPCC/NLPCC2017)

### 3.2 知识图谱Talk Slides

+ [CCKS slides](CCKS+NLPCC slides/CCKS)
+ [NLPCC slides](CCKS+NLPCC slides/NLPCC)

### 3.3 企业知识图谱产品说明

+ [Google](https://www.blog.google/products/search/introducing-knowledge-graph-things-not/)

+ [Bing](https://blogs.bing.com/search-quality-insights/2017-07/bring-rich-knowledge-of-people-places-things-and-local-businesses-to-your-apps)

+ [Uber](https://eng.uber.com/uber-eats-query-understanding/)
+ [Amazon](https://blog.aboutamazon.com/innovation/making-search-easier)
+ [Airbnb](https://medium.com/airbnb-engineering/scaling-knowledge-access-and-retrieval-at-airbnb-665b6ba21e95)
+ [eBay](https://www.ebayinc.com/stories/news/cracking-the-code-on-conversational-commerce/)
+ [Linkedin](https://engineering.linkedin.com/blog/2016/10/building-the-linkedin-knowledge-graph)
+ [Accenture](https://www.accenture.com/us-en/insights/digital/data-to-knowledge)
+ [Bloomberg](https://speakerdeck.com/emeij/understanding-news-using-the-bloomberg-knowledge-graph)
+ [Maana](https://engineering.linkedin.com/blog/2016/10/building-the-linkedin-knowledge-graph)
+ [阿里巴巴1](http://www.elecfans.com/d/908682.html)，[阿里巴巴2](https://www.sohu.com/a/168239286_629652)
+ [腾讯云知文](https://max.book118.com/html/2019/0122/8023043054002003.shtm)
+ [百度](https://baijiahao.baidu.com/s?id=1643915882369765998&wfr=spider&for=pc)
+ [美团KG构建方法](https://tech.meituan.com/2018/11/01/meituan-ai-nlp.html)，[美团餐饮娱乐知识图谱](https://tech.meituan.com/2018/11/22/meituan-brain-nlp-01.html)，[美团BERT](https://tech.meituan.com/2019/11/14/nlp-bert-practice.html)

