# TreeMapForEachCb

```TypeScript
export type TreeMapForEachCb<K, V> = (value: V, key: K, map: TreeMap<K, V>) => void
```

TreeMap的回调函数类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type TreeMapForEachCb<K, V> = (value: V, key: K, map: TreeMap<K, V>) => void--><!--Device-unnamed-export type TreeMapForEachCb<K, V> = (value: V, key: K, map: TreeMap<K, V>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | V | Yes | 当前元素的值。 |
| key | K | Yes | 当前元素的键。 |
| map | [TreeMap](arkts-arkts-util-treemap-treemap-c.md)&lt;K, V&gt; | Yes | 当前正在遍历的TreeMap实例。 |

