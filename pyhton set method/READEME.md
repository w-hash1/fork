## copy()
The `copy()` method creates a duplicate of the original set. Any modifications made to the copied set do not affect the original. and - The copy() method ensures that copied_set is independent of my_set

## difference()
The `difference()` method returns a new set containing elements that are in the original set but not in the specified set(s). It does not modify the source set.

## difference_update()
The `difference_update()` method removes all elements from the original set that are present in the specified set(s). Unlike `difference()`, this method modifies the original set in place rather than returning a new set.
## discard()
The `discard()` method removes the specified element from the set if it is present. Unlike `remove()`, `discard()` does not raise an error if the element is absent.

## intersection()
The `intersection()` method returns a new set containing elements that are common to the original set and the specified set(s). It does not modify the original sets.

## intersection_update()
The `intersection_update()` method updates the original set by keeping only elements found in both the set and the provided set(s). Unlike `intersection()`, it modifies the set in place.

## isdisjoint()
The `isdisjoint()` method tests whether two sets have no elements in common. It returns `True` if the sets are disjoint (i.e., share no common elements), and `False` if there is at least one common element.

## issubset()
The `issubset()` method checks whether every element in the original set is also contained within another set, effectively determining if the first set is a subset of the second. It returns `True` if all elements are present, and `False` if any element is missing.

## issuperset()
The `issuperset()` method checks whether the calling set contains all the elements of the specified set. It returns `True` if every element in the other set is also present in the calling set; otherwise, it returns `False`.

## pop()
The `pop()` method removes and returns an arbitrary element from the set. Because sets are unordered, you do not know in advance which element will be removed. Use this method when you need to remove an item without specifying which one.


## remove()
The `remove()` method deletes the specified element from the set. If the element is not present, it raises a `KeyError`, making it essential to ensure the element exists in the set before removal or to handle the exception appropriately.

## symmetric_difference()
The `symmetric_difference()` method returns a new set containing elements that are present in either of the two sets, but not in both. It is the union of the differences between the sets.

## symmetric_difference_update()
The `symmetric_difference_update()` method updates the original set by keeping only the elements that are unique to each set; that is, elements which appear in either the original set or the specified set(s) but not in both. This operation modifies the set in place.

## union()
The `union()` method returns a new set consisting of the unique elements present in either the original set or the specified set(s). It does not modify the existing sets.

## update()
The `update()` method adds elements from one or more iterables (such as sets, lists, or tuples) to the original set, modifying it in place. This method does not return a new set; instead, it updates the existing set with the new elements.



