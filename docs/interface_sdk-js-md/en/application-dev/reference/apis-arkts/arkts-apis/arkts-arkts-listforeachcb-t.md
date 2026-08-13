# ListForEachCb

```TypeScript
export type ListForEachCb<T> = (value: T, index: int, list: List<T>) => void
```

The type of List callback function.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type ListForEachCb<T> = (value: T, index: int, list: List<T>) => void--><!--Device-unnamed-export type ListForEachCb<T> = (value: T, index: int, list: List<T>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | The value of current element |
| index | int | Yes | The index of current element The value should be an integer. |
| list | [List](arkts-arkts-util-list-list-c.md)&lt;T&gt; | Yes | The List instance being traversed |

