USE [it_jobs]
GO

/****** Object:  Table [dbo].[companies]    Script Date: 6/28/2020 9:24:57 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[companies](
	[company_id] [nvarchar](100) NOT NULL,
	[company_size] [nvarchar](100) NOT NULL,
	[company_name] [nvarchar](100) NOT NULL,
	[company_type] [nvarchar](100) NOT NULL,
	[company_description] [varchar](max) NOT NULL,
	[company_industry] [nvarchar](100) NOT NULL,
 CONSTRAINT [PK_companies] PRIMARY KEY CLUSTERED 
(
	[company_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO


