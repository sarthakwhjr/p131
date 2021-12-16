import pandas as pd
import csv 


df=pd.read_csv("main.csv")

df['Radius']=df['Radius'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
mass= df ["Mass"].to_list()
radius= df ["Radius"].to_list()
gravity =[]

def convert_to_si(radius,mass):
    for i in range(0,len(radius)-1):
        radius[i] = radius[i]*6.957e+8
        mass[i] = mass[i]*1.989e+30
        
convert_to_si(radius,mass)
def gravity_calculation(radius,mass):
    G = 6.674e-11
    for index in range(0,len(mass)):
        g= (mass[index]*G)/((radius[index])**2)
        gravity.append(g)
        
gravity_calculation(radius,mass)

df["Gravity"] = gravity
df.to_csv("star_with_gravity.csv")
