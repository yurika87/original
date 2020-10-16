import pandas as pd
import matplotlib.pyplot as plt

injured_data = pd.read_csv('injured.csv')
   
hiroshima_speed = pd.read_csv('hiroshima.csv')
hanshin_speed = pd.read_csv('hanshin.csv')
kyojin_speed = pd.read_csv('kyojin.csv')
yakuruto_speed = pd.read_csv('yakuruto.csv')
chunichi_speed = pd.read_csv('chunichi.csv')
dena_speed = pd.read_csv('dena.csv')
seibu_speed = pd.read_csv('seibu.csv')
hamu_speed = pd.read_csv('hamu.csv')
rotte_speed = pd.read_csv('rotte.csv')
orikkusu_speed = pd.read_csv('orikkusu.csv')
softbank_speed = pd.read_csv('softbank.csv')
rakuten_speed = pd.read_csv('rakuten.csv')

join_speed = pd.concat([hiroshima_speed, hanshin_speed, kyojin_speed, yakuruto_speed, chunichi_speed, dena_speed, seibu_speed, hamu_speed, rotte_speed, orikkusu_speed, softbank_speed, rakuten_speed], ignore_index=True)

#print(join_speed)

injured_data["選手名"] = injured_data["選手名"].str.replace(" ","")

join_speed["選手名"] = join_speed["選手名"].str.replace('\d+', '')
join_speed["選手名"] = join_speed["選手名"].str.replace(':', '')

join_data_all = pd.merge(join_speed, injured_data, left_on="選手名", right_on="選手名", how="left")
join_data_injured = pd.merge(injured_data, join_speed, left_on="選手名", right_on="選手名", how="inner")

join_data_all.to_csv("join_data_all.csv", index=False)
#print(join_data)
join_data_injured.to_csv("join_data_injured", index=False)

dump_data_all = join_data_all[["選手名", "球団", "最高球速", "最低球速", "球速差", "日付", "詳細"]]
dump_data_all = dump_data_all.drop_duplicates()
#print(dump_data[dump_data.duplicated()])
dump_data_all.to_csv("dump_data_all.csv", index=False)

dump_data_injured = join_data_injured[["選手名", "球団", "最高球速", "最低球速", "球速差", "日付", "詳細"]]
dump_data_injured.to_csv("dump_data_injured.csv", index=False)


print("全体の最高球速の平均:" + str(dump_data_all["最高球速"].mean()))
print("けが人の最高球速の平均:" + str(dump_data_injured["最高球速"].mean()))

print("全体の球速差の平均:" + str(dump_data_all["球速差"].mean()))
print("けが人の球速差の平均:" + str(dump_data_injured["球速差"].mean()))

print("全体の最低球速の平均:" + str(dump_data_all["最低球速"].mean()))
print("けが人の最低球速の平均:" + str(dump_data_injured["最低球速"].mean()))



elbow = dump_data_all[dump_data_all['詳細'].str.contains('肘', na=False)]
sholder = dump_data_all[dump_data_all['詳細'].str.contains('肩', na=False)]
arm_injure = pd.concat([elbow, sholder], ignore_index=True)
#print(arm_injure)

print("肘・肩にケガをした投手の最高球速の平均：" + str(arm_injure["最高球速"].mean()))