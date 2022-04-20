# To remove the rows with column c startswith 'l'
df = df[~df['c'].astype(str).str.startswith('1')]
