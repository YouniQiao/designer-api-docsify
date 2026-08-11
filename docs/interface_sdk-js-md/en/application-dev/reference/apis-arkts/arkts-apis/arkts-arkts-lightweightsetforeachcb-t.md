# LightWeightSetForEachCb

```TypeScript
export type LightWeightSetForEachCb<T> = (value: T, key: T, set: LightWeightSet<T>) => void
```

The type of LightWeightSet callback function.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type LightWeightSetForEachCb<T> = (value: T, key: T, set: LightWeightSet<T>) => void--><!--Device-unnamed-export type LightWeightSetForEachCb<T> = (value: T, key: T, set: LightWeightSet<T>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | The value of current element |
| key | T | Yes | The key of current element(same as value) |
| set | [LightWeightSet](arkts-arkts-util-lightweightset-lightweightset-c.md)&lt;T&gt; | Yes | The LightWeightSet instance being traversed |

