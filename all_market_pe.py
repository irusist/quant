import pandas as pd

df_pe = pd.DataFrame.from_csv("/Users/zhulx/pe.csv")
date_list = df_pe.index.tolist()

pe_ratio_list = []
for d in date_list:
    print(d)
    pe_list = df_pe[:d]
    pe_ratio = len(pe_list.PE[pe_list.PE < pe_list.iloc[-1].PE])/float(len(pe_list.PE))*100
    pe_ratio_list.append(pe_ratio)

df = pd.DataFrame({'pe' : pd.Series(pe_ratio_list, index=date_list)})

df.to_csv('/Users/zhulx/pe_ratio.csv')


