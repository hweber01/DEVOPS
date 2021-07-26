#dictionaries
'''
adict={"www.google.com":"8.8.8.8","www.facebook.com":"7.7.7.7","www.youtube.com":["5.5.5.5","4.4.4.4"]}
bdict=dict()
cdict={"www.cccc.com":"9.9.9.9","wwww.dddd.com":"11.11.11.11"}
adict.update({"www.aaa.com":"9.9.9.9","wwww.bbb.com":"11.11.11.11"})
dictd={cdict.update(adict)}


print(adict)
print(cdict)
print(dictd)
print(str(len(adict)))
print(str(len(cdict)))
print(adict["www.google.com"])
print(adict.values())
adict["www.google.com"]="8.4.8.4"
print(adict["www.google.com"])
print(adict.values())

print("www.googl.com" in adict)
print("7.8.7.7" in adict.values())
'''

#LAB05

tdict={"Ron Smith":982,"James Jones":32,"Martha Viniard":28,"Brandy Car":40,"Jonah Brother":735}
print(tdict)
a=tdict["Ron Smith"] + tdict["Jonah Brother"]
tdict.update({"eric clap": a})
print("this is the sum of money: " + str(a))
print(tdict)
print(str(len(tdict)))
print("rosanne" in tdict)
