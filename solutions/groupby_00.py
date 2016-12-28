df.groupby(df.text.str.len()).review_overall.mean().plot(style='k.')
