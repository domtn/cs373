Bayes Rule Question


Let's say the probability of your house catching fire is 0.001.
     
     P(F) = 0.001

You call your neighbor every now and then and ask him if it's on fire.
Knowing that there's a probablity of 0.1 that your neighbor lies.
     
     P(lie) = 0.1

Observing that your neighbor says "Yes, it's burning"
     P(B)


Compute:
  a) Non-normalized P(F|B)
  b) Non-normalized P(not F | B)
  c) Normalized P(F|B)
  d) Normalized P(not F | B)


Answer:

a) Non-normalized P(F|B) = P(B|F)*P(F)
                         =  0.9  *0.001 = 0.0009

b) Non-normalized P(not F | B) = P(B| not F) * P(not F)
                               =     0.1     * 0.999
                               = 0.0999
c) Normalized P(F|B) =   [Non-normalized P(F|B)] / [Non-normalized P(F|B)  +  Non-normalized P(not F | B)]   
                     =          0.0009           / [        0.0009         +             0.0999          ]                           
                     =   0.0089

d) Normalized P(not F | B) = [Non-normalized P( not F | B)] / [Non-normalized P(F|B)  +  Non-normalized P(not F | B)]  
                           =          0.0999                / (        0.0009         +             0.0999          )                           
                           =   0.99
