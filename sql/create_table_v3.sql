USE [it_jobs]
GO

/****** Object:  Table [dbo].[jobs]    Script Date: 6/28/2020 9:23:04 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[jobs](
	[job_id] [varchar](20) NOT NULL,
	[yearmonth] [int] NOT NULL,
	[monthly_salary] [int] NOT NULL,
	[headcount] [bigint] NOT NULL,
	[title] [nvarchar](max) NOT NULL,
	[page_title] [nvarchar](max) NOT NULL,
	[zhinengleibie] [nvarchar](100) NOT NULL,
	[career] [nvarchar](100) NOT NULL,
	[city] [nvarchar](20) NOT NULL,
	[province] [nvarchar](20) NOT NULL,
	[company_id] [nvarchar](max) NOT NULL,
	[ageism] [bit] NOT NULL,
	[db_Apache_Hive] [bit] NOT NULL,
	[db_CouchBase] [bit] NOT NULL,
	[db_CouchDB] [bit] NOT NULL,
	[db_DB2] [bit] NOT NULL,
	[db_DynamoDB] [bit] NOT NULL,
	[db_Elasticsearch] [bit] NOT NULL,
	[db_FileMaker] [bit] NOT NULL,
	[db_Firebase] [bit] NOT NULL,
	[db_Firebird] [bit] NOT NULL,
	[db_Hbase] [bit] NOT NULL,
	[db_Informix] [bit] NOT NULL,
	[db_Ingres] [bit] NOT NULL,
	[db_MariaDB] [bit] NOT NULL,
	[db_Memcached] [bit] NOT NULL,
	[db_MongoDB] [bit] NOT NULL,
	[db_MySQL] [bit] NOT NULL,
	[db_Neo4j] [bit] NOT NULL,
	[db_Netezza] [bit] NOT NULL,
	[db_Oracle] [bit] NOT NULL,
	[db_PostgreSQL] [bit] NOT NULL,
	[db_Redis] [bit] NOT NULL,
	[db_Riak] [bit] NOT NULL,
	[db_SAP_HANA] [bit] NOT NULL,
	[db_SQL_Server] [bit] NOT NULL,
	[db_SQLite] [bit] NOT NULL,
	[db_Solr] [bit] NOT NULL,
	[db_Splunk] [bit] NOT NULL,
	[db_Sybase] [bit] NOT NULL,
	[db_Teradata] [bit] NOT NULL,
	[db_dBase] [bit] NOT NULL,
	[edu] [nvarchar](100) NOT NULL,
	[experience] [nvarchar](100) NOT NULL,
	[expert_adas] [bit] NOT NULL,
	[expert_blockchain] [bit] NOT NULL,
	[expert_embed] [bit] NOT NULL,
	[expert_expert] [bit] NOT NULL,
	[expert_gis] [bit] NOT NULL,
	[_996_yes] [bit] NOT NULL,
	[_996_no] [bit] NOT NULL,
	[lang_english] [bit] NOT NULL,
	[lang_japanese] [bit] NOT NULL,
	[job_description] [nvarchar](max) NOT NULL,
	[job_summary] [nvarchar](100) NOT NULL,
	[job_tags] [nvarchar](100) NOT NULL,
	[phone_android] [bit] NOT NULL,
	[phone_app] [bit] NOT NULL,
	[phone_iso] [bit] NOT NULL,
	[pl_c_sharp] [bit] NOT NULL,
	[pl_cpp] [bit] NOT NULL,
	[pl_delphi] [bit] NOT NULL,
	[pl_go] [bit] NOT NULL,
	[pl_haskell] [bit] NOT NULL,
	[pl_java] [bit] NOT NULL,
	[pl_javascript] [bit] NOT NULL,
	[pl_julia] [bit] NOT NULL,
	[pl_kotlin] [bit] NOT NULL,
	[pl_lua] [bit] NOT NULL,
	[pl_matlab] [bit] NOT NULL,
	[pl_objective_c] [bit] NOT NULL,
	[pl_perl] [bit] NOT NULL,
	[pl_php] [bit] NOT NULL,
	[pl_python] [bit] NOT NULL,
	[pl_ruby] [bit] NOT NULL,
	[pl_rust] [bit] NOT NULL,
	[pl_swift] [bit] NOT NULL,
	[pl_typescript] [bit] NOT NULL,
	[pl_vba] [bit] NOT NULL,
	[pl_visual_basic] [bit] NOT NULL,
	[pl_r] [bit] NOT NULL,
	[pl_scala] [bit] NOT NULL,
	[publish_date] [datetime] NOT NULL,
	[published_on_weekend] [bit] NOT NULL,
	[tag_baby_care] [bit] NOT NULL,
	[tag_five_insurance] [bit] NOT NULL,
	[tag_flexible] [bit] NOT NULL,
	[tag_no_overtime] [bit] NOT NULL,
	[tag_rest_one_day] [bit] NOT NULL,
	[tag_rest_two_days] [bit] NOT NULL,
	[tag_stock] [bit] NOT NULL,
	[ml_tensorflow] [bit] NOT NULL,
	[ml_caffe] [bit] NOT NULL,
	[ml_cntk] [bit] NOT NULL,
	[ml_chainer] [bit] NOT NULL,
	[ml_mxnet] [bit] NOT NULL,
	[ml_keras] [bit] NOT NULL,
	[ml_deeplearning4j] [bit] NOT NULL,
	[ml_theano] [bit] NOT NULL,
	[ml_sklearn] [bit] NOT NULL,
	[ml_mahout] [bit] NOT NULL,
	[ml_paddlepaddle] [bit] NOT NULL,
	[bd_hadoop] [bit] NOT NULL,
	[bd_spark] [bit] NOT NULL,
	[bd_hive] [bit] NOT NULL,
	[bd_mapReduce] [bit] NOT NULL,
	[bd_kafka] [bit] NOT NULL,
	[bd_hbase] [bit] NOT NULL,
	[bd_storm] [bit] NOT NULL,
	[bd_pig] [bit] NOT NULL,
	[bd_mahout] [bit] NOT NULL,
	[bd_impala] [bit] NOT NULL,
	[bd_yarn] [bit] NOT NULL,
	[bd_alluxio] [bit] NOT NULL,
	[bd_flink] [bit] NOT NULL,
	[bd_presto] [bit] NOT NULL,
	[bd_heron] [bit] NOT NULL,
 CONSTRAINT [PK_jobs] PRIMARY KEY CLUSTERED 
(
	[job_id] ASC,
	[yearmonth] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_expert_adas]  DEFAULT ((0)) FOR [expert_adas]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_expert_blockchain]  DEFAULT ((0)) FOR [expert_blockchain]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_expert_embed]  DEFAULT ((0)) FOR [expert_embed]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_expert_expert]  DEFAULT ((0)) FOR [expert_expert]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_expert_gis]  DEFAULT ((0)) FOR [expert_gis]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_pl_r]  DEFAULT ((0)) FOR [pl_r]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_pl_scala]  DEFAULT ((0)) FOR [pl_scala]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_ml_tensorflow]  DEFAULT ((0)) FOR [ml_tensorflow]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_ml_caffe]  DEFAULT ((0)) FOR [ml_caffe]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_ml_cntk]  DEFAULT ((0)) FOR [ml_cntk]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_ml_chainer]  DEFAULT ((0)) FOR [ml_chainer]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_ml_mxnet]  DEFAULT ((0)) FOR [ml_mxnet]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_ml_keras]  DEFAULT ((0)) FOR [ml_keras]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_ml_deeplearning4j]  DEFAULT ((0)) FOR [ml_deeplearning4j]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_ml_theano]  DEFAULT ((0)) FOR [ml_theano]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_ml_sklearn]  DEFAULT ((0)) FOR [ml_sklearn]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_ml_mahout]  DEFAULT ((0)) FOR [ml_mahout]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_ml_paddlepaddle]  DEFAULT ((0)) FOR [ml_paddlepaddle]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_bd_hadoop]  DEFAULT ((0)) FOR [bd_hadoop]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_bd_spark]  DEFAULT ((0)) FOR [bd_spark]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_bd_hive]  DEFAULT ((0)) FOR [bd_hive]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_bd_mapReduce]  DEFAULT ((0)) FOR [bd_mapReduce]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_bd_kafka]  DEFAULT ((0)) FOR [bd_kafka]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_bd_hbase]  DEFAULT ((0)) FOR [bd_hbase]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_bd_storm]  DEFAULT ((0)) FOR [bd_storm]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_bd_pig]  DEFAULT ((0)) FOR [bd_pig]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_bd_mahout]  DEFAULT ((0)) FOR [bd_mahout]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_bd_impala]  DEFAULT ((0)) FOR [bd_impala]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_bd_yarn]  DEFAULT ((0)) FOR [bd_yarn]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_bd_alluxio]  DEFAULT ((0)) FOR [bd_alluxio]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_bd_flink]  DEFAULT ((0)) FOR [bd_flink]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_bd_presto]  DEFAULT ((0)) FOR [bd_presto]
GO

ALTER TABLE [dbo].[jobs] ADD  CONSTRAINT [DF_jobs_bd_heron]  DEFAULT ((0)) FOR [bd_heron]
GO


