# PlainArrayForEachCb

```TypeScript
export type PlainArrayForEachCb<T> = (value: T, key: int, PlainArray: PlainArray<T>) => void
```

The type of PlainArray callback function.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type PlainArrayForEachCb<T> = (value: T, key: int, PlainArray: PlainArray<T>) => void--><!--Device-unnamed-export type PlainArrayForEachCb<T> = (value: T, key: int, PlainArray: PlainArray<T>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | The value of current element |
| key | int | Yes | The key of current element The value should be an integer. |
| PlainArray | [PlainArray](arkts-arkts-util-plainarray-plainarray-c.md)&lt;T&gt; | Yes | The PlainArray instance being traversed |

