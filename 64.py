# Python Access List Items 

# In order to access the list items to the index number. Use the index operator [] to access an item in a list. In Python, negative sequence indexes represent positions from the ned of the array. Instead of having to compute the offset as in List[len(List)-3], it is enough to just write List[-3]. Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second-last item, etc.

List = ["Geeks", "For", "Geeks"]
print("Accessing element from the list")
print(List[0])
print(List[2])
print("Accessing element using negative indexing")
print(List[-1])
print(List[-3])