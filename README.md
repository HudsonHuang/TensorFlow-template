| **`Linux CPU`** | 
|-----------------|
| ![Build Status](https://travis-ci.org/HudsonHuang/tensorflow-template.svg?branch=master) | 

# What ����ʲô
A template for most tensorflow projects.  

��һ���ļ���֯ģ�塣

# Why ΪʲôҪ�������Ŀ
I am a beginner and found that there is a far distance from the tensorflow example to mature, community-recognized tensorflow code.    
In order to maximize the extent of model reuse, the community gradually formed a set of unwritten standards. As a beginner, I try to discover these standards and start learning in an orderly manner.  

����һ����ѧ�ߣ����ִ�tensorflow���������ӣ�������ģ��������ϵ�tensorflow�����в�С�ľ��롣  
Ϊ�����ģ�͸��ó̶ȣ��������γ���һ�ײ����ĵı�׼������Ϊ��ѧ�ߣ�����ȥ������Щ��׼��������ؿ�ʼѧϰ��

# Goal Ŀ��
Maximizing code reuse, and limit the frequently user-modified parts in a few files.  

��󻯴��븴���ʣ�����ҪƵ��Ҫ�Լ�д�Ĳ��ֶ��޶��ڵ����ļ����ļ��С�

# Key concepts ���ĸ���
- module.py��model.py����ͼ����ͼ  
module.py and model.py is sub-graph and main-graph
- prepare������׼����  
prepare.py is the data pre-processor
- main��ͼ������������ָ����ʽ��ͨ����ͼע�����ݽ������У�  
main.py is the runner of the graph(feed the prepared data into graph in given manner)


# Zen of Deep Learning codes ����ѧϰ����֮��
- Let anyone run with one command  
Ҫ�ø��ֵ���һ�����������ͨ
- With the new model, you can not change more than two files, model.py and architecture.json  
����ģ�͵�ʱ�򣬲�Ҫ�ĳ��������ļ���model.py �� architecture.json 
- Let anyone who want to improve the model focus on one file, model.py  
����Ҫ�Ľ�����ֻ��Ҫ���и�һ���ļ� model.py
- Decouples the model, data, and code (those that are independent of the model and the data)  
��ģ�ͣ����ݺʹ��루��ģ�ͺ������޹ص���Щ���룩����
- Experimental steps should write on the .sh files for better debugging  
ʵ�鲽��Ӧ�÷���.sh�ļ�������ڵ���
- Training steps should write with TensorFlow-API to improve performance  
ѵ������Ӧ����TensorFlow-API����������������
- Use less TensorFlow for plain style, to the contrary where performance is important
Ҫ���ĵط�����TensorFlow����Ҫ���ܵĵط���֮


# Usage �÷�
- Default run Ĭ���÷�:  
Just run
`
bash all_default.sh
`
And wait everything done.    
ֻ������bash all_default.sh����

- You can edit ���޸ĵĲ���:
  - all_default.sh to fit your enviroumrnt(virtual enviroument, etc)  
    �޸�all_default.sh����Ӧ���Ļ������������⻷��֮��ģ�
  - prepare_features.py to do some data pre-processing  
    �޸�prepare_features.py�Խ���Ԥ����
  - params.py to change model parameters and hyper-parameters   
    �޸�params.py�Ըı�ģ�Ͳ�����ʵ�鳬����
  - models/*.py for models  
     �޸�models�ļ����µ�.py�ļ����Զ���ģ��
  - After modified everything, write a experiment_name.sh file to run it(eg: Minist_example.sh)  
    һ���޸ľ�����дһ��experiment_name.sh�ļ�����������ʵ�飨���Ӽ���Minist_example.sh��

# Sign ����
- x: input data  
x����������
- inputs: input of the model  
inputs��ģ�͵�����
- y: traget data (As label in supervised learning)  
y��Ŀ�����ݣ��ڼලѧϰ�У�����label��
- y_hat or y_: prediction of y  
y_hat����y_��y��Ԥ��ֵ

# TODO ����
- [ ] Compatible with common styles like [this](https://github.com/wiseodd/generative-models)   
���ݳ���ģ�Ͷ����񣬱���[���](https://github.com/wiseodd/generative-models)


# Give up ����
- [ ] Try tensorflow Estimator API to decouples Algorithm(net+loss+optim+...) and meta-Algorithm(experiment procedure: train, test,etc.)  
ʹ��tensorflow Estimator API��main.py�е��㷨(net+loss+optim+...)��ʵ�鲽��(train, test,etc.)��ʵ�鲽��Ҳ������ΪԪ�㷨�����������GAN������

Any advices and contributions are welcome! Please click [Here](https://github.com/HudsonHuang/tensorflow-template/issues/new) to give your comments.   
��ӭ���ֽ���͹�����
���[�˴�](https://github.com/HudsonHuang/tensorflow-template/issues/new)��������Ľ��顣



