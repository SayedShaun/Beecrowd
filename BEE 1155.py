def function(S):
  Sum = 0
  for i in range(1,S+1):
    Sum = Sum+(1/i)
        
  print(f"{Sum:.2f}")

function(100)