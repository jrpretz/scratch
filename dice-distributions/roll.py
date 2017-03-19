# roll.py
#
# simulates rolling a number of polyhedral die
#
# on the command line you specify any number of die by 
# the number of sides they have. The program returns to stdout
# a list of die totals and their probabilities.
#
# These are the mathematically precise probabilities. No intermediate
# simulation.
#
# Note it assumes die are number 1-nside. 

def jointProbability(results_a,results_b):
    results = {}
    for roll_a,prob_a in results_a.iteritems():
        for roll_b,prob_b in results_b.iteritems():
            sum = roll_a + roll_b
            if not results.has_key(sum):
                results[sum] = 0.0
            results[sum] = results[sum] + prob_a*prob_b
    return results

def diceProbabilities(sides):
    returned = {}
    for i in range(1,sides+1):
        returned[i] = 1./sides
    return returned

def sumDistribution(dice):
    cumulative = diceProbabilities(dice[0])
    if(len(dice) > 1):
        for i in range(1,len(dice)):
            cumulative = jointProbability(cumulative,diceProbabilities(dice[i]))
    return cumulative


if __name__ == "__main__":
    import sys
    inputSides = []
    if len(sys.argv) < 2:
        print "Usage: python roll.py DIE_SIDES"
        print " where DIE_SIDES is a list of the sides of the die you want to roll"
        print " e.g. \"python roll.py 4 4 20\" will compute the total probabilities"
        print " when rolling two 4-sided die and one 20-sided die"
        print " Output is just to stdout. First column is the dice sum. "
        print " Second column is the probability of getting that roll"
        print " Third column is the probability for getting that roll or lower"
        sys.exit(0)

    for i in range(1,len(sys.argv)):
        nside = None
        try:
            nside = int(sys.argv[i])
        except:
            print "couldn't parse option %d: '%s' as an int"%(i,sys.argv[i])
            sys.exit(1)
        inputSides.append(nside)

    distribution = sumDistribution(inputSides)

    cumulative = 0.0
    for roll,prob in distribution.iteritems():
        cumulative = cumulative + prob
        print roll,prob,cumulative
