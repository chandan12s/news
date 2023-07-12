# This is a comment
def news(budget):
    subscription = {
        "TOI": [3, 3, 3, 3, 3, 5, 6],
        "HT": [2, 2, 2, 2, 2, 4, 4],
        "ET": [4, 4, 4, 4, 4, 4, 10],
        "BM": [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5],
        "Hindu": [2.5, 2.5, 2.5, 2.5, 2.5, 4, 4],
        
    }
    
    sums = {
        "TOI": sum(subscription["TOI"]),
         "HT": sum(subscription["HT"]),
        "Hindu": sum(subscription["Hindu"]),
        "ET": sum(subscription["ET"]),
        "BM": sum(subscription["BM"]),
       
    }
    sums = dict(sorted(sums.items(), key=lambda item: item[1]))
    result_list = []
    for i in range(0,len(sums)):
      for j in range(i+1, len(sums)):
        if sums[list(sums)[i]] + sums[list(sums)[j]] <= budget:
          result_list.append([list(sums)[i], list(sums)[j]])
        else :
          break
    print (result_list)
news(35)
