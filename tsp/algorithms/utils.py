
def n_choose_k(n,k):
    """Returns the binomial coefficient C(n,k)
    This is used to calculate the expected number of distinct paths for a given
    source file. Assuming a complete graph with cardinality n, there will be C(n,2)
    paths.
    """
    result = 1
    for i in range(1, k+1):
        result = result * (n-i+1) / i
    return result