# State Groupings (for holdout data)
# d['StateGroup']   = d["State ID"]*0
d_cal = d[d["State"] == "California"]
d["StateGroup"]     = 1
d.loc[d["State ID"] == 5 , ['StateGroup']] = 2
d.loc[d["State ID"] == 10, ['StateGroup']] = 3
d.loc[d["State ID"] == 38, ['StateGroup']] = 4
d.loc[d["State ID"] == 14, ['StateGroup']] = 5
d.loc[d["State ID"] == 33, ['StateGroup']] = 6
# d.loc[d["State"]  =                 = "?", ['StateGroup' ]] = ?
# d.loc[d["State"]  =                 = "?", ['StateGroup' ]] = ?

grp = d["StateGroup"].unique()
g = d[["State ID", "State","StateGroup"]]
g=g.drop_duplicates().nlargest(6,"StateGroup")
print(g.shape)
print(d.shape)
print(g)
