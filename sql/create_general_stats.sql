USE [it_jobs]
GO

/****** Object:  Table [dbo].[general_stats]    Script Date: 8/2/2020 5:14:16 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[general_stats](
	[yearmonth] [int] NOT NULL,
	[salary_mean] [int] NOT NULL,
	[salary_median] [int] NOT NULL,
	[jd_count] [int] NOT NULL,
	[head_count] [int] NOT NULL,
 CONSTRAINT [PK_general_stats] PRIMARY KEY CLUSTERED 
(
	[yearmonth] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


