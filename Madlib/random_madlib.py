from sample_madlibs import hp, code, zombie, hungergames
import random

if _name_ == "_main_":
    m = random.choice([hp, code, zombie, hungergames])
    m.madlib()