# Product of Array Except Self
- Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
- You must write an algorithm that runs in O(n) time and without using the division operation.

---

## Approach (Prefix Product + Suffix Product)

For any index:

```text
answer[i]
=
(product of elements before i)
×
(product of elements after i)
```

Example:

```text
nums = [1,2,3,4]
```

For index 2:

```text
Left Product
=
1 × 2
=
2

Right Product
=
4

Answer
=
2 × 4
=
8
```

---

## Prefix Product

Store:

```text
answer[i]
=
product of all elements before i
```

For:

```text
nums = [1,2,3,4]
```

Prefix products become:

| Index | Prefix Product |
| ----- | -------------- |
| 0     | 1              |
| 1     | 1              |
| 2     | 2              |
| 3     | 6              |

Result:

```text
answer = [1,1,2,6]
```

---

## Suffix Product

Now traverse from right to left.

Maintain:

```text
suffix = 1
```

For every index:

```text
answer[i] *= suffix
```

Then update:

```text
suffix *= nums[i]
```


### Complexity
- Time : O(n)
- Space : O(1) 

---
