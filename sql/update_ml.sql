
--ALTER TABLE _201904 ADD ml_tensorflow bit DEFAULT 0 NOT NULL;
--update _201904 set ml_tensorflow=1, career_algorithm=1  where job_description like '%tensorflow%'

--ALTER TABLE _201904 ADD ml_caffe bit DEFAULT 0 NOT NULL;
--update _201904 set ml_caffe=1, career_algorithm=1  where job_description like '%caffe%'

--ALTER TABLE _201904 ADD ml_cntk bit DEFAULT 0 NOT NULL;
--update _201904 set ml_cntk=1, career_algorithm=1  where job_description like '%cntk%'

--ALTER TABLE _201904 ADD ml_chainer bit DEFAULT 0 NOT NULL;
--update _201904 set ml_chainer=1, career_algorithm=1  where job_description like '%chainer%'

--ALTER TABLE _201904 ADD ml_mxnet bit DEFAULT 0 NOT NULL;
--update _201904 set ml_mxnet=1, career_algorithm=1  where job_description like '%mxnet%'

--ALTER TABLE _201904 ADD ml_keras bit DEFAULT 0 NOT NULL;
--update _201904 set ml_keras=1, career_algorithm=1  where job_description like '%keras%'

--ALTER TABLE _201904 ADD ml_deeplearning4j bit DEFAULT 0 NOT NULL;
--update _201904 set ml_deeplearning4j=1, career_algorithm=1  where job_description like '%deeplearning4j%' or job_description like '%dl4j%'

--ALTER TABLE _201904 ADD ml_theano bit DEFAULT 0 NOT NULL;
--update _201904 set ml_theano=1, career_algorithm=1  where job_description like '%theano%'

--ALTER TABLE _201904 ADD ml_sklearn bit DEFAULT 0 NOT NULL;
--update _201904 set ml_sklearn=1, career_algorithm=1  where job_description like '%scikit-learn%' or  job_description like '%scikitlearn%' or  job_description like '%sklearn%'

--ALTER TABLE _201904 ADD ml_mahout bit DEFAULT 0 NOT NULL;
--update _201904 set ml_mahout=1, career_algorithm=1  where job_description like '%mahout%'

--ALTER TABLE _201904 ADD ml_paddlepaddle bit DEFAULT 0 NOT NULL;
--update _201904 set ml_paddlepaddle=1, career_algorithm=1  where job_description like '%paddlepaddle%'


