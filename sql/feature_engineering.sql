--career
delete from [jobs].[dbo].[_202005] where city ='����' and title like '00%(ְλ��ţ�%)'
delete from [jobs].[dbo].[_202001] where province ='�����Ƹ'
delete from [jobs].[dbo].[_202001] where job_summary like '%Ӧ����%'
delete from [jobs].[dbo].[_202001] where title like '%Ӧ��%'


update _202005 set career='�������ʦ' where zhinengleibie in ('�������ʦ', '�߼��������ʦ', 'PHP��������ʦ', 'Java��������ʦ', 'C��������ʦ', 'Python��������ʦ', '.NET��������ʦ', '�ű���������ʦ', 'Ruby��������ʦ', 'Go��������ʦ')
update _202005 set career='�������ʦ' where career='һ�����Ա'
update _202005 set career='Android��������ʦ' where title like '%Android%' or title like '%��׿%' 

update _202005 set career='�źŴ���' where title like '%�źŴ���%'
update _202005 set career='���濪������ʦ' where title like '%����%'
update _202005 set career='ADAS' where title like '%adas%'
update _202005 set career='������' where title like '%������%' or title like '%ROS%'
update _202005 set career='GIS' where title like '%GIS%'
update _202005 set career='CAE' where title like '%CAE%'
update _202005 set career='��ѧ�㷨' where title like '%��ѧ�㷨����ʦ%'
update _202005 set career='ETL' where title like '%ETL%'
update _202005 set career='Unity3D' where title like '%Unity3D%'
update _202005 set career='ң��' where title like '%ң��%'
update _202005 set career='�滮�㷨' where title like '%�滮�㷨����ʦ%'
update _202005 set career='�Ӿ��������ʦ' where title like '%��ά�ؽ�%'
update _202005 set career='�Ӿ��������ʦ' where title like '%�Ӿ��������ʦ%'


update _202005 set career='������' where title like '%������%'
update _202005 set career='CT�ؽ�' where title like '%CT�ؽ�%'
update _202005 set career='SLAM' where title like '%SLAM%'
update _202005 set career='DSP' where title like '%DSP%'
update _202005 set career='������Ϣ' where title like '%������Ϣ%'
update _202005 set career='��������������ʦ' where title like '%������%'
update _202005 set career='�㷨����ʦ' where title like '%�㷨%' or zhinengleibie='�㷨����ʦ'
update _202005 set career='��Ȼ���Դ���NLP��' where title like '%��Ȼ���Դ���%' or title like '%NLP%'

delete from _202005 where zhinengleibie='�Ƽ��㷨����ʦ' and not title like '%�Ƽ�%'
update _202005 set career='�Ƽ��㷨����ʦ' where title like '%�Ƽ��㷨%'

delete from _202005 where zhinengleibie='�����㷨����ʦ' and not title like '%����%'
update _202005 set career='�����㷨����ʦ' where title like '%�����㷨%' or title like '%Search Algorithm%'
update _202005 set career='�������㷨����ʦ' where title like '%������%'

update _202005 set career='ͼ������ʦ' where title like '%ͼ����%'
update _202005 set career='ͼ���㷨����ʦ' where title like '%ͼ���㷨%' or zhinengleibie='ͼ���㷨����ʦ'
update _202005 set career='�˹�����' where title like '%AI%' or title like '%�˹�����%' or title like '%������%'
update _202005 set career='����������' where title like '%������%' or zhinengleibie='����������'
update _202005 set career='CTO' where title like '%CTO%' or title like '%��ϯ������%'  or title like '%�ǻ��о�ԺԺ��%'
update _202005 set career='оƬ' where title like '%оƬ%' or title like '%SOC���%'
update _202005 set career='��������ʦ'  where title like '%driver%' or title like '%����%'
update _202005 set career='����ѧϰ' where title like '%����ѧϰ%' or zhinengleibie='����ѧϰ����ʦ'
update _202005 set career='���ѧϰ����ʦ' where title like '%���ѧϰ%'
update _202005 set career='���ݿ�ѧ��' where title like '%Data Scientist%' or  title like '%���ݿ�ѧ��%'


update _202005 set career='�ܹ�ʦ' where title like '%ϵͳ�ܹ�ʦ%' or title like '%�ܹ�ʦ%' or title like '%�ܹ�ר��%' or title like '%architect%'   or title like '%�ܹ��з�%'
update _202005 set career='��������' where title like '%����%' or title like '%leader%' 

update _202005 set career='�ֲ�ʽ' where career='�������ʦ' and title like '%�ֲ�ʽ%' 

update _202005 set career='���ݽ���' where title like '%���ݽ���%' or title like '%agile coach%'  or title like '%Scrum Master%' 

update _202005 set career='Cocos2d-x��������ʦ' where career='�������ʦ' and title like '%Cocos2d-x%' 

update _202005 set career='MES' where career='�������ʦ' and title like '%MES%' 

update _202005 set career='Hadoop����ʦ' where title like '%Hadoop%' 

update _202005 set career='Ƕ��ʽ�������' where title like '%Ƕ��ʽ%' or title like '%FPGA%' 

delete from _202005 where career='�˹�����' and not title like '%�˹�����%'


update _202005 set ageism=1 where job_description like '%��%'

update _202005 set ml_paddlepaddle=1 where job_description like '%paddlepaddle%'
update _202005 set ml_mahout=1 where job_description like '%mahout%'
update _202005 set ml_sklearn=1 where job_description like '%scikit-learn%' or  job_description like '%scikitlearn%' or  job_description like '%sklearn%'
update _202005 set ml_theano=1 where job_description like '%theano%'
update _202005 set ml_keras=1 where job_description like '%keras%'
update _202005 set ml_mxnet=1 where job_description like '%mxnet%'
update _202005 set ml_cntk=1 where job_description like '%cntk%'
update _202005 set ml_caffe=1 where job_description like '%caffe%'
update _202005 set ml_tensorflow=1 where job_description like '%tensorflow%'
update _202005 set ml_pytorch=1 where job_description like '%pytorch%'



