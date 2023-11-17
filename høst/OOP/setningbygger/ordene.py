'''
selve ordene definert ved hjelp av ordklasse
uavhengig av main
'''

import ordklasse as o

#gruppe 1
jeg = o.DetPersonligePronomenet("jeg",1,"SubJekt")
er = o.Verbet("er", "presens")
ikke = o.Ordet("ikke")
deg = o.DetPersonligePronomenet("deg",1,"akkusativ")

ordliste : list = [jeg,er,ikke,deg]


#gruppe 2
programvare = o.Substantivet("programvare","hankjønn")    
det = o.Pronomenet("det")
gruppe = o.Substantivet("gruppe","hankjønn")
forsto = o.Verbet("forsto","fortid")
energidrikk = o.Substantivet("energidrikk","hankjønn")
latterlig = o.Adjektivet("latterlig")
fornøyelig = o.Adjektivet("fornøyelig")
øy = o.Substantivet("øy","hankjønn")
kort = o.Substantivet("kort","intetkjønn")
mobil = o.Substantivet("mobil","hankjønn")
innhold = o.Substantivet("innhold","intetkjønn")
fargerik = o.Adjektivet("fargerik")
spennende = o.Adjektivet("spennende")
fjell = o.Substantivet("fjell", "intetkjønn")
hav = o.Substantivet("hav", "intetkjønn")
stol = o.Substantivet("stol", "hunkjønn")
bilde = o.Substantivet("bilde", "intetkjønn")
person = o.Substantivet("person","hankjønn")
forfatter = o.Substantivet("forfatter","hankjønn")
du = o.DetPersonligePronomenet("du",1)
hen = o.DetPersonligePronomenet("hen")
han = o.DetPersonligePronomenet("han")
hun = o.DetPersonligePronomenet("hun")
spiser = o.Verbet("spiser", "presens")
skriver = o.Verbet("skriver", "presens")
lærer = o.Verbet("lærer", "presens")
utvikler = o.Verbet("utvikler", "presens")
tester = o.Verbet("tester", "presens")
stor = o.Adjektivet("stor")
lykkelig = o.Adjektivet("lykkelig")
rask = o.Adjektivet("rask")
moderne = o.Adjektivet("moderne")
rolig = o.Adjektivet("rolig")


setningOrientertOrdliste : list = [jeg,er,ikke,deg,programvare,det,gruppe,forsto,energidrikk,latterlig,fornøyelig,øy,kort,mobil, innhold,fargerik,spennende,fjell,hav,stol,bilde, person,forfatter,du,hen,han,hun,spiser,lærer,utvikler,tester,stor,lykkelig,rask,moderne,rolig]
