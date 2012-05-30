Given 2 coins: 
  fair coin with P(H) = 0.5
  loaded coin with P(H) = 0.1

Take a coin with 50% chance of getting a fair coin
Flip it
Observe H

What is P(fair) ?

Applying Bayes Rule:

P(fair|H) = (1/alpha)*P(H|fair)*P(fair)

But alpha = P(H|fair)*P(H) + P(H|loaded)*P(H) 
          =   0.5    *0.5  +    0.1     *0.5
          = 0.3
Therefore,

P(fair|H) = (1/alpha)*P(H|fair)*P(fair)
          = (1.0/0.3)*  0.5    *0.5
          = 0.25/0.3
          = 0.833
