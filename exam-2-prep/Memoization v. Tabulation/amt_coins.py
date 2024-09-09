def amt_coins_memo(amt, coins, memo=None):
	"""Using 2D memoization and recursion, determines the minimum number
	of coins in an iterable (coins) needed to produce an amount (amt)."""
	if memo is None: memo = [[None for i in range(len(coins))] for j in range(amt+1)] # call with memo[amt][an index in coins]

	def _get_amt_coins(amt, coin_idx, coins, memo):
		"""Attempts to fetch the number using memoization, and uses recursion when that fails."""
		if memo[amt][coin_idx] is None:
			memo[amt][coin_idx] = amt_coins_memo(amt, coins, memo=memo)
		return memo[amt][coin_idx]
		
	# base case
	if amt == 0:
		return 0
	if amt in coins:
		return amt
	
	
	
	min_all_coins = amt + 1 # you will never go above this unless you use fractional coins, which this doesn't support
	for coin_idx, coin in enumerate(coins):
		# determine min coins recursively
		remainder = amt - coin
		if remainder >= 0:
			min_curr_coin = 1 + _get_amt_coins(remainder, coin_idx, coins, memo=memo)
			# if it's the least so far, overwrite the minimum
			if min_curr_coin < min_all_coins: min_all_coins = min_curr_coin

	return min_all_coins



def amt_coins_tab(amt, coins):
	"""Using tabulation, determines the minimum number
	of coins in an iterable (coins) needed to produce an amount (amt)."""
	# base cases/short circuits
	if amt == 0:
		return 0
	if amt in coins:
		return 1

	# subtract one of each coin, and find the minimum positive remainder
	# we don't want anything not less than what we start with (amt)
	

