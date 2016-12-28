fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x='d_rest', y='home_win',
            data=df.loc[(-3 <= df.d_rest) &
                        (df.d_rest <= 3)],
            color='#4c72b0', ax=ax)
sns.despine()
