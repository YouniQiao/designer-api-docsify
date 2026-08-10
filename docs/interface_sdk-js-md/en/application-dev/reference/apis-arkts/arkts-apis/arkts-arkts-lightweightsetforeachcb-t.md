# LightWeightSetForEachCb

```TypeScript
export type LightWeightSetForEachCb<T> = (value: T, key: T, set: LightWeightSet<T>) => void
```

LightWeightSet的回调函数类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type LightWeightSetForEachCb<T> = (value: T, key: T, set: LightWeightSet<T>) => void--><!--Device-unnamed-export type LightWeightSetForEachCb<T> = (value: T, key: T, set: LightWeightSet<T>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | 当前元素的值。 |
| key | T | Yes | 当前元素的键（与value相同）。 |
| set | [LightWeightSet](arkts-arkts-util-lightweightset-lightweightset-c.md)&lt;T&gt; | Yes | 当前正在遍历的LightWeightSet实例。 |

