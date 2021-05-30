from firebase import firebase

fb = firebase.FirebaseApplication("https://mavera-31c55-default-rtdb.firebaseio.com/",None)

# Sensörlerden gelen verileri aşağıda uygun değişkenlere ata

HES ='U4U6-9725-15' #String
Temperature = 36.3 #double
haveMask = False #Boolean


result = fb.put("User","HES",HES)
result = fb.put("User","Temperature",Temperature)
result = fb.put("User","haveMask",haveMask)


