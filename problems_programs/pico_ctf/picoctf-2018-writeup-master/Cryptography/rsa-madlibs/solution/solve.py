from pwn import *

s = remote('2018shell1.picoctf.com', 40440)
s.sendline('Y\n8815769761')
print s.recv()
s.sendline('Y\n77773')
print s.recv()
s.sendline('N')
print s.recv()
s.sendline('Y\n6256003596')
print s.recv()
s.sendline('Y\n26722917505435451150596710555980625220524134812001687080485341361511207096550823814926607028717403343344600191255790864873639087129323153797404989216681535785492257030896045464472300400447688001563694767148451912130180323038978568872458130612657140514751874493071944456290959151981399532582347021031424096175747508579453024891862161356081561032045394147561900547733602483979861042957169820579569242714893461713308057915755735700329990893197650028440038700231719057433874201113850357283873424698585951160069976869223244147124759020366717935504226979456299659682165757462057188430539271285705680101066120475874786208053')
print s.recv()
s.sendline('N')
print s.recv()
s.sendline('Y\n1405046269503207469140791548403639533127416416214210694972085079171787580463776820425965898174272870486015739516125786182821637006600742140682552321645503743280670839819078749092730110549881891271317396450158021688253989767145578723458252769465545504142139663476747479225923933192421405464414574786272963741656223941750084051228611576708609346787101088759062724389874160693008783334605903142528824559223515203978707969795087506678894006628296743079886244349469131831225757926844843554897638786146036869572653204735650843186722732736888918789379054050122205253165705085538743651258400390580971043144644984654914856729')
print s.recv()
s.sendline('Y\n240109877286251840533272915662757983981706320845661471802585807564915966910384301849411666983334013')
print s.recv()
s.close()

print str(hex(240109877286251840533272915662757983981706320845661471802585807564915966910384301849411666983334013))[2:].decode('hex')
