#Day38-Best-time-to-sell-buy-stock
arr=[7,4,1,2,5,3]
buy_at=float("inf")
sell_at=0
profit=0
for price in arr:
    if price<buy_at:
        buy_at=price
    if profit<price-buy_at:
        profit=price-buy_at
        sell_at=price
print("buy",buy_at)
print("sell",sell_at)
print("profit",profit)
#Time complexity:O(n)
#Space complexity:O(1)
