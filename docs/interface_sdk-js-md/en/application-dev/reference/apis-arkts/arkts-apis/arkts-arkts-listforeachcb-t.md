# ListForEachCb

```TypeScript
export type ListForEachCb<T> = (value: T, index: int, list: List<T>) => void
```

The type of List callback function.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type ListForEachCb<T> = (value: T, index: int, list: List<T>) => void--><!--Device-unnamed-export type ListForEachCb<T> = (value: T, index: int, list: List<T>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | The value of current element  |
| index | int | Yes | The index of current element The value should be an integer.  |
| list | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Yes | The List instance being traversed  |

