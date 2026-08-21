# ListReplaceCb

```TypeScript
export type ListReplaceCb<T> = (value: T, index: int, list: List<T>) => T
```

The type of List callback function.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type ListReplaceCb<T> = (value: T, index: int, list: List<T>) => T--><!--Device-unnamed-export type ListReplaceCb<T> = (value: T, index: int, list: List<T>) => T-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | The old value of current element |
| index | int | Yes | The index of current element The value should be an integer. |
| list | [List](arkts-arkts-utillist-list-c.md)&lt;T&gt; | Yes | The List instance being traversed |

**Return value:**

| Type | Description |
| --- | --- |
| T | The new value of current element |

