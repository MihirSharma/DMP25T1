import math

atlanta_lat = math.radians(33.7501)
atlanta_long = math.radians(84.3885)

orlando_lat = math.radians(28.5384)
orlando_long = math.radians(81.3789)

savannah_lat = math.radians(32.0809)
savannah_long = math.radians(81.0912)

charlotte_lat = math.radians(35.2216)
charlotte_long = math.radians(80.8401)

dao = 6371.01 * math.acos(math.sin(atlanta_lat)*math.sin(orlando_lat) + math.cos(atlanta_lat)*math.cos(orlando_lat)* math.cos(orlando_long-atlanta_long))
das = 6371.01 * math.acos(math.sin(atlanta_lat)*math.sin(savannah_lat) + math.cos(atlanta_lat)*math.cos(savannah_lat)* math.cos(savannah_long-atlanta_long))
dac = 6371.01 * math.acos(math.sin(atlanta_lat)*math.sin(charlotte_lat) + math.cos(atlanta_lat)*math.cos(charlotte_lat)* math.cos(charlotte_long-atlanta_long))
doc = 6371.01 * math.acos(math.sin(orlando_lat)*math.sin(charlotte_lat) + math.cos(orlando_lat)*math.cos(charlotte_lat)* math.cos(charlotte_long-orlando_long))
dos = 6371.01 * math.acos(math.sin(orlando_lat)*math.sin(savannah_lat) + math.cos(orlando_lat)*math.cos(savannah_lat)* math.cos(savannah_long-orlando_long))
dcs = 6371.01 * math.acos(math.sin(charlotte_lat)*math.sin(savannah_lat) + math.cos(charlotte_lat)*math.cos(savannah_lat)* math.cos(savannah_long-charlotte_long))


# print(dao,das,dac,doc,dos,dcs) #dao and doc

s_OCS = (doc + dcs + dos)/2
area_OCS = math.sqrt(s_OCS*(s_OCS-doc)*(s_OCS-dcs)*(s_OCS-dos))

s_OCA = (doc+ dao+ dac)/2
area_OCA = math.sqrt(s_OCA*(s_OCA-doc)*(s_OCA-dao)*(s_OCA-dac))

area = area_OCA+area_OCS

print(f"area bound by the cities is {area} sq.km")