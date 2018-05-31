import pandas, folium

data = pandas.read_excel("koordinatlar 30052018.xlsx")
enlem = list(data["Enlem"])
boylam = list(data["Boylam"])
ciro = list(data["İlk 4 Ay Ciro"])
bayi = list(data["Bayi"])
stler = list(data["Satis Temsilcisi"])
nokta = list(data["Müsteri Adi"])
kanal = list(data["Müsteri Grubu"])

def renk(dist):
    if dist == "ER HOCAOGLU - KOCAELI":
        return "blue"
    elif dist == "DILIKOGLU - SAKARYA":
        return "orange"
    elif dist == "AYPAR-DÜZCE" or dist == "AYPAR-BOLU":
        return "green"
    elif dist == "DORUK-ESKISEHIR":
        return "red"
    else:
        return "yellow"

map = folium.Map(location=[40.706747,29.93855], zoom_start=6)

fg = folium.FeatureGroup(name="My Map")
for enl,boy,c,byi,st,nok,knl in zip(enlem,boylam,ciro,bayi,stler,nokta,kanal):
    fg.add_child(folium.CircleMarker(location=[boy,enl], radius=6, popup="Kanal: "+knl+" ST: "+st+" "+nok+" 2018 İlk 4 Ay Ciro: "+str(c),
    color="grey", fill_opacity=0.7,fill_color=renk(byi)))

map.add_child(fg)

map.save("DM Koordinatlar 30052018.html")
