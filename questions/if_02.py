""" If-then-else Examples. """

price_of_shoes: int = 100

if price_of_shoes <= 40:
    print("The shoes are cheap.")
elif price_of_shoes <= 150:
    print("The shoes are reasonably priced.")
elif price_of_shoes <= 250:
    print("The shoes are a bit expensive.")
else:
    print("Not going to happen.")
