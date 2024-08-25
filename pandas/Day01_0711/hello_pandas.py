import pandas

print(pandas.__version__)

df =pandas.read_csv('../data/gapminder.tsv',sep='\t')
print(df)