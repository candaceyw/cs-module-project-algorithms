'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n, cache):
    # base cases
    if n < 0:
        return 0
    if n == 0:
        return 1

    # Before we try to solve our problem
    # lets see if the anwer is already stored in cache
    if cache[n] > 0:
        # this must have be3en precomputed
        return cache[n]

    # How can we get to the base case?
    # what if I ate just 1 cookie?
    number_of_ways = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)

    cache[n] = number_of_ways

    return number_of_ways


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
