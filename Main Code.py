#Create a Variable for each Jewel type and Rarity
#Multiply using * each type and rarity by quanitiy based off attack %
#Add each stat increase variable together for each Jewel type
import time

print("Hello there, welcome to Squek's Jewel Calculator..")
time.sleep(1)
#=====Infantry Jewels Green - Gold====
grinf = input("How many Green Infantry Attack Jewels do you have? ")
grinf_stat = float(grinf) * 3
time.sleep(1)
binf = input("How many Blue Infantry Attack Jewels do you have? ")
binf_raw = 6
binf_stat = float(binf) * 6
time.sleep(1)
pinf = input("How many Purple Infantry Attack Jewels do you have? ")
pinf_raw = 12
pinf_stat = float(pinf) * 12
time.sleep(1)
ginf = input("How many Gold Infantry Attack Jewels do you have? ")
ginf_raw = 20
ginf_stat = float(ginf) * 20
print("You can gain " + str(grinf_stat) + "% attack from green inf jewels") #total stats from Green
print("You can gain " + str(binf_stat) + "% attack from blue Infantry Jewels." )#total stats from blue
print("You can gain " + str(pinf_stat) + "% attack from Purple Infantry Jewels. ") #total stats from purple
print("You can gain " + str(ginf_stat) + "% attack from Gold Infantry Jewels.") #total stats from gold
#====Cavalry Attack Jewels Green - Gold ====
grcav = input("How many Green Cavalry Jewels do you have? ")
grcav_stat = float(grcav) * 3
time.sleep(1)
bcav = input("How many Blue Cavalry Attack Jewels do you have? ")
bcav_raw = 6
bcav_stat = float(bcav) * 6
time.sleep(1)
pcav = input("How many Purple Cavalry Attack Jewels do you have? ")
pcav_raw = 12
pcav_stat = float(pcav) * 12
time.sleep(1)
gcav = input("How many Gold Cavalry Attack Jewels do you have? ")
gcav_raw = 20
gcav_stat = float(gcav) * 20
print("You can gain " + str(grcav_stat) + "% attack from Green Cavalry Jewels") #total stats from Green
print("You can gain " + str(bcav_stat) + "% attack from Blue Cavalry Jewels." )#total stats from blue
print("You can gain " + str(pcav_stat) + "% attack from Purple Cavalry Jewels. ") #total stats from purple
print("You can gain " + str(gcav_stat) + "% attack from Gold Cavalry Jewels.") #total stats from gold
#==========Range Jewels Green - Gold =========
grrng = input("How many Green Range Jewels do you have? ")
grrng_stat = float(grrng) * 3
time.sleep(1)
brng = input("How many Blue Range Attack Jewels do you have? ")
brng_raw = 6
brng_stat = float(brng) * 6
time.sleep(1)
prng = input("How many Purple Range Attack Jewels do you have? ")
prng_raw = 12
prng_stat = float(prng) * 12
time.sleep(1)
grng = input("How many Gold Range Attack Jewels do you have? ")
grng_raw = 20
grng_stat = float(grng) * 20
print("You can gain " + str(grrng_stat) + "% attack from green inf jewels") #total stats from Green
print("You can gain " + str(brng_stat) + "% attack from blue Infantry Jewels." )#total stats from blue
print("You can gain " + str(prng_stat) + "% attack from Purple Infantry Jewels. ") #total stats from purple
print("You can gain " + str(grng_stat) + "% attack from Gold Infantry Jewels.") #total stats from gold
