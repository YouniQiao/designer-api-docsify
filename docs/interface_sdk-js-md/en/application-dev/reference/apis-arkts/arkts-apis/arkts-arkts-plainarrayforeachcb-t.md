# PlainArrayForEachCb

```TypeScript
export type PlainArrayForEachCb<T> = (value: T, key: int, PlainArray: PlainArray<T>) => void
```

PlainArray的回调函数类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type PlainArrayForEachCb<T> = (value: T, key: int, PlainArray: PlainArray<T>) => void--><!--Device-unnamed-export type PlainArrayForEachCb<T> = (value: T, key: int, PlainArray: PlainArray<T>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | 当前元素的值。 |
| key | int | Yes | 当前元素的键。 该值为整数。 |
| PlainArray | [PlainArray](arkts-arkts-util-plainarray-plainarray-c.md)&lt;T&gt; | Yes | 当前正在遍历的PlainArray实例。 |

