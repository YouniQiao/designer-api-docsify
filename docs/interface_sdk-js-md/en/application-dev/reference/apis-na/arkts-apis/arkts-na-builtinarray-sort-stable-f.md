# sort_stable

## sort_stable

```TypeScript
export function sort_stable<T>(arr: FixedArray<T>, startIndex: int, endIndex: int, comp: (lhs: T, rhs: T) => int): 
    void
```

Sorts elements of `arr` using stable sort algorithm.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function sort_stable<T>(arr: FixedArray<T>, startIndex: int, endIndex: int, comp: (lhs: T, rhs: T) => int):     void--><!--Device-unnamed-export function sort_stable<T>(arr: FixedArray<T>, startIndex: int, endIndex: int, comp: (lhs: T, rhs: T) => int):     void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | FixedArray&lt;T&gt; | Yes | The array to sort. |
| startIndex | int | Yes | The start index of sorting range. &lt;br&gt;The value should be an integer. |
| endIndex | int | Yes | The end index of sorting range. &lt;br&gt;The value should be an integer. |
| comp | (lhs: T, rhs: T) =&gt; int | Yes | Comparator function. |

