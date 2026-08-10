# ListForEachCb

```TypeScript
export type ListForEachCb<T> = (value: T, index: int, list: List<T>) => void
```

List的回调函数类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type ListForEachCb<T> = (value: T, index: int, list: List<T>) => void--><!--Device-unnamed-export type ListForEachCb<T> = (value: T, index: int, list: List<T>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | 当前元素的值。 |
| index | int | Yes | 当前元素的下标。 该值为整数。 |
| list | [List](arkts-arkts-util-list-list-c.md)&lt;T&gt; | Yes | 当前正在遍历的List实例。 |

