
import math

# Data $/ounce
gold = 1341.30
silver = 17.19
platinum = 1005.00
palladium = 1057.95

def cost(g_oz, s_oz, pl_oz, pa_oz):
    g1 = g_oz*gold
    s1 = s_oz*silver
    pl1 = pl_oz*platinum
    pa1 = pa_oz*palladium
    return (g1+s1+pl1+pa1)

def how_many_oz(value, money):
    if value == gold:
        return math.floor(money/gold)
    elif value == silver:
        return math.floor(money/silver)
    elif value == platinum:
        return math.floor(money/platinum)
    elif value == palladium:
        return math.floor(money/palladium)



def value(metal_oz, metal):
    if metal == "Au":
        return metal_oz*gold
    elif metal == "Ag":
        return metal_oz*silver
    elif metal == "Pd":
        return metal_oz*palladium
    elif metal == "Pt":
        return metal_oz*platinum

  



print(cost(3,0,0,0))
print(cost(0,2,0,0))
print(cost(0,0,3,0))
print(cost(0,0,0,2))
print(cost(3,1,4,5))
print(cost(2,400,3,4))

print(how_many_oz(gold,2.5*gold))
print(how_many_oz(silver,4*silver))
print(how_many_oz(platinum,math.pi*platinum))
print(how_many_oz(palladium,10/2*palladium))

print(value(10, "Au"))
print(value(10, "Ag"))
print(value(10, "Pd"))
print(value(10, "Pt"))