# What ����ʲô
A template for most tensorflow projects.  

��һ���ļ���֯ģ�塣

# Why ΪʲôҪ�������Ŀ
I am a beginner and found that there is a far distance from the tensorflow example to mature, community-recognized tensorflow code.    
In order to maximize the extent of model reuse, the community gradually formed a set of unwritten standards. As a beginner, I try to discover these standards and start learning in an orderly manner.  

����һ����ѧ�ߣ����ִ�tensorflow���������ӣ�������ģ��������ϵ�tensorflow�����в�С�ľ��롣  
Ϊ�����ģ�͸��ó̶ȣ��������γ���һ�ײ����ĵı�׼������Ϊ��ѧ�ߣ�����ȥ������Щ��׼��������ؿ�ʼѧϰ��

# Zen of Deep Learning codes ����ѧϰ����֮��
- Experimental steps should write on the .sh for better debugging  
ʵ�鲽�����bash����ڵ���
- Training steps should write with TensorFlow-API to improve performance
ѵ������tf������������
- With the new model, you can not change more than two files, model.py and architecture.json
����ģ�͵�ʱ�򣬲�Ҫ�ĳ��������ļ���model.py �� architecture.json 
- Let anyone run with one command
Ҫ�ø��ֵ���һ�����������ͨ
- Let anyone who want to improve the model focus on one file, model.py  
����Ҫ�Ľ�����ֻ��Ҫ���и�һ���ļ� model.py
- Decouples the model, data, and code (those that are independent of the model and the data)  
��ģ�ͣ����ݺʹ��루��ģ�ͺ������޹ص���Щ���룩����

# Goal Ŀ��
Maximizing code reuse, and limit the frequently user-modified parts in a few files.  

��󻯴��븴���ʣ�����ҪƵ��Ҫ�Լ�д�Ĳ��ֶ��޶��ڵ����ļ����ļ��С�

# TODO δ��
- [ ] Move data prepare procedure to download.sh and prepare_features.py  
������׼�������ƶ���download.sh��prepare_features.py��
- [ ] Add Minist_example.sh for these procedure:data_prepare - train - eval  
����Minist_example.sh���������²���data_prepare - train - eval
- [ ] Add eval.py to show some summary informations and some visualization code  
����eval.py����չʾģ����֤��Ϣ�Ϳ��ӻ���Ϣ
- [ ] Compatible with common styles like [this](https://github.com/wiseodd/generative-models)   
���ݳ���ģ�Ͷ����񣬱���[���](https://github.com/wiseodd/generative-models)
- [ ] Add module examples ( convolution layers, I think)  
����ģ�������(����ģ��)
- [ ] Add .json examples for network architecture definition  
����ʹ��.json�ļ�����ģ�ͽṹ������

Any advices and contributions are welcome!  
Please click [Here](https://github.com/HudsonHuang/tensorflow-template/issues/new) to give your comments. 

��ӭ���ֽ���͹�����
���[�˴�](https://github.com/HudsonHuang/tensorflow-template/issues/new)��������Ľ��顣



