USE [it_jobs]
GO

/****** Object:  Table [dbo].[city_stats]    Script Date: 8/2/2020 5:13:39 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[city_stats](
	[yearmonth] [int] NOT NULL,
	[city] [nvarchar](50) NOT NULL,
	[salary] [int] NOT NULL,
 CONSTRAINT [PK_city_stats] PRIMARY KEY CLUSTERED 
(
	[yearmonth] ASC,
	[city] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


