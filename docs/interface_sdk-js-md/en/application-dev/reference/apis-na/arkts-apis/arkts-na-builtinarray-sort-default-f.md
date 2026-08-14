# sort_default

## sort_default

```TypeScript
export function sort_default<T>(arr: FixedArray<T>, arrStr: FixedArray<buffStr>, startIndex: int, endIndex: int): 
    void
```

Sorts elements of `arr` using default sort.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function sort_default<T>(arr: FixedArray<T>, arrStr: FixedArray<buffStr>, startIndex: int, endIndex: int):     void--><!--Device-unnamed-export function sort_default<T>(arr: FixedArray<T>, arrStr: FixedArray<buffStr>, startIndex: int, endIndex: int):     void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | FixedArray&lt;T&gt; | Yes | The array to sort. |
| arrStr | FixedArray&lt;buffStr&gt; | Yes | Stringified array for comparison. |
| startIndex | int | Yes | The start index of sorting range. <br>The value should be an integer. |
| endIndex | int | Yes | The end index of sorting range. <br>The value should be an integer. |

