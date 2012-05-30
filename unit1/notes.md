Unit 1 Notes

SENSE - BAYES RULE

    Posterior P at i = (1/alpha)*(Measurement at i * Prior P at i)

    where alpha = SUM over i of ( Measurement at i * Prior P at i)


MOTION - TOTAL PROBABILITY

    P(X in location i now ) = SUM over all locations j 
                                ( P(X in location i now | given X in location j previously) * P(X in location j previously) )

                            =     P(X in location i now | given X in location 0 previously) * P(X in location 0 previously)
                                + P(X in location i now | given X in location 1 previously) * P(X in location 1 previously) 
                                + P(X in location i now | given X in location 2 previously) * P(X in location 2 previously)
                                + P(X in location i now | given X in location 3 previously) * P(X in location 3 previously)
                                ....

                                + P(X in location i now | given X in location i previously) * P(X in location i previously)
                                ....

                                + P(X in location i now | given X in location n previously) * P(X in location n previously)


      NOTE: P(X in location 0 previously) + P(X in location 1 previously) + ... + P(X in location n previously) = unity