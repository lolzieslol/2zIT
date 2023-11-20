'''
selve ordene definert ved hjelp av ordklasse
uavhengig av main
'''

import ordklasse as o

#gruppe 1
jeg = o.DetPersonligePronomenet("jeg",1,"SubJekt")
er = o.Verbet("er", "presens")
ikke = o.Ordet("ikke")
deg = o.DetPersonligePronomenet("deg",1,"akkusativ", None)

ordliste : list = [jeg,er,ikke,deg]


#gruppe 2
programvare = o.Substantivet("programvare","hankjønn")    
det = o.Pronomenet("det")
den = o.Pronomenet("den")
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
du = o.DetPersonligePronomenet("du",2,"subjekt",None)
vedkommende = o.DetPersonligePronomenet("vedkommende",3,"subjekt","annet")
hen = o.DetPersonligePronomenet("hen",3,"subjekt","annet")
han = o.DetPersonligePronomenet("han",3,"subjekt","hankjønn")
hun = o.DetPersonligePronomenet("hun",3,"subjekt","hunkjønn")
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

#gruppe 3

bolle = o.Substantivet("bolle","hankjønn")
vitenskap = o.Substantivet("vitenskap","hankjønn")
fysikk = o.Substantivet("fysikk","hankjønn")
informatikk = o.Substantivet("informatikk","hankjønn")
bok = o.Substantivet("bok","hankjønn")
kjemi = o.Substantivet("kjemi","hankjønn")
oppskrift = o.Substantivet("oppskrift","hankjønn")
urt = o.Substantivet("urt","hankjønn")
ide = o.Substantivet("ide","intetkjønn")
verb = o.Substantivet("verb","intetkjønn")
drikker = o.Verbet("drikker","presens")
formulerer = o.Verbet("formulerer","presens")
klandrer = o.Verbet("klandrer","presens")
koselig = o.Adjektivet("koselig")
fornybar = o.Adjektivet("fornybar")
tulling = o.Substantivet("tulling","hankjønn")
faglitteratur = o.Substantivet("faglitteratur","hankjønn")
prøver = o.Verbet("prøver","presens")
prøve = o.Substantivet("prøve","hankjønn")
bygger = o.Verbet("bygger")
glad = o.Adjektivet("glad")
sint = o.Adjektivet("sint")
trist = o.Adjektivet("sint")
frustrerende = o.Adjektivet("frustrerende")
beklagelig = o.Adjektivet("beklagelig")
heldig = o.Adjektivet("heldig")
forskning = o.Substantivet("forskning","hankjønn")
studerer = o.Verbet("studerer")
presenterer = o.Verbet("presenterer")
resultat = o.Substantivet("resultat","intetkjønn")
lykkelig = o.Adjektivet("lykkelig")
merkverdig = o.Adjektivet("merkverdig")
misfornøyd = o.Adjektivet("misfornøyd")
oransje = o.Adjektivet("oransje")
gruve = o.Substantivet("gruve","hankjønn")
ondskapsfull = o.Adjektivet("ondskapsfull")
kontroversiel = o.Adjektivet("kontroversiel")
materiel = o.Adjektivet("materiel")
skadelig = o.Adjektivet("skadelig")
ødelagt = o.Adjektivet("ødelagt")
liste = o.Substantivet("liste","hankjønn")
lese = o.Verbet("lese")
orddelingsfeil = o.Substantivet("orddelingsfeil","hankjønn")

setningOrientertOrdliste : list = [jeg,er,ikke,deg,programvare,det,den,gruppe,forsto,energidrikk,latterlig,fornøyelig,øy,kort,mobil, innhold,fargerik,spennende,fjell,hav,stol,bilde, person,forfatter,du,hen,han,hun,spiser,lærer,utvikler,tester,stor,lykkelig,rask,moderne,rolig,bolle,vitenskap,fysikk,bok,informatikk, kjemi, oppskrift,urt,ide,verb,drikker,formulerer,klandrer, koselig,fornybar,tulling,faglitteratur,prøver,prøve,bygger,glad,sint,trist,frustrerende,beklagelig,forskning,studerer,presenterer,lykkelig,merkverdig,misfornøyd,oransje,gruve,ondskapsfull,kontroversiel,materiel,skadelig,ødelagt,liste,lese,orddelingsfeil]


setningOrientertOrdlisteForståelig : list = [jeg,er,ikke,deg,programvare,det,den,gruppe,forsto,energidrikk,latterlig,fornøyelig,øy,kort,mobil, innhold,fargerik,spennende,fjell,hav,stol,bilde, person,forfatter,du,hen,han,hun,lærer,utvikler,tester,stor,lykkelig,moderne,rolig,bolle,vitenskap,fysikk,bok,informatikk, kjemi, oppskrift,urt,ide,verb,formulerer,klandrer, koselig,fornybar,tulling,faglitteratur,prøver,prøve,bygger,glad,sint,trist,frustrerende,beklagelig,forskning,studerer,presenterer,lykkelig,merkverdig,misfornøyd,oransje,gruve,ondskapsfull,kontroversiel,materiel,skadelig,ødelagt,liste,lese,orddelingsfeil]
