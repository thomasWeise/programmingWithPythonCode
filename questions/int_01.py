"""Compute how many potatoes I can buy."""

potatoes_in_store: int     = 1000  # total number of potatoes
cost_for_all_potatoes: int = 50    # cost if we would buy all potatoes
my_money: int              = 10    # the money I have

# Compute the cost of one single potato.
cost_per_potato = cost_for_all_potatoes // potatoes_in_store  # Line 8
print(f"One potato costs {cost_per_potato} RMB.")             # Line 9

# Compute the number of potatoes that I can buy with my money.
i_can_buy: int = my_money / cost_per_potato                   # Line 12
print(f"I can buy {i_can_buy} potatoes.")                     # Line 13
