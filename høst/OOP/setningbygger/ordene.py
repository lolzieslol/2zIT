'''
selve ordene definert ved hjelp av ordklasse + ordlister
'''

# "fjell" or self.name == "kjemi" or self.name == "fysikk" or self.name == "hav" or self.name == "kort": 

import ordklasse as o

#gruppe 1
jeg = o.DetPersonligePronomenet("jeg",1,"SubJekt")
er = o.Verbet("er", "presens")
ikke = o.Ordet("ikke")
deg = o.DetPersonligePronomenet("deg",1,"akkusativ", None)

ordliste : list = [jeg,er,ikke,deg]


#gruppe 2
programvare = o.Substantivet("programvare","hankjønn")    
det = o.DetPersonligePronomenet("det")
den = o.DetPersonligePronomenet("den") 
gruppe = o.Substantivet("gruppe","hankjønn")
forsto = o.Verbet("forsto","fortid")
energidrikk = o.Substantivet("energidrikk","hankjønn")
latterlig = o.Adjektivet("latterlig")
fornøyelig = o.Adjektivet("fornøyelig")
øy = o.Substantivet("øy","hankjønn")
kort = o.Substantivet("kort","intetkjønn","ingen")
mobil = o.Substantivet("mobil","hankjønn")
innhold = o.Substantivet("innhold","intetkjønn","ingen")
fargerik = o.Adjektivet("fargerik")
spennende = o.Adjektivet("spennende")
fjell = o.Substantivet("fjell", "intetkjønn","ingen")
hav = o.Substantivet("hav", "intetkjønn","ingen")
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
fysikk = o.Substantivet("fysikk","hankjønn","ingen")
informatikk = o.Substantivet("informatikk","hankjønn")
bok = o.Substantivet("bok","hankjønn","annen")
kjemi = o.Substantivet("kjemi","hankjønn","ingen")
oppskrift = o.Substantivet("oppskrift","hankjønn")
urt = o.Substantivet("urt","hankjønn")
ide = o.Substantivet("ide","hankjønn")
verb = o.Substantivet("verb","intetkjønn","ingen")
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
leser = o.Verbet("leser")
orddelingsfeil = o.Substantivet("orddelingsfeil","hankjønn")

#gruppe 3
to = o.Mengdeordet("to","2") 
tre = o.Mengdeordet("tre",3)
fire = o.Mengdeordet("fire",4)
fem = o.Mengdeordet("fem",5)
tusen = o.Mengdeordet("tusen",1000)
sol = o.Substantivet("sol","hunkjønn")

#gruppe 4
interessant = o.Adjektivet("interessant")
vi = o.DetPersonligePronomenet("vi",1,"subjekt",None,"flertall")
dere = o.DetPersonligePronomenet("dere",2,"subjekt",None,"flertall")
de = o.DetPersonligePronomenet("de",3,"subjekt",None,"flertall")
hyggelig = o.Adjektivet("hyggelig")
hygge = o.Substantivet("hygge","hankjønn")
brann = o.Substantivet("brann","hankjønn")
foreslår = o.Verbet("foreslår")
bibliografi = o.Substantivet("bibliografi","hankjønn")
bibliotek = o.Substantivet("bibliotek","intetkjønn")
miljø = o.Substantivet("miljø","intetkjønn","ingen")

#gruppe 5
som = o.DetRelativePronomenet("som")
man = o.Pronomenet("man")
hvem = o.SpørrePronomenet("hvem")
hva = o.SpørrePronomenet("hva")
mystisk = o.Adjektivet("mystisk")
stille = o.Adverbet("stille")
raskt = o.Adverbet("raskt")
effektivt = o.Adverbet("effektivt")
forsiktig = o.Adverbet("forsiktig")
heldigvis = o.Adverbet("heldigvis")
fornuftig = o.Adverbet("fornuftig")
ingen = o.Mengdeordet("ingen",0)
alle = o.Mengdeordet("alt",None) #sære regler (implementere?) (all/alle/alt)
tar = o.Verbet("tar")
forandrer = o.Verbet("forandrer")
endret = o.Verbet("endret","fortid")

setningOrientertOrdliste : list = [jeg,er,ikke,deg,programvare,det,den,gruppe,forsto,energidrikk,latterlig,fornøyelig,øy,kort,mobil, innhold,fargerik,spennende,fjell,hav,stol,bilde, person,forfatter,du,hen,han,hun,spiser,lærer,utvikler,tester,stor,lykkelig,rask,moderne,rolig,bolle,vitenskap,fysikk,bok,informatikk, kjemi, oppskrift,urt,ide,verb,drikker,formulerer,klandrer, koselig,fornybar,tulling,faglitteratur,prøver,prøve,bygger,glad,sint,trist,frustrerende,beklagelig,forskning,studerer,presenterer,lykkelig,merkverdig,misfornøyd,oransje,gruve,ondskapsfull,kontroversiel,materiel,skadelig,ødelagt,liste,leser,orddelingsfeil,to,tre,fire,fem,tusen,sol,interessant,vi,dere,de,hyggelig,brann,foreslår,bibliografi,bibliotek,vedkommende,miljø,som,man,hvem,hva,mystisk,stille,raskt,effektivt,forsiktig,heldigvis,fornuftig,ingen,alle,forandrer,endret]


setningOrientertOrdlisteForståelig : list = [jeg,er,ikke,deg,programvare,det,den,gruppe,forsto,energidrikk,latterlig,fornøyelig,øy,kort,mobil, innhold,fargerik,spennende,fjell,hav,stol,bilde, person,forfatter,du,hen,han,hun,lærer,utvikler,tester,stor,lykkelig,moderne,rolig,bolle,vitenskap,fysikk,bok,informatikk, kjemi, oppskrift,urt,ide,verb,formulerer,klandrer, koselig,fornybar,tulling,faglitteratur,prøver,prøve,bygger,glad,sint,trist,frustrerende,beklagelig,forskning,studerer,presenterer,lykkelig,merkverdig,misfornøyd,oransje,gruve,ondskapsfull,kontroversiel,materiel,skadelig,ødelagt,liste,leser,orddelingsfeil,to,tre,fire,fem,tusen,sol,interessant,vi,dere,de,hyggelig,brann,foreslår,bibliotek,bibliografi,vedkommende,miljø,som,man,hvem,hva,mystisk,stille,raskt,effektivt,forsiktig,heldigvis,fornuftig,ingen,forandrer,endret]
