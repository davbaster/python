from sys import path
path.append('C:\\Users\\cordobda\\py\\packages')

#first exercise
#import extra.iota
#print(extra.iota.FunI())

#second exercise
#another way to import it
#from extra.iota import FunI
#print(FunI())

#third exercise
#import extra.good.best.sigma
#from extra.good.best.tau import FunT

#print(extra.good.best.sigma.FunS())
#print(FunT())


#fourth exercise
import extra.good.best.sigma as sig
import extra.good.alpha as alp

print(sig.FunS())
print(alp.FunA())