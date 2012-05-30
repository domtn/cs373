Bayes Rule Question


Let's say the probability of your house catching fire is 0.001.
     
     P(F) = 0.001

You call your neighbor every now and then and ask him if it's on fire.
Knowing that there's a probablity of 0.1 that your neighbor lies.
     
     P(lie) = 0.1

Observing that your neighbor says "Yes, it's burning"
     P(B)


Compute:
  * Non-normalized P(F|B)
  * Non-normalized P(not F | B)
  * Normalized P(F|B)
  * Normalized P(not F | B)


Answer:

*  Non-normalized P(F|B) = P(B|F)*P(F)
*                        =  0.9  *0.001 = 0.0009

*  Non-normalized P(not F | B) = P(B| not F) * P(not F)
*                              =     0.1     * 0.999
*                              = 0.0999
*  Normalized P(F|B) =   [Non-normalized P(F|B)] / [Non-normalized P(F|B)  +  Non-normalized P(not F | B)]   
*                    =          0.0009           / [        0.0009         +             0.0999          ]                           
*                    =   0.0089

*  Normalized P(not F | B) = [Non-normalized P( not F | B)] / [Non-normalized P(F|B)  +  Non-normalized P(not F | B)]  
*                          =          0.0999                / (        0.0009         +             0.0999          )                           
*                          =   0.99
